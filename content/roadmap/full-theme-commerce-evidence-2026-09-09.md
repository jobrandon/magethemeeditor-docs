# Full-theme commerce integration · 9 September 2026

Status: **bounded populated local journey implemented; full catalog, default-theme release and SOL-530 remain open**.
Coordinator 2 transferred source/docs/local-INOX ownership to task `01a081a7-68d6-7b10-a015-ad9e83e868e7`
after the independent five-page review. This delivery uses the user-authorized Astra High allocation.
The checks began on 8 September UTC and completed after midnight on 9 September in Manila.

## Working shopper journey

| Destination | Current behavior |
| --- | --- |
| `/mte-theme-home` | Existing Silt story plus a populated native collection section and shared Shop/Search navigation |
| `/mte-theme-catalog?category=category-1440` | One category introduction and product grid containing the two synthetic local products |
| `/mte-theme-shopping?product=product-9734` | Focused Cup product page: matching heading, original local image, description, native $24 price/salability and purchase form |
| `/mte-theme-shopping?product=product-9735` | Corresponding Bowl product page, native $36 price and its own product form |
| `/mte-theme-search` | Focused search form; submitting `Silt` resolves both products through Magento's configured OpenSearch collection |
| `/mte-theme/checkout/cart/index/` | Current visitor's Magento quote, native add/update/remove forms, row prices and quote totals |
| `/default/checkout/` | Ordinary native Magento checkout; the authenticated synthetic session reached the shipping-address form with its cart intact |

The editor remains at `http://127.0.0.1:4177/theme`. Fourteen selected page resources now exist.
The old commerce component showcase is separate at `/mte-theme-commerce-examples`; its explicit
pickup/history/advanced-provider gaps are not shopper-template content. Full-theme Media/Motion and
Contact/Signup/Promotions reuse existing original packages. Forms remain conspicuously validation-only:
no email, subscription, customer field persistence or delivery provider is enabled.

These are selected full-theme routes rendered by the existing native CMS/layout boundary with actual
Magento catalog and cart services. Ordinary category/PDP/search paths retain the host storefront.
This does not establish replacement of every native route or compatibility with every extension.

## Trusted registration and isolation

Developer-owned package declarations now supply full-theme template registration, placement,
local assets, native service identifiers and optional component route bindings. The build creates
`contracts/full-capabilities.json`; editor eligibility and native validation consume that artifact.
Installed Magento DI maps service identifiers to trusted renderer implementations. The editor no
longer filters section namespaces to Studio/editorial. Shell placement remains separate from template
placement, preventing duplicate inherited/header/footer component insertion.

Only declared route-bound fields use URL context: the current product component and category
introduction/grid consume the current entity. Authored featured-product/category references remain
independent. A temporary mixed composition proved current Cup plus separately authored Bowl, including
correct hidden product IDs in both native forms, before restoring the focused product resource.

Older snapshots may omit newly registered pages. Read/restore accepts those resources; the editable
draft adds new defaults without replacing existing page buffers. Save/apply still compare revisions
and active/draft digests. Native apply re-resolves top-level and nested catalog references. Old hybrid
route gates and the fixed 03F boundary are retained.

The public editor receives bounded store-1 catalog metadata, never prices, quote/customer identifiers
or customer content. Its image endpoint requires an exact image in that current-store metadata,
checks local path containment and file type/size, and rejects unselected media. Prices, tax, inventory,
customer/session and cart authority remain on Magento. The full-theme cart adapter accepts only
expected form fields, validates form keys and quantity transport shapes, rejects invisible/foreign
products and quote items outside the current session, and delegates valid changes to core controllers.
No merchant-supplied price, related-product list, executable provider, return URL or quote identifier
is accepted. Complex options/product types are explicitly unavailable rather than silently purchased.

## Runtime and browser evidence

Local receipts are in ignored `product/.local/full-theme-commerce/`; screenshots are under
`output/playwright/full-theme-*`. No accepted Flux census, offline suite or whole previous browser
suite was repeated.

