# Validation record

This record distinguishes executed checks from intended coverage. A passing run
is evidence for the named examples at a point in time, not a production quality
certificate or a guarantee about future demo availability.

## Local baseline

- Date: 2026-10-27, America/Sao_Paulo.
- OS: Windows.
- Python: 3.13.15, isolated `.venv`.
- Playwright: 1.52.0; pytest: 8.3.5; pytest-playwright: 0.7.0.
- Target: headless Chromium, English locale, 1440 x 1000 viewport.
- External applications: hosted Toolshop and The Internet, without response mocks.
- Dependencies: `pip check` reported no broken requirements.
- Python sources: `compileall` completed successfully.

Command:

```powershell
.venv\Scripts\python -m pytest --junitxml=reports/junit.xml
```

Result: **18 passed in 69.92 seconds** (9 shop, 2 API, 7 lab).
No skips, expected failures or automatic retries were used.
JUnit evidence is generated locally in `reports/junit.xml` and intentionally
excluded from Git; CI publishes its own artifacts for each run.

## Issues found while developing the tests

1. The first browser waits assumed that catalog reads used GET. Network inspection
   showed the hosted UI actually uses QUERY. Response predicates were corrected
   to accept GET or QUERY, without removing the response-status check.
2. The checkout guest choice was initially treated as a button. The actual DOM
   exposes a tab, a hidden heading and a submit input with the same words. The
   scenario now clicks the specifically named tab and verifies the visible guest
   form. It does not use `first()` to conceal an ambiguous selector.

These were test implementation errors, not confirmed defects in either demo.
No product defect is claimed without reproducible evidence against an expectation.

## Continuous integration

The workflow targets Ubuntu 24.04 and Python 3.13, installs Chromium and its system
dependencies, executes the suite and retains JUnit/failure artifacts. Its actual
first-run status will be recorded separately from local validation.

## Remaining limitations

No successful order is submitted. Firefox, WebKit, mobile devices, payment,
accessibility, security and performance are not validated by this initial suite.
Public data and endpoints remain controlled by their owners. Exact direct
dependency pins do not constitute a full transitive lockfile.
