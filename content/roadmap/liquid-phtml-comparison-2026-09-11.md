# Liquid and native PHTML comparison — 11 September 2026

Status: **same-design baseline implemented and independently accepted locally by PM**.
Liquid remains the selected authoring direction. This controlled comparison advances
[ADR 0004](../decisions/0004-developer-theme-authoring.md) and SOL-521; it does not introduce a
second supported product engine or close full theme/editor/extension/release acceptance.

## Result and recommendation

The original Atelier Commerce design renders through both the accepted Liquid runtime and
Magento's native PHP template engine. Home and configurable-product documents match after
explicit normalization of formatting, route names and native session/return fields. Native
PHTML also completed a Gold quantity-1 add through the original Magento controller, producing
the same $34 unit/subtotal and confirmed consent-gated events. The exact disposable cart was removed.

These results support continuing the chosen Liquid implementation: native commerce authority
and the page design are independent of the template syntax when both consume the same data
contracts. Both sources remain readable. Liquid's strict missing-variable diagnostic is useful;
ordinary PHTML needs its own validation/error policy. This is an engineering assessment of the
implemented sample, not independent developer/merchant research or general extension compatibility.

## Controlled inputs and tested environment

| Input | Recorded value |
| --- | --- |
| Native installation | Existing `inox-us-staging.test`, Magento Open Source 2.4.6-p13, PHP 8.3.28 |
| Branch and HEAD | `fix/INOXUS-creative-assets-fpc`, `046d6e87866e7f6c5172e9c63f90097ac8b08295` |
| Scope | Store 1 / website 1; isolated `/mte-liquid/` and `/mte-phtml/` routes |
| Theme source/state | Read-only installed Atelier Commerce 1.0.2, revision 3; digest `fb014b5f8ebe5fab2c76609adf5fdb9cbf16f3b788a429f7619fb6c5519a4b84` |
| Data | Same accepted catalog/product/variant/form services, native prices, stock, visibility and URLs |
| Assets | Exactly the same installed CSS/modules, SHA384 identities and host browser lifecycle; no new dependency or asset |
| Browser | Disposable Chrome context; desktop 1365px and mobile 390px |
| PHTML source | `theme-comparison/phtml/`, handwritten markup rendered by `Magento\Framework\View\TemplateEngine\Php` |

The PHTML module declares a dependency on the existing `MageThemeEditor_LiquidTheme` provider
services. It reads the same assignment/repository without changing either, uses the same schema
and state contracts, and uses existing asset/runtime metadata. It **never calls the Liquid
template renderer or inserts Liquid-generated HTML**. Only its document/section/block/snippet
rendering differs. The comparison is therefore a view-layer experiment, not a standalone PHTML SDK.

PHTML templates use native `Escaper` text, attribute and URL methods. The renderer selects from
nine fixed template names; merchant content cannot choose a PHP path. One thin layout bridge
brings the total to ten PHTML files. The original Liquid package has eight template files.
Observed source counts are 212 PHTML lines including DocBlocks/bridge/head partial versus
102 Liquid lines. These counts describe this implementation's conventions; they are not a
controlled measure of authoring time or maintainability.

Product navigation targets the corresponding comparison route. The normal `form_key`, native
product/options/quantity fields, cart action and return URL retain Magento authority. The existing
`mte_liquid` marker requests the shared persisted-cart acknowledgement; it grants no access and
does not bypass CSRF or installed customer-group policy. The accepted local
SalesOne_CustomerGroupCatalog return-contract correction remains unchanged.

## Verification layers

| Layer | Writer evidence |
| --- | --- |
| Source | All 16 PHP/PHTML files pass PHP syntax and the 120-character line check; four XML files validate against installed Magento schemas with its URN resolver |
| Native wiring | 22 source files staged into the separate comparison module; controller resolves the normal native layout and PHP engine |
| Route isolation | Seven checks: home/product 200; missing page, hidden configurable child and unassigned store 404; earlier native product/Silt home 200 under their original renderers |
| Semantic parity | Home has 129 matching parsed HTML events; product has 124. Attributes, content, form structure and inert JSON agree after documented normalization |
| Editable input | Both engines reflect the same in-memory edited wordmark/text and section reordering; malicious-looking text remains escaped. No merchant draft or installed state is saved by this probe |
| Diagnostics | Both identify the missing product name's source; PHTML exposes a PHP warning under an installed temporary diagnostic handler, while Liquid rejects with a strict template exception |
| Template confinement | An undeclared `../document` PHTML fragment rejects |
| Browser | Collection-to-product, Gold $34 selection, quantity 1, native cart, consent/events, desktop/mobile and zero JavaScript errors |
| Native cart | One visible line, quantity 1, subtotal/grand total $34; acknowledgement item/SKU/quantity/price agrees with persisted quote rows |
| Cleanup | Exact quote 61436 and its two item rows removed through the native repository after the disposable browser closed; zero remaining quote/items and zero orders |

HTTP parity normalizes whitespace, attribute order, route names, `form_key`, encoded return URL
and inert JSON formatting. It does not remove arbitrary markup differences. The script is
`theme-comparison/phtml/scripts/compare-http.py`; raw documents and its receipt live under
ignored `.local/`. The native route remains private, `no-store`; public/FPC cache behavior is untested.

Nine rendering probes run inside the existing native CLI bootstrap. Their missing-data test
removes `catalog.products[0].name` only in memory. A temporary error handler captures PHTML's
`Undefined array key "name"` at `snippets/product-card.phtml:11`, and is immediately restored.
With that handler, PHTML returns output with a warning; Liquid throws
`snippets/product-card.liquid:4: Variable product.name not found`. This does not assert how every
Magento deployment configures PHP warning display or logging. The comparator's public error
path catches exceptions and returns fixed 503 text without private data.

