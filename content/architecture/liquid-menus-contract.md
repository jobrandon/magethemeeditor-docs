# Liquid shared menus and editor contract v2

Status on 11 September 2026: **corrected standalone SDK and local HTTP-v2 menu editor independently accepted in main**.
The main editor has a clean Atelier Navigation schema 1.1 installation alongside original Atelier
schema 1.0. The native Commerce package remains on its earlier schema. Silt/Daybreak migration,
native menu providers and publication remain open. See the [SDK guide](liquid-theme-sdk.md) and [execution plan](../roadmap/execution-plan.md).

## Purpose and version boundary

One merchant menu can be selected by the shared header, footer or any section/block on any page.
Menus, page instances and settings use one complete-state save, immutable history and revision.
Developers author their own readable Liquid markup; no theme-specific menu factory enters editor core.

| Version | Meaning |
| --- | --- |
| Theme `version` | Package release, for example Atelier Navigation `1.0.0`; independent of the state schema |
| Manifest `schemaVersion: "1.0.0"` | Existing four-key state: `settings`, `header`, `footer`, `pages`; rejects `menus` and menu-typed settings |
| Manifest `schemaVersion: "1.1.0"` | Opt-in shared menus; resolved state has those four keys plus required `menus` |
| Runtime `mte-liquid-1` | Existing PHP renderer and browser lifecycle; unchanged |
| Editor contract 1 | Understands schema 1.0 only; absence of an installed CLI capability flag means 1 |
| Editor contract 2 | Explicitly supports schema 1.0 and 1.1, using a state-schema discriminator before parsing |

Every installed schema 1.1 inspection, render and save requires `--editor-contract=2`. A v1 caller
gets an `editor-contract` diagnostic before inspection/render returns state, even when no setting
has type `menu`, or the persisted menu list is empty. Save checks capability and installed schema
inside the repository lock, after revision validation. Presence of `menus` is not negotiation.

Original schema 1.0 CLI envelopes and persisted selection shapes remain unchanged. Contract 2
adds response discriminators but never synthesizes `menus` into schema 1.0 state. A v2 client uses
a union of schema 1.0/four keys and schema 1.1/five keys; it must not treat all v2 states as 1.1.
Unknown schema/contract versions fail closed before reconstructing any state.

## Persisted state and identities

```json
{
  "settings": {},
  "header": [],
  "footer": [],
  "pages": {"home": [], "about": []},
  "menus": [{
    "id": "primary",
    "name": "Main navigation",
    "items": [{
      "id": "nav-home",
      "label": "Collection",
      "kind": "theme",
      "target": "home",
      "visibility": "all",
      "newWindow": false,
      "imageAssetId": "",
      "description": "",
      "children": []
    }]
  }]
}
```

The example illustrates the wire shape, not the installed theme's complete required settings.
An actual save includes every installed page and global setting, plus both shared groups. Existing
section/block schemas still validate their settings and normalize authored defaults. The editor
must retain all returned section/block fields rather than reconstructing a partial draft.

| Field | Required input and normalization |
| --- | --- |
| `menus` | Required list on every schema 1.1 save and explicit v2 preview draft, including `[]`; maximum 12 menus |
| Menu `id` | Required string matching `^[a-z][a-z0-9_-]{0,63}$`; unique across menus |
| Menu `name` | Required nonblank UTF-8 text, at most 120 Unicode characters |
| Menu `items` | Required ordered list; empty is valid |
| Item `id` | Required same identifier format; unique across every item in every menu, independent of menu IDs and section/block IDs |
| Item `label` | Required nonblank UTF-8 text, at most 120 Unicode characters |
| Item `kind` | Required enum: `theme`, `native`, `cms`, `category`, `product`, `url` |
| Item `target` | Required nonempty string; kind-specific limits below; never a resolved provider object |
| Item `children` | Required ordered list; root items are depth 1, maximum depth 3; depth-3 items require an empty child list |
| Item `visibility` | Optional enum `all`, `guest`, `customer`, `hidden`; omitted becomes `all` |
| Item `newWindow` | Optional boolean; omitted becomes `false` |
| Item `imageAssetId` | Optional string; omitted becomes `""`; otherwise an exact installed package path under `assets/` with lowercase extension `svg`, `png`, `jpg`, `jpeg`, `webp` or `avif` |
| Item `description` | Optional UTF-8 text, at most 1000 Unicode characters; omitted becomes `""` |

