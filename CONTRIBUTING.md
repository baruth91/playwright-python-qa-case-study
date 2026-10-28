# Contributing

Questions and beginner-friendly improvements are welcome. Keep public discussion,
documentation, code and test names in English so the material is accessible to
the international QA community.

Before adding a test, describe the customer risk or learning objective, the
observable expected outcome, the data needed and why existing coverage misses it.
Update `docs/coverage-map.md` and explain any environment assumptions.

Run the focused scenario while developing, then `python -m pytest` before opening
a pull request. Include the command, versions, result and any remaining limits.
Use only synthetic data and authorized practice environments. Keep public-demo
traffic modest. Do not introduce sleeps, retries that mask failures, copied
application source, credentials or personal data.

Prefer small readable changes with concrete validation. A useful bug report
includes reproduction steps, expected and actual behavior and an explanation of
whether the problem is in this test project or the external demo.
