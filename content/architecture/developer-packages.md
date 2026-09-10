# Developer-authored sections and components

Updated: **8 September 2026**. The user's product requirement is that theme developers can
build their own sections/components. This is a core authoring capability to prove, independent
of any future marketplace. The first local implementation demonstrates trusted package
registration, an original five-section collection, a separate author example, and one bounded
native Magento registration. It does not establish a public SDK or general native portability.

## Implemented package boundary

`component-library/packages.mjs` is the application owner's trusted local/build-time registration
entry point. It imports the Studio, editorial and author-example package modules.
A developer adds a package directory and one import/list entry here; the editor core needs no
per-section change. Package modules are executable trusted developer code, reviewed and installed
by the application owner. Merchant JSON is declarative data and cannot install code or select a
module path, PHP class, template, renderer or remote plugin.

| Package field | Implemented contract |
| --- | --- |
| `id` | Stable lowercase namespace, 2–40 characters; duplicate namespaces reject |
| `version`, `contractVersion` | Exact `1.0.0` in this bounded proof; other versions reject pending migration/compatibility work |
| `components` | Original component name → display metadata, field definitions, default preset, optional bounded block definitions |
| Component identity | `package-id/component-name`; section JSON also pins component `version` and exact package `{id, version}` |
| `previewRenderer` | Trusted original DOM renderer capability `mte-dom@1.0.0` |
| `nativeRenderers` | Explicit versioned native adapter declarations with component names and `local-dedicated-cms` scope; declaration alone does not install or prove an adapter |
| `dataCapabilities` | Bounded media-read, CMS-page-link and registered CMS-page-content requirements, or empty; unsupported capabilities reject |
| `assets` | Empty in this proof. Bundled assets reject until an adopted asset pipeline, inventory, rights review and native availability exist |
| `render` | Trusted package function returning original HTML after core validation; receives only the declared reference resolver functions |

The five Studio identities are `mte-studio/banner`, `mte-studio/rich-text`,
`mte-studio/image-text`, `mte-studio/cards` and `mte-studio/faq`. The separate notice identity is
`author-example/notice`. Section IDs and ordered block IDs are merchant-content identities;
block IDs are unique within their section, so duplicating a section preserves its local block
structure. No block ID is used as an unqualified global DOM ID.

The existing portable content 1.0.0 envelope is retained, and the component schema references
the generated original library schema. These are additive, explicitly registered capabilities;
old hero 1.0.0 is unchanged, and older consumers reject unsupported types. This is not a silent
conversion of historical drafts or a migration implementation.

## Small author example

The working package is `component-library/packages/author-example/package.mjs`. It defines only
three settings: a bounded heading, bounded message and a `quiet`/`highlight` choice. Its default
preset and renderer are in its own package file. It imports only the library's original HTML
escaping helper. It has no media, catalog, account, cart, checkout, forms or external services.

To author another small local section:

1. Create `component-library/packages/your-package/package.mjs`, following the author example.
   Choose a new package namespace and component name. Keep code and assets original or complete
   the [third-party review](../requirements/third-party-compliance.md) before adoption.
2. Define the supported fields, default preset and optional bounded blocks. Declare required
   data services explicitly; start with `nativeRenderers: []` until an adapter is installed and
   verified. Use empty `assets` for this proof.
3. Export the trusted preview renderer from that package. Escape all merchant text and use only
   the bounded resolver facade for media/page references. The helper rejects non-local, encoded,
   traversal, protocol-relative and otherwise unsafe path results. Package code is trusted code,
   not a sandbox; code review remains necessary.
4. Add the import and package to `component-library/packages.mjs`. Run `npm run verify` from
   `product/`. The build regenerates the portable schema/preset inventory and packages the original
   module graph into an explicit local asset manifest. Restart the local demo server after changing
   its package list, since server-side validators are initialized at process startup.
5. Open Add section. The generic registry supplies the catalog entry; generic controls come from
   the fields. Add/edit/duplicate/reorder/undo, export/import, validation, save and reload all operate
   on the portable document. The preview dispatcher calls the package renderer. No editor-core
   switch or component-specific control file is required.