The first browser harness used the fixture's SKU-derived description as its visible link name;
the actual product name is **Liquid Test Cup**. That locator failed before any cart submission.
The corrected browser used the actual label and submitted once. The first read-only database
probe omitted Magento's table prefix; it was corrected to use `ResourceConnection::getTableName`
before any mutation. Neither harness failure is counted as successful proof.

## Bounded rendering timings

Measurements use the same pre-resolved state/data/assets in one already-running native PHP
CLI process, with CLI OPcache disabled. Engines alternate to reduce order effects. Ten samples
per engine/page are summarized by the mean of the middle two sorted values. No network,
database/provider resolution, repository loading, FPC, cold Magento startup or browser time is
included. Fresh-instance measurements include renderer construction and rendering; they better
resemble the current route's per-request view setup than reusing a parsed Liquid renderer.

| Page / renderer lifecycle | PHTML median | Liquid median |
| --- | ---: | ---: |
| Home, reused renderer | 0.269 ms | 0.114 ms |
| Product, reused renderer | 0.176 ms | 0.131 ms |
| Home, fresh renderer | 0.287 ms | 0.442 ms |
| Product, fresh renderer | 0.197 ms | 0.549 ms |

The same small fixture produces different rankings under the two lifecycles. Do not turn these
values into a universal speed claim or commercial performance clearance. End-to-end cold/warm
requests, realistic large themes, cache invalidation and editor-outage tests remain open.
Raw samples/ranges, CLI settings and protocol are recorded in `.local/render-probes.json`.

## Exact writes, preservation and reversal

The only persistent native source addition is `app/code/MageThemeEditor/ThemeComparison/`.
The 22-file source/staged aggregate is
`225fb5fd2882e002347c6f6db1aa95b0eaa36a033173626ca684f03dd72d3d2f`, encoded as SHA256 of sorted
relative path, NUL, file SHA256 and newline. The manifest is
`theme-comparison/phtml/.local/staged-files.json`.

`app/etc/config.php` changed only by adding `MageThemeEditor_ThemeComparison => 1`:

- Before: `dd69ff6d5010cee581a288ba5bb62e6d0d1b18a442e9d2829566b04b253d53e4`.
- After: `a41ee3cd8d3f525de5ecab92f34fad0dba2c027d8654a476472b86593dd561ae`.

The native `module:enable` command cleared its normal configuration/generated-class caches;
explicit cache cleaning was limited to `config` and `layout`. No setup upgrade, static-content
clear/deploy, global theme assignment, branch change, commit or push ran. The proposed
`pub/media/mte-phtml` and `var/mte-phtml` directories were unnecessary and were not created.
All 340 frozen SDK files and 241 staged Liquid files retain their accepted hashes.

One disposable guest quote was created by the browser: **61436**, parent item **261358**
(product 9738, Gold SKU, quantity 1, $34) and child item **261359** (product 9737, quantity 1,
native child row price $0). No customer was created; no address, order or payment was submitted.
Cleanup validated the pre-run ID/time bounds, guest/store/quantity/totals, exact two products and
absence of orders before deleting only that quote. Fresh queries found zero remaining rows.
Existing product fixtures and earlier commerce evidence remain intact.

To reverse the module, first verify current owned file hashes and preserve any wanted newer
comparison edits. Disable only `MageThemeEditor_ThemeComparison`, then remove only that module's
configuration entry and owned directory. Compare the current configuration before editing;
never restore the whole before-file over later unrelated work. Clean only config/layout caches.
The shared Liquid assignment/state/assets/module and existing products are not part of reversal.
The recorded disposable quote has already been removed and must not be recreated for reversal.

## Independent acceptance

PM accepted this bounded comparison after independently reproducing all seven HTTP isolation
checks, both normalized document comparisons and all nine rendering probes. It repeated the
bounded fresh/reused timing protocol without treating those view timings as end-to-end performance.
Fresh desktop/mobile Chrome checks covered collection-to-product navigation, Gold selection,
$34 price, quantity 1, complete header/footer, zero JavaScript errors and no mobile overflow.
Those review sessions submitted no cart request and loaded no analytics.

Direct read-only database checks found zero rows for quote 61436, items 261358/261359 and orders
for that quote. PM verified all 22 source/staged hashes and the aggregate above, and confirmed
that removing only the comparison module entry makes the decoded configuration strictly equal
to the recorded before-file. All 340 SDK files, 241 native Liquid files, 17 original drafts and
main Atelier revision 1 were preserved.

The native cart submission, persisted acknowledgement and consent-gated events were accepted
from reviewed writer evidence and the inspected cart screenshot; PM did not repeat that
transaction. Syntax and XML validation also remain writer evidence. Receipt:
`product/.local/source-refactor-review/phtml-comparison/acceptance.json`.

## Remaining acceptance

PM has accepted and integrated the separate [HTTP-v2/shared-menu editor](../architecture/liquid-menus-contract.md#main-editor-acceptance):
33 product paths, 170 main tests, 141 matching artifacts and 28 HTTP cases independently reproduced
in each checkout. Main menu movement/navigation checks are independent; persisted whole-theme
save/conflict/schema-upgrade browser cases remain reviewed writer evidence.
Full Silt/Daybreak migration, reviewed editor-shell/section-and-block DnD parity, native
menus/cart/account surfaces, wider installed extension/price-hiding behavior, custom-provider
example, store-wide analytics/external SDK policy, locale/dialect completeness, migrations/
uninstall, independent authoring and release support/inventory remain open. This comparison
does not satisfy those criteria by sharing the same native data services.
