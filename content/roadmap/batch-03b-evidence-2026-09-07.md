# Batch 03B native grid and live commerce · 7 September 2026

Status: **bounded local experiment completed; independent review required**. Execution task
`01a07bcf-79dd-7e30-aa67-470909cc9075`, GPT-6 Astra; coordinator
`01a07a34-9a91-7160-8ff1-835cfc8011f3`. This extends the independently accepted Batch 03A
hero and F1/F2 corrections. It does not complete the full renderer, adapter or fixture issues.

## Result and exact scope

The unchanged portable content fixture renders `hero-1` then `grid-1` through registered native
templates in one selected Luma home/CMS region. Reversed order, repeated grids and grid-only content
also preserve IDs/order and one region owner. Hero-only remains available. Store `default`/id 1,
website 1, en_US, USD, anonymous guest/group 0, theme Magento/luma 100.4.6-p13 were exercised.
Native PDP/category/cart remain commerce routes, not editing targets. The illustrative editor
iframe is unconnected; its code, dist and both manual drafts were preserved.

The same fixed mapping remains `store-en/home/page-home/region/hero-region` → home
`mte-native-home`, route `cms_index_index`, CMS block `mte-native-hero`. Same-block unassigned CMS,
other blocks, store/theme/route mismatches and unsupported regions retain current originals.
Selection requires explicit local CLI action and both full_page/block_html disabled.

| Native browser observation | Actual result |
| --- | --- |
| Empty guest cart before adding | Native mini-cart reports no items |
| Simple grid Add to Cart | One cup, product 3 / mte-grid-simple, quantity 1, USD 18.50 |
| Configurable with no selected finish | Native PDP validation reports required field; existing cart unchanged |
| Native option selection | MTE Clay changes the native displayed price from minimum 24.00 to 29.00 |
| Native configurable Add to Cart | Parent product 6, selected simple child 5 / mte-grid-clay, quantity 1, USD 29.00 |
| Same guest cart | Quote 1, visible item IDs 1 and 2, subtotal USD 47.50; native service output agrees |
| Cleanup | Both owned lines removed using native cart controls; quote 1 is empty, subtotal 0 |

The child quote row retains its native zero-priced child representation under the configurable
parent; it is not flattened or double charged. No direct quote mutation, checkout, order or payment
was performed. Native quote/service evidence and browser screenshot/DOM captures are retained.
One-click/quantity-one outcomes, one native form declaration per grid and consumed `data-mage-init`
provide static initialization evidence. Authenticated editor preview updates and widget disposal
are explicitly unproven.

## Original catalog and live data

Only six original products and an original `mte_finish` attribute/options were added through an
idempotent Magento data patch and native product/stock/configurable APIs. The prior mte-simple
product, original category, home/sibling blocks and unassigned page remain unchanged. No client
texts/images, imports, customers or orders are included. The dataset contains no image/video;
Magento's native placeholder appears where its cart/PDP requires imagery.

| Opaque reference | Fixture-native identity | Seed / policy |
| --- | --- | --- |
| product-simple | mte-grid-simple | Cup, 18.50, quantity 20, enabled/visible |
| product-configurable | mte-grid-configurable | Bowl with Sand child 24.00 and Clay child 29.00, each quantity 20 |
| product-disabled | mte-grid-disabled | Enabled stock but disabled product; omitted |
| product-out-of-stock | mte-grid-out-of-stock | Price 19.00, quantity 0, no backorders; unavailable text and no purchase control |
| product-missing | mte-grid-deliberately-missing | Intentionally absent; omitted independently |

`ProductRepositoryInterface` loads in current store context with forced reload. Status, visibility,
website membership and supported native type gate resolution; native salability gates controls.
A private native Magento price renderer supplies final/minimum price presentation and unique
section-specific price IDs; URLs/form keys/cart widget come from Magento. Design JSON contains
only grid productIds and columns, with no frozen commerce/session data.

An actual native repository update changed the cup **18.50 → 21.75 → 18.50**. Fresh selected HTTP
responses showed each value while the active design bytes remained identical. Seeded price/stock
were restored. No claim follows for alternate currencies, customer groups, tax rules, promotions,
MSI configurations or cache coherence outside this generated guest context.

## Validation and selection boundaries

