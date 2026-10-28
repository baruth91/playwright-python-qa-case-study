# Automation decisions

## Python, pytest and the official Playwright plugin

The requested language is Python. pytest offers readable functions,
parametrization and fixtures. The official plugin provides independent browser
contexts and failure artifacts, avoiding a custom browser lifecycle framework.
The synchronous API keeps the first learning path approachable.

## Small page objects and explicit assertions

Only repeated shopping interactions are extracted. Assertions about identity,
quantity and money remain in the test so a reader can see its oracle. Labs stay
as direct tests because their interactions are the lesson. No base-page hierarchy,
generic click wrappers or BDD layer is required for the initial problem.

## Locator choices

Toolshop provides `data-test`; configuration sets this as the Playwright test-id
attribute. We also use roles and visible names. Generated IDs and Angular classes
are avoided. In The Internet, IDs are used where controls have no suitable label;
that is a documented compromise rather than a universal selector rule.

## Synchronization and diagnosis

Search and sorting issue asynchronous API requests. Waits are registered before
the triggering action; web-first assertions then check rendered state. We do not
use `sleep`, `force=True`, arbitrary global network-idle waits or retry plugins.
Expected dynamic-control delays use a focused 15-second assertion timeout.

## Monetary oracle

Use `Decimal`, not floating point. Read the unit price from the product screen,
calculate independently in test code, and compare the cart's amounts. This detects
inconsistency and arithmetic errors. It cannot prove that the upstream catalog's
price is commercially correct; a real system needs an independent price contract.

## Public demos and reproducibility

No public URL is assumed immutable. The first suite runs on the hosted demos to
minimize setup for learners. The repository includes configuration for equivalent
authorized environments, but does not vendor their code. Toolshop's repository
documents local Docker execution and restrictions on redistribution and hosting.
Before packaging a local application, review its current terms. A future controlled
baseline should record application revision, seed data and browser version.

## Dependency baseline and maintenance

The initial versions are exact pins matching the installed baseline used for
validation: Python 3.13, Playwright 1.52.0, pytest 8.3.5 and pytest-playwright 0.7.0.
This is not a claim of latest-version support. Upgrade as a separate change:
install the corresponding browsers, rerun the full suite and update the validation
record. Transitive dependencies are not fully locked in this first iteration.

## Honest scope

The first journey ends at checkout identity. Completing checkout needs additional
acceptance criteria, synthetic identity data and a controlled demo payment flow.
We prefer a verified, clearly bounded example over an unverified full-purchase
claim. Removal, boundary quantities, multiple-item carts and category filtering
are candidates for the next increment, not implemented coverage.
