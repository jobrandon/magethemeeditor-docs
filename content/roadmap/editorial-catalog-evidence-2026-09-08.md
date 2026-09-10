# Editorial catalog evidence · 8 September 2026

SOL-532 now has original portable/editor/native equivalents for all **14 assigned editorial stems**,
shown in populated **Editorial collection** and **Stories & details** templates. This is a working
local implementation with an explicit partial-parity boundary, not completion of the full Flux
catalog milestone. SOL-532 remains **In Progress** for independent substantive review and scope
adjudication. No parent issue or milestone scope was changed.

The [canonical catalog](silt-form-catalog-coverage-2026-09-08.md) and
[field ledger](editorial-field-coverage-2026-09-08.md) account for all 326 assigned census entries:
239 implemented original equivalents, 36 metadata entries, 25 explicit dependency gaps, and 26
partial equivalents. The partial entries comprise 12 CMS-only URL equivalents, nine structured-text
equivalents, three original-preset substitutions and two registered-CMS page equivalents. The 25
open entries are assigned to the existing families: SOL-533 (17 interactive/media settings),
SOL-536 (seven countdown fields), and SOL-534 (one product-provider field). Nothing is silently
removed from the milestone or claimed as complete reference behavior.

## Ownership and environment

Coordinator 2 assigned this owner sole source/docs/local-INOX write access for SOL-532. Astra High
was authorized for the scoped component/native-extension architecture and implementation. No
additional agents or new tasks were dispatched. Source/docs ownership returns to Coordinator 2
for an independent substantive review after this evidence is verified.

- Product and component-library remain without a product Git baseline; no source SHA is claimed.
- Docs: `main`, baseline `b9704c423a6a1065b58252aace9fa8492caa5171`, pre-existing dirty files preserved.
- Existing INOX: `/Users/branorphiano/Projects/s1/inox-us-staging`, branch
  `fix/INOXUS-creative-assets-fpc`, HEAD `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
- Native bootstrap pins that root and existing local database identity before Magento bootstraps.
  Store 1 and its existing `Magento/luma` theme are retained. No branch/theme/database replacement.
- Node 22.22.0, PHP 8.3.28. No new dependency, SDK, copied vendor source, font or image was adopted.
  The existing reviewed original ceramics image and previously reviewed dependency graph are reused.

## Open the working demos

| Surface | Purpose |
| --- | --- |
| `http://127.0.0.1:4177/?page=silt-editorial` | Eight-section editorial template, independent saved draft, native apply/update/restore |
| `http://127.0.0.1:4177/?page=silt-stories` | Six-section stories template, independent saved draft, native apply/update/restore |
| `https://inox-us-staging.test/mte-silt-editorial` | Dedicated native Luma CMS page 243 |
| `https://inox-us-staging.test/mte-silt-stories` | Dedicated native Luma CMS page 244 |
| `https://inox-us-staging.test/mte-silt-source` | Magento-owned fictional studio text, CMS page 245 |

Final selections use the independently saved editorial/story drafts. Existing Home/About/FAQ pages
240–242 keep their saved draft and selection bytes. The new pages expose navigation to the full
five-page collection; the existing three-page shell navigation stays unchanged. The new templates
are also available as deliberate starting points through the generic template chooser.

The original `mte-studio@1.0.0` definitions remain byte-identical to their pre-batch source. Expanded
editorial equivalents use additive `mte-editorial@1.0.0`, avoiding silent required-field additions
to the accepted foundation schema. During this unaccepted batch, only its newly created Editorial
and Stories r2 drafts were augmented with the additional package defaults and advanced to r3;
authored heading/order values were retained. No historical/manual/foundation draft was migrated.

## Implemented behavior

The trusted package registration provides definitions, bounded schemas, presets, controls and
render dispatch. No editorial type switch was added to editor core. Package-owned semantic
validation and document-identity metadata support color pairs, linked images, the two-image count
and unique anchor names. PHP has explicit installed DI registrations for every supported type.
Merchant JSON cannot name or load a PHP class, template, module, script, URL service or package.

| Family | Actual behavior |
| --- | --- |
| Paired banners, heading/image compositions, information/promotion cards, columns | Ordered blocks, desktop/mobile column counts, per-image size/ratio/fit/visibility, per-card headings/captions/surfaces, original bordered/plain/overlay arrangements, readable panel-off overlays |
| Image banner, image/text and two-image stories | Responsive stacking, image-side/column sizing, vertical alignment, image overlay/radius, optional mobile image reference, CMS-linked images, separate text-panel surface and mobile text-below-image behavior; maximum two image blocks in the two-image composition |
| Rich text | Ordered semantic headings, captions, plain paragraphs with whole-paragraph emphasis, lists, quotes, images and independent action blocks; no arbitrary inline HTML |
| Disclosures | Native `details`/`summary`, individual/first/all initial-open modes, stack/split arrangement, row surfaces and original plus/number markers, CMS links, empty state |
| Anchors and separators | Unique bounded named focus targets with local fragment links; semantic line/dot separators and decorative spacing |
| Main/reusable page composition | Registered Magento source title/plain paragraphs, optional title, explicit no-content/unavailable states and a safe source link |
| Shared presentation | Original heading level/size/font choices, mobile heading/alignment, caption/text size, scoped width/reading measure, independent/theme padding/margin, surface palettes and paired custom hex colors with a 4.5 contrast-ratio validator guard |
| Links and media | Opaque registered CMS/media identities; escaped output; missing references have readable states; new-tab links include `noopener noreferrer` and an announcement |