Contract stays **1.0.0**. The PHP ingestion subset accepts 1–12 unique hero/product-grid sections,
exact document/scope/state/token keys and versions, 16 KiB minified UTF-8 JSON plus newline, depth 8,
and bounded revision. Hero settings remain heading/alignment. Grid settings contain only productIds
(1–24 distinct opaque references) and integer columns 1–4. Five references are registered locally,
so this fixed fixture currently resolves at most five distinct references in one grid.

Unknown references, numeric IDs, SKUs, URLs, duplicates, empty/oversized lists, invalid columns,
extra commerce/template fields, versions and unsupported components reject without replacing state.
The canonical Node validator validates the original input before staging; this is not full PHP/schema,
signature, inheritance, capability, publication or hosted authentication parity. No custom-module
provider, visual binding, Liquid or marketplace feature is implemented.

Only registered PHP classes/templates execute. CSS roots scope hero/grid styles, no product JS or
remote script is added, and repeated grid instances have distinct price element IDs. F1's filesystem
warning normalization and F2's process-fork denial are unchanged and reverified.

## Additive native prerequisite and recovery

The starting 181-package subset lacked `fotoramaVideoEvents`, required by the native configurable
widget. The first PDP browser run retained this real RequireJS failure. The exact
`magento/module-product-video` **100.4.6**, 88 as-installed files, was reviewed from the authorized
INOX vendor tree. Required dependencies were already present. OSL/AFL terms, file notices, intended
single-user local use and release limits are recorded in product/integration/grid-third-party-review.md.
No commercial/client package, credential, font or media was copied into product source.
[Exact package metadata](https://github.com/magento/magento2/blob/2.4.6-p13/app/code/Magento/ProductVideo/composer.json),
[OSL terms](https://github.com/magento/magento2/blob/2.4.6-p13/LICENSE.txt),
[AFL terms](https://github.com/magento/magento2/blob/2.4.6-p13/LICENSE_AFL.txt).

The coordinator clarified that the necessary additive upgrade is covered by the existing autonomous
batch authorization; the prohibition still excludes destructive setup/reset/reinstall. Before
mutation, fixture ownership/current policy were checked and a generated-fixture-only recovery dump
plus config/autoload/selection checkpoint was saved. The 655,326-byte dump SHA-256 is
`40d336e1f5ae141a74e3e5091ee781b9ba983765869a8a00088a74e561046744`.
It remains ignored/private, not published documentation or a tested restore claim.

Native patch inventory found only this batch's SeedGrid pending. Actual `setup:upgrade --dry-run=1
--safe-mode=1` recorded one CREATE TABLE, no drops or unrelated schema work; it did not apply data
patches. The apply initially exposed SeedGrid's missing setup area context; the patch now emulates
adminhtml and restores caller context. The recovered `setup:upgrade --safe-mode=1` succeeded.
Final table inventory adds only `catalog_product_entity_media_gallery_value_video`, enabled modules
add only ProductVideo, no patches remain pending, and `setup:db:status` reports all modules current.

All Magento/Composer calls used the unchanged mandatory sandbox wrapper, including autoload with
plugins/scripts/network disabled. Both excluded cache types remain disabled. No service restart,
full rebuild, reset or original-store mutation occurred. The fixture is now a **182-package
as-installed Open Source subset**, base 2.4.6-p13 / PHP 8.2.29 / MySQL 8.0.40 / OpenSearch 2.12.0,
not a pristine distribution, installable Composer lock, supported release or commercialization promise.
Second-install/reset reproducibility remains SOL-494 work.

ProductVideo intentionally changes the fixture's native RequireJS aliases/PDP initialization.
Selection/unassignment comparisons use the completed 182-package baseline. Fresh grid resource
inventory observed 213 local assets/resources, no external URLs; no video data/provider is configured.
The native configurable PDP loaded its options after the prerequisite. Browser inventory is an
observed resource snapshot, not an exhaustive network security audit.

## Verification and retained evidence

All new evidence is under ignored `product/.local/batch-03b/`; historical 03A/review/remediation
reports, repros, source maps and evidence are preserved. No product Git repository/commit exists.
Accepted start: **90 files**, SHA-256
`91105e7c183372e4ddeb320a2027e9037e0391ddd0eabdb234c5e4aa367bf9a4`.
Authored finish: **103 files**, SHA-256
`a8aff8bfe56a96549b2495161d0836b9b063db73b3505618dae617efd1979937`.
Algorithm: compact key-sorted product-relative filename → file-SHA256 JSON, SHA-256 over that map;
exclude `.local`, `node_modules`, `.git`, `dist`, `.DS_Store`. Exact map/11 modified/13 added paths
are in `source-final.json`; no canonical contract/editor/dependency-lock edits occurred.

| Check | Result / evidence |
| --- | --- |
| Existing npm verify | 82 pass; exact authored copy and node_modules link in ignored node-verify, so original dist is untouched |
| Existing PHP harness | 57 pass; production code with Magento doubles, no bootstrap |
| Grid domain | 27 pass; pure validation boundaries |
| Native grid services | 13 pass; actual Magento context, resolution, salability, native prices, children/options/URLs |
| Expanded actual CLI/HTTP | 69 checks, 23 retained responses; runtime-final-expanded/results.json |
| Existing actual negative runner | Eight cases pass; updated obsolete grid rejection to unsupported grid price field; fresh output path required |
| F1 permanent actual-handler | Eight pass; storage-final.json |
| F2 actual subprocess/egress/write/env | 19 pass; isolation-final.json; live HTTP sandbox independently checked |
| F1 actual HTTP fallback | 18 responses; adapted runner changes only root/output paths, original script preserved |
| Cache guards | Both full_page and block_html reject selection; exact files restored |
| Native commerce | Actual browser controls, browser-cart.png/.txt and quote-browser-filled/empty.json agree |

Raw responses retain complete script content. Comparisons normalize only generated link IDs, request
form keys and the native CAPTCHA timestamp. Earlier comparison failures due to the timestamp are
retained and explained; no complete scripts were stripped. Selected/unassigned five-route comparisons
preserve header/footer/scripts and unassigned main output; selection removal restores all compared
parts. New tests also cover one region owner and unique price IDs across multiple grids.

Negative runners restore original inbox/active/lock/env bytes and modes in finally. Runtime mutations
are limited to the existing permitted fixture state; no broader sandbox write/egress allowance was
introduced. Temporary price changes are restored and the original hero is unassigned at completion.
Current-original restoration remains distinct from versioned durable rollback.

## Ownership, Linear and remaining acceptance

Creation/resource owner remains Batch 03A `01a07b5a-dbf4-7e31-a3b3-d63d2f58d3ab`; this operational
handoff did not replace guards. Preserved services: HTTP **11517/4180**, MySQL **9965/19306**,
search relay **10032/19210**, container `mte-batch03a-search`, internal network
`mte-batch03a-internal`, docs **5726/8017**. The user editor was already absent before this task;
its cause remains undiagnosed and it was not implicitly restarted.

SOL-496 retains In Progress for preparatory renderer evidence, still blocked by SOL-495. SOL-498
moved from Backlog to In Progress only as actual native Luma price/widget/cart work began, with
SOL-496 still open. SOL-494 remains In Progress with generated-fixture/prerequisite evidence only.
Original descriptions, unchecked criteria and dependencies are preserved; none moved Done.
The future marketplace project remains plans/artifacts only.

Independent review follows. Full fixture reproducibility/reset, Hyvä/Porto, other store/currency/group
contexts, header/footer editing, Page Builder/widgets, generic handshake, authenticated preview
lifecycle, cache identities/invalidation/outage, durable publication/rollback, customer acceptance
and commercial rights remain open. No next batch, new issue, commit/push/PR, source upload, repository
visibility change or public deployment was performed.

## Final preservation and documentation check

`make -C docs verify` passes: **28 source pages, 29 HTML pages, 1,880 local links**, including
anchors, assets, navigation and source/output separation. The new evidence page and affected
execution/architecture/fixture/support pages were inspected in the preserved docs listener.
Final source/deployed module bytes and served hero/grid CSS match. All 1,452 historical evidence
files checked, original vendor package bytes, manual drafts, dist, owner/policy/HTTP records,
inbox/lock/env bytes and modes are preserved; `.docs` still resolves to `docs/content`.
Only five existing current docs pages/navigation files plus this new report changed in this batch;
unrelated dirty docs and dated research remain unchanged. Exact lists are in preservation-final.json.

A final six-route HTTP smoke (original home/CMS, original simple, configurable, out-of-stock and
empty cart) returned the expected non-error content with no unexpected new log errors. All 22
PHP/template syntax checks passed. Live Linear readback confirms all three issues remain In Progress,
with original descriptions/dependencies and the new scoped comments present. No other Linear project
or issue was changed. This task stops for coordinator-owned independent review.