All menu and item objects reject unknown fields. **Explicit null is invalid for every field**,
including optional fields. Output contains all normalized fields. Text excludes control characters
U+0000–0008, U+000B–000C, U+000E–001F and U+007F; tabs/newlines are permitted. Markup-looking
text remains text and must be escaped in the theme. There are at most **100 items in total across
all menus and depths**. Duplicate identities, cycles and excessive depth reject rather than truncate.
Duplicating a menu or subtree in the editor must regenerate every copied item ID and the new menu ID.

| Target kind | Stored reference |
| --- | --- |
| `theme` | Declared manifest page ID; same lowercase identifier format; missing page rejects the state |
| `native` | Host route ID, same lowercase identifier format; no Magento URL or PHP class supplied by the merchant |
| `cms`, `category`, `product` | Opaque host reference matching `^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`; namespaced mapping belongs to the host |
| `url` | At most 2048 bytes; root-relative path beginning with one slash, fragment, or valid lowercase `https://` URL without credentials; whitespace, backslashes, protocol-relative URLs and other schemes reject |

Each `menu` setting has the ordinary `id`, `label`, `type: "menu"`, `default` fields. Its value
is an existing menu ID or `""` for unassigned. The default follows the same rule against resolved
package defaults. All global, shared-section, page-section and block references validate together.
Deleting an assigned menu fails; the same complete-state transaction may instead reassign or clear
every reference. There is no cascading silent deletion. Liquid templates guard `""` before lookup:

```liquid
{% if section.settings.menu != '' %}
  {% assign navigation = menus[section.settings.menu] %}
  {% render 'snippets/menu-items', items: navigation.items %}
{% endif %}
```

## Host-owned references and rendering

Host data is outside merchant state. Save/render HTTP bodies cannot supply `data`, resolved URLs,
provider results, store/customer context, asset roots or resources. The SDK's trusted renderer
accepts the following `data.navigation` from its host:

```json
{
  "customerLoggedIn": false,
  "currentUrl": "/?page=home",
  "targets": {
    "theme": {"home": {"url": "/?page=home", "available": true}},
    "native": {"account": {"url": "/customer/account/", "available": true}},
    "cms": {}, "category": {}, "product": {}
  }
}
```

The navigation object and its three keys may be omitted; defaults are false, empty URL and empty
target map. Explicit null and unknown keys reject. Each present target collection is a map of
references to objects containing exactly required string `url` and boolean `available`. Target URL
values must pass the same safe-URL rule before use; missing, unavailable, empty or unsafe references
produce an empty URL, `available: false` and a warning diagnostic identifying the item. They never
fall back to a guessed Magento path. The merchant reference is preserved for later repair.

The host resolves current store, website, permissions and entity visibility on every render.
Guest/customer menu visibility is presentation only and grants no access. Invisible items and their
subtrees are omitted; missing host authentication context defaults to guest. Price hiding and native
route authorization still require their respective adapters. Fixture reference IDs in Atelier
Navigation do not imply those entities exist in Magento.

The Liquid global `menus` is a map keyed by menu ID. Each menu has `id`, `name`, `items`.
Resolved items contain exactly `id`, `label`, `url`, `available`, `current`, `active`, `newWindow`,
`rel`, `imageUrl`, `description`, `children`. They do not contain native objects or raw credentials.
`current` matches path and parsed query parameters, ignoring fragments and query ordering; absolute
URLs must also match the current URL's scheme, host and explicit port. Fragment-only links are never
current. `active` also includes any active descendant. The host supplies its canonical route query;
tracking parameters should be removed there if they should not affect current-page matching.

For `newWindow: true`, `rel` is `noopener noreferrer`; otherwise it is empty. Themes output
`target="_blank"` with that relation. They escape URLs, labels and descriptions, render unavailable
items without a navigable link, and use appropriate disclosure controls. This is trusted theme code,
not a JavaScript or SVG sandbox.

