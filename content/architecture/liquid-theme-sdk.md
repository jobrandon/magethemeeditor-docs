# Liquid theme SDK

Status: **PHP SDK, first editor adapter and native configurable cart/shipping handoff implemented locally; full parity and broader acceptance remain open**.
Updated: 11 September 2026. This is the implementation workstream for
[ADR 0004](../decisions/0004-developer-theme-authoring.md).

## Source and commands

The SDK is in `theme-sdk/` at the product workspace root. It has its own Composer/npm
locks and does not edit the active editor worktree. Maintained browser lifecycle code
is strict TypeScript; PHP implements package validation, persistence and rendering.

```text
theme-sdk/
  bin/theme.php                  Developer CLI
  src/
    Console.php                  CLI request validation and dispatch
    PackageFiles.php             Bounded package snapshot and digest
    ThemePackage.php             Manifest, components and resolved theme state
    SettingsSchema.php           Public setting definitions and value validation
    RichSettings.php             Schema 1.2 typed values and field constraints
    RichState.php                Complete rich-state and raw JSON shape validation
    ResourceCatalog.php          One trusted catalog for menus and typed resources
    SettingResources.php         Render-only resource projections
    Json/                        Raw lexemes, exact integers and map-aware output
    AssetManifest.php            Explicit assets, dependency order and integrity
    RuntimeMarkup.php            Host-owned browser bootstrap metadata
    Renderer.php                 Shared PHP Liquid rendering entry point
    ThemeRepository.php          Immutable releases and separate merchant state
    ThemeException.php           File/line diagnostics
    Liquid/                     Package-local file lookup and custom filters
  storefront/
    lifecycle.ts                 Module mount, teardown, consent and event ownership
    analytics.ts                 Injected analytics transport adapter
    script-registry.ts           Same-origin module loading with browser SRI
    bootstrap.ts                 Public registration, consent and remount API
    commerce.ts                  Native option selection and confirmed cart events
  magento/LiquidTheme/            Native layout, assignment and provider adapter
  examples/starter-theme/         Original Atelier developer theme
  examples/commerce-theme/        Separate Atelier Commerce home/product example
  examples/navigation-theme/      Original two-page shared-menu example
  examples/rich-settings-theme/   Original schema 1.2 typed-field example
  test/                          Runtime and browser-module lifecycle tests
  third-party/                   Exact-use review and preserved engine notice
```

Activate the repository's pinned Node 24.21.0/npm 11.19.0 runtime. PHP 8.3.28 was
used for this checkpoint; PHP 8.2 and other Magento PHP combinations remain untested.

```bash
cd theme-sdk
composer install --no-dev --no-plugins --no-scripts
npm ci --ignore-scripts
npm run verify
php bin/theme.php validate examples/starter-theme
php bin/theme.php inspect examples/starter-theme
php bin/theme.php install examples/starter-theme .local/themes
php bin/theme.php status .local/themes atelier
php bin/theme.php export .local/themes atelier .local/atelier-export
```

`render THEME_DIRECTORY` reads JSON from standard input:
`{page, state?, data, assetBaseUrl, preview?, runtimeBaseUrl?}`. Its result contains `html`, declared
`assets`, `diagnostics`, resolved `state`, `theme` identity and package `digest`.
Failures exit with code 1 and diagnostics containing `severity`, `file`, `line` and
`message`. `inspect` returns the manifest, control schemas, component definitions
and resolved default state; it does not import a theme-specific JavaScript factory.

`inspect-installed REPOSITORY ID` returns the same inspection plus `selection`, from
one coherent package/state snapshot. `render-installed REPOSITORY ID` takes the render
request plus required `expectedRevision`, defaults to saved state, and returns the
revision it used. Stale previews reject with a `revision` diagnostic; previewing never
saves state. A host can supply an unsaved complete state for rendering.