| Check | Result and practical limit |
| --- | --- |
| Product `npm run verify` | 110 passing tests, including developer namespace registration and template/shell placement cases; original dependency checks/build pass |
| Native commerce lifecycle | 41 checks passed: seven new family routes, actual HTML and full-theme assets, CSP meta before assets, populated collection/search, native price/forms, invalid form key/extra fields/quantity arrays/non-visible product rejection, GET denial, session isolation, update/remove/totals, foreign-reference failed apply, previous/original restoration and populated reapply |
| Mixed composition | Current Cup and authored Bowl render separate correct native product forms; focused product page restored afterward |
| Native browser cart | Added Cup, updated quantity 1→2, observed native row/subtotal/grand total $48.00, then transitioned with the same session |
| Native checkout | Guest checkout correctly refused because it is disabled. Synthetic customer 20141 authenticated through native login and reached ordinary checkout shipping-address UI. No checkout setting changed, address submitted, order placed or payment attempted |
| Independent coordinator observation | Search submitted `Silt`, returned Bowl $36/Cup $24, and Bowl link reached matching full-theme PDP; no warning/error on that product page; this evidence is reused |
| Full-theme forms | Required consent rejection followed by valid sample/consent produced a native validation-only acknowledgement; no field text was transmitted to a delivery service |
| Editor/native bridge | Search page head title saved/applied through the UI, reopened and observed in native HTML; catalog image loads and unselected-image 404 confirmed |
| Visual checks | Focused desktop/mobile product inspection; corrected package CSS override on quantity controls and the product image/details layout; no horizontal overflow at 390px |
| Magento DI | Compilation successful on existing PHP 8.3.28 installation |

Initial empty category/search results were not treated as completion. Category creation encountered a
required installation attribute (`online_merchandiser`); the dedicated category uses value 0. Its
ancestry needed an explicit native resource correction to `1/2/1440`, followed by scoped reindexing.
Search was then traced to the generic fulltext factory: the configured native OpenSearch factory
returns the populated results and is now bound to this local catalog service. No search-engine/store
configuration or foreign website index inventory was replaced.

## CSP and remaining limitations

The independent P2 evidence correction is incorporated. The package CSP **meta** policy is emitted
before all resource elements and constrains scripts to self. Actual responses still retain broad
inherited Magento CSP response headers, including unsafe-eval and third-party origins. Browser
policies intersect; exclusive response-header ownership remains a local default-theme release gap.
No global Magento CSP change was made.

The selected theme loads five declared local scripts: original interactive/commerce/forms runtimes,
`full-theme.js` and the reviewed Alpine CSP build. Alpine supplies named navigation/disclosure and
quantity behavior; other original package DOM behavior is reused. No RequireJS/Luma script joins
these selected pages. The ordinary checkout retains its existing runtime and pre-existing CSP error;
reaching its shipping form does not prove error-free checkout, payment or order completion.

The existing optional Varnish listener at 6084 remains unavailable; direct local HTTPS proof is not
Varnish/edge delivery proof. The installed media metadata plugin logged its pre-existing constructor
error while native product media was saved; the two referenced images were subsequently served and
visually inspected. Neither broader host-environment repair nor commercial support is claimed.

The 921-entry commerce field ledger retains **684 open field gaps**. Six opaque-reference mappings
now have bounded populated evidence; no full field/block equivalence is claimed. Configurable/bundle/
custom options, richer galleries, tier/tax/customer-group price presentation, related products, pickup,
private recently viewed, predictive product cards, bulk ordering, full filtering/pagination,
advanced menus and unfinished registration/recovery/address/order presentation remain open.
SOL-534/535/555 remain In Progress; SOL-530 remains Todo. No independent review was launched by this owner.

## Scoped changes and reversal

INOX remains on `fix/INOXUS-creative-assets-fpc`, HEAD
`046d6e87866e7f6c5172e9c63f90097ac8b08295`. Docs remains on `main`, baseline HEAD
`b9704c423a6a1065b58252aace9fa8492caa5171`. No commit, push, PR, remote operation, new environment,
database replacement or global theme/checkout configuration change occurred.

