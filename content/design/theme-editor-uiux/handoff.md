# Implementation handoff

Implementation update · 2026-09-10: the user subsequently requested integration into the actual local product. See [Resource Desk implementation and verification](implementation-2026-09-10.md). The design-phase status and sandbox restrictions below are preserved as historical context.

Status: **compact visual refinement under review**, 2026-09-10. No redesign has been integrated into the actual editor. [Review overview](index.md).

## What exists and what is proposed

Next navigation requirement · 2026-09-10: use the
[interactive storefront navigation specification](storefront-navigation.md) for the user-required
editor layer, ordinary links and unsaved-change guard. Its acceptance checks supplement this
historical handoff; it does not establish a newly dispatched implementation batch.

| Concern | Current evidence from source/UI | Proposed design work |
| --- | --- | --- |
| Full-page structure | Fixed shared Header/Footer and page template preview | Unified outline with synchronized contextual selection |
| Component inventory | 66 registered types; 52 template, 13 shell, 1 outside full registration | Searchable categorized catalog with all types and honest eligibility |
| Section/block controls | Flat generated fields and nested fieldsets with arrow order controls | Grouped inspector, typed block navigation and direct drag-and-drop |
| Menus | Named shared menus, three levels, sibling drag, indent/outdent | Nested before/after/within targets, keyboard Move dialog and clear scope |
| Save | Page/global resources have independent save calls; global combines shell/settings/menus | Scoped save labels and changed-resource detail without false independent commits |
| Undo | Session-wide snapshots, bounded history, cleared by save/reload | Coalesced commands and per-resource undo; implementation decision remains open |
| Generic visibility | No generic section/child visibility field in current strict schema | Local sandbox sidecar state; product contract decision required later |
| History | Current draft plus previous/original applied restore controls | Local saved-draft archive and Restore as draft; no matching product API yet |
| Desktop/mobile | Current mobile toggle sets canvas to 390px | Fluid Desktop matching its container; fixed Tablet/Phone widths and preservation of selection |
| Canvas click | Existing links navigate/switch page or open native destinations | Edit-mode component selection; distinct safe sample Preview mode |
| Commerce | Registration and dated family evidence describe bounded simple-product/native behaviors | Fictional samples and truthful unavailable states; no new runtime promise |
| Forms | Current registered non-delivering validation preview | Explicit validation-only UX; no real email, subscription or capture |
| Third-party icons | New local 55-icon reviewed candidate set | Use exact assets in sandbox; separate release inventory/review before product adoption |

Read the exact [control census](coverage/index.md) before implementation. The current section contract has `id`, `type`, `version`, package identity, settings and optional typed blocks, with strict additional-property rejection. Do not add generic visibility, arbitrary nesting or editor-only grouping metadata to serialized product data without an explicit contract/version decision.

## Local prototype boundary after selection

Create the selected frontend only under `uiux/theme-editor/`. Use the existing Product Design workflow/template as appropriate, with an explicit visual target. Do not install into `product/`, import its server, call `/api/full-theme/*`, load native PHP/bridge code or read real store data. Treat `product/` and `component-library/` as read-only references. Use extracted inert JSON and locally authored fictional sample documents. The review directory remains separate from both Git repositories and from all Magento installations.

Use a free loopback-only port distinct from 4177. Keep any prototype process and log under the review directory with a documented stop command. Do not stop the running editor. A static review document or icon gallery is not an interactive editor prototype and must not be reported as one.

Suggested frontend model: separate `savedResources`, editable `buffers`, selection/viewport UI state, bounded local history and `visibilityByNodeId`. Namespace browser storage to this design review. Never use source server URLs as service endpoints. Render safe sample references; external/native links resolve to local explanatory views. No credentials, customer profiles, payments or active account forms belong in fixtures.

Model mutations as commands carrying resource, parent/node IDs, before/after data and selection. Validate legal placement before commit. Coalesce a field edit or drag into one command. Prevent cycles, over-capacity blocks and cross-scope accidental moves. Store save checkpoints separately from undo history. A restored historical sample revision becomes editable and dirty; it does not activate anything.

