# A QA case study with Playwright and Python

An executable, English-language learning project offered to the QA community by
[baruth91](https://github.com/baruth91), drawing on 12 years of QA experience.

The purpose is to connect product risks, test selection, readable automation and
failure investigation. Each scenario explains what it checks and why it belongs
in the suite. Beginners can run a working example; experienced testers can review
the trade-offs and suggest improvements.

This is an independent educational portfolio project using public practice
applications. It does not claim a client engagement or affiliation with their owners.

## What you will learn

- Turn a customer journey into a small, risk-based suite.
- Separate browser interactions from business assertions with small page objects.
- Use isolated browser contexts, synthetic data and retrying assertions.
- Check prices with `Decimal`, including quantity changes and line totals.
- Complement UI coverage with read-only API consumer checks.
- Handle dropdowns, checkboxes, asynchronous controls, dialogs, uploads and frames.
- Investigate failures with screenshots, traces and JUnit results.

## Start here

Requirements: Python 3.13, Git, and internet access to the practice applications.
The pinned versions in `requirements.txt` are the initial tested baseline, not a
claim that they are the latest releases. Browser binaries are installed separately.

```powershell
git clone https://github.com/baruth91/playwright-python-qa-case-study.git
cd playwright-python-qa-case-study
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m playwright install chromium
.venv\Scripts\python -m pytest
```

On macOS/Linux, use `.venv/bin/python` instead of `.venv\Scripts\python`.
On Linux, install browser system dependencies with
`.venv/bin/python -m playwright install --with-deps chromium`.
No shell activation is required.

## Choose a learning path

Commands below assume the virtual environment's Python is selected. You can always
substitute its full path from the quick start.

```bash
python -m pytest -m smoke
python -m pytest -m shop --headed --slowmo 150
python -m pytest -m api
python -m pytest -m lab
python -m pytest tests/ui/test_shopping.py -k quantity
python -m pytest --junitxml=reports/junit.xml
```

Start with [the guided walkthrough](docs/learning-guide.md), then read
[the product understanding](docs/product-understanding.md),
[risk assessment](docs/risk-assessment.md) and [test strategy](docs/test-strategy.md).
The [coverage map](docs/coverage-map.md) connects every scenario to its purpose.

## The two practice applications

**Toolshop** is the business case: discover a product, review its price, add a
quantity, review the cart and reach checkout. The initial suite stops at the
identity step; it does not submit orders or test payment processing.

**The Internet** is a separate interaction lab. Its examples teach browser
techniques and do not count as Toolshop business coverage.

| Setting | Default |
| --- | --- |
| `SHOP_URL` | `https://practicesoftwaretesting.com` |
| `SHOP_API_URL` | `https://api.practicesoftwaretesting.com` |
| `LAB_URL` | `https://the-internet.herokuapp.com` |

To target an equivalent authorized environment in PowerShell:

```powershell
$env:SHOP_URL = 'http://localhost:4200'
$env:SHOP_API_URL = 'http://localhost:8091'
python -m pytest -m 'shop or api'
```

Public demos can change, reset data or become unavailable. This repository does
not ship their application code or promise immutable environments. See
[environment limitations and decisions](docs/automation-decisions.md).

## How the code is organized

```text
conftest.py                       # URLs, test-id contract, isolation configuration
pages/shop.py                     # catalog, product and cart interactions
tests/ui/test_shopping.py          # business assertions
tests/api/test_catalog_api.py      # read-only consumer contracts
tests/labs/test_web_interactions.py # focused learning exercises
docs/                             # rationale, coverage and investigation
.github/workflows/tests.yml        # Chromium workflow and diagnostics
```

Tests use real public applications without mocked responses. Each browser test
gets its own context. Cart tests create disposable anonymous demo carts; API
checks read catalog data. There are no personal accounts, credentials or real
payment data in this project.

## Results and continuous integration

The default GitHub Actions job runs **9 cases: 2 API checks and 7 interaction lab
exercises** on pushes to `main`, pull requests and manual dispatch. It runs serially
in Chromium and preserves JUnit results and failure artifacts for seven days.
No scheduled runs or automatic retries hide intermittent failures.

Initial validation: **18 tests passed locally on Windows in 69.92 seconds**.
When the complete suite ran on a GitHub-hosted runner, those 9 cases passed, but
Cloudflare human verification blocked the Toolshop website before its 9 business
scenarios could run. A green default workflow therefore does **not** mean all 18
cases passed in CI.

[The revised default CI run passed all 9 selected cases](https://github.com/baruth91/playwright-python-qa-case-study/actions/runs/40688756239)
on Ubuntu on 2026-10-28, with zero test failures or skips.

To explicitly attempt the Toolshop UI job, open **Actions → QA case study checks →
Run workflow**, enable `run_shop_ui`, and provide an authorized Toolshop URL reachable
from the runner. The hosted default may still present a challenge. Tests keep that
failure visible; this project does not automate human verification or bypass it.
Local `python -m pytest` still selects all 18 cases.

Read [the validation record](docs/validation.md) for the actual execution evidence
and the distinction between local verification and the GitHub workflow.
Read [failure investigation](docs/failure-investigation.md) before changing a
locator or increasing a timeout.

## Community contributions

This project is shared to help the QA community learn by doing. Questions,
improvements to explanations, and focused test contributions are welcome.
See [CONTRIBUTING.md](CONTRIBUTING.md). A useful contribution explains the risk,
the evidence and the smallest maintainable check that addresses it.

## References and attribution

- [Playwright Python documentation](https://playwright.dev/python/docs/intro)
- [Official pytest plugin](https://github.com/microsoft/playwright-pytest)
- [Toolshop application and usage terms](https://github.com/testsmith-io/practice-software-testing)
- [The Internet](https://the-internet.herokuapp.com/)
- [Automation Panda's tutorial](https://github.com/AutomationPanda/playwright-python-tutorial): inspiration for progressive teaching; the author notes parts are outdated.
- [Artem Bondar's practice app](https://github.com/bondar-artem/pw-practice-app): an additional UI practice reference.

Original test code and documentation in this repository are MIT licensed. The
practice applications retain their own licenses and terms. No third-party
application source is redistributed here.