Version 2 inspection adds `images`, a read-only list of `{file, mimeType, integrity}` derived from
the immutable installed package. `file` is the value stored in `imageAssetId`; integrity is SHA384
SRI. This includes packaged images without adding them to the executable CSS/module manifest.
Hosts serve only those exact files from the inspected release with the declared MIME type,
`nosniff`, existing confinement/digest checks and an SVG script-denying response CSP. They do not
accept arbitrary upload paths. Image IDs are package assets in this increment; merchant media
libraries need their own later versioned reference contract.

## Installed CLI contract implemented in the SDK

```bash
php theme-sdk/bin/theme.php install theme-sdk/examples/navigation-theme /tmp/mte-navigation
php theme-sdk/bin/theme.php inspect-installed /tmp/mte-navigation atelier-navigation --editor-contract=2
php theme-sdk/bin/theme.php render-installed /tmp/mte-navigation atelier-navigation --editor-contract=2 < request.json
php theme-sdk/bin/theme.php save /tmp/mte-navigation atelier-navigation --editor-contract=2 < save.json
```

`render-installed` requires `expectedRevision`, `stateSchemaVersion`, `page`, host `data` and
`assetBaseUrl`; optional `preview`, `runtimeBaseUrl` and complete `state`. Omitted state renders the
installed snapshot; an explicitly supplied draft must be complete. `save` requires
`expectedRevision`, `stateSchemaVersion` and complete `state`. The discriminator must equal the
installed manifest schema; package semver is not a substitute. No implicit fallback to contract 1.

| Response | Version-2 additions |
| --- | --- |
| Inspection | `editorContractVersion: 2`, `stateSchemaVersion`, `images`; `theme.schemaVersion` must agree |
| Inspection `defaults` | Complete state interpreted using the parent discriminator |
| Inspection `selection` | `stateSchemaVersion`, complete state and existing identity/digest/revision/previous fields |
| Render result | `stateSchemaVersion`, complete resolved state and existing HTML/assets/diagnostics/theme/digest/revision |
| Save acknowledgement | `stateSchemaVersion`, complete saved state and incremented revision |

The CLI's general `status`, `install`, `rollback`, source `inspect` and source `render` remain
developer/operator APIs. Stored schema 1.1 selections contain `stateSchemaVersion`; original 1.0
selections do not gain it. Source inspection/render of a 1.1 package expose the new discriminator;
source inspection also exposes images. Those operator commands are not a substitute for the
negotiated installed editor endpoints. Direct PHP `ThemeRepository::save` may omit the capability
argument for trusted native/developer callers; complete-state and package validation still run.
Every HTTP adapter must explicitly pass capability 1 or 2 rather than use that direct-call exemption.

## Accepted HTTP v2 specification for the sole editor owner

Use **separate explicit routes** `/api/v2/liquid-themes/{id}/{action}`, where action is GET `status`
or POST `render`/`save`. Keep existing `/api/liquid-themes/...` as contract 1. Every v2 success/error
JSON envelope has `contractVersion: 2`; there is no retry or silent downgrade to v1. Existing
origin/CSRF/content-type/size/timeout/allowlist controls remain in force. The existing editor can
move to the v2 API for both supported state schemas after PM acceptance.

Status returns `{contractVersion: 2, inspection, resources}`. Inspection is the SDK shape above.
Host-owned `resources` is required and contains exactly `targets` and `images` lists:

```json
{
  "targets": [{"kind": "theme", "id": "home", "label": "Home", "available": true}],
  "images": [{"id": "assets/menu-cup.svg", "label": "Menu cup", "url": "/api/v2/liquid-themes/atelier-navigation/assets/assets/menu-cup.svg"}]
}
```

