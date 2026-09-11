# Editor frontend standards implementation — 11 September 2026

Status: **independently reviewed, integrated locally and pushed to private product main at `0e05ace` with user authorization**.
This scoped refactor applies the [source policy](../../contributing/policies/source-code.md) and
[Tailwind-first styling policy](../../contributing/policies/styling.md) to the maintained editor.
It preserves the reviewed merchant layout and existing legacy, Studio and Liquid behaviors.

## Baseline and ownership

The worktree remains at detached Git baseline `35caa57d63601ffe202e6a209d6df7fb180ebeb7` with
maintained canonical TSX/HTTP4 files seeded through a 595-path SHA256 allowlist, preserving
11 intentional deletions. Work paused for the completed-source release and resumed without
resetting, merging over or replacing the expert's unfinished changes. The final source delta is
against released product `2080a79954d76a74c2b34df14e89bd066eea1984`, including the exact released
commerce-test correction. See the [release receipt](../../roadmap/completed-source-release-2026-09-11.md).

The requested Senior Frontend Expert, collaboration agent `senior_frontend_expert` using GPT-6
Astra High, owned editor source and existing CSS. The coordinating writer owned bootstrap,
Tailwind/build integration, dependencies/notices, test integration and independent browser review.
PM retains original-checkout integration and main4177 restarts. SDK/native source ownership was
unchanged. This task performed no commit, push, publication, main restart or worktree cleanup.

## Source changes

| Area | Result |
| --- | --- |
| Shared UI | Direct imports from component folders: Button, Icon, IconButton, Choice, Disclosure, Dialog, ArrayField, ColorField, ImageField, InspectorSearch, ReferencePicker, SchemaFields and TextField. Pure helpers remain `.ts`; no universal barrels or empty scaffolds. |
| Studio composition | The workspace retains existing resource, selection, navigation and preview providers. DraftResourceStatus owns toolbar status presentation. RevisionHistory reuses the shared Disclosure with controlled open state. |
| Liquid composition | LiquidToolbar and LiquidWorkspace separate presentation from the root. The complete-state journal, API negotiation, persistence leases and frame trust boundaries retain their existing owners. Five React hooks move from `.ts` to `.tsx`. |
| Readability | Migrated components/hooks use multiline braced guards and logical blank-line grouping. Scoped Biome enforcement covers the migrated boundaries; unrelated pure-domain and legacy code was not broadly reformatted. |
| Styling | Actual Studio shell/rail/toolbar, shared controls and Liquid shell/workspace use complete Tailwind utility names and explicit variants. Central base rules and compatibility feature CSS remain. No storefront migration, Sass, CSS Modules or large `@apply` sheets. |
| Build | `editor/tailwind.css` declares CSS-first token aliases, explicit component source discovery and no Preflight. `src/build-editor-css.mjs` compiles one editor utility entry during the existing production build. All three editor documents load it once; storefront frames do not load it. |

The changed source map contains **100 paths: 33 additions, 50 modifications and 17 deletions**
relative to the released baseline; moves appear as add/delete pairs. There are **142 generated
build artifacts**. Source and build manifests include individual SHA256 values for review.