`save REPOSITORY ID` reads `{expectedRevision, state}`. `rollback REPOSITORY ID`
reads `{expectedRevision}`. A stale revision is rejected. Saves require complete global settings, groups and pages. Explicit null/non-list page/group/block values and invalid disabled flags are rejected without changing selection bytes, revision or content. Package installation uses
versioned immutable releases, a lock and atomic selection replacement. An identical
install is idempotent; replacing bytes under the same version is rejected. Upgrades
validate the existing merchant state first. Removed/renamed settings currently require
an explicit migration and are rejected rather than discarded. Rollback validates current
merchant state against the previous source; it also rejects incompatible changes.
Export includes theme source/defaults, not merchant drafts. General uninstall,
migration tooling and Magento publication recovery are still required.

## Developer theme structure

```text
atelier/
  theme.json                     Versioned manifest, pages, providers and assets
  layout/theme.liquid            Complete HTML document and page shell
  templates/home.json            Default ordered section instances
  sections/
    hero.liquid                  Readable HTML and Liquid
    hero.schema.json             Label, group, settings and allowed blocks
    header.liquid
    header.schema.json
    footer.liquid
    footer.schema.json
    products.liquid
    products.schema.json
  blocks/text.liquid
  blocks/text.schema.json
  snippets/product-card.liquid
  config/settings_schema.json    Global controls
  config/settings_data.json      Theme defaults and shared header/footer instances
  locales/en.default.json         Translation resource; lookup integration pending
  assets/theme.css
```

The manifest declares `schemaVersion: 1.0.0`, `runtime: mte-liquid-1`, a lowercase
theme ID, exact semantic version, layout and named page templates. It declares asset
identity, file, `css`/`module` kind, `essential`/`analytics` purpose, preview policy and
ordered dependencies. Supported control types are text, textarea, checkbox, number,
range, select, color and URL. Rich media/reference controls and existing catalog
schema migration remain work to complete; the small original starter is runtime proof,
not a replacement for the promised full theme/component coverage.

Theme state has global `settings`, shared `header`/`footer` section lists and `pages`
mapping page keys to ordered section instances. Instances have `id`, `type`, `settings`,
`blocks` and `disabled`. Block instances have `id`, `type` and `settings`. Source defaults
and merchant state are separate. Unknown settings, unsupported blocks, duplicate IDs,
unsafe setting URLs and malformed types are rejected by the runtime.

## Rendering and data boundary