Target kind is one of the five reference kinds, never `url`; ID follows that kind's stored-reference
rule, label is nonblank text up to 120 characters, available is boolean. All four fields are required
and non-null. Image ID must match `inspection.images[].file`; label follows the same rule and URL
is generated by the host's exact same-origin asset route. All image fields are required/non-null.
Collections may be empty, have no duplicate `(kind,id)`/image IDs and reject unknown fields. These
lists are read-only picker data, not persisted journal state. Omitted references already saved in a
menu remain editable and display unavailable; list refresh must not remove them from the draft.

Host configuration owns native/entity labels and IDs. Theme page entries come from the installed
manifest. The first local host may use fictional configured references; dynamic Magento searches
and a native menu provider are later acceptance. Render context is constructed from the same trusted
configuration plus the requested declared page. Browser request bodies never override it.

POST save body has exactly `{expectedRevision, stateSchemaVersion, state}`. POST render adds required
`page`; no other fields. Host validation checks the discriminator before parsing state, passes the
explicit CLI flag and validates returned schema/identity/digest/revision before replacing anything.
Success shapes are `{contractVersion: 2, selection}` and `{contractVersion: 2, result}` respectively.
Use `/api/v2/liquid-themes/{id}/assets/{file}` for v2 package resources and the existing host-owned
browser runtime route; an asset request needs no capability header. V1 assets remain isolated from
new-schema packages. Digest/release identity must be checked coherently when selecting asset bytes.

| Failure | Proposed HTTP handling |
| --- | --- |
| Unsupported contract or schema | 422, actionable `error`, SDK diagnostic `editor-contract`; no state reconstruction or mutation |
| Installed schema differs from request | 409 with `state-schema` diagnostic; preserve dirty buffer and require reload/reconciliation |
| Revision conflict, including an upgrade while the request was in flight | 409 with `revision` diagnostic; no automatic overwrite/retry |
| Invalid/incomplete state, menu/reference bounds or undeclared page | 422 with source diagnostic; retain draft and persisted bytes |
| Invalid SDK response or inconsistent identities | 502; do not accept the response into state |
| Aborted/stale render | Existing request-generation cancellation; never replace the newer canvas or dirty buffer |

Errors use `{contractVersion: 2, error: string, diagnostics: Diagnostic[]}` with all fields required;
each diagnostic retains `severity`, `file`, nullable `line`, `message`. SDK errors currently locate
menu validation at `menus`, and reference errors at the owning settings/section/block ID; they do
not yet carry a separate JSON pointer. Revision, schema and full-state checks occur inside the
repository's locked write path. A host preflight alone cannot authorize a later mutation.

## Upgrade and rollback behavior

Installation into an empty repository resolves authored defaults. Upgrading a schema 1.0 package to
a compatible 1.1 release preserves merchant settings/pages/groups and adds declared default menus
(or `[]`). New menu settings resolve their declared defaults. Upgrading compatible 1.1 releases and
rolling back to a compatible 1.1 release preserve edited menus and nonvisible pages. New release
defaults never overwrite existing menus. Missing required menu references or removed referenced
package images make an upgrade reject before changing selection.

Rolling back from 1.1 to 1.0 currently rejects the extra menu state, even when empty. No lossy
downgrade or automatic migration is implemented. A future explicit migration must define how
merchant state is preserved and reviewed. Install/export/rollback are operator operations, not
new editor buttons authorized by this contract.

## Validation and remaining work

The standalone SDK has PHP probes for duplicate/missing IDs, null/unknown fields, cyclic/deep/large
trees, all target kinds, safe URL resolution, visibility/current state, referenced-menu deletion,
two-page rendering, complete-state CAS and compatible upgrade/rollback. Actual installed CLI
probes cover v1 refusal before lossy parsing, empty menus, all menu fields surviving render/save/
reload, legacy envelope preservation, and an installed schema upgrade during a stale request.

The original `theme-sdk/examples/navigation-theme/` uses header/footer shared menus and home/about
templates. Three readable snippet levels match the bounded tree depth; eager parser recursion is
not used. The selected engine's `blank` equality does not implement the expected empty-string
comparison, so this example explicitly compares to `''` and checks list `.size`. This observed
dialect gap belongs in the future complete support matrix; the example does not imply Shopify
theme compatibility. Its image is an original SDK-authored SVG, with no new dependency.

