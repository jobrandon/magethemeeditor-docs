# Liquid rich settings SDK checkpoint

Date: 11 September 2026. Status: **schema 1.3 SDK and local HTTP4 editor accepted and integrated into the shared checkout**. This is the bounded field slice in the
[agreed rich settings contract](../architecture/liquid-rich-settings-contract.md), not full
Silt/Daybreak migration or native provider acceptance.

Schema **1.3.0 / CLI4** typed-video support follows this accepted slice. HTTP4 is integrated in the shared checkout with HTTP3 fallback for schemas 1.0–1.2; it has not restarted or repinned the separately accepted main runtime.

## Developer outcome

Developers can install the original `theme-sdk/examples/rich-settings-theme/` package with
readable Liquid layouts, section/block templates and JSON schemas. Its two pages exercise
global, section and block settings without registering a theme-specific editor factory.
Source/defaults remain separate from merchant state. Installed schema 1.2 operations require
CLI capability 3; older clients refuse them. Capability 3 also handles existing schema 1.0/1.1
packages with their original field rules.

PM integrated the 31 reviewed product paths into main, rebuilt 141 artifacts, activated the
immutable 363-file schema 1.2 SDK snapshot, and restarted the local preview. The main route is
`http://127.0.0.1:4177/liquid-theme?id=reference-settings-slice`; its status reports contract 3,
schema 1.2.0 and revision 1. Existing Atelier, Atelier Navigation, Silt and Daybreak canvases
continue to load with clean saves and no browser errors.

```text
rich-settings-theme/
  theme.json
  README.md
  layout/theme.liquid
  templates/home.json
  templates/about.json
  sections/story.liquid
  sections/story.schema.json
  blocks/story__note.liquid
  blocks/story__note.schema.json
  config/settings_schema.json
  config/settings_data.json
  assets/menu-cup.svg
```

The fields include bounded Unicode text, exact integers, ordered string lists, optional colors,
package/host image identities and typed page/entity references. Empty values and unavailable
host identities survive save/reload. Missing package images and undeclared theme pages reject.
The fixture uses an original SVG from Atelier Navigation; no dependency or external asset was
adopted. Its example media URL requires the editor host's approved endpoint, which the standalone
source preview server does not implement.

## Runtime boundaries

Paths in the table are relative to `theme-sdk/src/`.

| Responsibility | Maintained source | Behavior |
| --- | --- | --- |
| Raw JSON | `Json/JsonDocument.php`, `ExactInteger.php` | Bounded bytes/depth/tokens; duplicate decoded keys and invalid Unicode reject; exact numeric lexemes retained until role validation |
| Field schemas and values | `RichSettings.php` | Per-type keys, complete defaults, Unicode bounds, integer bounds/step and typed identities; legacy validator remains separate |
| State boundary | `RichState.php` | Object/list shapes, all settings and normalized instance fields required for complete saves/drafts |
| JSON output | `Json/RichEncoding.php` | Declared empty maps remain objects; menus/groups/blocks/string lists remain arrays |
| Host resources | `ResourceCatalog.php`, `SettingResources.php` | One normalized catalog supplies menus and render-only field resources; unsafe URLs become unavailable, malformed records reject |
| Installed operations | `ThemeRepository.php`, `Console.php` | Revision/schema checks, validation inside save lock, coherent snapshots, compatible upgrades/rollback and rejected lossy downgrade |
| Immutable assets | `inspect-release` | Digest-bound retained-release directory and deduplicated image/CSS/module allowlist; no active-release fallback |

## Standalone typed-video prototype

`theme-sdk/examples/video-settings-theme/` is an original schema 1.3 package that exercises a
host-owned, opaque video identity in readable Liquid. CLI4 validates package `.mp4`/`.webm`
targets or approved host video records with MIME, dimensions, duration and integrity metadata.
It refuses contracts 1–3, preserves unavailable identities and rejects malformed records. The
same complete state carries each declared page's editable bounded title and description, exposed
to Liquid as `page.title` and `page.description`. The standalone `npm run verify` passes **45 PHP
and 24 Node tests**.

HTTP4 is integrated in the shared checkout: it exposes typed video controls, same-origin local video endpoints, complete page metadata, raw complete-state CAS and browser save/reload acceptance. The accepted main runtime pin and merchant drafts remain unchanged. Full Silt migration still requires provider-backed media, native commerce/forms interactions, coupled validators and a reversible import/export workflow.