`contracts/sections.schema.json` is a portable JSON Schema 2020-12 artifact;
`contracts/packages.json` records package metadata and original preset inventory. `packages/*`
are authored source, while these JSON files are generated from that source. No Shopify schema
is imported or translated. Native declaration/version changes do not automatically broaden the
generic publication model, which still rejects package sections pending a real release pipeline.

## Supported fields, blocks and validation

The proof supports bounded strings, Boolean fields, bounded integer choices, string enums and
bounded string lists. Unknown schema keywords/types reject at registration. Every setting is
required; an explicit empty image/page reference means no image/link. Arbitrary objects, HTML,
Liquid, script, style strings, URLs, catalog snapshots and arbitrary nesting are unavailable.

Sections use fixed surface, spacing, width and alignment tokens where their package defines them.
Cards allow 1–4 desktop columns, two columns at medium widths and one at narrow widths. Split
sections stack on narrow screens. Rich text uses ordered paragraphs with normal/strong/emphasis,
subheadings, lists and quotes. FAQ blocks use native `details`/`summary` for keyboard disclosure
without a package interaction script. The editor uses a separate selection button so a section's
links and disclosures are not nested inside a button-role container.

Block arrays may be empty with an explicit empty state. Rich text/FAQ allow up to 24 blocks and
cards up to 12. The wire envelope is bounded to 1 MiB and depth 32 by the existing parser; it
rejects duplicate JSON keys, unsafe numeric forms and invalid Unicode. JSON Schema checks shape,
types, constants and bounds. Semantic validation additionally checks block identity uniqueness,
accessible media, complete link pairs, safe identities and demo reference availability. Browser
validation is tested against the same limited schema vocabulary and Node/Ajv validation.

Media requires an opaque Magento-owned asset reference and an alt description unless explicitly
decorative. Links pair an opaque CMS page reference with a label. The illustrative editor resolves
only its existing original ceramics asset and fictional studio page. These service names describe
the required native ownership; the first Studio package does not yet call Magento media/CMS services.
Missing resolver results render an unavailable state, with no broken external link or executable URL.

## Native Magento registration proved separately

The accepted 03F bridge still projects only the historical home hero to its fixed target. It
rejects all package sections. Its old native validator, selection files and rendering code were
preserved. A new, separate `MageThemeEditor_SectionLibraryExperiment` module registers only
`author-example/notice@1.0.0` from `author-example@1.0.0` with renderer `mte-local/notice-php@1.0.0`.

The native package schema is an exact generated copy of that author's original section schema,
protected by a parity test. The trusted PHP registry chooses an installed PHP renderer. Its
validator accepts only the fixed target document/scope, one registered notice, exact package and
component versions, exact fields and bounded canonical JSON. Unknown package/type/version,
foreign target, executable fields and malformed bytes reject. Native Magento escaping protects
the final HTML. There is no JavaScript package execution or React on the shopper page.

The dedicated existing-INOX CMS page is `mte-package-library`, page 239, store 1, with its existing
Luma theme. Its block checks local root, host, route, page identity, store, theme and non-cacheable
layout before reading its private selection. The neighboring native CMS content is independent.
Saved editor JSON was staged with the exact authored notice section intact, selected locally,
rendered on this page and then restored. [Dated runtime evidence and reversal](../roadmap/section-library-evidence-2026-09-08.md)
give the exact commands and limits.

