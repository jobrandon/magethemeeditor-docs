# Silt and Daybreak Liquid migration inventory — 11 September 2026

Status: **source inventory with initial Daybreak and complete-page-family Silt Liquid packages**. The original `theme-sdk/examples/daybreak-liquid-theme/` now maps all 19 homepage instances through 19 section and 23 block definitions under schema 1.3/CLI4. `theme-sdk/examples/silt-liquid-theme/` maps all 14 Silt source pages with 57 section instances, 44 section definitions, 47 block definitions, page metadata and menus under schema 1.3/CLI4. Both are readable standalone packages rather than wrappers around JavaScript factories. They remain reference conversions, not lossless Magento migrations: host media/providers, commerce/forms interaction, coupled validators and reversible merchant-draft conversion remain open. No persisted draft or native assignment was migrated.

## Measured starting point

The inventory evaluates the existing authored `defaultTheme()` factories and registered component
definitions. It never reads or saves merchant drafts and never contacts Magento. These are current
original source defaults, not a new import of the external reference theme or a claim of its full parity.

| Current source | Pages | Section instances | Semantic section types | Block instances | Setting definitions |
| --- | ---: | ---: | ---: | ---: | ---: |
| `silt-form/full` | 14 | 57 | 44 | 87 | 1,349 |
| `daybreak-market/full` | 1 | 19 | 19 | 47 | 812 |

Setting definitions count each field in each used section type and its declared block types once,
including shared definitions repeated across semantic types. They are not unique controls or saved
values. Silt's full-page defaults contain home, about, FAQ, editorial, stories, media, motion, catalog,
shopping, search, commerce examples, contact, signup and promotions. Daybreak contains its populated
homepage. Header/footer/menu resources are separate from these section counts.

Silt's native shell/account/cart surfaces and hybrid family pages are not all represented by these
14 factories. The wider [catalog coverage ledger](silt-form-catalog-coverage-2026-09-08.md), native
commerce evidence and [Daybreak receipt](../design/theme-editor-uiux/daybreak-preset-2026-09-10.md)
retain their separate scope and unfinished requirements. This inventory does not narrow them.

The reproducible local extraction is `docs/.local/liquid-reference-inventory.mjs`, with the complete
field/type map, 39 source-file hashes and counts in `docs/.local/liquid-reference-inventory.json`.
It uses the product's pinned Node 24.21.0 runtime. Neither artifact belongs in a distributed theme.

## Lossless settings prerequisites

The current SDK accepts text, textarea, checkbox, number, range, select, color and URL settings;
schema 1.1 adds menu references. Several existing values need a richer, explicitly versioned contract
before their portable migration. Treating them as unvalidated strings would change their behavior.

| Existing definition | Silt count | Daybreak count | Required migration behavior |
| --- | ---: | ---: | --- |
| Image reference | 39 | 22 | Preserve media identity; resolve through declared host/package resources with dimensions, alt text and unavailable state. Do not substitute a filesystem path or arbitrary image URL |
| Video reference | 2 | 0 | Existing video/video-background asset identities require a typed video contract; these ports are blocked and must not be coerced into image fields |
| CMS page reference | 35 | 25 | Preserve the target and choose from host-owned references; missing targets remain explicit and editable |
| Product/category reference | 8 | 5 | Preserve typed native identity and store context; host providers own visibility, price and stock |
| Bounded string list | 5 | 5 | Retain array shape, item order, empty-item semantics, item/count bounds and complete-state round trips |
| Bounded integer | 230 | 137 | Retain integer-only values and bounds; the current generic number/range validator accepts finite fractions |
| Optional color | 36 | 30 | Preserve empty as inheritance/unset alongside valid hex; current color settings require six-digit hex |
| Bounded text | 264 | 143 | Retain per-field minimum/maximum lengths; current text uses a shared 16,000-byte ceiling |
| Constrained anchor | 1 | 0 | Preserve the explicit safe-anchor grammar; do not expose an unrestricted merchant regex |

Existing select and checkbox settings can retain their native value shapes, but their IDs, defaults,
labels and constraints still need explicit mapping and verification. This table describes source
requirements; it does not announce an implemented schema version or relax schema 1.0/1.1 validation.
The shared menu image resource contract is useful precedent, not proof of general image controls,
media upload, product pickers or native reference providers.

## Coupled rules and non-section metadata

The snapshot now includes `component-library/src/html.mjs` and `src/render.mjs` alongside the
registry, original package definitions/renderers and theme factories. The JSON inventory records
actual `validate` function source for review, `uniqueFields`, `routeBindings`, `referenceFields`,
block limits, global settings/menus/slots/store, and each page's title/description/template/revision,
document identity, tokens and scope. Executable validators are audit material only; they must not
be copied into portable Liquid packages. Host/runtime dependencies outside these source inputs
still need their own migration and adoption review.

