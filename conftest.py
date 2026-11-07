"""Export-root pytest resource setup for typings.

Binds the resource-marker hook and the per-user-directory isolation at the
repository root, the one conftest every exported test sits under. Without it the
vendored ``resources_test`` meets an unregistered ``real_user_dirs`` marker and
fails at collection.
"""

from typing import Final

from lib.testing.resources import (
    isolate_user_dirs,
    pytest_collection_modifyitems,
    pytest_configure,
)


# Honored only in the rootdir conftest: each invocation claims its own basetemp,
# so concurrent sessions never clean up one another's directories.
pytest_plugins: Final = ("lib.testing.basetemp",)

__all__ = ["isolate_user_dirs", "pytest_collection_modifyitems", "pytest_configure"]