## Selected editor styling standard

On 2026-09-10 the user selected **Tailwind CSS v4** for the new editor, first in the separate review workspace and later in the reviewed editor integration. React remains the editor framework; Alpine remains the default storefront interaction layer. This styling decision does not authorize a Magento/storefront migration or resume development.

The review now pins `tailwindcss@4.3.3` and `@tailwindcss/cli@4.3.3` in its own package manifest and npm lock. It uses existing Node 22.22.0/npm 10.9.4. Run `npm ci --ignore-scripts`, `npm run build`, and `npm run verify:css` inside `uiux/theme-editor/`. The optional `build:watch` command uses the same local compiler. No dependency was added to the working product and no browser/CDN Tailwind runtime is used. [Official CLI workflow](https://tailwindcss.com/docs/installation/tailwind-cli).

Author shared CSS-first tokens in `styles/tokens.css`; the four page-specific sources under `styles/` produce `compiled/controls.css`, `compiled/gallery.css`, `compiled/review.css` and `compiled/viewport.css`. Every page actually loads its compiled output. Each entry uses `source(none)` and explicit sandbox HTML/module paths; product, storefront and docs sources are excluded. Preserve the explicit specimen base styles by importing theme/utilities without Preflight during this bounded migration. [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files), [theme tokens](https://tailwindcss.com/docs/theme).

Keep static complete utility names in React/HTML/module source. Use validated runtime CSS variables for merchant values; theme JSON must remain portable semantic data, independent of Tailwind classes. The review's `--inspector-width` is UI state, not theme content. Editor CSS belongs in its own document/root; storefront CSS requires a separate entry, source scope and build. Never load editor global styles or resets into the storefront iframe.

Tailwind's stated browser baseline is Chrome 111, Safari 16.4 and Firefox 128; optional modern utilities may require newer support. This is not a completed cross-browser certification of the review UI. [Browser requirements](https://tailwindcss.com/docs/compatibility).

The scoped dependency review is `uiux/theme-editor/third-party/tailwind-review.md`, with exact artifact integrity, license hashes, all 33 installed package license texts and a 66-entry lock inventory including uninstalled platform variants. MIT, ISC, BSD-3-Clause and Apache-2.0 tooling terms were recorded. Lightning CSS 1.32.0/MPL-2.0 is used unchanged for local compilation and is not shipped in CSS; any tool redistribution requires separate covered-source/notice review. Full native-binary or bundled-code redistribution clearance is not claimed. [Lightning CSS license](https://github.com/parcel-bundler/lightningcss/blob/v1.32.0/LICENSE), [Mozilla usage guidance](https://www.mozilla.org/en-US/MPL/2.0/FAQ/).

Every generated CSS file retains Tailwind's version banner and full MIT notice. Preserve those with delivered CSS, as well as the separately reviewed icon notices. Reassess changed versions, platforms, plugins, hosted build services or distribution scope under the third-party requirements (`content/requirements/third-party-compliance.md` in the workspace). [Tailwind 4.3.3 license](https://github.com/tailwindlabs/tailwindcss/blob/v4.3.3/LICENSE).

## Responsive implementation constraints

At approximately 1440px editor width, reserve roughly 240–280px outline and 280–320px inspector, with flexible canvas space. At narrower widths collapse one side panel, keep explicit reopen controls and avoid horizontally clipping form fields. Page/viewport controls remain reachable. Desktop preview follows its available container at 100% with no width cap or scaling, including widths above 1440px. Browser/panel resizing must resize that iframe directly. Tablet/Phone retain their fixed device widths, using workspace scrolling when necessary. Phone preview does not imply phone authoring support.

The user's compact Resource Desk refinement supersedes those initial width ranges for that candidate: 48px activity rail, about 220px tree, 268px inspector, 12px indent increments, 32px compact pointer controls and 44px touch targets. Replace Optional image Change/Remove text buttons with bare pencil/trash glyphs on transparent, borderless hit areas, preserving tooltips, accessible names and a keyboard focus ring; the trash graphic alone turns red on hover and keyboard focus. Removal requires a named confirmation dialog with Cancel initially focused and Undo after confirmation. Keep the storefront as the flexible primary area.

Apply the adaptive choice renderer to enum and boolean fields: two to four options become segmented toggles only when their complete rendered labels fit; otherwise use a select. Recalculate on panel, font and label changes while preserving typed values and focus. The isolated `controls.html` specimen demonstrates this rule, including Page/Block, Enabled/Disabled and a six-option select. Its local samples add no product fields.

Use the selected direction's layout and hierarchy faithfully while applying the documented corrections: exact Lucide icons, system sans inspector inputs, correct shared scope wording, no invented Media feature, no false 66-template count and no fake publication claim. Frame artwork is a visual target, not the source of serialized settings or capability truth.

Desktop behavior is implemented in the isolated `viewport.html` review specimen with an original local sample storefront in a separate iframe document. Its editor styling uses the existing pinned Tailwind build; sample storefront CSS stays separate. This is a viewport behavior example, not a completed editor integration.

## Acceptance checks for the later sandbox

| Check | Passing evidence required |
| --- | --- |
| Registry coverage | Every current type and all fields/blocks represented; unsupported placements explain why |
| Library insertion | Pointer drag into tree and canvas, keyboard insertion, search/category filtering, no-results state |
| Reordering | First/middle/last sections, nested blocks, valid/invalid parent, auto-scroll, Escape and pointer cancellation |
| Selection | Canvas/tree/inspector agree; nested selection, typing focus and Preview navigation are distinct |
| Editing | Every schema control class works; adaptive toggles/selects preserve values through resizing and long labels; bounds/reference errors remain recoverable |
| Visibility/actions | Hide/show, duplicate, confirmed remove, cancel, undo and redo preserve exact state/identity rules |
| Menus | Three-level nesting, cycles/limits rejected, assignment safety and audience labels |
| Resources | Page/shared independence, dirty buffers across navigation, active-scope save |
| Draft persistence | Save/reload local state, independent history restoration, storage failure and no false saved feedback |
| Navigation/viewports | Return, page/template distinction, preview refresh, uncapped fluid Desktop, browser/panel resizing, 768/390 frames and preservation of edits |
| Accessibility | Keyboard-only journey, focus return, live announcements, readable zoom and reduced motion |
| Visual fidelity | Paired selected-target/rendered-screen comparison at matching state and viewport, documented corrections |
| Isolation | No network/bridge requests to Magento or actual-editor API; no server-module imports; no live publication |

Use the in-app browser for interaction verification. Test only the isolated prototype and its meaningful contracts. Do not run the existing product's full test suites or any Magento lifecycle scripts for this design review. Capture actual results and unresolved defects instead of pre-marking these checks as passed.

## Third-party and asset handoff

The local review's icon folder holds Lucide Static 1.44.0 SVGs and the upstream ISC plus Feather-derived MIT license texts. The icon sub-agent recorded provenance and accepted this local review use. Preserve notices in any delivered copy. SVGs are static copied assets; no runtime icon package or transitive library install was added here. Reconcile exact assets, notices and any new package graph before product/browser distribution.

The three raster frames were generated using built-in Image Gen from the captured fictional editor UI, with prompt text saved locally. No Flux code/icons/vendor asset source was copied. The frames are concept artwork, not reusable production image licenses or a cleared product asset inventory. System UI fonts require no new bundled font files. Any future external photography/fonts/libraries require the existing third-party review (`content/requirements/third-party-compliance.md` in the workspace) for exact use.

## Completion of this phase

This phase supplies three visual directions, current-state captures, full component/control coverage, state/interaction requirements, exact icon assets and an implementation handoff. The user is refining the third original direction; the compact revision with bare icons is the current visual candidate. Adaptive fields and image confirmation are implemented as isolated control specimens, with the complete editor sandbox still outstanding. Magento development, backend integration, publishing and coordination automation stay paused.
