# Coverage map

Identifiers appear in test docstrings. Parametrized variants are counted as
separate executed tests: 9 shop + 2 API + 7 labs = 18 cases.

| ID | Scenario | Risk or learning purpose | Location |
| --- | --- | --- | --- |
| SHOP-01 | Exact known-product search | R1: discovery | `tests/ui/test_shopping.py` |
| SHOP-02 | Unmatched query and empty state | R1: no stale results | same |
| SHOP-03 | Empty-to-valid search recovery | R1: recoverable journey | same |
| SHOP-04a/b | Ascending and descending price | R4: numeric visible-page order | same |
| SHOP-05a/b | Add 1 and 3 units | R2: identity, quantity, unit/line/cart amounts | same |
| SHOP-06 | Edit quantity in cart | R2: recalculation | same |
| SHOP-07 | Search to checkout identity | R3: integration journey | same |
| API-01 | Catalog consumer contract | R5: usable IDs, names, prices | `tests/api/test_catalog_api.py` |
| API-02 | Listing/detail consistency | R5: same identity and price | same |
| LAB-01 | Native dropdown | Select and verify state | `tests/labs/test_web_interactions.py` |
| LAB-02 | Checkboxes | Idempotent state-setting | same |
| LAB-03 | Dynamic loading | Wait for rendered outcome | same |
| LAB-04 | Disabled-to-enabled input | Assert state before interaction | same |
| LAB-05 | Confirm cancellation | Handler registered before trigger | same |
| LAB-06 | Synthetic upload | File payload and visible confirmation | same |
| LAB-07 | Nested frames | Explicit document boundaries | same |

## What these checks cannot establish

An API/UI price comparison establishes consistency, not an independently correct
business price. Single-line totals do not prove multi-item aggregation, taxes or
discounts. Visible-page sorting does not prove global order across pagination.
Reaching identity does not prove a successful purchase. A file-name confirmation
does not prove secure storage or content validation. No coverage percentage is
claimed because the full requirement set is unknown.
