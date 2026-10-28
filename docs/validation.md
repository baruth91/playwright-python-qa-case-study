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

The first workflow could not start a hosted runner. That prerequisite was resolved.

[The first executed complete-suite run](https://github.com/baruth91/playwright-python-qa-case-study/actions/runs/40688231617)
ran on 2026-10-28 with Ubuntu 24.04, Python 3.13.17 and Chromium:
**9 passed, 9 failed in 64.40 seconds**. Both API checks and all seven labs passed.
All nine Toolshop UI cases stopped at initial navigation: traces show HTTP 403,
and screenshots show Cloudflare's human-verification page instead of the catalog.
There is no evidence from this run about the Toolshop business outcomes.

The default workflow now selects API and lab checks explicitly. Toolshop UI is a
separate manual opt-in job with a configurable authorized URL. Local execution
still selects all 18 tests. This split does not reclassify the failed attempt as
a success or establish that Toolshop UI works on Linux.

[The revised default workflow](https://github.com/baruth91/playwright-python-qa-case-study/actions/runs/40688756239)
completed successfully on 2026-10-28 at code revision `82227ce`:
**9 passed, 0 failed, 0 errors, 0 skipped**, with 21.309 seconds recorded in JUnit.
Those are exactly 2 API checks and 7 lab exercises. The separate Toolshop UI job
was intentionally not selected; its scenarios were not executed in this run.

After adding an explicit HTTP-status diagnostic to catalog navigation, the local
Toolshop smoke selection also passed: **2 passed, 16 deselected in 30.38 seconds**.
This checks search and the journey to the guest form; it is not a new full-suite run.

JUnit and failure artifacts are retained for seven days. No CAPTCHA handling,
stealth settings, response substitution or automatic retries are used.

## Remaining limitations

No successful order is submitted. Firefox, WebKit, mobile devices, payment,
accessibility, security and performance are not validated by this initial suite.
Public data and endpoints remain controlled by their owners. Exact direct
dependency pins do not constitute a full transitive lockfile.