CMS composition is deliberately bounded. `References::content()` reads only the dedicated source
page, rejects oversized content, executable tags and Magento directives, and returns escaped plain
paragraphs. It never evaluates a CMS filter/template or recursively embeds a selected page. Empty,
disabled and unsafe source states were tested against the actual Magento page, with content and
activation restored afterward. This is not general HTML/widget conversion or a general CMS provider.

The mobile image control selects within the existing original-media allowlist. The current local
demo has one reviewed image identity; it does not pretend to offer a larger media library. Alternative
reference bindings are contract support, not evidence of another installed provider or asset corpus.

## Explicit scope decisions and dependencies

These are implementation decisions and limitations for review, not authorization to remove criteria:

1. **ED-01:** Preserve accepted Studio 1.0.0 and foundation data; register expanded equivalents under
   the new editorial package. This maintains wire compatibility for existing pages and 03F rejection.
2. **ED-02:** Use original typography, palettes, spacing, template composition and structured text.
   Vendor-specific named presets, exact option/range identity, arbitrary inline formatting and hidden
   snippet behavior are not asserted equivalent. Partial entries remain visible for adjudication.
3. **ED-03:** CMS composition is dedicated, Magento-owned plain editorial content. Arbitrary native
   page HTML, directives, layouts and third-party widgets require the appropriate provider/renderer
   work. FAQ page references are safe links, not an assertion of arbitrary nested page rendering.
4. **ED-04:** Links resolve only registered Magento CMS pages; arbitrary external/catalog links are
   not accepted. Media is restricted to reviewed Magento-owned references. Interactive sliders,
   swiping/arrows, video, animations and highlight behavior remain SOL-533 dependencies; countdown
   timezone/expiry behavior remains SOL-536; product-backed information cards remain SOL-534.
5. **ED-05:** All these gaps remain in `reference/editorial-coverage.json`, merged into
   `reference/delivery-coverage.json`. SOL-532, SOL-530 and the full milestone cannot be closed by
   treating a section name or screenshot as complete field/snippet parity.

## Verification

| Check | Outcome and limit |
| --- | --- |
| `npm --prefix product run verify` | 104/104 tests pass; includes previous foundation/03F tests, full-schema controls validation, all 14 native/preview HTML comparisons, variant/empty states, contrast/URL/anchor/image-count rejection, coverage-destination integrity and editorial-CSS layout scope |
| `node component-library/native/silt-form/build.mjs` | Original schema/native metadata/CSS generation; the editorial CSS filename includes its content hash |
| `python3 component-library/scripts/editorial-coverage.py` then `python3 component-library/scripts/plan-coverage.py` | Reuses accepted census only; 14/326 assigned entries retained; complete 76-stem map and other owners preserved |
| PHP lint plus `php -d memory_limit=2G bin/magento setup:di:compile` in INOX | Native source syntax and actual DI compilation pass; no Composer/SDK/package operation |
| `node component-library/native/silt-form/editorial-runtime.mjs` | 39 native/API checks pass, including exact saved apply, variants/order/colors, malformed/oversized selection fallback, interrupted staging, foreign/executable/unsaved input and stale/cross-origin rejection, original restore and preservation controls |
| `source-state-test.php` controlled local source sequence | Empty, directive-bearing and disabled source states render their explicit native fallbacks while other sections remain selected; original content/activation restored |
| Browser, editorial flow | Edited heading, Save r2, reload retained text, Apply, native exact heading; independent Stories Save/Apply; later r3 defaults are the same batch's additive settings expansion; Stories r4 was saved/applied with a real mobile-image reference and linked-image setting, confirmed in native DOM; UI Restore showed the original page, reload kept r4, and Apply returned it to native selection |
| Browser, native responsive/keyboard | Actual native grids at 1280px; 390px document width equals viewport for both pages, 360px shell and 320px stacked content; native images loaded; Enter on the second summary expands it with focus retained on SUMMARY; native anchor navigation focuses its unique target; docs field tables stay inside their scroll container at 390px |
| P2 route/cache scope | Fresh local route receipt covers all five Silt pages after cache clean: only Editorial and Stories load the merged editorial CSS; Home, About and FAQ remain free of editorial selectors and editorial markup. Browser inspection confirms normal Home and editorial collection rendering. |
| `make -C docs verify` | Strict build and site check pass: 36 source pages, 37 HTML pages, 3,073 local links; anchors, assets, navigation and source/output separation checked |

