# Full-page theme and shared navigation

Status: **required default-theme architecture; populated local commerce integration verified 9 September 2026**.
This supersedes the CMS-content-only shell as the final architecture. The optional
[hybrid path](../requirements/hybrid-adoption.md) remains supported by its separate experiments.
See [current commerce evidence and remaining gaps](../roadmap/full-theme-commerce-evidence-2026-09-09.md) and the [first boundary evidence](../roadmap/full-page-theme-evidence-2026-09-08.md).

## Required outcome

A selected full-theme page has one theme owner from head to footer. The package owns head metadata,
assets, announcement, header/navigation, page template, footer and shared appearance. The editor
exposes **Header / Template / Footer**, shared theme settings and reusable menus. A CMS region inside
an inherited INOX/Luma masthead, iframe, CSS-hidden wrapper, duplicate menu/logo, or static account
link card cannot satisfy full-theme acceptance. Unassigned routes retain their existing renderer.

The user selected **Alpine.js for the shopper-facing default theme**, with an explicit local asset
set independent of RequireJS and Luma JavaScript. The existing React editor remains separate.
Magento owns authentication, customer/session state, catalog/prices/inventory, quote/cart, orders,
form-key checks and checkout. Backend services are retained even when their old presentation is absent.
No custom payment/checkout implementation is authorized by this choice.

## Current Magento boundary

The original `MageThemeEditor/silt` theme has no Luma or Hyvä parent. `FullThemeDesign` chooses it
only for the exact selected local store-1 routes. `FullThemeBoundary` loads the package's page
configuration handle `mte_fulltheme` and separate page-layout handle `mte_full_theme`; inherited
`default` handles do not join that layout. The full page is produced by native Magento layout and
a trusted block, with the installed package renderers reused through declared full-theme capabilities inside its main region.

The theme's original root template and explicit head renderer exclude inherited head/includes and
marketing assets. Required CSS/JavaScript URLs include a source-content SHA prefix, so an ordinary
reload loads changed assets without altering the host's static-cache settings. Selected responses
are private/no-store; global Magento cache types remain enabled. This is local development behavior,
not general FPC, multi-node, hosted publication or release-installation proof.

Native account/cart aliases under `/mte-theme/` dispatch the actual allowlisted Magento controllers.
Generated account URLs, including store-code and controller-index variants, stay inside that
scope. Guest login, successful authentication, invalid-form-key rejection and logout have browser
proof. Native registration, password recovery, addresses and orders remain unfinished. The cart
uses native add/update/remove controllers and quote totals. A dedicated authenticated test session reached
native checkout shipping UI; no order/payment was submitted and normal checkout was not modified.

## Shared resources and page content

`component-library/themes/silt-form/full/model.mjs` declares the full-theme identity/version,
registered pages, supported menu slots and original defaults. Trusted package `fullTheme` declarations
are compiled into `full-capabilities.json`; native DI supplies declared service adapters. Template
eligibility is not an editor namespace filter. Explicit per-component route bindings distinguish current
entity context from independent authored featured references. The local envelope has:

| Resource | Ownership and persistence |
| --- | --- |
| `global.settings` | Wordmark, announcement, footer note, accent, system-font choice, spacing, navigation layout |
| `global.menus` | Named reusable menu trees with stable menu/item IDs and explicit store 1 scope |
| `global.slots` | Header/footer assignments to existing menu IDs; no inline hardcoded page-link array |
| `pages[key]` | Independent template selection, head title/description, resource revision and existing validated content document |

Template selection copies defaults into one page buffer. It does not edit the factory, another page,
or shared navigation. Fourteen registered resources include focused Home/collection/product/search pages and separate
capability examples. Existing portable content documents retain their schema and identities.
The full-theme envelope is additive; historical CMS-region drafts/selections are not migrated.

Each page and the shared-resource collection have independent save revisions. Native `State` reads
the current draft under a file lock and replaces only the requested resource after comparison.
Apply checks the observed active digest and complete saved-draft digest, validates all references,
and atomically replaces one manifest containing the complete theme, pages, menus and assignments.
Previous restoration swaps coherent snapshots; original restoration removes the full-theme
selection while retaining saved resources. This first bridge applies the saved theme as a unit;
per-page publication and independent per-menu revision history remain open. Older snapshots can omit
new pages; their restoration remains valid. New defaults are added to the editable draft without replacing
existing page resources.