| Existing rule owner | Rules that field-type conversion alone does not preserve |
| --- | --- |
| Shared registry | Image requires alt text unless decorative; CMS reference and trimmed link label must both be present/absent; reference whitespace restrictions; per-page unique anchors; at most one shell header |
| Editorial package | Background/foreground colors set together and contrast at least 4.5 using its recorded luminance calculation; linked image requires CMS target; mobile image needs alt unless decorative; at most two image blocks in two-image story |
| Interactive package | Visible on at least one viewport; initial tab must identify an existing block; mobile and before/after image descriptions; linked-image target; required trimmed labels/description/transcript/quote/name/disclosure |
| Forms package | Required trimmed labels; linked-image target; at most one email-form block; popup visible on at least one viewport |
| Commerce package | Typed category/product reference identity restrictions and route bindings; native provider owns entity access and commerce behavior |
| Shell package | Trimmed nonblank heading/text/wordmark/link labels; native shell/service ownership remains separate from page factories |
| Daybreak preset | Inherits its original package validators; own theme/entity reference allowlists, no native routes and text-only menus; fictional services remain explicitly local |
| Shared theme/global model | Exact keys/revisions/store scope; bounded plain nonblank wordmark/announcement/footer text; menu/slot assignment and legacy identity/label/image constraints |

These are blockers for affected full-theme ports until represented by a bounded declared constraint
vocabulary or another reviewed equivalent. Positive text length does not preserve trimmed-nonblank
validation. The first richer-field fixture does not claim this cross-field validation parity.

Editable page titles/descriptions, template selection and page/global tokens have no complete
mapping in the current five-key Liquid state. Put immutable source scope/revision/provenance in a
migration receipt, but define a real editable/rendered destination before porting page metadata.
Do not discard it into that receipt or silently turn it into fixed package source. The first field
slice does not migrate these legacy pages.

Both current default factories have globally unique page/section/block instance IDs that fit the
SDK grammar. Arbitrary valid merchant drafts may repeat block IDs across sections or use longer
legacy menu IDs. The observed defaults do not prove those drafts are compatible.

## Stable source and state mapping

Create independently installable Liquid packages in new directories after ownership coordination.
Keep the original JavaScript themes and their drafts intact during conversion and acceptance.
Each package must contain readable layout, templates, section/block schemas, snippets, assets,
locales, defaults and developer instructions. Rendering must use authored Liquid rather than a
wrapper around the old JavaScript HTML generator.

The inventory proposes and checks these identifier transformations without applying them:

- `mte-studio/banner` becomes section type `studio-banner`; `daybreak-market/hero` becomes
  `daybreak-market-hero`. Presentation follows that semantic type when instances are duplicated.
- `imageAssetId` becomes setting `image_asset_id`. Every section/block field mapping was checked
  for target collisions and the SDK's lowercase setting grammar.
- Per-section block names become qualified global names, such as `studio-rich-text__paragraph`.
  The SDK defines blocks globally; unrelated legacy `paragraph`, `image` or `card` definitions
  must not silently overwrite one another. Proposed names fit its 64-character identifier bound.
- Preserve section/block instance IDs, order, disabled state and every mapped value. Preserve
  global settings and shared menus in the same atomic target revision. Missing or incompatible
  values produce an actionable migration report; do not silently reset them to defaults.

An import needs explicit source identities/revisions, a complete field and menu map, source and
destination hashes and a disposable destination first. Shared scalar fields map explicitly; header/
footer slots map to declared menu settings. Menu `storeId` must match the validated host/store and
is retained in reversible migration metadata, not silently discarded. Legacy `external` maps to
`url`; opaque menu images map to exact packaged images. Legacy 80-character IDs and 160-character
labels must fit the SDK's 64/120 limits or produce a reviewed reversible alias/rejection, never truncation. It must reconcile independent legacy page/shared
revisions into one target snapshot without overwriting a concurrent edit. The existing clean
Atelier and Navigation installations are unrelated baselines, not migration destinations.

## Coordinated implementation sequence

1. Preserve the now-accepted menu-editor baseline: 33 integrated product paths, 170 passing tests,
   141 matching artifacts, 340 SDK files, 17 original drafts and clean Atelier/Navigation revision 1.
   The [main acceptance receipt](../architecture/liquid-menus-contract.md#main-editor-acceptance) records exact proof layers.
2. Agree the [minimal richer-settings contract](../architecture/liquid-rich-settings-contract.md) with the sole editor owner. SDK validation,
   provider/resource resolution, strict TypeScript controls, complete-state saves and old-client
   rejection must agree. Preserve schema 1.0/1.1 behavior and use disposable repositories for
   incompatible-schema tests. Do not overload an existing version with newly lossy values.
3. The original Daybreak package supplies all 19 semantic section families. The Silt package supplies every current source page and instance with static mapping data, metadata and shared menus. Complete both with provider-backed media, legacy control/validator behavior, interactions, catalog/newsletter semantics and reversible merchant conversion before calling either a lossless port.
   Native providers remain separately accepted. Asset/module adoption and notices require the
   existing exact-version/provenance review, including Alpine CSP lifecycle behavior.
4. Port Silt's complete current page family and shared shell, then its remaining native surfaces.
   Resolve actual Magento providers and installed extension policy through trusted adapters.
   Keep prior default-store assignments and unassigned routes intact.
5. Verify one complete import/export/save/reload/rollback cycle for each package, every mapped
   field family, section/block duplication/reordering, responsive and keyboard interactions,
   native commerce boundaries and an independent developer's install/customize/debug workflow.

The schema and editor owners retain their separate files; this inventory grants no competing
product writer or new task. A field map and package preview do not complete native extension,
cache/outage, independent authoring or commercial-release acceptance.
