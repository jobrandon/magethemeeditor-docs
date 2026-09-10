# Product overview

Status: confirmed product direction with an architecture recommendation to validate.
Updated: 7 September 2026. Sources: the [research baseline](../architecture/theme-editor-research-2026-09-07.md),
the user's subsequent hybrid-adoption direction, and the
[live-read Linear project baseline](../roadmap/linear-baseline-2026-09-07.md).

## Default-theme requirement · 8 September 2026

The original default-theme candidate must own selected pages from head to footer, with shared
menus/settings, Header / Template / Footer editing, Alpine CSP storefront behavior independent of
RequireJS/Luma JavaScript, and Magento-owned account/catalog/cart/checkout operations. See the
[full-theme contract](../architecture/full-page-theme.md) and
[populated local commerce evidence](../roadmap/full-theme-commerce-evidence-2026-09-09.md).
The complete Flux capability set remains required; the first five full-theme pages are not final scope.

## Merchant outcome

Help merchants and agencies make routine storefront changes, preview the actual result, publish
deliberately, and restore a previous state while keeping Magento's commerce behavior intact.
Reduced developer effort is a product hypothesis; customer demand, willingness to pay, and time
savings have not been measured.

## Adoption paths

| Path | Intended editing surface | Required boundary |
| --- | --- | --- |
| Existing storefront, selected pages | Home/CMS pages, selected PDPs, selected category pages | Explicit assignment and renderer selection; retain the active theme and unassigned pages |
| Existing storefront, selected regions | Declared slots in otherwise unchanged templates | Registered adapter, one renderer per region, scoped styles/scripts |
| Free compatible reference theme | Broad control over exposed tokens, sections, header/footer variants, navigation, supported templates | Theme contract and support matrix; commerce regression proof still required |

A merchant does not need to replace the whole storefront to use a supported page or region.
The complete editing path uses a compatible theme designed to expose its controls. Neither path
makes arbitrary hardcoded PHP or third-party extension markup automatically editable.
See [hybrid adoption](../requirements/hybrid-adoption.md).

## Ownership

The product's private infrastructure owns the hosted editor, account/store permissions, drafts,
validation, publishing coordination, history, and future automation. Magento owns catalog,
prices, tax, inventory, sessions, carts, checkout, orders, and native review data. Published JSON
and assets are versioned; a generic local runtime renders supported components.

Initial installation and new native capabilities may require Magento deployment. Routine edits
within installed capabilities should publish as data. Subscription/outage behavior still needs
validation and final policy; the recommendation is to preserve the last local publication.

## Private-beta boundaries

The intended initial library is restrained: hero, text/image, product and category presentations,
FAQ, announcements, trust content, and declared theme controls. Final supported versions, product
types, page surfaces, and library size remain scope work.

Checkout replacement, universal theme conversion, a general template engine, hosted headless
rendering, and an unrestricted marketplace are outside the initial commitment. Liquid is optional;
it is not a dependency for JSON settings or native Magento templates. Locator, advanced reviews,
app blocks, and assisted editing require later discovery.

## Future creator ecosystem

The user has confirmed third-party themes and an eventual marketplace as future direction.
Developers can author their own themes, sections, and blocks against our standards; creators may
later sell themes through seller accounts, with a possible platform commission on theme sales.
The [future ecosystem roadmap](../roadmap/theme-ecosystem.md) proposes staged delivery and preserves
hybrid adoption. Actual Liquid support, authoring runtime, commercial terms, and delivery dates
remain undecided. Marketplace implementation is outside the initial editor scope.

## Validation before product claims

Interview merchants and agencies about recent changes, current effort, incumbent editors, adoption
constraints, and willingness to pay. Prove a complete editing/publishing/restoration task on both
declared theme fixtures. Establish success metrics from a baseline before setting targets or
claiming conversion lift. The [validation plan](../requirements/validation-plan.md) defines the
evidence still needed.
