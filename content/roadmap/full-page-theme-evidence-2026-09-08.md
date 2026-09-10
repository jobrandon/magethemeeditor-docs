# Full-page Silt theme correction · 8 September 2026

Status: **first native full-page boundary implemented and locally verified; full-catalog acceptance remains open; the independent review accepted the bounded five-page implementation with a P2 CSP evidence correction**. Owner: task `01a08176-b7f4-7741-913b-22c66a02fa4f`,
GPT-6 Astra High under the user's scoped authorization. Coordinator 2 released sole source/docs/INOX
ownership after SOL-536 stopped writing. This handoff returns coordination to
`01a07c28-b8ed-78d1-85e2-25f171859b5f`; no next batch is dispatched by this owner.

The [9 September commerce delivery](full-theme-commerce-evidence-2026-09-09.md) supersedes the five-page/catalog-open current-state claims below; this page retains the dated first-boundary receipts.

## Working entry and routes

- Editor: `http://127.0.0.1:4177/theme`; the default 4177 entry redirects here.
- Native pages: `https://inox-us-staging.test/mte-theme-home`, `/mte-theme-about`, `/mte-theme-faq`,
  `/mte-theme-editorial`, `/mte-theme-stories`.
- Native account: `https://inox-us-staging.test/mte-theme/customer/account/index/`; guests redirect
  to `/mte-theme/customer/account/login/`. Login POST, authenticated account and logout use core controllers.
- Native cart read: `https://inox-us-staging.test/mte-theme/checkout/cart/index/`.
- Existing `/mte-silt-*` pages remain historical **hybrid/CMS-region demos**. Their editor banner links
  to the full-theme editor. `/mte-silt-account` visibly identifies its historical status and links to
  the real full-theme account template. Those earlier cards cannot close the full-page account criterion.

## Architecture and observed result

[The canonical full-theme contract](../architecture/full-page-theme.md) defines the corrected scope.
A new parentless native `MageThemeEditor/silt` theme, request-scoped design selection, dedicated
page layout and package-owned head render the full document. No CSS-hidden host wrapper or storefront
iframe is used. Inherited `default` layout handles and host head/includes do not load. The original
Studio/editorial renderers remain reused. Home has a single main heading and one header/footer.

Header / Template / Footer, shared settings and named menu resources now have real editor controls.
Menus have stable identities, slots, bounded nesting, drag/keyboard controls, visibility, safe target
selection, original image/description cards, current-link state and responsive Alpine disclosures.
The local bridge saves each page independently and applies/restores complete coherent theme snapshots.

## Verification

Observed 8 September 2026 on the existing INOX installation; exact receipts are retained locally.
Node 22.22.0, PHP web 8.3.28; product `npm run verify` passed **107 tests**. The focused full-theme
unit cases cover independent defaults, strict menus, foreign scope, executable URLs, duplicate
identities, missing assignments, depth, current links, visibility and unavailable states.

`node component-library/native/full-theme/lifecycle.mjs` passed **48 checks** against native Magento:
seven routes returned actual `200 text/html`, full Silt ownership, no inherited chrome/RequireJS/Luma
markers and private/no-store headers; guest account redirect stayed themed. Shared menu/announcement
edits propagated to Home/About, while Home content/head metadata and About revisions stayed independent.
Stale resource saves, stale active/draft digests, foreign menu scope, unsafe URLs, duplicate IDs and
unavailable product references rejected. Failed apply retained the active digest. Previous snapshot
and original CMS output restoration passed; the populated theme was reapplied with original demo values.

A separate actual CMS-reference check resolved store-1 page 258, temporarily disabled only that new
owned page, observed an explicit unavailable menu link on native Home, then restored its active flag
and the original saved/applied menu values. No existing CMS content was modified for that check.

Browser evidence includes:

- Real native login POST authenticated a dedicated synthetic customer into the themed account view;
  native logout returned to the themed logout/login presentation. Invalid form-key submission did not
  authenticate and returned to the themed login. No welcome/reset/contact/newsletter mail was sent.
- Shared-menu rename saved through the UI, followed an About page switch, and applied with a native
  acknowledgement. Menu duplicate/undo, keyboard nesting/undo and actual drag-handle sibling reorder/undo
  were exercised. The compact item list expands only the item being edited.
- Desktop submenu contents were visibly open, including the original image card. Escape closed it
  and returned focus to The studio. Mobile outer/inner disclosures worked at 390px with no horizontal
  overflow; returning to desktop kept the main navigation visible. The shipped Alpine runtime reported 3.17.2.
- The existing-session independent visual check confirmed submenu/Escape, hash-changing asset URLs,
  internal preview navigation, corrected preview wording and a single-column 390px preview hero.
  This is useful focused visual evidence, not an independent security/whole-catalog review.
- The rendered native script set is only `full-theme.js` and `alpine-csp-3.17.2.js`, both with content
  identity query versions. Actual resources load from the local theme; no RequireJS/Luma runtime appears.
  The package CSP meta policy omits unsafe-eval and inline-script permission. Independent review found inherited Magento CSP response headers that still include unsafe-eval and third-party origins; the effective browser policies intersect. Exclusive header-level policy ownership is not implemented and remains a local default-theme release gap. Historical initial-install errors are
  retained as development evidence; they are not the final runtime result.