This initial proof is one independently registered author example with a manual local native adapter.
The subsequent [Silt & Form foundation](#silt-form-starter-theme-package) adds the five Studio native
renderers on separate dedicated pages. Registering another preview package does not automatically
produce a Magento adapter.
Generic package installation, native SDK lifecycle, signing, hosted permissions, durable publication,
cache invalidation, multi-node recovery, broad theme/version support and commercial distribution
remain open. Marketplace sales, seller accounts and commissions/payouts remain future planning only.

## Silt & Form starter theme package

The next local foundation adds `component-library/themes/silt-form/theme.mjs`. This original
`Silt & Form@1.0.0` package declares its identity, description, supported package pins, required
original media reference, accent/spacing settings and scoped hybrid shell. Its Home, About and FAQ
factories assemble the current Studio sections with populated copy, ordered blocks and media/page
references. The theme package owns its preview shell function and presentation copy/navigation; native
`ShellRenderer` consumes generated `contracts/theme.json`, so those values are not editor-core constants. The package is a content-theme layer on dedicated pages, not a replacement Magento theme.

Open the [local starter editor](http://127.0.0.1:4177/?page=silt-home). Pick a page, choose a starter,
edit its copy/media/page links and ordered sections/blocks, then **Save draft**. **Apply to local
page** selects that exact saved draft on its dedicated INOX page; later saves use **Update local
page**. **Open Magento page** shows native output. **Restore original** removes only the selected
page’s active content, preserving its independent saved draft. All actions are editor controls;
the merchant does not copy JSON or run terminal commands. Starter defaults, unsaved edits, saved
revision and actual applied revision have separate UI states.

The initial pages are `/mte-silt-home` (CMS 240), `/mte-silt-about` (241), and `/mte-silt-faq` (242),
all on the existing `inox-us-staging.test` default store 1 with Luma. The local editor’s separate
saved files are `product/.local/silt-form/drafts/silt-{home,about,faq}.json`. Template factories return
fresh objects. Choosing a starter explicitly replaces the current edit buffer, with explanatory
dialog text and undo; it does not overwrite saved content or other pages. The portable content
1.0.0 format stays unchanged. Package metadata and executable code are not embedded into merchant
content. Required package/type/version pins remain in each section.

### Extending the collection

1. Add an original section through `component-library/packages.mjs` and the package’s `components`
   definitions/render function, as described above. Fields and bounded block controls are generated;
   the editor has no per-Studio-type control switch. Add its package pin to the theme’s supported
   package metadata. `supportsStarterSection` discovers support from those installed pins.
2. Add a template factory, catalog entry and page-instance declaration in the **theme package**.
   The editor discovers its template choices and supported section catalog from package data;
   it does not enumerate three template cards or five section types in core. Current native targets
   intentionally remain a trusted allowlist. A new native route requires explicit developer-owned
   CMS/store identity registration and layout, never a path supplied by merchant content.
3. Supply a native class implementing
   `MageThemeEditor\SiltFormDemo\Api\RendererInterface`. Register declarative type → injected
   renderer mappings in Magento `etc/di.xml`. The native `Registry` dispatches the installed object;
   JSON cannot name an executable class, renderer path, template or service URL.
4. Generate native schema and scoped original CSS using
   `node component-library/native/silt-form/build.mjs`. The native validator consumes the same
   installed section schema and exact package/component pins. Its deliberately small schema
   vocabulary supports the current bounded object/string/choice/integer/Boolean/list/block unions.
   New field vocabularies or data capabilities require deliberate validator/service work and parity
   tests; registration does not magically implement providers.
5. Extend actual reference services and local target registration when needed, then prove save,
   reopen, native field/order equivalence, responsive/keyboard behavior, rejection and restoration.
   Preserve existing page selections and all earlier proofs during extensions.

This is an extensible **local example**, not a finished generic SDK, plugin installer, signed
package system or untrusted-code sandbox. The local adapter currently resolves one original image
from Magento `pub/media/mte-silt-form/ceramics.png` and the registered dedicated CMS page references (initially three; expanded below)
through `PageRepositoryInterface`, requiring exact store membership `[1]`. The editor receives that
same catalog from the local bridge and serves the same media bytes. Unknown references reject;
deleted/missing references render readable fallback states. No client product images or data are
redistributed. The existing Magento image optimizer may produce its own local WebP rendition.

### Local selection boundary

`product/src/silt-local-bridge.mjs` starts a fixed installed local PHP entry point with JSON stdin,
a fixed PHP executable and working directory, and no shell. The loopback server requires an exact
Host and same-origin JSON POST for apply/restore; native bridge routes are enabled only for the
separate starter demo server. It validates the exact saved draft before invoking Magento. Native
bootstrap verifies the existing root/database, emulates the default storefront and verifies Luma.

The native `Selection` validates the generated schema, declarative target, actual page/media
references and last-observed selection hash under a lock. It atomically renames complete per-page
content and records before/after hashes in local receipts. A stale selection rejects. Missing,
malformed or oversized selected content restores original rendering. Each dedicated block also
checks host, route, page ID/identifier, store, current theme and non-cacheable layout. Assets and
active content remain on Magento when the editor is stopped. The surrounding native header,
footer, catalog, cart and checkout remain Magento-owned.

This provides local apply/update and original restoration, not signed hosted publication,
multi-tenant authentication, multi-node coherence, durable crash recovery, arbitrary image upload
or a general media browser. A timeout has an uncertain acknowledgement; refresh status before
retrying. Global caches remain enabled; the dedicated page layout is non-cacheable. No general
cache invalidation claim follows.

The [dated starter evidence](../roadmap/section-library-evidence-2026-09-08.md#silt-form-starter-foundation)
records exact checks, local touches and reversal. The [full catalog coverage plan](../roadmap/silt-form-catalog-coverage-2026-09-08.md)
assigns every reference family to SOL-531–537. This five-section foundation does not complete that
milestone, Hyvä/Porto, catalog/PDP/search/checkout, provider integrations or commercial readiness.

## Editorial package extension

SOL-532 adds `mte-editorial@1.0.0` with 14 original types and populated Editorial/Stories templates,
while retaining the accepted Studio definitions. [Editorial evidence](../roadmap/editorial-catalog-evidence-2026-09-08.md)
and the [field ledger](../roadmap/editorial-field-coverage-2026-09-08.md) distinguish supported controls
from explicit provider dependencies and partial equivalence decisions. Native pages 243–244 are
additional opt-in targets; source page 245 provides bounded Magento-owned editorial text.

Three small trusted definition hooks extend the existing authoring boundary:

- `referenceFields` maps extra control names to the already available reference catalog, such as
  `mobileImageAssetId: 'assets'`. It is package metadata, not merchant data. The generic editor
  renders the selector, and reference validation includes the selected identity.
- `validate(section)` supplies package-owned semantic checks after generated-schema validation.
  The editorial package uses it for paired readable colors, media/link accessibility and the
  two-image limit. These checks are explicitly mirrored by the installed native validator.
- `uniqueFields` lists package fields that must be unique within a document, used for named
  anchors. The shared contract/editor call `validateLibraryDocument`; editor core does not
  switch on editorial section types.

The declared `magento.cms-page.content` capability exposes only a scoped `resolvePageContent`
function to the preview renderer. The fixed local bridge supplies title/plain paragraphs only
for source page 245. It does not enable arbitrary CMS HTML, template evaluation, widgets or a
general provider SDK. Native references are validated against installed store/page ownership.

The native build emits an editorial CSS filename derived from its content hash and registers
it in the dedicated layout handles. This avoids stale browser reuse of a merged stylesheet
URL when the original editorial CSS changes. General publication/cache behavior remains open.

## Interactive media package boundary

SOL-533 adds `mte-interactive@1.0.0` with ten original component definitions and an installed native
adapter on dedicated INOX pages 246–247. The original progressive runtime has fixed preview imports
and content-hashed native assets; merchant JSON cannot supply script/class/provider paths. The local
media resolver recognizes original image identities and one original silent WebM. No generic remote
video/review/product provider or broader SDK capability was introduced. Read the
[interactive evidence and reversal](../roadmap/interactive-catalog-evidence-2026-09-08.md) and
[299-entry coverage ledger](../roadmap/interactive-field-coverage-2026-09-08.md) before extending it;
working original subsets and unaccepted reference exclusions remain distinct.