| Area | Exact scope and reversal |
| --- | --- |
| Catalog | Dedicated category **1440**, simple products **9734/9735**, SKUs `mte-full-commerce-cup`/`mte-full-commerce-bowl`, website 1, native stock/index records; delete only verified fixture identities through native repositories after restoring theme content |
| Media | Original image copies `/c/e/ceramics_1.png` and `/c/e/ceramics_1_1.png`; remove only fixture-owned unreferenced originals/generated derivatives after product deletion |
| CMS | Added **262 Media, 263 Motion, 264 Catalog, 265 Product, 266 Contact, 267 Signup, 268 Promotions, 269 Search, 270 Commerce examples**; delete only these matching identifiers/store assignments if retiring the delivery. Pages 240–261 retain their original database content |
| Test identity/session | Synthetic customer **20141** and its verified empty quote **61429** deleted after native cart removal and logout; zero orders verified. Local credential file and fill helper removed. No real customer row modified |
| Source | Package `fullTheme`/route-binding declarations; generated capability/assets; full-theme PHP service adapters/route guard/forms revision support; React full-theme editor; fixed local media bridge; focused tests and operational helpers |
| Saved state | Full-theme draft/active/previous use normal save/apply/restore. The pre-transfer three files are separately backed up. Revert only after preserving newer user resources; never restore an entire older module directory over later work |
| Prior experiments | Historical hybrid source gates, selections/drafts and 03F remain outside the new route/runtime assignment |

Use editor **Restore original** first, preserving newer draft resources. The installed
`var/mte-full-theme/commerce-fixture.json` names every dedicated fixture identity. The ignored
`before-manifest.json` and `before/` directory preserve 140 pre-transfer source/state files; the final
preservation/change receipts distinguish intended edits from retained experiments. Reverse only listed
files, remove newly owned files when appropriate, rebuild metadata/editor, regenerate local DI and
clean affected local caches. Retain the populated fixtures while this demonstration remains in use.

No third-party package, service, font, image source or SDK was added or upgraded. The existing
Magento Open Source **2.4.6-p13** installation and reviewed Alpine/React dependency graph are reused.
This local integration does not expand vendor entitlements, redistribute client/vendor source or
clear the existing serializer workaround for commercial release.


## Final preservation and pause

At **2026-09-08 16:22 UTC / 9 September 00:22 Manila**, cleanup removed only the disposable
customer and its empty quote. The two dedicated products, category, all nine new CMS pages and
populated saved/applied theme remain available. Empty anonymous lifecycle sessions were left to
normal Magento expiry; no unrelated quote/session was guessed or deleted.

Final receipts confirm all **22 original CMS pages (240–261)** retain exact title/content/identifier/
activation hashes. All **70 historical files outside the SiltFormDemo module** match the prior
experiment/state baseline. All **80 module files and seven theme files** match the workspace source
mirrors. The pre-transfer backup comparison records 29 intended source/state changes; the final source
inventory separately records current hashes, including files absent from that backup. Website 2 still
has 9,567 product assignments; website 1 has its original assignment plus the two fixtures.
`cleanup.json`, `database-preservation.json`, `preservation.json`, `source-inventory.json` and the
updated `fixture.json` are stored with the ignored local receipts. The legacy forms renderer harness
also rendered successfully with its required JSON input after the full-theme extension.

The user instructed ongoing work to finish and **all further execution to pause until tomorrow**.
This implementation batch is finished; source/docs/local-INOX ownership returns to Coordinator 2.
The populated editor and native theme stay available. No new review, feature family or task was started.
The existing coordinator manages its automation pause.

On explicit resumption, Coordinator 2 should first read this evidence and current saved-state hashes,
then commission the pending independent review of registration, route binding, cart guards and editor
media containment. Reuse the passing 110-test suite, 41-check lifecycle and independent shopper proof
unless source changes or a finding justify rerunning them. The remaining field/provider/account work
and response-header ownership gap require a separately scoped next batch; no parent acceptance is
implied. SOL-534/535/555 retain In Progress and SOL-530 retains Todo with scoped progress evidence.
