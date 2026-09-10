# Commerce catalog evidence · 8 September 2026

SOL-534 is **In Progress; original subset implemented, full family acceptance open**.
The original `mte-commerce@1.0.0` package registers exactly the assigned 19 stems on
existing local INOX Luma CMS pages 248–249. Every stem has a portable schema, generated editor
controls, preset and native renderer dispatch. That establishes bounded contract/native-state
coverage, **not working populated catalog, product-detail or purchase equivalence**.

The [921-entry field ledger](commerce-field-coverage-2026-09-08.md) retains all 58 blocks,
129 metadata entries, 102 original partial field mappings, six reference mappings with data gaps,
and 684 open field gaps. No material substitution or provider exclusion is accepted by this report.
The [complete catalog map](silt-form-catalog-coverage-2026-09-08.md) remains partial.

**Later bounded delivery:** [9 September full-theme commerce evidence](full-theme-commerce-evidence-2026-09-09.md) now establishes populated synthetic catalog/search and native simple-cart/totals/checkout transition. The empty-store observations below are historical. Full family/field/provider acceptance remains open.

## Ownership and boundaries

Coordinator 2 assigned task `01a080fe-b095-7242-aa55-0fe7f4c066ff` sole source/docs/local-INOX
ownership for SOL-534, with Astra High authorized for this scoped Magento integration architecture
and implementation. No additional agents were started. The accepted census was reused; Flux
source, templates, schema files, assets and snippets were neither recrawled nor copied.

