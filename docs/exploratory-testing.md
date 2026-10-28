# Exploration notes

Session date: 2026-10-27, America/Sao_Paulo.

## Charter

Explore product discovery and an anonymous cart to identify stable observable
outcomes, asynchronous boundaries and useful automation candidates.

## Observed evidence

- Toolshop displayed `v2.5`, build `2026-10-11`, Angular `20.0.5`.
- The catalog exposes `data-test` attributes. Product IDs are generated values;
  product names offer a more readable seed-data precondition.
- `Combination Pliers` was available with a displayed unit price of USD 14.15.
  The tests capture the current price rather than freezing this observation.
- The hosted UI uses `QUERY /products/search` and `QUERY /products` with request
  bodies; a direct read-only `GET /products` also works. Assuming every read uses
  GET caused the initial test synchronization failure and was corrected.
  The search heading can appear while old
  product cards remain visible; this was observed during the first probe.
- Cart navigation is asynchronous. Reading immediately after clicking initially
  returned the previous product page; waiting for cart content resolved that probe.
- The cart exposes product quantity, unit price, line price and a cart total.
- Proceeding to checkout reveals login and guest choices.
- `GET /products` provides paginated JSON. Product detail is retrieved by the ID
  obtained from the listing; hard-coded generated IDs are unnecessary.

## Automation implications

Register a response wait before triggering a search, then assert its rendered
outcome. Do not interpret a changed heading as proof of completed results. Wait
for destination content after navigation. Use `Decimal` for money. Create a new
browser context for every scenario so a cart from one test cannot satisfy another.

## Findings versus defects

The initial asynchronous observations are test-design findings, not confirmed
application defects. We do not invent bug reports to make the portfolio appear
more realistic. Record a product defect only after reproduction against a stated
expectation and inspection of the relevant evidence.

Exploration is intentionally bounded. It does not establish accessibility,
security, performance, inventory integrity or complete checkout correctness.
