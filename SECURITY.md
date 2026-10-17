# Security Policy

## Why this file exists

typings ships stub files that type checkers load, and a build hook that runs at
install time. Security reports need a private path so exploit details are not
published before review.

## Reporting a vulnerability

Please report suspected security vulnerabilities privately by emailing hello@rekursiv.ai.

Include:

- Affected version or commit.
- Steps to reproduce.
- Expected impact.
- Any suggested mitigation.

Please do not open public issues for vulnerabilities until we have investigated and coordinated disclosure.

## Scope

Security reports are especially useful for:

- Code that runs while building or installing either distribution.
- Dependency or packaging issues that affect installed users.
- Supply-chain concerns in the published wheel or sdist.