The editor owner found an invalid-default gap during read-only review: defaults could escape validation
when overridden or never instantiated. The SDK now checks all global/section/block menu defaults
independently against resolved package-default menus. Focused cases cover invalid and repaired valid
overridden global/section and unused section/block defaults. Required checks pass **46 tests**
(32 PHP, 14 Node), strict types, lint, formatting, PHP syntax and browser build. The exact 340-file
snapshot is `theme-sdk/.local/menu-checkpoint.json`, aggregate SHA256
`51cf480c0354c51ce32c5573398a23b984107b5200855eaee8482724b55dcda0`.
Atelier Navigation 1.0.0 digest is
`3be2e3ff090219f38d3f950e7829b0d9a573f04f1ba1be9fdd2898f59da0c3a2`.

Standalone Chrome checks passed keyboard disclosure through three levels, home/about navigation,
current-page annotations, guest/hidden visibility, new-window relations, consent-gated module load,
reload and 390px layout without horizontal overflow or JavaScript errors. Receipt:
`theme-sdk/.local/menu-browser.json`; screenshots: `theme-sdk/output/playwright/navigation-*.png`.
This browser exercises the read-only SDK preview, not editor persistence. Installed CLI tests cover
state persistence separately. The sole editor owner implemented the agreed v2/menu interface in worktree 6b5c; PM subsequently
accepted and integrated it as described below. Final JSON-boundary probes also found PHP associative decoding could collapse empty objects into
empty arrays. Package defaults and installed CLI request parsing now validate menu/items/children
list shapes before conversion; malformed objects reject without changing saved bytes. This supersedes
the earlier 45-test snapshot. PM independently accepted the corrected 340-file snapshot in
`product/.local/source-refactor-review/liquid-menu-sdk/acceptance.json`. It matched every source hash
and aggregate, ran all 32 PHP tests plus the three installed menu CLI tests (**35 independent tests**),
and verified main v1 Atelier status/full-page render at schema 1.0/revision 1. All 17 drafts and 241
staged native files remained unchanged. The full 46-test suite and standalone navigation browser
journey above are writer evidence; PM did not independently repeat all of them. Executable SDK
source/packages/build retain that accepted snapshot while the next richer-settings contract is reviewed.

## Main editor acceptance

PM integrated 33 product paths and ran the required main checks: **170 tests passed**, strict
TypeScript, lint, formatting and build; all 141 generated artifacts matched the reviewed worktree.
It independently reproduced all 28 HTTP cases in both worktree and main. Those cover coherent
schema responses, real image bytes/SHA384, SVG restrictions, malformed inputs, conflicts and
unchanged persisted state after rejected requests.

Fresh main browser checks covered pointer reorder, keyboard nesting, undo, cycle rejection,
Escape cancellation, stable previews across inspector changes and two-page in-memory retention
through the actual iframe About link. Unsaved leave confirmation, Stay and undo retained/restored
the correct buffer. Phone preview measured 390px. Fresh Atelier, Silt and Daybreak canvases also
mounted without JavaScript errors. PM submitted no original draft save.

The writer's actual complete save/reload across Home/About and shared menus, unavailable-reference
save, revision conflict, explicit schema conflict, schema upgrade and stale-render browser cases
were accepted from reviewed evidence; PM did not repeat those persisted saves. Its receipt explains
the intercepted expected revision used to reach the distinct schema-conflict branch.

Open `http://127.0.0.1:4177/liquid-theme?id=atelier-navigation` for the local editor. Main has clean
Navigation schema 1.1/revision 1 alongside original Atelier schema 1.0/revision 1. All 17 original
drafts, 241 staged native Liquid files and 340 SDK files retain their accepted hashes. No disposable
QA repository or schema-probe installation was transferred. Independent receipt:
`product/.local/source-refactor-review/liquid-v2/main-acceptance.json`.

Full reviewed-shell/section-and-block drag/drop parity, Silt/Daybreak migration, Alpine integration,
richer resource schemas and native navigation remain open. Host resources are fictional local
fixtures in this checkpoint. This is local editor acceptance, not publication or native menu proof.
