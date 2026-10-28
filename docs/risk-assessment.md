# Risk assessment

These ordinal priorities are educational judgments, not measured production
incident probabilities. Impact describes the hypothetical customer harm;
likelihood describes plausible failure opportunities in this journey.

| Risk | Impact | Likelihood | Priority | Initial response |
| --- | --- | --- | --- | --- |
| R1: Customer cannot discover a known item | High | Medium | High | Exact search, empty state, recovery |
| R2: Cart loses identity, quantity or monetary consistency | High | Medium | High | Quantity examples and arithmetic checks |
| R3: Customer cannot progress from cart | High | Medium | High | Search-to-checkout identity journey |
| R4: Price sorting misleads comparison | Medium | Medium | Medium | Both numeric directions on visible page |
| R5: Catalog and detail API disagree | High | Medium | High | Read-only consistency check |
| R6: Public environment changes or fails | Medium | High | High | Explicit assumptions and retained diagnostics |

## Why automate these checks?

They are repeatable, produce observable outcomes and protect a recognizable
customer journey. The price examples exercise both a single unit and a quantity
greater than one. The recovery scenario tests a state transition that isolated
happy paths would miss.

## Why leave other work exploratory for now?

Visual usability, product relevance and broad accessibility need richer judgment
and dedicated methods. Authentication, payments, multiple-item promotions,
inventory races and abuse prevention need explicit contracts and controlled data.
Their omission is a coverage gap, not a declaration that their risk is low.

The interaction lab has learning objectives rather than commerce risk IDs. Its
seven examples must not inflate claims about business coverage.