Browser inspection caught a real merged-CSS cache issue: correct native HTML initially used a cached
foundation stylesheet URL and showed block layout. The native build now emits a content-hashed
editorial CSS asset and registers it in the dedicated layout handles. The changed merged URL was
verified in the browser; computed grid columns changed from `none` to the correct column widths.
This is a local asset-cache fix, not proof of a production publishing/cache-invalidation system.

## P2 asset-route remediation · 8 September 2026

Independent review identified that the content-hashed editorial stylesheet was selector-scoped but
still attached to all five Silt & Form layout handles, allowing the same merged asset to be served
to the foundation pages. The native build now removes editorial CSS from every Silt layout before
adding the generated hash only to `cms_page_view_id_mte-silt-editorial.xml` and
`cms_page_view_id_mte-silt-stories.xml`. Foundation CSS remains shared by all five pages.

After copying the generated handles to the authorized local INOX installation and cleaning its
`layout`, `block_html`, and `full_page` caches, a fresh five-route probe recorded the following in
`product/.local/sol-532/route-scope-results.json`: Home, About, and FAQ each returned the shared
merged asset `a432f7ebc1088fce7c7349c835f8a52e.css`, with no `.ed-section` selector and no
`data-editorial-kind` markup. Editorial and Stories each returned
`614984e47749a6c612b1866c27b6da04.css`, which contains `.ed-section`, with 8 and 6 editorial
markers respectively. Both routes were `200` HTML. Browser inspection then confirmed the ordinary
Home composition and the editorial collection render in the local storefront. This fixes the
reviewed routing issue; it does not establish a production cache-invalidation process.

Evidence is under ignored `product/.local/sol-532/`: product verification, DI compile, native runtime
results, actual native HTML, source-state results, exact `touched-files.json` and preservation hashes. Existing native global
CSP/third-party console messages and ordinary store chrome are outside this editorial package.
No whole-store accessibility, checkout, catalog, production or commercial-readiness claim follows.

## Exact changes and reversal

| Area | Scoped changes |
| --- | --- |
| Original package | `component-library/packages/editorial/`, trusted package list, generic registry/reference/semantic hooks, generated schema/metadata and scoped editorial CSS |
| Theme/editor | Original editorial template factory, additive targets/references/package pin; generic extra-reference controls and page-content preview resolver; product contract document-identity validation and tests |
| Native source | Additive `EditorialRenderer`, DI entries, validator/reference/selection/shell extensions, dedicated 243–244 layouts, generated contracts and content-hashed CSS attached only to the two editorial layout handles; local install/runtime/source-state scripts |
| Existing INOX source | Matching `app/code/MageThemeEditor/SiltFormDemo/` files and installation-only target-map additions; generated DI/cache/static artifacts. No new module enablement or `app/etc/config.php` edit in this batch |
| Database | New `cms_page` rows 243 (`mte-silt-editorial`), 244 (`mte-silt-stories`), 245 (`mte-silt-source`) and store-1 `cms_page_store` relations. Source 245 content/activation temporarily varied and restored for tests; normal CMS modification timestamps can advance |
| Selection/drafts | New independent editorial/stories draft files and native selection files; existing shared receipt log appended. Existing manual/foundation draft and native selection hashes match pre-batch values |
| Documentation | This evidence, field ledger, canonical coverage and execution/navigation notes; historical research bytes preserved |

A before snapshot lives at `product/.local/sol-532/before/`, including product/editor/source,
component library, canonical docs, the installed SiltFormDemo module, native state and existing drafts.
It is a local recovery artifact, not a distributable product archive.

To reverse only this batch:

1. Restore original selection for `editorial` and `stories` using the local controls (or the fixed
   local command with current selection hashes). This retains saved draft content.
2. Remove the two new target entries and the source reference only after verifying identifiers,
   page IDs and `[1]` store scope. Delete only newly created CMS pages 243–245 and their normal store
   relations through the Magento repository. Never delete pages 239–242 or ordinary CMS content.
3. Restore only the batch-touched SiltFormDemo source/target-map files from the before snapshot;
   remove its newly added renderer/layout/generated editorial assets. Preserve unrelated modules,
   the existing enabled-module config and other experiments. Recompile DI and clean the same local
   `config/layout/block_html` cache types as needed; do not replace databases or disable global caches.
4. Remove only the new editorial/stories native selection and draft files if desired, retaining
   receipts as evidence. Revert scoped package/editor/docs changes using the before snapshot,
   preserving later user work, then rebuild product and restart only the 4177 Silt demo server.

The accepted [serializer compatibility boundary](section-library-evidence-2026-09-08.md#silt-form-starter-foundation)
remains unchanged: the earlier vendor-file workaround is local, non-commercial and not upgrade-safe.
This batch neither edits nor broadens that workaround. No commit, push, PR, publication, remote
operation, new environment, real customer communication or marketplace/checkout work was performed.