The implementation currently selects `keepsuit/liquid` 0.12.0, source revision
`f91f238054d4430d56e0e390ccabfe1faab95dd5`. Its Composer manifest requires PHP `^8.2`
and `ext-mbstring`, with no transitive runtime packages. The matching MIT notice is
preserved and the exact-use review is in `theme-sdk/third-party/review-2026-09-11.md`.
[Pinned upstream source](https://github.com/keepsuit/php-liquid/tree/f91f238054d4430d56e0e390ccabfe1faab95dd5).

The same PHP engine now runs in the isolated Magento adapter and loopback preview. This
keeps local Magento rendering independent of a storefront Node daemon and hosted
editor availability. The first asynchronous editor adapter is accepted locally; full editor parity remains open. The engine
implements Liquid syntax, not Shopify's commerce objects or theme runtime. Its
`render` tag accepts explicit package paths such as `snippets/product-card`.
Schema sidecars are MageThemeEditor's JSON contract, not Shopify `{% schema %}` tags.

Templates receive global `settings`, `theme`, `request` and plain `data`; individual
components receive `section` and/or `block`. The layout receives renderer-owned
`content_for_header`, `content_for_header_sections`, `content_for_layout` and
`content_for_footer_sections`. Sections also receive `content_for_blocks`.

Provider data must be bounded JSON-compatible values. PHP objects, resources, deep
or cyclic data are rejected. Strict variables/filters surface missing data with file
and line diagnostics. Theme packages cannot contain PHP or select filesystem paths
outside the in-memory package snapshot. Symlinks, traversal, unknown source types and
oversized packages are rejected. Engine work/output limits are one layer, not an OS
process sandbox. Cumulative render work is now bounded across separately rendered sections and blocks
and covered by a regression test. Production process time/memory boundaries still
require hardening and measurement.

Liquid output is not automatically HTML escaped by this engine. The reference theme
uses explicit `escape` filters for text and attribute values. Developer templates are
trusted code; a future installation policy must validate unsafe output patterns and
review intentional HTML/JavaScript capability. Provider implementations must validate
their URLs and context. Passing the reference escaping test does not prove arbitrary
third-party themes safe.

## Third-party scripts

`ThemeLifecycle` owns module mounting, teardown, abort signals and a storefront event
target. Analytics modules do not load until consent is granted; withdrawal tears them
down while preserving essential UI instances. Pending loads receive cancellation signals.
Editor-only remounts clean old listeners, late module loads cannot mount after
revocation, and acknowledged commerce event IDs can suppress duplicate delivery.
Storefront-only modules are excluded from preview.

`createAnalyticsModule` accepts a transport with a `track(event, properties)` method.
A store-owned adapter can wrap Mixpanel's SDK; current tests use a local collector.
No Mixpanel dependency, account token, live transport or production analytics request
has been added. Browser bootstrap and actual package module loading now work in the
loopback and native routes. The host passes a same-origin `runtimeBaseUrl`; the renderer
emits encoded JSON configuration and a module bootstrap in the document head. Module
entries require same-origin URLs and browser-verified SHA384 integrity. A failed or
altered script produces an asset diagnostic while the page remains readable.

Developer modules register their declared identity and keep effects inside `mount`:

```javascript
window.MageThemeEditor.registerModule('my-feature', {
  mount({ root, events, signal, reportError }) {
    // Attach DOM and storefront-event listeners with { signal }.
    // Return a synchronous cleanup function for SDK-specific disposal if necessary.
  },
});
```

The runtime exposes `setAnalyticsConsent(boolean)`, `remount()`, `emit(...)` and
`dispose()`. Consent defaults to denied on each document. The original Atelier 1.1.0
example provides explicit allow/reject controls and a local-only analytics module.
No consent is inferred or persisted by that demonstration. Stylesheets are essential
and follow manifest order; explicit `requires` connects module entries. Registered
modules initialize in dependency order and clean up in reverse order.

These are trusted JavaScript packages, not a JavaScript sandbox. SRI validates declared
entry bytes; it does not prove arbitrary imports or an external vendor SDK safe, remove
already executed code, or revoke data previously transmitted. External SDK URL policy,
store-owned integration configuration remain open. Native confirmed add/cart-updated events now have bounded evidence in the separate commerce example; broader commerce event coverage remains open.
Shared store analytics settings
must eventually remain separate from theme source so switching themes preserves them.

## Verification and remaining acceptance

At this checkpoint, `npm run verify` passed strict TypeScript, Biome lint/formatting,
PHP syntax checks, 32 PHP tests, eight script-lifecycle tests, one installed-preview CLI
test, two commerce parsing/selection tests, three versioned menu CLI tests and the browser-module
build (**46 tests total**). This includes the newer standalone menu/schema 1.1 work; earlier native
and first-editor receipts retain their original tested source snapshots.
The PHP tests cover full-page rendering, settings/order changes, explicit escaping,
source diagnostics, package boundaries, render limits, source integrity, stale saves,
idempotent installation, upgrade/export/rollback and incompatible-upgrade rejection.
The script tests cover consent, remount cleanup, duplicate events, late loads, preview
policy, dependency failure, pending-load cancellation and preservation of essential UI
on consent changes. These are source/runtime tests. A subsequent browser check at `http://127.0.0.1:4320/`
confirmed the complete starter document, loaded stylesheet, product cards and collection
anchor navigation. It uses fictional local data. Native evidence below remains distinct
from editor parity and the full commerce acceptance criteria.

| Requirement | Current evidence / remaining work |
| --- | --- |
| Readable full-page authoring | Original small starter runs; Silt/Daybreak migration and catalog breadth open |
| Public schemas, packages and state | Executable inspect/render/install/export/save/rollback; richer controls, migrations and uninstall open |
| Developer scripts and tracking | Native browser loading, consent/withdrawal, remount and altered-entry rejection pass; store-wide configuration/external SDK policy open |
| Editor parity | HTTP-v2 shared-menu/two-page adapter accepted in main; reviewed shell, general section/block drag/drop and richer reference parity remain open |
| Magento commerce/data provider/extension | Native configurable prices/options, cart acknowledgements, rejected-request preservation and authenticated shipping handoff pass; one installed extension return-contract fix tested; broader policy/provider acceptance open |
| PHTML comparison, caching/performance/outage | Same-design native PHTML baseline independently accepted; bounded view timings only. End-to-end cache/performance/outage acceptance remains open |
| Independent developer authoring | Not yet performed; a fixture authored by this implementation task does not substitute |
| Dependency/distribution readiness | Exact implementation pin and notices reviewed; final release inventory/support matrix open |

PM's independent read-only review found two defects in the initial checkpoint:
manifest fields could override computed asset URLs/integrity, and explicit null state
could reset merchant content to defaults. Both were corrected. Asset fields now have
an allowlist and computed delivery fields take precedence; malformed/incomplete saves
are rejected atomically. New regressions cover the reproduced overrides and 11 invalid
save shapes. PM independently reran eight disposable probes and confirmed both findings closed: overrides reject, valid assets have computed same-origin URLs/SHA384, and invalid saves preserve exact bytes/revision/headline. This is bounded source/persistence acceptance; broader acceptance remains open.

## Native Magento checkpoint and reversal

The existing INOX installation remains on `fix/INOXUS-creative-assets-fpc`, Magento CLI
2.4.6-p13, native checkout commit `046d6e87866e7f6c5172e9c63f90097ac8b08295`, local PHP 8.3.28. This identifies the tested environment; it is not a supported
release matrix. PM coordinated the new `MageThemeEditor_LiquidTheme` module and isolated
`/mte-liquid/...` routes. The module was staged from `theme-sdk/magento/LiquidTheme` into
the existing `app/code/MageThemeEditor/LiquidTheme`; SDK PHP source, reviewed engine and
notices are included in its local staging bundle. Magento's Composer files were unchanged.

The native layout result loads only `mte_liquid`, with a root container and thin PHTML
view-model bridge. The installed Liquid package produces the complete HTML document.
No global Magento design theme is assigned. Trusted providers are registered through
Magento DI and implement `ProviderInterface`; themes declare identifiers, never PHP classes.
The catalog provider uses `ProductRenderListInterface`, website/status/visibility filters,
current store/currency and native price/salability results. The current default-store
fixtures display Silt Test Cup at $24 and Silt Test Bowl at $36. Browser navigation from
Liquid reached the original native product page with its matching $24 price.

Five HTTP checks passed: assigned Liquid route 200; unknown page 404; unassigned store
404; original product and prior Silt home 200 without the Liquid renderer header. Liquid
responses contain one complete document and `private, no-store` headers. No full-page
cache acceptance is implied by choosing uncached responses.

Atelier was upgraded locally from 1.0.0 to 1.1.0 with exactly identical merchant state.
Native Chrome checks in a disposable browser confirmed: no analytics request before
consent; one analytics and one essential-module request despite repeated consent/remount
operations; cleanup on withdrawal; four remounts without duplicate mock event delivery;
390px layout without horizontal overflow; altered analytics bytes rejected by SRI while
the storefront remained readable. Commerce events in that test were synthetic local
acknowledgements, not evidence of a real Magento cart mutation.

PM independently accepted this exact staged checkpoint. Its fresh review matched all
229 staged module-file hashes, the selected package/state, the sole configuration delta,
the runtime digest and all 17 existing editor drafts. It reproduced all five HTTP checks
and the disposable native browser consent/remount/mobile/SRI scenarios. Its independent
receipt is `product/.local/source-refactor-review/liquid-native-independent/acceptance.json`.
This acceptance covers staged runtime `39a937953cebf044430b2351b2505e7c0b38b52947a8c144a4df4c495c75d956`;
the later standalone installed-preview CLI commands and invalid-cleanup guard were not
in that native bundle. The native review freeze has been released. Broader commerce,
extension, caching/outage and editor acceptance remain open.

At that initial rendering-only checkpoint, these native paths changed: the new module directory; one enabled module entry in
`app/etc/config.php`; `var/mte-liquid` for assignments, runtime identity and immutable theme
releases/selection; and `pub/media/mte-liquid` for content-addressed theme/runtime assets.
`module:enable` and scoped `cache:clean config layout` ran. No `setup:upgrade`, database
content change, environment creation, commit or push ran at that initial checkpoint. The subsequent commerce receipt below adds three products and one local extension correction. Existing dirty configuration
was retained; its pre/post diff contains only `MageThemeEditor_LiquidTheme => 1`.

The local receipt under `theme-sdk/.local/native-validation/` contains the original
configuration copy, staged-file hashes, pre-upgrade selection, HTTP checks and isolated
browser results. Screenshots are under `theme-sdk/output/playwright/`. To reverse this
scoped installation: disable only `MageThemeEditor_LiquidTheme`, remove only its new
configuration entry after comparing current changes, and remove its owned module/state/
asset directories only after verifying the receipt hashes and preserving wanted theme
state. Never restore the entire earlier configuration over unrelated subsequent edits.
Clean config/layout caches after reversal. No other MageThemeEditor module or draft path
belongs to this receipt.

## Native configurable commerce checkpoint

The separate `examples/commerce-theme` package is **Atelier Commerce 1.0.2**. Its digest is
`fb014b5f8ebe5fab2c76609adf5fdb9cbf16f3b788a429f7619fb6c5519a4b84`.
It preserves the original Atelier 1.1.0 package and editor fixture. Readable
`sections/product.liquid`, `product.schema.json`, `templates/product.json` and
`assets/product.js` add a product page. The native `product` provider resolves options,
prices, availability, form key and native cart URLs. The shared `commerce.ts` module
selects native variants and enhances a normal Magento form; preview mode prevents cart writes.

Exact product reads use `ProductRepositoryInterface` and the native product-render
collector with explicit website/status/visibility checks. They cannot reuse a catalog
listing's category visibility condition, which excludes hidden configurable children.
Hidden children remain inaccessible as standalone product pages. Cart mutations still
run through Magento's original cart controller, form-key validation and access policy.

After native cart persistence, the adapter verifies the saved quote item and returns
`X-MTE-Cart-Event`. The browser requires successful HTTP and a valid acknowledgement
before emitting `cart:item-added`/`cart:updated`. `line_quantity` is the persisted line
quantity, not the amount added by the latest request. No quote ID, session or customer
identifier enters the event. A failed or ambiguous request shows an unconfirmed message
and is not automatically retried. This is not server-side idempotency.

Browser and native evidence now covers Black $28 / Gold $34, quantity selection, Gold2
at $68, Black1 at $28, native cart subtotal $96, and exact item/quantity/price/subtotal
preservation for invalid form key, invalid combination and excess-stock requests.
The local analytics collector received one confirmed add and one updated event after
consent. Guest checkout retained the existing disabled policy. One synthetic customer
then reached native checkout `#shipping`, with the loading mask gone and all three
units/subtotal preserved. No address, order or payment was submitted.

An installed **SalesOne_CustomerGroupCatalog 1.0.0** plugin declared only `ResultInterface`,
although native AJAX add returns `ResponseInterface`. That mismatch caused HTTP 500 after
successful persistence. A minimal local union-return correction restored acknowledgements;
six native probes include permitted response/result passthrough and a denied policy that
never invokes the action. Its proprietary source is not included in this SDK. Price hiding
and the extension's wider frontend policy still need an explicit adapter and acceptance.

Current staging contains 241 owned module files; native runtime digest is
`4906d600854ffae72156916ae378c4eb0d396568312b8d567754439f08998fa1`.
The three owned products remain for review. All five recorded disposable quotes and the
synthetic customer were removed after logout; fresh counts confirmed zero remaining
identities/items and zero orders. Temporary credentials/session files were removed.
The [commerce receipt](../roadmap/liquid-native-commerce-2026-09-11.md) records exact scope,
failures, test identities and reversal. PM accepted this later 241-file checkpoint in
`product/.local/source-refactor-review/liquid-native-independent/commerce-acceptance.json`.
It independently reproduced six native probes, seven HTTP cases and fresh product/price/consent
browser checks, and verified native hashes, cleanup, retained products and preserved drafts. The
cart/authenticated-shipping journey was accepted from reviewed writer evidence and code, without
repeating transactions. Shipping-method/address/payment/order acceptance remains outside this scope.

## Richer field SDK checkpoint

The [agreed schema 1.2/CLI3/HTTP3 field slice](liquid-rich-settings-contract.md) is assigned to the
existing SDK and sole editor owners. Main remains on a byte-identical accepted 340-file SDK copy.
Original `theme-sdk/` now implements the bounded schema 1.2/CLI3 slice: exact raw JSON/integer
roles, richer fields/defaults/complete state, coherent resource projections and retained-release
inspection. Full required verification passes **64 tests (44 PHP, 20 Node)**; its 363-file
source/build/vendor snapshot is independently accepted and remains frozen for product interoperability.
PM reproduced all 64 tests and matched 363 files plus five supplemental runtime/notice files.
See the [SDK checkpoint](../roadmap/liquid-rich-sdk-2026-09-11.md) for source identity, commands,
boundaries and preservation evidence. PM accepted the 31-path local HTTP3 integration in main4177:
183 product checks, two 46-case HTTP runs, rich-field browser acceptance and preserved drafts,
selections and native/PHTML snapshots. Full Silt/Daybreak migration remains open.

## Shared menus and schema 1.1

The separate original `examples/navigation-theme` package opts into schema 1.1 with home/about
templates, shared header/footer menus, bounded nested navigation and an original package image.
Menu settings reference shared merchant state; validation covers identities, limits, assigned-menu
deletion and compatible upgrades/rollback. Host-owned references resolve native/entities safely;
guest/customer display rules do not grant access. The original Atelier and Commerce packages remain
unchanged. This increment is standalone and has not been staged into Magento.

Installed schema 1.1 inspection/render/save requires explicit CLI contract 2; older clients fail
before losing menu state. Whole-state save validates the installed schema, revision and complete
menus inside the lock. The [concrete menu and HTTP-v2 contract](liquid-menus-contract.md) defines
wire shapes, host resources, nullability, errors and legacy preservation. SDK behavior is implemented;
PM accepted and integrated the sole owner's HTTP-v2 implementation: 33 product paths, 170 required
tests, 141 matching build artifacts and 28 independently reproduced HTTP cases on both worktree and
main. Fresh main pointer/keyboard menu movement, two-page buffer retention, unsaved navigation,
Phone preview and legacy canvases passed. Actual whole-state persistence/conflict/schema-upgrade
browser cases were accepted from reviewed writer evidence without repeating saves. Clean Navigation
schema 1.1/revision 1 is available at `http://127.0.0.1:4177/liquid-theme?id=atelier-navigation`; original
Atelier and 17 drafts remain intact. See the [main menu acceptance](liquid-menus-contract.md#main-editor-acceptance)
and `product/.local/source-refactor-review/liquid-v2/main-acceptance.json`.
PM independently accepted the corrected 340-file SDK snapshot:
32 PHP tests plus three installed menu CLI tests, exact hashes, unchanged main v1 Atelier render,
17 drafts and 241 staged native files. The full 46-test suite and standalone navigation browser
checks are separate writer evidence. Receipt: `product/.local/source-refactor-review/liquid-menu-sdk/acceptance.json`.

## Editor integration contract v1

PM accepted and integrated the first Liquid HTTP-v1 editor adapter in the main checkout:
29 product paths, 160 passing required tests, 141 matching build artifacts and 239 matching
SDK snapshot files. Eighteen actual SDK HTTP cases cover contracts, asset integrity,
validation, conflicts and preservation. Disposable browser checks cover complete-state
save/reload, 409 buffer retention, stale-render suppression, cancelled save navigation,
full-document head assets, consent and disposal. PM's fresh main checks mounted Liquid,
Silt and Daybreak without JavaScript errors; all 17 original drafts remained unchanged.
Receipt: `product/.local/source-refactor-review/liquid-integration/main-acceptance.json`.

The main local route is `http://127.0.0.1:4177/liquid-theme?id=atelier`. It uses fictional
catalog data and a clean separate Atelier 1.1.0 installation under
`product/.local/liquid-editor/repository`. This is separate from Magento publication.
The editor still uses a basic schema interface and ordering arrows. The reviewed shell,
drag/drop, menus, richer settings and multipage browser parity remain open. The sole
first adapter assignment is complete; its owner is now implementing the coordinated v2/menu scope. PM owns main integration/restarts.

The implemented host adapter uses an explicit `contractVersion: 1` HTTP envelope around
existing CLI data. Its host-configured endpoints are:

| Host endpoint | SDK operation and response |
| --- | --- |
| `GET /api/liquid-themes/:id/status` | `inspect-installed REPOSITORY ID`; return `{contractVersion: 1, inspection}` including coherent `selection` |
| `POST /api/liquid-themes/:id/render` | Body `{expectedRevision, page, state}`; host supplies fixture/provider data, asset/runtime paths and `preview: true`; call `render-installed`; return `{contractVersion: 1, result}` |
| `POST /api/liquid-themes/:id/save` | Body `{expectedRevision, state}`; call `save`; return `{contractVersion: 1, selection}` |

Theme state is `{settings, header, footer, pages}`. Settings are scalar strings/numbers/
booleans. Each page is an ordered section array; sections have `{id, type, settings,
blocks, disabled}` and blocks have `{id, type, settings}`. Global control schemas and
section/block schema sidecars come directly from inspection. One integer selection
revision covers the complete state transaction; the adapter must not silently weaken
it into independent per-page revisions or discard fields while translating editor state.

Keep PHP subprocess arguments as arrays, constrain theme IDs to an installed allowlist,
use bounded stdin/stdout and timeout/cancellation, validate the response in strict
TypeScript, and serve only declared assets and host-owned runtime files. Return 409 for
`revision` conflicts and 422 for validation diagnostics; abort/transport errors remain
distinct. Repository paths, PHP executable, provider implementations and source package
installation are host configuration, not request fields. Use an isolated local Liquid
repository and explicit local-data labeling for the first editor preset; do not write
existing Silt/Daybreak draft stores or native publication state.

The renderer returns a whole HTML document. The editor must use a separate asynchronous
whole-document path with stale-response suppression and existing selection/navigation/
save guards. Do not nest it in the old body-only shell. Preserve source annotations,
diagnostics, head assets and script lifecycle; schema controls, global groups, ordering,
duplication, save/reload and draft conflict behavior require browser acceptance. Menu
schema and complete reference-theme capabilities still need coordinated extensions.

The active objective remains **complete the Liquid implementation**. None of the
unfinished items above is silently removed from that objective.

## Native PHTML comparison

The [same-design comparison receipt](../roadmap/liquid-phtml-comparison-2026-09-11.md) records a
separate handwritten native PHTML module with matching home/product structures, the same
state/providers/assets, bounded renderer timings, source diagnostics and a cleaned Gold quantity-1
/$34 guest-cart smoke. PM independently accepted the 22-file comparison after seven HTTP checks,
two document comparisons, nine render probes, read-only browser checks and exact cleanup/configuration
verification. Cart submission and consent events were accepted from reviewed writer evidence without
repeating the transaction. The frozen SDK and staged Liquid bundle remain unchanged. This bounded
acceptance does not establish a second supported engine or full theme/editor acceptance.