The exact existing Node **24.21.0** / npm **11.19.0** runtime was reused through its project-local
PATH. Tailwind and its CLI are pinned to **4.3.3**. The compiler adds the same 66 package artifacts
already reviewed for the separate UI specimens, with no transitive version changes. The product
lock and tooling inventory preserve exact identities. The companion review under
`product/third-party/tailwind/` extends use to locally generated editor CSS; full MIT notices are
retained in compiled CSS and `THIRD_PARTY_NOTICES.txt`. Tool binaries are not browser assets.
The compiler follows Tailwind's [explicit source discovery](https://tailwindcss.com/docs/detecting-classes-in-source-files)
and [CSS-first token model](https://tailwindcss.com/docs/theme).

## Verification

Final commands used the reviewed runtime and disposable storage:

```text
npm ci --ignore-scripts --no-audit --no-fund     PASS
npm run verify                                PASS: types, lint, format, build, 187 tests
node src/check-inventory.mjs                   PASS: 11 existing dependencies, 106 tool artifacts
python3 product/.local/standards-2026-09-11/manifest.py
                                              100 source deltas, 142 build artifacts
git diff --check                               PASS
```

The module-route regression now verifies compiled CSS delivery, complete license retention,
one stylesheet link per editor document, private raw CSS source, and iframe stylesheet isolation.
The moved array-helper test import was corrected during integration. Independent visual review
found and corrected a missing Draft history disclosure layout and a 2.9px search-label difference.
The corrected history summary is 44px high; the search label is 10px and its input remains 35px.
The legacy editor favicon now uses the existing self-hosted image instead of a CSP-blocked data URL.

Playwright CLI drove a real local browser against **127.0.0.1:4209**. The server uses fresh
legacy/preset/Silt fixture drafts and a separate Liquid repository installed from a sealed,
read-only **620-file SDK fixture**. Its package installs contain original Silt Liquid, Daybreak
Liquid, Atelier Navigation and the rich-settings reference. All fixture hashes and **112 project
skill/notice hashes** were unchanged after verification.

| Browser coverage | Actual result |
| --- | --- |
| Legacy editor | Loads without the former favicon CSP error; heading edit, undo/redo and draft save/reload pass. |
| Studio Daybreak | Metadata edit, undo/redo and draft save/reload pass. Outline/inspector collapse and restore preserve grid layout. |
| Studio Silt fixture | Unsaved page guard appears; Stay retains the page; Save draft and continue navigates; return and reload retain the saved title. |
| Studio responsive previews | At a 1440px viewport the desktop frame fills the available 872px canvas. Tablet and Phone are 768px and 390px. |
| Adaptive Choice | Narrowing a real control container from 231px to 90px switches segments to select and transfers focus; restoring width returns focus to the selected radio without changing its value. |
| Liquid Silt HTTP4 | Edits on Home and About survive one complete-state save/reload. Undo/redo and 768px/390px preview modes pass. |
| Liquid Daybreak HTTP4 | Page metadata save/reload passes. |
| Older Liquid schema | Atelier Navigation's expected HTTP4 422 probe falls back to HTTP3. Pointer movement across menus and keyboard reorder preserve all 10 links. Unsaved departure cancellation and menu save/reload preserve the new order. |
| Viewport layout | Baseline and final screenshots cover legacy, Studio and Liquid at 1440×1000, 768×1024 and 390×844. The existing narrow Liquid horizontal workspace is preserved. |

Existing source tests and earlier scoped receipts retain coverage for detailed conflict, stale
response, whole-state acknowledgement, schema fallback, rich/video-field and frame-trust cases.
Those untouched adversarial scenarios were not all repeated interactively in this refactor.

## Evidence and handoff

Raw evidence lives in the worktree's ignored `product/.local/standards-2026-09-11/`:

- `scope-and-acceptance.md`, `baseline-manifest.json`, `source-delta.json`, `source-delta.patch`.
- `build-manifest.json`, `final-verify.log`, `sdk-fixture-manifest.json`, `skill-hashes.json`.
- Browser scripts/logs for Studio, navigation, Liquid, menus, legacy and adaptive Choice.
- `baseline-*.png`, `final-daybreak-desktop.png`, `final-studio-{tablet,phone}.png`,
  `final-liquid-{desktop,tablet,phone,menus}.png`, `final-legacy-{desktop,tablet,phone}.png`.

The source delta lists expected released hashes as well as final hashes so PM can detect
concurrent changes before integration. It excludes fixtures, drafts, node_modules and raw evidence.
The 4209 server is an inspectable local fixture preview; it is not main4177 acceptance.

The browser retains the existing same-origin iframe sandbox warning. Older-schema HTTP4 422
probes are expected negotiation responses. Liquid packages also display unavailable-resource
warnings because the fixture provider has no native catalog/media targets. These are separate
from editor JavaScript failures. No Magento, native commerce, production or commercial-release
acceptance is claimed. Retained feature CSS is a compatibility boundary; this is a bounded
standards adoption, not a complete rewrite of every legacy stylesheet.

## PM local integration and review workflow

On 11 September 2026, PM independently compared the handoff with released `2080a79` and
corrected one manifest-only scope error: `component-library/AGENTS.md` was absent from the
seeded worktree and must not be deleted. The corrected manifest contains exactly 100 product
paths. All baseline and final source hashes were verified before copying; existing source and
build bytes were backed up under canonical `product/.local/standards-integration-2026-09-11/`.

The canonical checkout passed `npm ci --ignore-scripts --no-audit --no-fund` and
`npm run verify`: strict TypeScript, lint, formatting, build and **187/187 tests**.
All **142** generated artifacts match the writer's frozen manifest. Existing locked artifacts
are unchanged, and all 66 added compiler artifact identities match the earlier reviewed graph.

Independent Playwright checks on the disposable 4209 host confirmed the migrated Studio
controls, Draft history disclosure and Tablet/Phone widths of **768px/390px**. Desktop fills
the available canvas; its measured width varies with scrollbars. The compiled utility sheet
loads once in the editor and is absent from its storefront document.

PM restarted canonical main4177 as process **90801**, using the same Node **24.21.0** and
host configuration. The configured immutable schema-1.2 SDK remains unchanged; all **563**
protected file hashes, including **17** existing draft/preset files, remain intact. Native
full-theme status before and after integration is identical. All three configured Liquid
status routes, the legacy/Studio/Liquid documents and compiled CSS return HTTP 200. Fresh
main browser checks confirm Silt and the rich-settings Liquid preview render with editor
utilities isolated from their storefront documents. No merchant save or native apply was
performed during PM acceptance. This is local editor evidence, not broader commerce acceptance.

The user requested direct local development for immediate source review and interruption.
The existing frontend task confirmed that future authorized increments use the canonical
checkout explicitly, even though its historical app cwd still names worktree2653. It is the
sole editor implementation writer. The current batch is ready for review, with no subsequent
batch running. After local review, the user explicitly requested this completed batch be pushed.
The product refactor is delivered on private `main` at
`0e05acea053f80a51f1e0b95216e6693ff854963` with the Conventional Commit
`refactor(editor): organize components and adopt Tailwind v4`. Delivery rechecked every source
and build hash against the accepted test evidence; source was unchanged and the passing suite
was not repeated. The documentation receipt and local workflow are delivered separately in
the documentation repository. Drafts, screenshots, generated output and historical worktrees
are excluded from the commits and remain preserved locally.

This push authorization covers the completed batch. Future refactor increments remain local
and uncommitted until the user requests another delivery. See the
[local review workflow](../../contributing/policies/coordination.md#local-frontend-review-workflow).
