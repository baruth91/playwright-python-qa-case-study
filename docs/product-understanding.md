# Understanding the product before automating it

## Context and objective

Toolshop is a demo store built for testing practice. A customer needs to find an
appropriate tool, understand its price and quantity, and carry the intended item
into checkout. Our first quality question is: can the customer get from product
discovery to the checkout identity step with a correct cart?

The initial objective deliberately ends before account creation and order
submission. A passing run provides evidence for that segment only.

## Actors and boundaries

- Anonymous customer: browses, searches and builds a cart.
- Catalog API: supplies listings and product details.
- Browser: renders results and holds an isolated anonymous session.
- External demo owner: controls releases, product data and availability.

## Working acceptance criteria

These are our educational acceptance hypotheses, informed by observed behavior
on 2026-10-27 (America/Sao_Paulo). They are not stakeholder-approved requirements.

1. Searching for the exact seeded name `Combination Pliers` returns that product.
2. An unmatched query displays an explicit empty state without stale cards.
3. A subsequent valid query recovers from an empty result.
4. Price sorting orders the products on the currently visible page numerically.
5. Adding one or three units preserves identity, unit price and quantity in the cart.
6. A line total equals unit price times quantity; a single-line cart has that same total.
7. Editing cart quantity recalculates the displayed totals.
8. A populated cart allows navigation to checkout's identity choices.
9. Catalog and detail API responses agree on product identity and price.

## Questions for a real product team

What is the authoritative price source? Are taxes, discounts and shipping included?
What are valid quantity limits? How does inventory reservation work? Is search
exact, partial or relevance-based? Does sorting apply across every page? Can guests
complete checkout? What browsers and assistive technologies do customers use?

Those questions drive future coverage. A demo's observed behavior alone cannot
establish the desired behavior of a real commerce system.
