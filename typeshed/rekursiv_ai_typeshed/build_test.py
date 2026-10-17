"""``build`` assembles both trees, and ``_read_member`` decodes ty's archive."""

from __future__ import annotations

from importlib.machinery import ModuleSpec
from typing import TYPE_CHECKING, Protocol, cast

import importlib
import io
import sys
import zipfile

import pytest

# From the submodule path: the package re-exports a ``build`` FUNCTION, which
# shadows the submodule on ``from rekursiv_ai_typeshed import build``.
from rekursiv_ai_typeshed.build import (
    _read_member,
    build,
    bundle_dir,
    extract_ty_stdlib,
)


if TYPE_CHECKING:
    from pathlib import Path


_BUILD_MODULE = sys.modules[extract_ty_stdlib.__module__]


class _Zstd(Protocol):
    def compress(self, data: bytes) -> bytes: ...

    def decompress(self, data: bytes) -> bytes: ...


def _archive(compress_type: int, payload: bytes) -> zipfile.ZipFile:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as writer:
        writer.writestr(zipfile.ZipInfo("stdlib/a.pyi"), payload, compress_type)
    return zipfile.ZipFile(io.BytesIO(buffer.getvalue()))


def _fake_extract(target: Path) -> None:
    (target / "stdlib").mkdir(parents=True)
    (target / "stdlib" / "builtins.pyi").write_text("def p() -> Any: ...\n")


def test_build_patches_overlays_and_splits_the_trees(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A tiny stand-in bundle runs every step without the real 7k-file copy."""
    source = tmp_path / "src"
    (source / "typings" / "stdlib").mkdir(parents=True)
    (source / "typings" / "stdlib" / "overlay.pyi").write_text("O: int\n")
    extensions = source / "typings" / "basedpyright" / "ty_extensions"
    extensions.mkdir(parents=True)
    (extensions / "__init__.pyi").write_text("Intersection = object\n")
    (source / "typeshed.patch").write_text(
        "--- a/stdlib/builtins.pyi\n+++ b/stdlib/builtins.pyi\n"
        "@@ -1 +1 @@\n-def p() -> Any: ...\n+def p() -> float: ...\n",
    )
    bundle = tmp_path / "bundle"
    (bundle / "stubs" / "six").mkdir(parents=True)
    (bundle / "commit.txt").write_text("abc\n")
    monkeypatch.setattr(_BUILD_MODULE, "_CWD", source)
    monkeypatch.setattr(_BUILD_MODULE, "extract_ty_stdlib", _fake_extract)
    monkeypatch.setattr(_BUILD_MODULE, "bundle_dir", lambda: bundle)
    target = tmp_path / "out"
    (target / "stale").mkdir(parents=True)

    build(target)

    for checker in ("ty", "basedpyright"):
        stdlib = target / checker / "stdlib"
        assert (stdlib / "builtins.pyi").read_text() == "def p() -> float: ...\n"
        assert (stdlib / "overlay.pyi").read_text() == "O: int\n"
    assert (target / "basedpyright" / "stubs" / "six").is_dir()
    assert (target / "basedpyright" / "stubs.commit.txt").read_text() == "abc\n"
    assert (target / "basedpyright" / "stdlib" / "ty_extensions").is_dir()
    assert not (target / "ty" / "stdlib" / "ty_extensions").exists()
    assert not (target / "stale").exists()


def test_bundle_dir_holds_basedpyrights_typeshed() -> None:
    assert (bundle_dir() / "commit.txt").is_file()


@pytest.mark.parametrize(
    ("spec", "match"),
    [
        (None, r"^Expected spec is not None\.$"),
        (ModuleSpec("basedpyright", None), r"^Expected spec\.origin is not None\.$"),
    ],
)
def test_bundle_dir_rejects_a_missing_basedpyright(
    monkeypatch: pytest.MonkeyPatch,
    spec: ModuleSpec | None,
    match: str,
) -> None:
    def find_spec(*_: object) -> ModuleSpec | None:
        return spec

    monkeypatch.setattr(_BUILD_MODULE, "find_spec", find_spec)
    with pytest.raises(ValueError, match=match):
        bundle_dir()


def test_a_zstandard_member_needs_an_open_archive(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive = _archive(zipfile.ZIP_STORED, b"x")
    archive.getinfo("stdlib/a.pyi").compress_type = 93
    archive.close()
    monkeypatch.setattr(sys, "version_info", (3, 12, 0))
    with pytest.raises(ValueError, match=r"^Expected archive\.fp is not None\.$"):
        _read_member(archive, "stdlib/a.pyi")


@pytest.mark.parametrize("compress_type", [zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED])
def test_a_member_zipfile_decodes_is_read_directly(compress_type: int) -> None:
    payload = b"def f() -> int: ...\n" * 50
    assert _read_member(_archive(compress_type, payload), "stdlib/a.pyi") == payload


def test_a_zstandard_member_is_decoded(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ty's own archive format: method 93, through ``backports.zstd`` before 3.14."""
    # The backport is the 3.14 stdlib module repackaged, so whichever this
    # interpreter has stands in for it.
    zstd = cast(
        _Zstd,
        cast(
            object,
            importlib.import_module(
                "compression.zstd" if sys.version_info >= (3, 14) else "backports.zstd",
            ),
        ),
    )
    monkeypatch.setitem(sys.modules, "backports.zstd", zstd)
    payload = b"class int: ...\n" * 50
    compressed = zstd.compress(payload)
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as writer:
        info = zipfile.ZipInfo("stdlib/a.pyi")
        writer.writestr(info, compressed, zipfile.ZIP_STORED)
    # Relabel the stored member as Zstandard: the bytes ARE zstd frames, so a
    # reader honoring method 93 recovers ``payload``.
    raw = bytearray(buffer.getvalue())
    for header in (b"PK\x03\x04", b"PK\x01\x02"):
        at = raw.find(header)
        method = at + (8 if header == b"PK\x03\x04" else 10)
        raw[method : method + 2] = (93).to_bytes(2, "little")
    archive = zipfile.ZipFile(io.BytesIO(bytes(raw)))
    assert archive.getinfo("stdlib/a.pyi").compress_type == 93
    # Forces the pre-3.14 branch, the one the CLI decodes.
    monkeypatch.setattr(sys, "version_info", (3, 12, 0))

    assert _read_member(archive, "stdlib/a.pyi") == payload


def test_the_real_ty_archive_round_trips(tmp_path: Path) -> None:
    """Every stdlib member ty ships comes back as parseable stub text."""
    extract_ty_stdlib(tmp_path)
    builtins = (tmp_path / "stdlib" / "builtins.pyi").read_text()
    assert "class int" in builtins
    assert (tmp_path / "commit.txt").read_text().strip()


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