- Product root: `MageThemeEditor`, implementation in `component-library/` and `product/`.
- Local target: existing `inox-us-staging.test`, resolved installation
  `/Users/branorphiano/Projects/s1/inox-us-staging`; branch `fix/INOXUS-creative-assets-fpc`, SHA `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
- Existing local bootstrap pins the installation and database identity before Magento starts.
- Store 1 (`default`), website 1, root category 2, existing `Magento/luma` theme.
- Dedicated CMS identifiers: `mte-silt-catalog` (248), `mte-silt-shopping` (249), assigned only
  to store 1. Prior pages 240–247, selections/drafts, native experiments and 03F are preserved.
- No new environment, database replacement, catalog/store assignment, customer identity,
  quote/cart/order creation, communications, remote operation, commit, push, PR or publication.

## Observed local data

A read-only database and service audit found no child categories under root 2. Website 1 contains
one assigned item, product 9457, with visibility 1 and a null name in the current store. It is
rejected as non-individually-visible. Website 2 has 9,567 assigned products under the other store
root; these are not borrowed for the default-store demo. The runtime snapshot therefore returns
`state: empty`, `categories: []`, `products: []`.

The native fulltext collection executes and returns an empty array for `rings`. Exact SKU lookup
returns no result for the non-visible item's SKU and for an unknown test SKU. Category 3, the
other store root, and a product assigned exclusively to website 2 are rejected. These are real current Magento reads, not mock results. Synthetic
positive data is used only in isolated source tests; it never populates the editor or native demo.

Successful populated category/product/related-result proof needs usable, already authorized
catalog data in the target store or a separately approved integration target. This task did not
change visibility, assignments, names, prices, stock, catalog indexes or create replacement products.

## Implemented subset and explicit gaps

| Assigned stems | Original behavior / native evidence | Remaining acceptance |
| --- | --- | --- |
| `collection-list`, `main-list-collections`, `subcollections` | Registered category references or bounded current-root/child queries, active ancestry checks, escaped native labels/links; genuine empty state | Populated result proof, image variants, ordering/pagination/carousel and advanced reference controls |
| `collection-tabs`, `featured-collections` | Ordered category references, optional labels, native disclosure groups and bounded category-product queries | Disclosure grouping substitutes for tabs; explicit scope decision and full tab/collection/preset parity remain open |
| `featured-collection`, `main-collection-product-grid` | Native category/product selection, position/name/newest ordering, bounded results, responsive grid contracts | Populated results, filtering, pagination, counts, sorting UI, rating/price/variant/cart controls and promo blocks |
| `image-banner-with-collections`, `image-banner-with-featured-collection` | Existing original editorial still-life reference plus category/product composition; alternative text required | Editorial image is not a catalog product; successful data binding, mobile art direction and complex banner blocks remain open |
| `main-collection-banner` | Current-store category title/description and native link; missing-category state | Actual category route opt-in, breadcrumbs and full banner/media behavior |
| `featured-product`, `main-product` | Enabled, individually visible, current-website product resolver and bounded plain description/native PDP link | No populated product; no embedded gallery, variant/pricing/stock/purchase or nested PDP block parity. `main-product` retains malformed reference-schema classification |
| `related-products` | Magento-owned relationship IDs filtered back through current-store visible-product resolver | Populated relationship proof, ratings/carousel and full appearance controls |
| `main-search` | Native fulltext collection, bounded escaped query, result/error/idle states, native full-search link | Empty search observed; successful results, filtering, article/CMS search remain open |
| `predictive-search` | Original debounced, abortable enhancement calls existing native search-term suggestions; text-only rendering, live status, Escape dismissal, ordinary submit fallback | Search-term suggestions differ from predictive product/page/blog cards; fragment has no schema. Empty response is not positive suggestion-result proof |
| `quick-order-list` | Read-only exact SKU lookup, ordered product reference contract, native PDP handoff | Bulk quantities, product options and quote submission are not implemented; no cart-success claim |
| `sticky-add-to-cart` | Product reference and persistent native PDP action when a visible product resolves | PDP action is not add-to-cart; embedded options/quantity/quote adapter and populated sticky behavior remain open |
| `pickup-availability` | Typed product reference plus explicit missing pickup-provider state | No source-location/inventory provider is bound; no availability or pickup promise is invented |
| `recently-viewed-products` | Explicit requirement for private browser-scoped history provider | No history provider, tracking, session data or private customer history is exposed; native history behavior is open |

No ordinary PDP/category/search/cart route is replaced. Pricing, customer-group context, tax,
stock, configurable options and cart actions remain on native Magento pages. All reference
substitutions above are recorded as **unaccepted**, and SOL-534 is not completed.

## Trust and execution

Merchant JSON has bounded strings, allowlisted choices and opaque `category-N` / `product-N`
references. Additional fields, URLs, PHP classes, renderer paths, price snapshots, invalid versions,
control characters and unsupported targets are rejected. Trusted DI alone selects installed
renderers. The native validator independently checks schema, package pin and target; apply also
re-resolves every non-empty catalog reference in the current store before replacing selected bytes.

`CommerceData` resolves through existing Magento repositories/collections with explicit store,
website, status, visibility and category ancestry checks. URLs must stay on the current store origin
and contain a safe path; raw catalog descriptions are bounded and escaped, with directives and
executable markup excluded. The editor receives public catalog reference metadata only, without
prices, quote/customer IDs, inventory promises or another store's fallback content.

The new layouts are non-cacheable only on their two dedicated CMS handles. Search is a GET read;
CMS search does not persist search-query history. Existing Magento suggestion responses provide
search terms only. JavaScript uses `textContent`, bounded suggestions, cancellation and request
ordering. There is no `eval`, external player, HTML response injection or merchant endpoint field.

The local selection mechanism retains file locking, compare-before-change and original fallback.
Corrupt bytes return the original dedicated region. This remains a single-machine demo, not a
production publication, durable rollback or multi-node cache-coherence system.

## Verification and evidence

Evidence files are kept locally under `product/.local/sol-534/`; browser captures are under
`output/playwright/sol534-*`. They are not public website artifacts.

| Check | Observed outcome |
| --- | --- |
| `npm --prefix product run verify` | 104 passing tests; reviewed eight-package dependency/notice check and editor build |
| `node --test component-library/test/*.test.mjs` | 26 passing tests, including eight commerce checks, exact census/schema mapping and cross-target rejection |
| `php component-library/native/silt-form/commerce-domain-test.php` | 26 synthetic source assertions for current website, visibility, active ancestry, unsafe URLs, result bounds, exact SKU/native fulltext dispatch and provider errors |
| Native schema boundaries | Both interpreters accept supported enum/numeric/Boolean boundaries and reject unsafe fields, unknown versions and foreign target documents |
| INOX `php -d memory_limit=2G bin/magento setup:di:compile` | Successful after adapting injection to Magento's virtual fulltext factory using its concrete product collection factory type |
| Native read check | Actual empty current-store catalog/search/SKU results; foreign root and non-visible product rejection |
| Editor lifecycle | Catalog and shopping edits survive save/reload; native headings verified; restore returns original content while drafts remain; both demos reapplied |
| `node component-library/native/silt-form/commerce-lifecycle-check.mjs` | 21 passing native HTTP/CLI assertions: both-page foreign-reference rejection, current-byte preservation, empty rendering, stale-hash rejection, corrupt-file fallback, exact-byte restoration, search input rejection/escaping, cache boundary and ordinary-route controls |
| Native browser | Nine shopping sections, desktop/390px mobile screenshots, labeled search/SKU fields, live native suggestion JSON `[]`, Escape dismissal/focus, real search and exact-SKU submit returning empty results |
| Documentation browser | Evidence page, headings and three tables rendered in the existing local docs server; completion warning remains visible |
| Preservation | Prior draft/selection hashes unchanged; pages 240–247 content hashes, store/root identities and product-assignment counts match baseline |
| `make -C docs verify` | Strict build and generated-site links/anchors/navigation check pass; does not establish runtime support |

The first shopping apply rejected `SCHEMA_VARIANT` while the long-running editor server held the
previous in-memory schema. The server was restarted on 4177 after the final build. Only the newly
created shopping draft's removed, nonfunctional fields were dropped, its revision advanced and it
was re-saved through the editor. Earlier drafts and the manual 4173 editor were untouched. The
failed attempt did not become a native selection.

Mobile QA caught and corrected a 22px SKU input overflow using scoped border-box sizing and an
explicit input type. Live suggestions exposed Magento's `/default/` URL prefix; the fixed-route
same-origin guard now accepts valid store codes. Escape's native search-input behavior was prevented
to keep dismissal status and focus stable. The final native browser check passed all these cases.
No successful product-result or purchase interaction was simulated to make the demo appear populated.

Focused browser checks are not formal WCAG certification. The editor's pre-existing `data:,`
favicon CSP warning and surrounding native theme/asset behavior are distinct from this package.
No weakening of CSP, external asset rules or the accepted serializer workaround was performed.

## Source, database and runtime changes

| Area | Scoped changes |
| --- | --- |
| Original package | `packages/commerce/{package,render,runtime}.mjs`, scoped CSS; `themes/silt-form/commerce.mjs` factories |
| Shared source | Trusted package list/catalog read capability and dispatch, starter targets/template gating/navigation, generated schemas/metadata; catalog reference controls and preview services/forms; commerce-specific preview boundary label |
| Native source | New `CommerceData`/`CommerceRenderer`, DI registration, additive schema, target gate and reference validation in selection, conditional catalog reference status, navigation preserving previous pages |
| Native new assets | Content-hashed commerce CSS/JS and exactly two CMS layout handles; old handles unchanged |
| Local installation | Matching changed `app/code/MageThemeEditor/SiltFormDemo` files; `local-targets.json` adds only catalog 248/shopping 249 |
| CMS database | Two new CMS pages and corresponding store assignments; all other content/catalog/customer/quote/order rows preserved |
| Editor/native state | New `silt-catalog.json`, `silt-shopping.json` draft files, new catalog/shopping active selections and ordinary append-only selection receipts |
| Generated runtime | DI compilation; local `config`, `layout`, `block_html`, `full_page` cache cleaning; no cache type disabled |
| Documentation/coverage | 19-stem commerce overlay, regeneration integration, field ledger, this report and canonical links/status |

No third-party dependency, SDK, service, font, icon or new image/video was adopted or upgraded.
The existing reviewed React/Ajv graph and original ceramics asset are reused. Native Magento
catalog/search services remain in the already installed edition; no vendor source is redistributed.
The already installed Playwright CLI 0.1.19 and its existing Playwright/core
1.63.0-alpha-2026-08-31 runtime were used for local development QA without installation or shipping.
The prior serializer workaround remains **local and non-commercial**; this batch does not clear it
for product distribution, upgrade safety or commercial release.

## Practical reversal and independent review

1. Save any newer user work first. Use **Restore original** on Catalog and Shopping in the editor,
   or the existing fixed local command with each current selection hash. These actions leave drafts.
2. For complete removal, remove only the two newly owned drafts and selection files after backing
   them up. Keep the shared receipts log and all pre-existing selections/drafts.
3. Verify CMS IDs 248/249 still belong to `mte-silt-catalog`/`mte-silt-shopping`, then remove only
   these pages through Magento's CMS repository and remove their two local target-map entries.
4. `product/.local/sol-534/before/` and `before-manifest.json` preserve source/installed files and
   prior drafts/selections. `installed-changes.json` names each installed mutation. Reverse only
   this batch's listed changes; do not overwrite later family work with a whole-folder restore.
   Remove the new commerce package, registered capability/targets, new native classes/layouts/assets;
   restore the prior generated schema/theme files or regenerate from the retained package list.
5. Rebuild editor/native metadata, recompile existing Magento DI and clean the same local cache
   types if reversing source. Restart only the verified Silt demo listener on 4177. Leave 4173,
   vendor serializer, `app/etc/config.php`, branches and other experiments untouched.

Independent substantive review must examine store/website boundaries, search-term/provider
substitutions, missing success-path runtime proof, native/preview semantics and all material gaps.
The coordinator must either schedule remaining implementation/data work or record explicit scope
acceptance. These open criteria cannot be closed by the presence of 19 component names or schemas.
