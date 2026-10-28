# Investigating a failed run

1. Record the failing test ID, command, environment, browser and time.
2. Read the first relevant failure. DNS errors, HTTP errors and assertion failures
   imply different investigations.
3. Open the screenshot and trace in `test-results/`. Review the request, action,
   locator resolution and before/after DOM snapshots.
4. Check whether the named product still exists and whether the demo changed.
5. Reproduce the single scenario once with `--headed`. Do not repeatedly hammer
   a public demo or rerun until a green result replaces the evidence.
6. Compare the result with the stated acceptance hypothesis. Categorize as a
   product issue, test issue, changed contract, environment issue or unresolved.
7. Make a focused fix or record a reproducible defect. Run affected checks and
   then the appropriate regression scope.

## Common examples

- A cart total mismatch may indicate a product calculation problem. Compare unit
  price, selected quantity and request payload before changing the assertion.
- Missing `Combination Pliers` may be changed seed data. Do not silently choose
  any random product; update the precondition and explain the change.
- A sort assertion that captured the old list may indicate missing synchronization.
  Wait for an explicit rendered outcome instead of inserting a fixed delay.
- An unreachable public demo is an environment failure. It is not evidence that
  the product's business behavior regressed.

## Defect report template

```text
Title:
Environment and application version:
Risk / acceptance hypothesis:
Preconditions and synthetic data:
Steps to reproduce:
Expected result:
Actual result:
Evidence and reproduction frequency:
Customer impact:
Open questions:
```

Review diagnostics before sharing them: real projects may capture private data in
screenshots and traces. This demo suite uses public pages and synthetic input.
