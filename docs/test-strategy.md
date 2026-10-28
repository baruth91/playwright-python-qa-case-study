# Test strategy

## Scope and test layers

The UI suite covers the anonymous journey from discovery to the checkout identity
step. Two API checks add a minimal catalog consumer contract and listing/detail
consistency. Seven independent labs teach difficult web interactions.

We do not own the demo application's unit or integration layers, so this is not
a complete test pyramid. API tests complement UI tests; they do not replace the
browser evidence about rendering and interactions.

## Execution and data

- Chromium is the initial verified browser target, using an English desktop viewport.
- Every test has a fresh browser context; no login state or cart is reused.
- UI tests depend on one explicit seed name, `Combination Pliers`.
- Prices and generated IDs are read at runtime; no USD 14.15 assertion is baked in.
- API checks are read-only. Cart scenarios use anonymous disposable demo data.
- Upload exercises create a synthetic temporary file.
- Run serially, without automatic retries or scheduled traffic against public demos.
- Default CI selects the 2 API checks and 7 labs. The 9 Toolshop UI scenarios are
  a separate manual opt-in job because the public host challenged GitHub runners.
  A green default CI result validates those 9 selected cases only; the separate
  Toolshop job is intentionally not run unless explicitly requested.

## Evidence and failure policy

A meaningful pass requires asserting the business result, not only that a click
or request completed. Store traces and screenshots on failure and JUnit results
for the run. A missing seed, DNS failure or HTTP error is a visible failure to
investigate; tests do not silently skip it or fabricate replacement data.

## Entry and completion criteria

Entry: required dependencies and browser installed, named demos reachable, seed
item available, and the stated hypotheses appropriate for the environment.

Initial completion: all implemented scenarios pass on the declared baseline,
each scenario maps to a risk or learning objective, setup is reproducible, and
limitations are documented. GitHub CI execution must be verified separately after
publication. These criteria do not constitute product release approval.

## Explicit exclusions

Order submission, real payments, account creation, authenticated authorization,
load/security testing, full accessibility audits, mobile validation, visual
regression, discount/tax logic, multiple-item totals and global pagination order.

Future work should follow a newly stated risk and observable contract. Adding a
framework, plugin or abstraction requires a maintenance or teaching benefit.
