# Liquid richer settings and lossless theme migration

Status on 11 September 2026: **bounded SDK field slice and local HTTP3 editor accepted in main4177**.
The schema/CLI implementation has the [SDK checkpoint](../roadmap/liquid-rich-sdk-2026-09-11.md);
HTTP/browser acceptance is recorded in the SDK checkpoint and main integration receipt. PM accepted the previous
[menu editor](liquid-menus-contract.md#main-editor-acceptance); its SDK, product and native source
snapshots remain protected while this work proceeds. The [source inventory](../roadmap/liquid-reference-migration-2026-09-11.md)
records the original Silt/Daybreak values this proposal must preserve.

PM and the editor owner accepted the versioning direction and requested concrete boundary
corrections. The editor owner's delta review agrees with this corrected bounded slice; it verified
all 39 inventory hashes and the expanded fixture. PM then assigned the existing SDK owner to original
`theme-sdk/` and the sole editor owner to product v3 in worktree 6b5c. Main uses a byte-identical
accepted SDK copy at `product/.local/liquid-editor/sdk-snapshots/schema-1.1-51cf480c0354/`; the
pin receipt is `product/.local/liquid-editor/sdk-runtime-pin.json`. Neither implementation owner
may modify the pinned runtime, main repositories/configuration or native modules.

The SDK now connects bounded raw JSON and exact integer validation to package/default/state,
CLI3 saves/renders, normalized resources and retained-release inspection. Full required SDK checks
pass **64 tests: 44 PHP and 20 Node**. PM independently reproduced those 64 tests and verified the
363-file source/build/vendor checkpoint plus five supplemental files. PM then integrated the 31-path
product HTTP3 delta, rebuilt 141 artifacts, passed 183 product checks, two 46-case HTTP runs and
main browser acceptance. The accepted main runtime now uses the schema 1.2 immutable pin; the
former schema 1.1 snapshot remains preserved as accepted historical evidence.

## Version and ownership boundary

Propose manifest/state schema **1.2.0**, installed CLI capability **3** and explicit HTTP routes
`/api/v3/liquid-themes/{id}/{action}`. Package release versions remain independent. Keep runtime
identifier `mte-liquid-1`; the package schema selects the supported vocabulary. Versions 1/2 and
schema 1.0/1.1 keep their existing behavior and envelopes. A contract-3 client supports all three
schemas as a discriminated union and never synthesizes menus into schema 1.0 state.

Every installed inspect/render/save for schema 1.2 requires `--editor-contract=3`. Contracts 1/2
reject it before reconstructing state, including packages whose current values happen to be scalar.
Unknown versions reject explicitly. Revision, package schema and complete-state validation happen
inside the save lock in the existing order. A stale revision still produces `revision` before a
different installed schema produces `state-schema`; neither error overwrites the dirty buffer.

Schema 1.2 objects remain JSON objects even when empty: `settings: {}` and empty provider maps
never become `[]` through PHP associative decoding. The `pages` container is a map whose
values are ordered section arrays; menus, groups, blocks and string-list values remain arrays.
Typed references are exact two-key objects; the empty string is their sole optional value. Historical empty-array-as-empty-map compatibility stays confined to older schema
branches, including when those packages use contract 3.

Authored defaults and source-template instances may omit setting values, which resolve from their
validated definition defaults. A schema 1.2 complete installed save or explicit preview draft must
include every declared global setting and every declared setting on every present section/block.
It also includes all pages/groups/menus and normalized instance fields. Missing fields reject;
complete-save validation must not quietly backfill defaults. This distinction does not tighten
older state schemas or their package definition rules when accessed over v3.

Schema 1.2 retains the exact five top-level state keys `settings`, `header`, `footer`, `pages`,
`menus`. Resource catalogs and resolved objects are never persisted. Existing section/block
identity, group, order, disabled state and menu rules remain in force. The SDK owner implements
SDK/package/provider boundaries only after agreement; the sole editor owner implements strict
TypeScript controls and host translation in its existing worktree. PM owns main integration.

## Settings vocabulary

Every field has required `id`, nonblank `label`, `type`, `default`. Schema 1.2 field and select-option
labels are bounded to 120 Unicode code points with the same control-character exclusions as text.
Both owners agreed this explicit bound; older schema labels retain their existing validation.
IDs retain the SDK's lowercase
setting grammar. Reject unknown keys and explicit null at every schema/value boundary. Validate
defaults for every global/section/block definition even when overridden or never instantiated.
The new constraints apply to schema 1.2; do not retroactively reject accepted older packages.

Existing checkbox, select, URL and menu meanings remain unchanged. `text`/`textarea` gain
`min_length` and `max_length`: integers, default 0/4000, `0 <= min <= max <= 4000`, counted in
Unicode code points. Reject U+0000–0008, U+000B–000C, U+000E–001F and U+007F; tab, LF and CR
remain legal unless a fixed field grammar excludes them. List strings use the same rule. The
existing total request/provider/render budgets still apply. Text may declare `format: "anchor"`,
which additionally requires `^[a-z][a-z0-9-]{0,47}$`; no arbitrary schema-supplied regex is executed.
Omitted format means plain text. No trimming or markup interpretation occurs. Positive minimum
length alone does not enforce nonblank trimmed text; legacy nonblank rules remain explicit migration blockers.

| Field | Extra schema keys | Exact value and bounds |
| --- | --- | --- |
| `integer` | Required `min`, `max`; optional `step` default 1 | Finite mathematical integer within JavaScript's safe integer range, inclusive bounds; positive integer step; `(value - min)` divisible by step. Reject strings, booleans and fractions. Canonical output is an integer; numeric JSON `1.0`/`1e0` mean 1 |
| `string_list` | Required `min_items`, `max_items`, `item_min_length`, `item_max_length` | Ordered JSON array of strings, never object; `0 <= min_items <= max_items <= 24`, `0 <= item_min_length <= item_max_length <= 4000` Unicode code points. Preserve order, empty strings when permitted, duplicates and embedded newlines |
| `color` | Optional `allow_empty` default false | Existing six-digit hex, plus exactly `""` when allowed. Empty means inheritance/unset, not transparent or an invented fallback |
| `image` | Optional `required` default false | Exactly `""` when optional, or exact `{kind, target}` with kind `package` or `media` and a string target. No null/URL/path object supplied by the merchant |
| `reference` | Required nonempty unique `kinds` list; optional `required` default false | Exactly `""` when optional, or `{kind: "theme" | "native" | "cms" | "category" | "product", target: string}` with kind permitted by the field |

Integer bounds and step must themselves be safe integers; compare step alignment without lossy
floating arithmetic. Existing `number`/`range` remain finite numeric controls with their previous
semantics. Use `integer` when migrating old integer schemas rather than treating a visual stepper
as validation. Numeric step mismatch must reject at the PHP and TypeScript boundaries alike.

Image package targets are exact inspected files beneath `assets/` using the existing image
extension/MIME/path rules. Missing package files invalidate defaults/state; themes cannot point at
another release or executable asset. Media targets use the existing opaque host-ID grammar
`^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`. Theme targets must name a declared page; native targets use the
lowercase identifier grammar; CMS/category/product targets use the opaque host-ID grammar.
Unknown host references remain valid identities with unavailable rendering, so refresh/save never
silently deletes a merchant's selection. `required` forbids the empty value; it does not guarantee
that a provider is currently available.

Example section settings:

```json
[
  {"id":"heading","label":"Heading","type":"text","default":"Made slowly.","min_length":1,"max_length":160},
  {"id":"columns","label":"Columns","type":"integer","default":3,"min":1,"max":4,"step":1},
  {"id":"background_color","label":"Background","type":"color","default":"","allow_empty":true},
  {"id":"image","label":"Image","type":"image","default":{"kind":"package","target":"assets/menu-cup.svg"}},
  {"id":"image_description","label":"Image description","type":"text","default":"An original illustrated cup","max_length":300},
  {"id":"page","label":"Page","type":"reference","kinds":["theme","cms"],"default":{"kind":"theme","target":"about"}},
  {"id":"points","label":"Points","type":"string_list","default":["Original design","Readable source"],"min_items":0,"max_items":12,"item_min_length":1,"item_max_length":500}
]
```

## Schema 1.3 typed video prototype

The SDK now has a standalone **schema 1.3.0 / CLI capability 4** prototype for the two Silt
`videoAssetId` values and editable page titles/descriptions. A `video` field has the same explicit optional/required behavior as an
image, but stores exactly `{kind, target}` with `kind: "package" | "video"`. A package target is
an inspected immutable `assets/*.mp4` or `assets/*.webm` file. A host target is an opaque video
ID; it is neither a filesystem path nor a merchant URL.

Host video records are exact `{label, url, available, mimeType, width, height, duration, integrity}`
objects. MIME is `video/mp4` or `video/webm`; dimensions are 0–100000; duration is an integer
0–86400 seconds; integrity is SHA384 or empty. The host accepts only the ID's approved same-origin
endpoint. A structurally valid unsafe/unavailable record becomes render-only unavailable without
deleting the saved ID. Wrong keys, MIME, duration or metadata reject. Video records are not accepted
by schemas 1.0–1.2.

The package `theme-sdk/examples/video-settings-theme/` demonstrates an available host video in
plain Liquid. Schema 1.3 state adds required `page_metadata`, a map keyed by declared page with
exact `{title, description}` values. Titles are nonblank Unicode text up to 160 code points;
descriptions are bounded Unicode text up to 320. It renders as `page.title` and
`page.description`, while the page's declared template remains immutable package identity.
Contracts 1–3 reject schema 1.3 before reconstructing merchant state; contract 4 does not claim
compatibility with existing schema 1.0/1.1 editor routes. The local SDK verification passes 45 PHP
and 24 Node tests, including CLI4 install/render/save, metadata state isolation and
malformed-provider cases. No HTTP4 route, TypeScript field control, local video serving endpoint,
upload, remote fetch, external player, Magento provider, main runtime pin or browser acceptance
exists yet. This is an implemented SDK prerequisite, not a completed Silt video migration.

## Raw JSON and exact numeric validation

V3 transport and schema 1.2 package/CLI readers must retain raw number lexemes and object/list
shape before ordinary JSON conversion. Maximum nesting depth is 20; existing per-file and
transport byte limits remain in force. Validate UTF-8 bytes, JSON grammar and escapes, reject
lone surrogate escapes, and reject duplicate decoded keys in every object, including `"x"` versus
`"\u0078"`. Enforce bounded depth/bytes while scanning. `JSON.parse`/`json_decode` alone cannot
establish these guarantees after numeric precision or duplicate properties have been lost.

For each schema-identified integer setting/default/min/max/step, normalize its raw decimal token
exactly as coefficient and base-10 exponent. Reject nonzero fractional digits and mathematical
values outside ±9007199254740991 before converting to a host number. Accept integral spellings
such as `1.0` and `1e0`. Reject `9007199254740991.1`, even though JavaScript rounds it into a safe
integer. Numeric role checks happen after schema selection using retained lexemes; the generic
scan must not forbid valid older-schema fractional number values. Negative zero canonicalizes to zero.
Retain lexemes through every unvalidated Node-to-PHP hop; a parse/stringify before schema-role
validation loses the guarantee. Canonicalize only after the exact value has been validated.

Compute step alignment using exact integer arithmetic: `value - min` may exceed the safe integer
range even when both operands fit it. Never use rounded subtraction/modulo. Limit each numeric
token to 128 ASCII bytes and its exponent magnitude to 1000000; reject
representations exceeding those resource limits before expansion. Handle zero coefficients without
expanding exponents. Every safe integer remains expressible in a permitted compact spelling; the
contract does not accept unbounded equivalent spellings. Tests include safe limits, decimal/exponent
integral equivalence, rounded fractions, extreme exponents and step differences across zero.
Include the negative step vector value/max 9007199254740991, min -9007199254740990 and step 2:
its exact difference 18014398509481981 is odd, while binary64 subtraction rounds to an even value.
The companion min -9007199254740991 case is valid but cannot alone detect naive rounded arithmetic.
Existing product JSON validation is precedent, but its ban on every decimal/exponent token cannot
be copied unchanged into this reader.

New schema field keys are exactly the common keys plus the applicable type/constraint keys above;
select `options` and existing number/range `min`/`max`/`step` retain their type-specific branches.
Reject irrelevant options, `required` on scalars, `allow_empty` outside color, `format` outside
text/textarea, invalid constraint types, unknown keys and null. Older package/schema readers
retain their accepted behavior; v3 transport adds the stated raw JSON checks without changing
older field vocabulary, value semantics or historical empty-map normalization.

## Resource identities and render context

The trusted host supplies `data.resources`, with optional `media`, `theme`, `native`, `cms`,
`category`, `product` maps keyed by stored target. Missing collections are empty. Each non-media
entry is exactly `{label: string, url: string, available: boolean}`. Media entries additionally
require `{mimeType: string, width: integer, height: integer, integrity: string}`.

Malformed host structure rejects: wrong map/list shape, unknown/missing keys, wrong primitive
types, invalid IDs/labels/MIME/integrity/dimensions and duplicate keys. The HTTP adapter reports
invalid provider output as 502 without acknowledging state; developer CLI reports a source error.
A structurally valid record with `available: false`, an empty/unsafe/unapproved URL, or a missing
target instead normalizes to unavailable with a field warning. Missing records and malformed
records are distinct. Availability never invalidates a syntactically valid saved host identity.

Labels are nonblank UTF-8 text up to 120 code points. Link URLs use the existing safe URL rule.
Media MIME is an allowed image MIME; dimensions are integers 0–100000, with zero meaning unknown.
Media integrity is valid SHA384 SRI or `""` when the trusted host has no immutable hash. Package
image references resolve internally from inspected release bytes and always retain exact path,
MIME and SHA384. Package `settingImages` metadata must agree with inspection on all three;
matching the image ID alone is insufficient. Available records have nonempty approved URLs.

Media URLs must match an exact host-owned media-ID-to-endpoint mapping. Fragments and arbitrary
HTTPS links are not media endpoints. The first adapter permits same-origin approved image paths,
correct MIME, `nosniff` and SVG script restrictions; there is no generic URL-fetch/proxy endpoint.
Unsupported origins/executable delivery cannot become selectable images. Uploads, remote-CDN
adoption and videos remain separate work. Unsafe but structurally string-valued URLs normalize
unavailable; wrong URL types reject. Provider-supplied dimensions/integrity never override inspected
package metadata. Unknown host image dimensions may be zero, without guessing a size.

Build menu targets, field references and render resources from one normalized catalog snapshot,
resolved in current store/customer context, so one `(kind,target)` cannot have conflicting
availability within a render. Browser request bodies cannot supply catalogs, provider data, URLs,
context, filesystem roots or asset bases. Reference visibility grants no native access and never
replaces Magento's authorization, price or stock policy.

Render-only `setting_resources` contains resolved global image/reference fields; `section.resources`
and `block.resources` contain their own resolved fields. Only declared image/reference IDs appear.
These maps are absent from persisted state and schema 1.0/1.1 render contexts. Original settings
remain their stored identities. Catalog/product data stays under explicit provider contracts;
these resources expose links/images, not an invented product or purchase API.

Each resolved resource has exactly `{kind, target, available, label, url}`; image fields also have
`{mimeType, width, height, integrity}`. Empty settings produce kind/target/label/URL `""` and false.
Unavailable nonempty settings retain only stored kind/target; label/URL are `""` and available false.
All unavailable image metadata is `mimeType: ""`, `integrity: ""`, width 0 and height 0. A missing
provider entry can produce that shape; a supplied malformed media MIME still rejects before
normalization. Picker labels may retain a trusted last-known label, without changing state or the
unavailable render shape. Strict Liquid can guard availability without missing-variable exceptions.

```liquid
{% if section.resources.image.available %}
  <img src="{{ section.resources.image.url | escape }}"
       alt="{{ section.settings.image_description | escape }}">
{% endif %}
{% if section.resources.page.available %}
  <a href="{{ section.resources.page.url | escape }}">Read the story</a>
{% endif %}
<ul>{% for point in section.settings.points %}<li>{{ point | escape }}</li>{% endfor %}</ul>
```

## Editor and CLI contract 3

V3 status is `{contractVersion: 3, inspection, resources}`. Inspection retains v2 metadata/images
but reports `editorContractVersion: 3`; each state-bearing envelope carries its actual schema.
The resources object has exactly `snapshot`, existing v2 `targets`, existing v2 `images`, and new
`settingImages`. The two older lists retain their existing field shapes.

`snapshot` has exactly `{themeId, version, digest, stateSchemaVersion, revision, resourceRevision,
contextKey}`. Its first five fields equal inspection/selection. The final two are opaque host-owned
nonempty tokens matching `^[A-Za-z0-9_-]{1,128}$`: resourceRevision identifies the normalized catalog,
contextKey identifies its current store/customer context without exposing session/credential data.
They are comparison tokens, not authorization supplied by the browser. One render uses one captured
catalog/context and returns this same shape as `result.resourceSnapshot`. This is host-added HTTP
metadata, derived from the verified SDK result identity and the catalog/context actually supplied
to that render. It is not a new browser input or a required argument for standalone source rendering.

Status uses one installed repository snapshot for schemas, selection and catalogs. Before emitting
it, the host rechecks the installed identity/revision; a change returns 409 rather than mixing two
releases. An explicit render compares request revision/schema within the repository operation and
uses that package's immutable bytes plus one current normalized provider snapshot. Later provider
changes affect a subsequent render, not partial fields inside the current one.

A picker refresh fetches status using its own request generation. The editor accepts its catalogs
only when the response matches the loaded theme/version/digest/schema/revision and latest generation.
It never acknowledges a save, replaces history/dirty state or clears unavailable IDs. An upgraded
or changed selection produces conflict/reload handling, without automatic overwrite; a failed or
stale refresh leaves the current buffer intact. After explicit reload, the new selection/catalogs
are adopted together. Context changes require a fresh host render, not reuse of old private output.

V3 package assets use `/api/v3/liquid-themes/{id}/releases/{digest}/assets/{file}`. The host verifies
that exact immutable release belongs to the allowed theme before serving its bytes. An old preview
may receive that retained release, or 410 when unavailable; it must never fall back to current-release
bytes at the same path. Apply this binding to package images and executable/CSS assets, including
inspected picker URLs. Integrity metadata alone does not bind a normal image GET. Media endpoints
are separately constrained to the trusted host mapping above.

`settingImages` entries are exactly `{kind: "package" | "media", id, label, available, url,
mimeType, width, height, integrity}`. Identities are unique within kind. Package IDs and metadata
match inspection. Targets remain unique by `(kind,id)`. For schema 1.0/1.1 accessed over v3,
`settingImages` is `[]` and existing image/target limits remain unchanged, including a valid legacy
package with 501 images. Do not apply new schema validation limits retroactively.

For schema 1.2 only, cap each targets/settingImages catalog at 500 and require the complete package
image catalog to fit. Reject over-500 package image inventories during package acceptance, before
installation; reject an oversized combined host catalog with a `resource-limit` diagnostic and
operator correction instructions. Preserve the existing bounded transport budget. Never silently
truncate choices. Native paginated catalog search is outside this first slice. Test the 500 boundary
and both new-package rejection and older-package usability with 501 small images.

Render/save bodies retain exact v2 fields and use contract-3 response envelopes. The host passes
CLI capability 3 even for older packages, selects validation by their actual schema, and checks
all returned identities before accepting state. Errors retain required `error`/`diagnostics`:
422 invalid state/unsupported capability, 409 revision/schema conflict, 502 invalid SDK/provider
output. Existing v1/v2 routes and schema behavior remain unchanged and reject schema 1.2 state.

Strict TypeScript represents richer values by field/schema without `any` or scalar-only reconstruction.
Deep-clone object/list defaults for each new section/block and history entry. List controls preserve
individual item order/empty values/duplicates with insert/remove/reorder, keyboard focus and undo.
References/images retain unavailable IDs; color exposes explicit inheritance; integer/text controls
show SDK constraints. No uploads, native search or theme-specific application registration belongs
in these controls.

## Agreed executable CLI interfaces

These interfaces were confirmed with the sole editor owner before coupling changes; they remain
implementation targets until the SDK delivery receipt says otherwise.

```text
inspect-installed REPOSITORY ID --editor-contract=3
save REPOSITORY ID --editor-contract=3
render-installed REPOSITORY ID --editor-contract=3
inspect-release REPOSITORY ID DIGEST --editor-contract=3
```

Save stdin is the original raw HTTP JSON object. Render stdin retains the existing flat CLI shape:
the original raw HTTP members plus trusted `data`, `assetBaseUrl`, `preview` and optional
`runtimeBaseUrl`. After its bounded reader validates a complete top-level object and exact HTTP
keys, the host may remove only the final closing brace and append JSON-encoded trusted members.
This preserves merchant numeric lexemes. Never stringify parsed merchant state before schema-role
validation. Combined CLI stdin remains bounded to 2 MB; reject oversized combined context/draft,
never truncate or silently increase another transport budget.

CLI3 inspection is ordinary inspection with `editorContractVersion: 3`, actual `stateSchemaVersion`
and coherent selection. Schema 1.2 empty maps serialize as objects. Installed render returns its
captured theme/version/digest/revision/schema; the host adds resourceSnapshot. For schema 1.2,
`data.navigation` contains only optional `currentUrl`/`customerLoggedIn`; separately supplied
targets reject. The SDK derives navigation targets from the same validated `data.resources` used
by fields. Older schemas retain their existing navigation input. The host generates actual
editor/native route URLs; fixture `/?page=...` links are not production routing instructions.

`inspect-release` returns normal CLI3 inspection **without selection**, retaining top-level
stateSchemaVersion, plus `release: {id, version, digest, directory, files}`. Directory is the internal
absolute verified retained-release path and must never reach the browser. Files is a de-duplicated
list of exact inspected images and declared CSS/modules, each `{file, mimeType, integrity}`. The
host verifies the requested file against this list and hashes the actual read bytes before serving.
The SDK owns digest-to-retained-release lookup; the host does not infer repository layout. Missing,
invalid or tampered digest lookup uses diagnostic source `release`, mapped to HTTP 410, with no
active-release fallback.

## Lossless migration and reverse map

Migration is an explicit developer/operator operation into a separate disposable destination first,
not an automatic side effect of opening a legacy preset. The full source snapshot includes every
page and shared-resource revision. A draft assembled from mixed or changed revisions rejects.
Generate and review a bidirectional map before writing any target state:

```json
{
  "sourceType":"mte-studio/image-text",
  "targetType":"studio-image-text",
  "settings":{"imageAssetId":"image_asset_id","pageId":"page_id","imageFit":"image_fit"},
  "references":{"imageAssetId":{"asset-ceramics":{"kind":"package","target":"assets/ceramics.png"}}},
  "blocks":{}
}
```

The generated inventory contains actual section/block mappings, including the qualified
`studio-rich-text__paragraph` for the existing rich-text paragraph block. Qualified block types prevent
collisions between different per-section definitions with the same old name. Camel-case setting
IDs map explicitly to snake case with collision checks. Preserve section/block instance IDs,
ordering, disabled state and each mapped value. Store original identity/revision/hash metadata in
the migration receipt, not as undeclared merchant state fields.

Opaque legacy IDs need a concrete mapping to installed package media or trusted host entities.
Never infer `cms-901` means Magento entity 901. A missing mapping rejects the migration with its
source location; an intentionally mapped but unavailable host target remains preserved. Lists
stay arrays, optional colors stay empty, integers stay integers and authored text stays exact.
Cross-field legacy validation, such as paired custom colors/contrast, must be retained by a
declared constraint or explicitly reported as an unresolved blocker; no silent loss of validation.

The inventory now distinguishes 39 Silt image references from two `videoAssetId` references;
Daybreak has 22 image references. The standalone schema 1.3 video contract now preserves typed
video identities, but video/video-background ports remain blocked on the HTTP4 editor, trusted
provider and complete migration map. The [coupled-rule inventory](../roadmap/liquid-reference-migration-2026-09-11.md#coupled-rules-and-non-section-metadata)
records registry/package validators, inherited Daybreak rules, unique anchors, per-kind block
limits, route bindings and preset restrictions. Full ports also require editable page title,
description/template and token destinations. The field slice below intentionally does not port
those themes or claim their validation/metadata parity.

A complete reverse map covers global scalar fields, header/footer menu-slot assignments, menu
store provenance, `external` to `url`, opaque menu images and entity IDs. Validate source `storeId`
against the destination's host scope and retain it in reversible metadata. Legacy menu/item IDs
can be 80 characters and labels 160, versus target 64/120. Reject incompatible values unless an
explicit reversible alias is reviewed; never truncate. Different source references must map
injectively or retain a source-location alias map so reverse conversion remains exact.

Legacy block identity is scoped to its section, while the SDK requires uniqueness across a rendered
page. Record source location `(page, section, block)` in the map, detect collisions, and reject
until an explicit reversible ID mapping is agreed. The current defaults' unique IDs do not prove
arbitrary drafts compatible. Source scopes, tokens, page metadata and render semantics are part
of the reconciliation report, not unexamined fields to omit.

Source capture requires an atomic host export or coordinated locks for all source pages/shared
resources in a documented order. Recheck their revisions/hashes under that protection immediately
before destination commit. An unlocked double read alone is not atomic snapshot proof. The
separate destination uses expected revision and package digest inside its write lock. The import
key is SHA256 of canonical source snapshot hash, map version/hash and destination package digest.
Commit its receipt with target state atomically. Repeating the key returns the prior result only
while the current destination still matches its recorded revision/hash; after any target edit,
return conflict instead of overwriting. No import operation is authorized by this proposal.

Compatible 1.2 package upgrades/rollback retain richer state and validate against the destination
definitions. Schema 1.1 to 1.2 upgrade requires the explicit reviewed map when types/IDs change;
even identity-only transitions must validate every destination definition and saved value. A
1.2-to-older downgrade rejects by default. A separate reviewed reverse mapping may export a
legacy snapshot, but never overwrites the original store automatically. Source and destination
revision/hash guards protect both sides; repeated import of the same snapshot is idempotent.

## Representative package slice and acceptance cases

The initial ignored `docs/.local/liquid-rich-settings/independent-package/` proposal is preserved;
its implemented original developer package is `theme-sdk/examples/rich-settings-theme/`. It combines
two pages, image/reference/list fields at global, section and qualified-block scopes, integer and
optional-color settings, optional empty values, unavailable/media cases, a shared menu assignment,
original packaged SVG and readable Liquid. It installs/renders using CLI3 without theme-specific
editor/core registration and rejects on the accepted main schema 1.1 SDK. The implementation owner
wrote this example; it is not independent developer acceptance.

Required acceptance includes valid and rejected values/defaults in unused definitions; raw JSON
arrays versus objects; null/unknown keys; Unicode/empty-list/empty-color edges; fractional/step
rejection; missing/unsafe host references and exact package image identity; old-client refusal;
both legacy schemas unchanged; complete two-page/menu/settings save with one CAS revision; stale
revision/schema/preview retention; source-to-target-to-source equality; duplicate/reordered instances
retaining semantic presentation; collisions/unmapped IDs rejecting without writes; compatible
upgrade/rollback and rejected lossy downgrade. Browser evidence must exercise every new control
family using disposable persistence. Native provider and independent developer acceptance remain
separate from these source/fixture tests.

## Agreed scope boundary for the first implementation slice

After corrected interface agreement, the bounded slice is v3 negotiation; exact rich-field/default
validation; typed complete-state history/CAS; normalized read-only resources and release-bound
assets; and the six field families on this original two-page fixture. Extend tests to global and
block scope, deep-cloned defaults, resource-refresh/upgrade races, missing references, raw JSON
precision/shape/Unicode/duplicates and all older-client/schema compatibility branches.

Automatic migration, general import UI, video, uploads, native providers and full Silt/Daybreak
ports remain outside that first slice. A later pure in-memory migration proof requires complete
metadata/reference/constraint/reverse maps before source-to-target-to-source equality can be claimed.
