# Silt & Form catalog delivery coverage · 8 September 2026

## Full-page correction and current limits

The [full-theme base](full-page-theme-evidence-2026-09-08.md) now renders five native Studio/editorial
pages and real account login/session behavior with package-owned head/header/footer and Alpine CSP.
[SOL-555](https://linear.app/solventech/issue/SOL-555) adds named reusable menus and declared theme slots.
Existing family pages listed below remain hybrid until integrated into that boundary. Full catalog,
other templates/providers, populated commerce and full reference equivalence remain outstanding;
this correction does not reduce the accepted census or complete SOL-530.

This is the coverage and dependency plan for milestone **Flux component catalog and working demo
theme**, `c75032a6-70a2-4830-9c8d-f8d3129639e5`. The user requires the full reference capability
catalog. Home, About and FAQ with five Studio components are the **first working foundation**, not
the milestone finish line. Coordinator 2 retains ownership of subsequent source-writing batches.

The accepted [reference inventory](section-library-reference-inventory-2026-09-08.md) is reused;
no new vendor-source crawl occurred. `component-library/reference/delivery-coverage.json` assigns
all 76 section stems exactly once, their 1,408 section-setting entries, 122 block definitions and
710 block-setting entries, both section groups, all 155 top-level global settings and seven nested
color-setting definitions. Metadata entries remain labeled metadata; they do not become merchant
values. A source hash pins the inventory used. Run `python3 component-library/scripts/plan-coverage.py`
from the workspace root to reproduce the mapping from the existing inventory alone.

Each field has its reference identity, capability intent, named delivery owner and original
implementation destination. Each section tracks editor, validator, native, data, template, evidence
and reference parity separately. The base five map to existing original types as a partial subset;
other destinations are explicitly planned. Field-equivalence evidence remains open even when a
base section has native rendering. This avoids converting a similar heading or layout into a false
claim that all reference settings, nested blocks and interactions are implemented.

## Delivery sequence and acceptance

| Task | Ownership / deliverable | Current boundary |
| --- | --- | --- |
| [SOL-526](https://linear.app/solventech/issue/SOL-526) | Original theme package, Home/About/FAQ defaults and scoped content shell | First populated template collection |
| [SOL-527](https://linear.app/solventech/issue/SOL-527) | Native equivalents of the five current Studio sections and CMS/media references | Existing local INOX default-store Luma pages only |
| [SOL-528](https://linear.app/solventech/issue/SOL-528) | Template choice, independent page editing, saves and preview | Local editor; no hosted ownership/inheritance claim |
| [SOL-529](https://linear.app/solventech/issue/SOL-529) | Save/apply/update/restore controls | Local fixed installation and registered page targets |
| [SOL-531](https://linear.app/solventech/issue/SOL-531) | Coverage map and full demo template collection | Map delivered; later family templates and behavioral parity remain open |
| [SOL-532](https://linear.app/solventech/issue/SOL-532) | 14 editorial/layout/base-setting stems | 14 native equivalents; explicit field gaps and substantive review remain |
| [SOL-533](https://linear.app/solventech/issue/SOL-533) | 10 interactive/media stems | 10 original native subsets on pages 246–247; explicit provider/field gaps and independent review remain |
| [SOL-534](https://linear.app/solventech/issue/SOL-534) | 19 catalog/product/search/purchase stems | Real Magento catalog, price/stock, variants, customer context and quote behavior |
| [SOL-535](https://linear.app/solventech/issue/SOL-535) | 21 shell/system/cart/account stems, groups and global settings | [13 original components on pages 250–253](shell-catalog-evidence-2026-09-08.md); five owned fragments and three unregistered semantic gaps; full acceptance open |
| [SOL-536](https://linear.app/solventech/issue/SOL-536) | Four form/promotion stems | [Four non-delivering original components on pages 254–256](forms-catalog-evidence-2026-09-08.md); 103 field entries, native form-key checks and browser-only values; capture/provider acceptance remains open |
| [SOL-537](https://linear.app/solventech/issue/SOL-537) | Eight provider/extension stems | Explicit providers and rights; missing services remain visible gaps |
| [SOL-530](https://linear.app/solventech/issue/SOL-530) | Final full-catalog acceptance | Blocked on the preceding work; never complete from a five-section screenshot |

For each family, deliver schema-driven controls, portable save/reload, registered native output,
actual provider data when required, populated demo scenarios, responsive and keyboard behavior,
unsafe/foreign input rejection and apply/restore evidence. Section registration or a static preview
card is insufficient. Do not close an owner while meaningful settings, blocks, template/snippet
behavior or provider requirements are silently absent. Record material semantic substitutions or
exclusions as explicit scope decisions.

## Native and provider boundaries

The initial native registry is a trusted Magento DI mapping of declarative component identities to
installed `RendererInterface` implementations. The portable schema is generated from installed
original packages. New package definitions supply generated editor fields and preview dispatch;
new native code and explicit target registrations supply Magento behavior. These are extension
points, not a completed installable SDK or permission system. Merchant JSON cannot choose a PHP
class, template, executable code, URL endpoint or filesystem path.

The first theme uses Magento-owned local media storage and active CMS pages scoped to store 1.
Later catalog, product, search, quote, account and order families must use the appropriate native
services and bounded local test sessions. No invented prices, fake cart success, customer data or
checkout imitation is acceptable. Provider families cannot assume that Magento core supplies a
blog, events, maps or arbitrary review feeds. Existing installed providers need explicit capability
and rights validation; missing providers are an unavailable state and outstanding work.

Shopify password/activation behavior requires an explicit Magento semantic decision. App and
custom-Liquid slots map to trusted installed developer/widget components; unrestricted merchant
Liquid and vendor-code execution are out of scope. The seven no-schema fragments are associated
with their native owning components rather than presented as seven addable sections. The three
malformed schemas (`footer`, `info-cards`, `main-product`) stay assigned; malformed JSON does not
exclude their feature intent. The accepted census does not itself prove relevant template/snippet
runtime behavior; each family must inspect and establish that behavior during implementation
without copying source, schemas, defaults, styling, fonts or assets.

## Exact section assignment

Classification counts remain 44 valid preset-bearing candidates, 22 fixed/no-preset sections,
seven fragments and three malformed schemas. The full field identities and original capability
intent are in the machine-readable map; the table below provides a readable section-level route
into each named owner. Editorial and interactive families now have local original subsets; the remaining families are planned. This is not full-catalog completion.

### SOL-532 · Editorial layouts and base settings

All 14 stems now have original package/native equivalents in two populated local templates.
This is **implemented subset coverage**, with explicit reference gaps and independent review pending.
The accepted five Studio definitions and saved foundation pages remain preserved. Expanded variants
are registered through `mte-editorial@1.0.0`, not silently added to existing versioned schemas.

[Editorial evidence, decisions and reversal](editorial-catalog-evidence-2026-09-08.md) and the
[field-by-field ledger](editorial-field-coverage-2026-09-08.md) distinguish verified supported controls
from partial substitutions and unresolved capabilities. `reference/editorial-coverage.json` covers
all 326 assigned census field entries; `plan-coverage.py` now preserves that overlay on regeneration.

| Reference stem | Original destination | Populated template | Partial or open field entries |
| --- | --- | --- | --- |
| `anchor-link` | `mte-editorial/anchor-link` | Editorial | 0 |
| `banner-two-columns` | `mte-editorial/banner-two-columns` | Editorial | 4 |
| `collapsible-content` | `mte-editorial/collapsible-content` | Stories | 2 |
| `heading-with-images` | `mte-editorial/heading-with-images` | Editorial | 1 |
| `image-banner` | `mte-editorial/image-banner` | Stories | 13 |
| `image-with-text` | `mte-editorial/image-with-text` | Stories | 6 |
| `info-cards` | `mte-editorial/info-cards` | Editorial | 3 |
| `main-page` | `mte-editorial/main-page` | Editorial | 0 |
| `multicolumn` | `mte-editorial/multicolumn` | Stories | 8 |
| `page` | `mte-editorial/page` | Editorial | 1 |
| `promotion-cards` | `mte-editorial/promotion-cards` | Editorial | 4 |
| `rich-text` | `mte-editorial/rich-text` | Stories | 7 |
| `separator` | `mte-editorial/separator` | Editorial | 0 |
| `two-images-text` | `mte-editorial/two-images-text` | Stories | 2 |

### SOL-533 · Interactive media

All ten stems have original portable definitions, controls, populated templates and native local interactions on dedicated INOX pages 246–247. The complete 299-entry [field ledger](interactive-field-coverage-2026-09-08.md) and [runtime/reversal evidence](interactive-catalog-evidence-2026-09-08.md) record partial support and unaccepted exclusions. No remote video, product, review or countdown provider is simulated.

| Reference stem | Original destination | Populated template | Coverage |
| --- | --- | --- | --- |
| `advanced-slider` | `mte-interactive/advanced-slider` | media | Native original subset; reference parity open |
| `comparison-slider` | `mte-interactive/comparison-slider` | media | Native original subset; reference parity open |
| `image-gallery` | `mte-interactive/image-gallery` | media | Native original subset; reference parity open |
| `image-hotspots` | `mte-interactive/image-hotspots` | media | Native original subset; reference parity open |
| `scrolling-text` | `mte-interactive/scrolling-text` | motion | Native original subset; reference parity open |
| `slick-slider` | `mte-interactive/slick-slider` | motion | Native original subset; reference parity open |
| `tabs` | `mte-interactive/tabs` | media | Native original subset; reference parity open |
| `testimonials` | `mte-interactive/testimonials` | motion | Native original subset; reference parity open |
| `video-background` | `mte-interactive/video-background` | motion | Native original subset; reference parity open |
| `video` | `mte-interactive/video` | motion | Native original subset; reference parity open |

### SOL-534 · Magento catalog and purchase

Magento catalog/search, scoped customer price/stock, variants, quote/cart, pickup service when available. Planned template collection: Opt-in collection, product, search and purchase scenarios.

| Reference stem | Classification | Original destination | Settings / blocks / block settings | Coverage |
| --- | --- | --- | --- | --- |
| `collection-list` | valid-preset-bearing | Planned collection list equivalent | 27 / 1 / 3 | Outstanding |
| `collection-tabs` | valid-preset-bearing | Planned collection tabs equivalent | 52 / 1 / 2 | Outstanding |
| `featured-collection` | valid-preset-bearing | Planned featured collection equivalent | 44 / 1 / 15 | Outstanding |
| `featured-collections` | valid-preset-bearing | Planned featured collections equivalent | 18 / 5 / 17 | Outstanding |
| `featured-product` | valid-preset-bearing | Planned featured product equivalent | 18 / 19 / 72 | Outstanding |
| `image-banner-with-collections` | valid-preset-bearing | Planned image banner with collections equivalent | 52 / 1 / 5 | Outstanding |
| `image-banner-with-featured-collection` | valid-preset-bearing | Planned image banner with featured collection equivalent | 49 / 4 / 19 | Outstanding |
| `main-collection-banner` | valid-fixed-no-preset | Planned main collection banner equivalent | 17 / 0 / 0 | Outstanding |
| `main-collection-product-grid` | valid-fixed-no-preset | Planned main collection product grid equivalent | 51 / 1 / 15 | Outstanding |
| `main-list-collections` | valid-fixed-no-preset | Planned main list collections equivalent | 10 / 0 / 0 | Outstanding |
| `main-product` | malformed-json-schema | Planned main product equivalent | 38 / 25 / 261 | Outstanding |
| `main-search` | valid-fixed-no-preset | Planned main search equivalent | 23 / 0 / 0 | Outstanding |
| `pickup-availability` | fragment-no-schema | Planned pickup availability equivalent | 0 / 0 / 0 | Outstanding |
| `predictive-search` | fragment-no-schema | Planned predictive search equivalent | 0 / 0 / 0 | Outstanding |
| `quick-order-list` | valid-preset-bearing | Planned quick order list equivalent | 8 / 0 / 0 | Outstanding |
| `recently-viewed-products` | valid-preset-bearing | Planned recently viewed products equivalent | 35 / 0 / 0 | Outstanding |
| `related-products` | valid-fixed-no-preset | Planned related products equivalent | 28 / 0 / 0 | Outstanding |
| `sticky-add-to-cart` | valid-preset-bearing | Planned sticky add to cart equivalent | 16 / 0 / 0 | Outstanding |
| `subcollections` | valid-fixed-no-preset | Planned subcollections equivalent | 26 / 0 / 0 | Outstanding |

### SOL-535 · Theme shell, global settings and system

Magento native region, navigation, customer/account/order/quote services; explicit password/activation semantic decisions. Planned template collection: Opt-in shell, cart, account and error states.

| Reference stem | Classification | Original destination | Settings / blocks / block settings | Coverage |
| --- | --- | --- | --- | --- |
| `announcement-bar` | valid-preset-bearing | Planned announcement bar equivalent | 25 / 1 / 2 | Outstanding |
| `cart-drawer` | fragment-no-schema | Planned cart drawer equivalent | 0 / 0 / 0 | Outstanding |
| `cart-icon-bubble` | fragment-no-schema | Planned cart icon bubble equivalent | 0 / 0 / 0 | Outstanding |
| `cart-live-region-text` | fragment-no-schema | Planned cart live region text equivalent | 0 / 0 / 0 | Outstanding |
| `cart-notification-button` | fragment-no-schema | Planned cart notification button equivalent | 0 / 0 / 0 | Outstanding |
| `cart-notification-product` | fragment-no-schema | Planned cart notification product equivalent | 0 / 0 / 0 | Outstanding |
| `footer` | malformed-json-schema | Planned footer equivalent | 40 / 5 / 24 | Outstanding |
| `header` | valid-fixed-no-preset | Planned header equivalent | 59 / 2 / 58 | Outstanding |
| `main-404` | valid-fixed-no-preset | Planned main 404 equivalent | 8 / 0 / 0 | Outstanding |
| `main-account` | valid-fixed-no-preset | Planned main account equivalent | 5 / 0 / 0 | Outstanding |
| `main-activate-account` | valid-fixed-no-preset | Planned main activate account equivalent | 3 / 0 / 0 | Outstanding |
| `main-addresses` | valid-fixed-no-preset | Planned main addresses equivalent | 4 / 0 / 0 | Outstanding |
| `main-cart-footer` | valid-fixed-no-preset | Planned main cart footer equivalent | 7 / 5 / 8 | Outstanding |
| `main-cart-items` | valid-fixed-no-preset | Planned main cart items equivalent | 8 / 0 / 0 | Outstanding |
| `main-login` | valid-fixed-no-preset | Planned main login equivalent | 5 / 0 / 0 | Outstanding |
| `main-order` | valid-fixed-no-preset | Planned main order equivalent | 3 / 0 / 0 | Outstanding |
| `main-password-footer` | valid-fixed-no-preset | Planned main password footer equivalent | 2 / 0 / 0 | Outstanding |
| `main-password-header` | valid-fixed-no-preset | Planned main password header equivalent | 4 / 0 / 0 | Outstanding |
| `main-register` | valid-fixed-no-preset | Planned main register equivalent | 5 / 0 / 0 | Outstanding |
| `main-reset-password` | valid-fixed-no-preset | Planned main reset password equivalent | 3 / 0 / 0 | Outstanding |
| `quick-info-bar` | valid-preset-bearing | Planned quick info bar equivalent | 30 / 0 / 0 | Outstanding |

### SOL-536 · Forms and promotions

Magento form keys/session, consent, controlled local capture; no real email or campaign sends. Planned template collection: Contact, newsletter and promotion scenarios.

| Reference stem | Classification | Original destination | Settings / blocks / block settings | Coverage |
| --- | --- | --- | --- | --- |
| `contact-form` | valid-preset-bearing | Planned contact form equivalent | 30 / 0 / 0 | Outstanding |
| `email-signup-banner` | valid-preset-bearing | Planned email signup banner equivalent | 17 / 4 / 9 | Outstanding |
| `newsletter` | valid-preset-bearing | Planned newsletter equivalent | 13 / 4 / 5 | Outstanding |
| `popup` | valid-preset-bearing | Planned popup equivalent | 29 / 0 / 0 | Outstanding |

### SOL-537 · Providers and trusted extensions

Magento review ownership; explicit installed blog/event/map/review provider and rights; installed developer slots instead of executable merchant Liquid. Planned template collection: Provider capability collection with honest unavailable states.

| Reference stem | Classification | Original destination | Settings / blocks / block settings | Coverage |
| --- | --- | --- | --- | --- |
| `apps` | valid-preset-bearing | Planned apps equivalent | 4 / 1 / 0 | Outstanding |
| `custom-liquid` | valid-preset-bearing | Planned custom liquid equivalent | 7 / 0 / 0 | Outstanding |
| `ep-reviews-carousel` | valid-preset-bearing | Planned ep reviews carousel equivalent | 31 / 0 / 0 | Outstanding |
| `events-calendar` | valid-preset-bearing | Planned events calendar equivalent | 21 / 1 / 17 | Outstanding |
| `featured-blog` | valid-preset-bearing | Planned featured blog equivalent | 29 / 0 / 0 | Outstanding |
| `location-map` | valid-preset-bearing | Planned location map equivalent | 27 / 0 / 0 | Outstanding |
| `main-article` | valid-fixed-no-preset | Planned main article equivalent | 5 / 7 / 6 | Outstanding |
| `main-blog` | valid-fixed-no-preset | Planned main blog equivalent | 19 / 0 / 0 | Outstanding |

## Groups and global settings

Both groups are assigned to SOL-535. Footer-group popup behavior also depends on SOL-536.

| Group | Referenced owners | State |
| --- | --- | --- |
| `sections/footer-group.json` | footer, popup | Outstanding native region group |
| `sections/header-group.json` | announcement-bar, header | Outstanding native region group |

All global groups below belong to SOL-535; field-level identities, including nested color definitions, remain in the map. The foundation’s two scoped accent/spacing tokens do not complete these globals.

| Reference global group | Top-level settings | State |
| --- | --- | --- |
| `t:settings_schema.logo.name` | 5 | Equivalence outstanding |
| `t:settings_schema.breadcrumbs.name` | 4 | Equivalence outstanding |
| `t:settings_schema.animations.name` | 9 | Equivalence outstanding |
| `t:settings_schema.colors.name` | 1 | Equivalence outstanding |
| `t:settings_schema.colors_add.name` | 19 | Equivalence outstanding |
| `t:settings_schema.typography.name` | 12 | Equivalence outstanding |
| `t:settings_schema.layout.name` | 6 | Equivalence outstanding |
| `t:settings_schema.buttons.name` | 5 | Equivalence outstanding |
| `t:settings_schema.global_design.name` | 11 | Equivalence outstanding |
| `t:settings_schema.cards.name` | 4 | Equivalence outstanding |
| `t:settings_schema.quick_view.name` | 2 | Equivalence outstanding |
| `t:settings_schema.blog_cards.name` | 1 | Equivalence outstanding |
| `t:settings_schema.badges.name` | 12 | Equivalence outstanding |
| `t:settings_schema.social-media.name` | 13 | Equivalence outstanding |
| `t:settings_schema.search_input.name` | 4 | Equivalence outstanding |
| `t:settings_schema.currency_format.name` | 3 | Equivalence outstanding |
| `t:settings_schema.cart.name` | 37 | Equivalence outstanding |
| `Mixpanel analytics` | 7 | Equivalence outstanding |

## Foundation evidence and handoff

Use the [starter/native evidence](section-library-evidence-2026-09-08.md#silt-form-starter-foundation) for the actual first delivery and the [developer package guide](../architecture/developer-packages.md#silt-form-starter-theme-package) for extension points. Each later owner updates its statuses only after producing its own native and merchant-flow evidence. Preserve the accepted notice package, 03C/03D/03F evidence, manual drafts, current branches and ordinary storefront behavior.

## SOL-534 original commerce subset

The [commerce evidence](commerce-catalog-evidence-2026-09-08.md) and
[field/block ledger](commerce-field-coverage-2026-09-08.md) cover exactly 19 stems, 921 settings
and 58 blocks. The [9 September full-theme delivery](full-theme-commerce-evidence-2026-09-09.md) adds populated collection/product/search, native simple cart/totals and authenticated checkout transition. Six reference mappings have bounded populated evidence. Historical pages 248–249 expose native catalog/search/SKU reads and honest missing
data/provider states. No populated catalog or purchase success is claimed. Default Luma store
data is unusable for positive product/category proof; foreign website data is rejected.
All material substitutions and 684 open setting gaps remain unaccepted. SOL-534 remains In Progress.