The bridge binds to the loopback editor, exact Origin/Host, JSON size/type, fixed PHP executable,
fixed installation and fixed command. Merchant JSON cannot choose an executable, native class,
filesystem path, installation, route prefix or store. There is no public apply endpoint on Magento.

## Developer menu contract

Header declares `dropdown` and structured `mega` presentation; Footer declares `columns`. Both
support at most three levels. Menus are data resources assigned to slots, rather than markup in
page sections. The local collection permits 1–12 menus and 100 items total; stable identities must
be unique. Duplicating a menu creates fresh menu/item IDs. Tree structure, uniqueness and depth
checks prevent cycles, orphaned children and excessive nesting.

An item declares a plain-text label, target type/reference, visibility (`all`, `guest`, `customer`,
`hidden`), new-window behavior, optional original menu image/description, and ordered children.
Supported targets are registered full-theme pages/native services, Magento CMS/category/product
references, or validated HTTPS external URLs without credentials or executable schemes. Magento
repositories resolve current store/website visibility; selected category/product links resolve to
the full-theme collection/product templates, with query-aware current-link state; missing or disabled active targets render
an unavailable state, and applying unresolved/foreign references rejects before activation.

The native renderer consumes the same named tree and slot assignments on every template. Current
links have `aria-current`; new windows use `noopener noreferrer`. Original image/description cards
supply the implemented mega-menu subset. Full Flux header-block/mega-menu equivalence remains open.
The old hybrid route's host navigation is unaffected by these resources.

## Merchant workflow

1. Open the full-theme editor at `http://127.0.0.1:4177/theme` (also the default 4177 entry).
2. Select a page. Use Template to change starter, sections/blocks, content and head metadata.
3. Use Header, Footer and Theme settings for shared appearance and menu assignments.
4. Use Menus to create/name/duplicate menus. Expand an item to edit it; use its drag handle to reorder
   siblings, or keyboard-accessible arrows and Indent/Outdent controls. Undo/Redo recover buffer edits.
   An unused menu may be removed; assigned menus cannot be removed without reassigning their slots.
5. Save the affected page or shared resources. Save all changed resources before Apply saved theme.
6. Open Magento to use native account/cart behavior. Preview links switch page buffers; account/bag
   links open their native full-theme routes. The preview contains no iframe and no private session data.
7. Restore previous or Restore original from the toolbar. Saved resources remain available to apply again.

## Alpine and rights boundary

The pinned shipped CSP build is `@alpinejs/csp@3.17.2`, with `@vue/reactivity@3.5.40` and
`@vue/shared@3.5.40`. Exact manifests, integrity values and notices are recorded in product's
third-party inventory and `alpine-review-2026-09-08.md`. Both MIT notices accompany and are embedded
in the served runtime. The [tagged Alpine notice](https://github.com/alpinejs/alpine/blob/v3.17.2/LICENSE.md)
and [official CSP-build documentation](https://alpinejs.dev/advanced/csp) support the bounded adoption.
No paid Alpine UI or Hyvä/Flux vendor code/assets are used; no additional hosted service is required.
This is reviewed local development use, not overall commercialization clearance.

External named `siltNavigation`/`siltDisclosure` components own responsive disclosure state, outside
clicks and Escape/focus behavior. Directives use named methods/providers; scripts require neither
unsafe-eval nor inline scripts. The package CSP meta policy restricts scripts to self. Selected responses also retain inherited Magento CSP response headers, including a broad policy with unsafe-eval and third-party origins. Browser policies intersect; this is not exclusive header-level CSP ownership. Header-level policy control remains a local default-theme release gap. The actual upstream CSP
build was browser-tested. No Hyvä/Alpine package was found in the inspected current local
invictus-staging vendor/theme trees; broader Hyvä extension compatibility is therefore unproven.
No Hyvä utility globals are required or copied.

## Remaining acceptance

[SOL-555](https://linear.app/solventech/issue/SOL-555) retains full shared-menu acceptance;
[SOL-535](https://linear.app/solventech/issue/SOL-535) retains full shell/native account/cart scope.
[SOL-530](https://linear.app/solventech/issue/SOL-530) cannot close from this five-page first boundary.
The current bounded delivery integrates the existing families and proves a populated two-product
collection/PDP/search/native-cart/totals/checkout-transition journey. It does not close full field,
provider, account or default-template acceptance. Complex product options and richer price/tax
presentation, pickup/history/predictive providers, full menu parity and exclusive CSP response-header
ownership remain open. No new environment or custom checkout was introduced.
