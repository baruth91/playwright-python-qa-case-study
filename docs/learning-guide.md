# Guided walkthrough

## 1. Start with a customer problem

Read `product-understanding.md` and `risk-assessment.md`. Explain why a wrong cart
total could matter, and why an empty-state recovery deserves its own scenario.
Then run `python -m pytest -m smoke --headed`.

## 2. Read one test from beginning to end

Open `tests/ui/test_shopping.py` and find
`test_cart_preserves_product_quantity_and_amounts`. Its arrange phase locates a
known product and captures its unit price. Its action adds a specified quantity.
Its assertions verify identity, quantity and three monetary displays.

For three units at a displayed USD 14.15, the independently calculated expected
line amount is USD 42.45. The implementation captures the live price so this
illustration does not become a hidden fixed-price dependency.

Run the two variants with:

```bash
python -m pytest tests/ui/test_shopping.py -k preserves --headed
```

## 3. Follow an interaction into the page object

Open `pages/shop.py`. `Catalog.search` waits for the request caused by the action.
The test then checks the product list. Request completion and correct screen
content are distinct pieces of evidence. `Product.add_to_cart` waits for the cart
badge, navigates and waits for the cart total. pytest supplies a clean session
for the next test.

## 4. Understand the API layer

Run `python -m pytest -m api`. One test checks only fields the consumer needs;
another takes an ID from the catalog and reads that product's details. Neither
test changes demo data. Consider what an independently maintained price contract
would add beyond checking agreement between two endpoints.

## 5. Practice focused browser techniques

Run `python -m pytest -m lab --headed`. Each exercise introduces one idea. Notice
that clicking a checkbox would depend on its starting state, while `check()`
expresses the intended state. Notice that a dialog handler must exist before
the button is clicked. The upload uses generated text, not a personal file.

## 6. Investigate a deliberate local failure

On a temporary branch, change an expected quantity to an incorrect value and run
only that scenario. Read the assertion error and open its generated trace:

```bash
python -m playwright show-trace test-results/<failed-test-directory>/trace.zip
```

Replace the placeholder with the actual generated directory. Inspect the state
before and after the action. Restore your temporary change before committing.
Use `failure-investigation.md` to distinguish a test error from an application
or environment failure.

## 7. Add one justified scenario

Propose multiple-item cart aggregation. Write the risk, preconditions and expected
result first. Explain why the current single-item arithmetic tests cannot detect
the same failure. Implement the smallest useful addition and update the coverage
map. Avoid claiming coverage you have not executed.
