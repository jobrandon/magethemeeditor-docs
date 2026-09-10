# Shell, global and system evidence · 8 September 2026

SOL-535 remains **In Progress: original local subset implemented; full family acceptance open**.
Thirteen original components provide four populated dedicated demos on existing INOX Luma CMS
pages 250–253. Five cart fragments remain owned by the header/cart presentation. Three
password/activation stems have no registered equivalent. This is not completion of the full
Flux catalog, authenticated account UI, live purchase behavior or global theme replacement.

The [465-entry field ledger](shell-field-coverage-2026-09-08.md) retains every assigned stem,
13 reference blocks, 18 global groups, two section groups and nested global fields. The
[canonical catalog map](silt-form-catalog-coverage-2026-09-08.md) preserves the original
classifications, including malformed `footer` and the five no-schema fragments. Every material
substitution and exclusion below is **unaccepted**; this implementation does not waive criteria.

## Ownership and local target

Coordinator 2 assigned SOL-535 source, documentation and local INOX ownership to the shell
implementation task. Astra High is authorized for this scoped shell/Magento trust-boundary work.
No additional agent or execution batch was started. The accepted reference census was reused;
Flux source was not recrawled, copied, translated or shipped.

- Product implementation: `component-library/` and `product/` in MageThemeEditor; no product Git repository.
- Existing local installation: `/Users/branorphiano/Projects/s1/inox-us-staging`;
  branch `fix/INOXUS-creative-assets-fpc`, SHA `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
- Fixed local bootstrap verifies the root and existing database before Magento starts.
- Store 1, website 1, existing `Magento/luma`; no store/theme/navigation/catalog assignment changes.
- New CMS/store rows only: shell 250 (`mte-silt-shell`), account 251 (`mte-silt-account`),
  cart 252 (`mte-silt-cart`), system 253 (`mte-silt-system`). All four are assigned only to store 1.
- Pages 240–249, prior drafts/selections, 03F and ordinary native storefront routes remain preserved.
- No remote/production changes, customer communications, authentication/impersonation, checkout,
  new environment, dependency installation, commit, push, PR or publishing.

## Open the populated demos

The existing local editor serves all four targets on port 4177:

| Demo | Editor target | Native path | Purpose |
| --- | --- | --- | --- |
| Shell & style | `?page=silt-shell` | `/mte-silt-shell` | Announcement, editable header/page style, information cards and footer |
| Account handoffs | `?page=silt-account` | `/mte-silt-account` | Six editable presentations with fixed native account routes |
| Shopping bag | `?page=silt-cart` | `/mte-silt-cart` | Native browser cart observer and native cart handoff |
| Page states | `?page=silt-system` | `/mte-silt-system` | Missing-page presentation in a dedicated CMS demo |

All four independent drafts are saved and applied at revision 2. The shell demo shows an edited
heading, serif typography, clay palette, reading width and outlined links. It was saved, reloaded,
applied, restored through the editor, verified as original native output, and reapplied. Other
demos retain their populated original presets. The manual 4173 editor and earlier drafts stay intact.

## Exact stem boundaries and decisions

| Stems | Working original subset | Outstanding acceptance |
| --- | --- | --- |
| `announcement-bar` | Plain heading/body, surface, alignment, symmetric padding, ordered registered CMS links, visit-only dismissal with focus return to the demo heading | Sticky/device positioning, rotation/slider blocks, countdown, social/country selectors, exact reference settings and persistence |
| `header` | Wordmark, scoped palette/font/width/link choices, CMS-link navigation, optional fixed native search/account routes and read-only cart disclosure | This is content-region chrome. Native category/mega navigation, global logo/theme replacement, sticky/transparent variants, account modal and advanced blocks remain open |
| `footer` | Plain heading/body, registered links, surface/padding and back-to-demo-start link | Reference brand/image/menu/app blocks, policies/provider data, newsletter, localization/payment/social and device-specific layout variants |
| `quick-info-bar` | Ordered title/body cards, bounded desktop columns, mobile stacking, border/surface/padding | Image/icon sizing, per-card colors, independent edge/margin controls and exact four-slot layout equivalence |
| `main-404` | Editable missing-page copy and registered recovery links | Dedicated HTTP 200 CMS demo only. No actual no-route/HTTP 404 replacement, image equivalent or full status routing |
| `main-account`, `main-login`, `main-register`, `main-reset-password`, `main-addresses`, `main-order` | Editable intro/surface/padding and fixed native account/login/create/forgot-password/address/history links | Route handoffs are not embedded forms, authentication, addresses, order details, account data or token-based reset UI. No customer data flows to the editor |
| `main-cart-items` | Read-only native browser observer with unavailable/empty/count/recent-item states, escaped text, scoped identity checks and native cart link | Fresh-browser native data was `{}`, so only real unavailable-state proof exists. Synthetic unit tests cover empty/ready/change states; no real populated cart, totals/options/quantity/remove operation proof |
| `main-cart-footer` | Editable copy/surface/padding and fixed native cart route | Totals, discounts, terms, dynamic payment buttons, shipping calculations and checkout remain native and unimplemented in this region |
| `cart-drawer`, `cart-icon-bubble`, `cart-live-region-text`, `cart-notification-button`, `cart-notification-product` | Owned by header/cart: nonmodal disclosure, count text, one count-change live status, native cart link and bounded recent item names/quantities | Not addable sections. No modal drawer equivalence, positive add-to-cart notification, purchase event/product image/options or live populated proof |
| `main-activate-account` | Unregistered explicit semantic gap | Magento confirmation/token behavior requires its native security integration; no unsigned activation UI or fabricated activation state |
| `main-password-header`, `main-password-footer` | Unregistered explicit semantic gap | Shopify password-store locking has no proved Magento equivalent in this scope; authentication presentation cannot substitute for a store access gate |

Decision records SH-01–SH-06 in `reference/shell-coverage.json` record these boundaries. They
are implementation decisions or proposals for review, not accepted material scope reductions.
SOL-535 and the milestone cannot be closed from this evidence.

## Global contract and native ownership

The single `mte-shell/header` component owns the demo page's typography, paired palette, width
and link appearance. All are bounded enum choices. Both browser and native validators reject
duplicate header owners; a header-free empty page uses safe defaults. System fonts require no
font download. Three paired palettes meet 4.5:1 normal-text contrast for paper and tint surfaces;
the inverse surface uses the same pairs. These settings style only `.mte-shell-page`.

This remains a page-scoped presentation contract. It does not edit Magento global configuration,
locale/currency, native categories/navigation, tracking, price display or checkout. Independent
heading/body/navigation font choices, arbitrary brand colors, advanced button/grid/card settings
and the remaining global field ledger stay open. Region accent/spacing controls are hidden on
these four editor targets because their values do not govern this separate shell; the editor
explains that page appearance is edited through the Demo header.

Earlier targets reject all shell component types. New shell targets accept only the shell package,
which avoids pretending other family assets are available in these layouts. Existing content
1.0.0, Studio/editorial/interactive/commerce schemas, original drafts and the fixed 03F projection
retain their boundaries. The four new layouts are non-cacheable only on their dedicated CMS handles.
The ordinary native Luma header, navigation, search, cart and footer remain rendered around them.

`ChromeRenderer` uses installed DI services and fixed route constants. Merchant JSON has no class,
renderer, route, URL, customer identifier, quote ID, template, executable CSS or arbitrary HTML field.
Registered CMS references resolve through existing store-scoped `References`; apply re-resolves them
before replacing selected bytes. Native route output rejects foreign hosts, credentials, query and
fragment data. No customer or quote service is queried by the editor or native renderer.

The small browser runtime observes the installed `Magento_Customer/js/customer-data` cart
observable. It requires the expected store and website, numeric bounded count and an item array.
It uses only text nodes for at most ten recent item labels/quantities. It does not call `reload`,
`invalidate`, `set`, fetch, quote mutation or customer API. Missing/foreign/invalid data clears old
items/count/status and shows the native cart handoff. The disclosure is intentionally nonmodal;
Escape closes it and returns focus to its summary. Exactly one host announces count changes.
No persisted cart data is created by this package and no synthetic fixture is inserted into Magento.

## Verification

Local evidence resides under `product/.local/sol-535/`; browser images under
`output/playwright/sol535-*`. These are local QA artifacts, not published documentation assets.

| Check | Result and limit |
| --- | --- |
| Product verify | 104 passing tests; reviewed eight-package inventory/notices and browser build |
| Library suite | 33 passing tests including shell browser/PHP choice parity, target/owner rejection, unsafe fields, fragment exclusion, exact census coverage, cart observer isolation and palette contrast |
| Native DI | `php -d memory_limit=2G bin/magento setup:di:compile` passed on installed PHP 8.3.28 |
| Native lifecycle | 65 passing checks on four dedicated selections: current revision/output, foreign reference rejection in browser and native apply, unchanged rejected bytes, empty content, stale hash, alternate style, escaping, hidden optional cart, restore, corrupt fallback, exact bytes, private-cache headers, ten ordinary/prior-route controls and three guest authentication redirects |
| Browser editor | Header edits/save/reload/apply, original restore and reapply; all four new drafts saved/applied at revision 2; private cart preview remains explicitly separate |
| Native browser | Four responsive demos; 390px document width without horizontal overflow; actual serif/clay/reading/outlined style; visit dismissal; cart Escape/focus; address handoff to native Customer Login without submission |
| Private cart evidence | Fresh browser's real Magento cart observable has no keys. Unavailable output is correct; positive empty/populated/cart-change outcomes are synthetic source tests only |
| Cache/CSP boundary | New handles retain `cacheable=false`; no global cache types disabled, CSP weakened, executable merchant data or remote package resource introduced |
| Preservation | Hash comparison of 32 prior local state files; prior CMS/store-assignment/config/store/root/catalog-assignment snapshot hashes unchanged |
| Docs | `make -C docs verify`, strict build and generated navigation/link/anchor checks; browser evidence/field-table inspection |

The first product run exposed a test matrix assumption that all newly added templates belonged to
every page. The test was updated to assert both directions of the explicit shell family boundary.
Native tests verified that boundary independently. The initial CLI lifecycle harness did not catch a
synchronous browser-validator rejection; its handling was corrected and native apply was tested
separately. These test corrections did not accept a bad native selection.

Mobile inspection caught cramped footer links; scoped spacing and 44px link height corrected it.
The surrounding store's cookie banner remains a native overlay and was not hidden or altered for
screenshots. The editor's existing `data:,` favicon CSP warning and native store warning are outside
this package. Focused checks are not full WCAG certification, production cache-coherence proof or
broader Magento/Luma version support; Hyvä/Porto and commercial readiness remain unverified.

## Source changes and reversal

Original source adds `packages/shell/{package,render,runtime}.mjs`, scoped CSS,
`themes/silt-form/shell.mjs`, the native `ChromeRenderer`, four generated layouts and content-hashed
assets. Shared changes are the trusted package registration, starter target/template boundaries,
one-header validation, native shell/validator branches, editor preview/caption/appearance handling,
generated schema/metadata, tests and coverage overlays. All production application behavior uses
constructor DI; local scripts bootstrap only the already authorized installation.

The local installation's exact changed paths are recorded in `native-changed.json`, including
`etc/local-targets.json`, with its pre-change module backup in `native-before/`. Its target map adds
only the four new page IDs. `manifest-remediation.json` records the target-map before/after hashes,
the four scoped entries, and the manifest inclusion check. New drafts/selections and append-only
receipts are expected; prior selection/draft files are preserved. Generated DI metadata and local
layout/config/block/full-page caches were refreshed.
No dependency, SDK, hosted service, font, image, icon or video was adopted or upgraded. Existing
reviewed React/Ajv and installed Magento services are reused; no vendor code is distributed. The
existing Playwright CLI 0.1.19 runtime was used without installing or shipping it. The local
serializer workaround was not changed or widened and remains outside commercial clearance.

To reverse this family's visible presentation, use **Restore original** independently for each of
the four new demos. This removes only that page's selected JSON; saved drafts remain available.
For complete local removal, first export these new drafts if wanted, restore their selections, then
remove only CMS pages 250–253 after verifying their identifiers and store 1 ownership. Use the
manifest entry `etc/local-targets.json` and its paired `native-before/etc/local-targets.json` backup
to remove only the `shell/account/cart/system` entries from the current local target mapping; preserve
all other entries. Verify the target-map hash and retained page IDs before and after that selective edit.
Remove this family's DI items, `ChromeRenderer`, the four layouts and their shell assets, and remove
its registration/targets from the product after saving wanted portable documents. Rebuild schemas,
browser output and native DI, then clean the affected cache types. Do not restore an old whole module
backup over later work; `native-before/` is a selective comparison/recovery source only.

Do not delete prior pages 240–249, original serializer files, catalog/customer/quote data, previous
experiments or unrelated generated/source work. The four new pages remain applied for review.
Independent substantive review should prioritize scope/classification honesty, fixed-route and
private-state boundaries, target isolation, failing-state restoration, accessible interaction and
reproducibility. Accepted dependency decisions and missing live behavior remain subsequent work.