The editor was stopped during an HTTP page/asset/media probe, then restarted on 4177. Explicit TCP
probes returned **ECONNREFUSED before and after** all **43 successful page/asset/media requests**. Native
pages and required local CSS, scripts and original image remained available. Byte receipts are in ignored `product/.local/full-theme/offline-results.json`; this tests editor-service
independence on this local setup, not all production CDN/cache failure modes.

Ignored evidence: `product/.local/full-theme/` contains installation, lifecycle, CMS-state, compilation,
unit suite, offline and preservation receipts. Browser snapshots/screenshots are in the existing
ignored `.playwright-cli/` output and selected copies under `product/.local/full-theme/`. Credentials
were never included in authored docs; transient synthetic credentials and login scripts were removed.

## Exact local changes and reversal

INOX branch stayed `fix/INOXUS-creative-assets-fpc`, HEAD
`046d6e87866e7f6c5172e9c63f90097ac8b08295`. Documentation stayed on `main`, baseline HEAD
`b9704c423a6a1065b58252aace9fa8492caa5171`. No branch switch, commit, push, PR, remote deployment,
new Magento environment, database replacement or global theme/store configuration change occurred.

| Change | Exact scope | Reversal |
| --- | --- | --- |
| Native theme | Added theme row **11**, `MageThemeEditor/silt`, no parent; source mirror under `app/design/frontend/MageThemeEditor/silt/` | Restore original selection first; remove this unused theme row and only its owned theme/static/preprocessed files |
| Dedicated CMS pages | Store-1 pages **257 Home, 258 About, 259 FAQ, 260 Editorial, 261 Stories**; identifiers `mte-theme-*` | After restoring selection, delete only these identified pages/store mappings through native repositories |
| Temporary CMS state | Page 258 `is_active` toggled 1→0→1 for missing-target proof | Already restored to 1; original content/title/layout remained intact |
| Synthetic login test | Inserted customer **20140**, website/store 1, reserved `.invalid` email; native login created empty quote **61428** | Logged out; exact synthetic customer and empty quote deleted; zero matching customer rows verified |
| Full-theme module additions | `Model/FullTheme/{State,Validation,Destinations,Context}.php`, `Plugin/{FullThemeBoundary,FullThemeDesign}.php`, `Block/FullTheme.php`, `etc/frontend/di.xml`, `contracts/full-{defaults,package}.json`, `view/frontend/layout/mte_fulltheme.xml`, `view/frontend/page_layout/mte_full_theme.xml` under existing `MageThemeEditor/SiltFormDemo` | Remove only these added files after selection restore, then regenerate DI and clean affected layout/config caches |
| Existing native Page block | Only an explicit historical account-demo notice/link added to `Block/Page.php` | Remove that notice/link if retiring the full-theme demonstration |
| Selection/drafts | New private `var/mte-full-theme/{draft,active,previous}.json`, lock and receipts | UI Restore original removes active selection; retain/export drafts or delete only this task's directory when intentionally removing the demo |
| Generated runtime files | Local DI compilation, new theme static symlinks/preprocessed assets, targeted cache cleanup | Regenerate after source reversal; do not remove other experiments or globally disable caches |

Source-of-truth counterparts remain in `component-library/native/SiltFormDemo/` and
`component-library/native/SiltTheme/`. New operational helpers are `native/full-theme/{command,install}.php`
and `lifecycle.mjs`. Original full-theme defaults/rendering/menu checks are in
`themes/silt-form/full/model.mjs`; the React surface is `product/editor/full-theme*`, served by the
existing demo server and fixed `product/src/full-theme-bridge.mjs`. The package lock, rights inventory,
notices and build copies include the reviewed Alpine CSP dependency graph.

The initial preservation receipt hashed 127 pre-existing module/state/draft files. At final check,
126 were byte-identical; the one expected difference was the historical account notice in `Block/Page.php`.
Existing hybrid drafts/selections, forms source/state, 03F, active store themes and ordinary content
were preserved. The existing optional Varnish listener at port 6084 was unavailable during native cache
invalidation; direct local HTTPS proof is distinct from Varnish delivery proof. No remote purge occurred.

## Open full-theme work

This is the first working **full-page base-theme candidate**, not completion of the full Flux catalog.
The current full-theme page registration covers five Studio/editorial templates. Existing interactive,
commerce, forms and other family demos remain on their historical hybrid routes until their supported
behavior is integrated into the full-page/Alpine package. This is a capability boundary, not acceptance
of a five-page/five-component final scope.

Next coordinated work under SOL-534/535: populate dedicated reversible local catalog records where
needed, prove collection/PDP/search, native add-to-cart/cart mutations/totals and native checkout
transition. The current empty store-1 catalog and read-only cart are not commerce completion.
Account registration/recovery, addresses/orders, extended shell/global fields, full mega-menu/reference
parity, other templates/providers, independent per-menu revision histories and broader accessibility,
performance, cache, security and Hyvä compatibility remain open. Native checkout must be preserved.

SOL-526/528/529/531/535 and SOL-555 receive scoped evidence, with criteria/dependencies preserved.
SOL-530 and the complete default-theme/catalog milestone remain open for further implementation and
independent review. There is no hosted, marketplace, commercial or production-readiness claim.