The parser rejects rounded fractional attacks before PHP or JavaScript conversion can lose
precision. Safe integer subtraction and modulo use 64-bit PHP integer arithmetic, including
the cross-zero difference that exceeds JavaScript's exact integer range. Schema constraints,
unused definitions, overridden template defaults and incoming values all receive their own
role checks. Integral decimal/exponent spellings normalize to integers.

Only the host controls resource catalogs, customer/store context and exact media endpoint mappings.
The SDK revalidates record keys, labels, MIME, integrity, dimensions and canonical same-origin
media paths. It never fetches a merchant URL. Package image integrity is calculated from the
immutable package snapshot and cached for reuse across fields.

## Verification and source identity

The required `npm run verify` passed on Node **24.21.0**, npm **11.19.0**, PHP **8.3.28**:

- Strict types, lint, formatting, PHP syntax and production build passed.
- **44 PHP tests** cover existing runtime/menu behavior and new raw JSON, rich defaults, Unicode,
  integer precision, complete-state shapes, unavailable resources and catalog limits.
- **20 Node tests** cover existing browser lifecycle/commerce/CLI behavior and six new actual-CLI
  groups: rich two-page save/render, retained releases, legacy compatibility, raw transport/provider
  failures, empty-map persistence and upgrade/rollback protection.

Command-level tests use disposable repositories and compare selection bytes after rejected saves.
They exercise integral exponent input, fractional precision attacks, stale revision before schema
conflict, old-client refusal, dirty two-page values, missing block settings, Unicode/list preservation,
unavailable resources and reinspection after one successful revision increment. Schema 1.2 accepts
500 package images and rejects 501; legacy packages retain 501-image support. Provider catalogs
reject oversized combined lists without truncation.

The frozen checkpoint is `theme-sdk/.local/rich-settings/final-checkpoint.json`, containing **363
source/build/vendor files**, a supplemental runtime/notice inventory and the required-check log hash.
Its aggregate SHA256 is
`5fbf967b18bbff745980a0d684833b68d02bdbf7979aecf0e973563351e7c7f4`.
The hash input is sorted relative path, NUL, file SHA256 and LF for each file. The original rich
package is `reference-settings-slice` **0.1.0**, schema **1.2.0**, digest
`bf8c0392c4585887def32b06de96def0c8b7e3a065e3f4fc8092941d693b130f`.

Composer/npm manifests and locks remain unchanged. Fresh hash checks preserved all **340** pinned
main SDK files, **241** staged native Liquid files and **22** PHTML comparison files. Original
Atelier, Navigation and Commerce package digests are unchanged. The main editor still uses its
accepted schema 1.1 SDK pin; this owner did not repoint or restart it.

## Accepted local integration

PM independently reviewed the raw reader, exact integer arithmetic, rich defaults/complete state,
resource normalization, version guards and retained-release paths. It reproduced **44 PHP and
20 Node tests** with the exact Node/PHP runtime, matched all **363** checkpoint files plus **five**
supplemental runtime/notice files, and verified the main pin, both original revision-1 selections,
241 native Liquid files and 22 PHTML comparison files. Receipt:
`product/.local/source-refactor-review/liquid-v3-sdk/acceptance.json`. Full type/lint/format/build
checks remain the writer's verified evidence; PM independently reran the complete test suite.

PM accepted 31 integrated product paths (15 new, 16 modified), matching all 367 main source files
and 141 rebuilt artifacts. Product verification passed strict types, lint, formatting, build and
**183 tests**. Two independent 46-case HTTP runs passed—one disposable and one against main4177—
with rejected requests preserving selection. Browser acceptance confirmed all six rich field families,
unavailable references, two-page buffering, refresh-preserved history, unsaved-leave protection,
undo, Desktop and 390px Phone layouts, and zero JavaScript errors. Legacy Atelier, Navigation,
Silt and Daybreak canvases loaded with clean save state.

The acceptance receipt is `product/.local/source-refactor-review/liquid-v3/main-acceptance.json`.
It verifies 17 existing draft hashes, both original selection hashes/revision 1, 241 native Liquid
files, 22 PHTML comparison files, the original SDK plus its new immutable pin, and excludes
disposable QA repositories from main. The SDK source stays frozen; this acceptance grants no new
implementation or native scope.

## Remaining scope

Full lossless Silt/Daybreak migration remains blocked by provider-backed media, coupled validators,
source identity/reference maps and complete reversible conversion. Automatic imports, uploads,
native rich-field providers, broader PHP/runtime support and independent developer authoring are
outside this checkpoint. Existing native commerce and PHTML evidence remain separate.
