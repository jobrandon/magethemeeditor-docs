# Editor source refactor — 11 September 2026

Observation date: 11 September 2026, Asia/Manila. This is a dated local implementation
receipt, not a commercial release or a live task dashboard.

The editor now has authored TypeScript/TSX source, focused feature ownership and required
type, lint and formatting checks. Generated browser bundles remain disposable build output.
The source refactor is integrated and accepted locally in the original checkout. Strict
checks and all 150 tests pass; fresh Silt and Daybreak editors load their full-page previews.

## Source structure

```text
product/editor/
  main.tsx                         Full editor entry
  StudioApp.tsx                    Provider composition
  components/                     Reusable fields and controls
  features/
    resources/                    Draft buffers, saves and acknowledgements
    workspace/                    Selection, layout and toolbar
    inspector/                    Settings UI and selection mutations
    outline/                      Movement rules and drag interaction
    navigation/                   Browser history and leave confirmation
    preview/                      Render requests and frame messages
    dialogs/                      Dialog state and presentation
    library/                      Section and component discovery
  services/                       Validated API and JSON boundaries
  adapters/                       Existing theme integration
  legacy/                         Supported historical editor views and hooks
  theme-studio-model.ts            Pure resource history and mutations
  theme-studio-navigation.ts       DOM-free navigation and save controller
  theme-studio-frame.ts            Full editor iframe entry
  preview.ts                      Historical editor iframe entry
```

React components and providers use `.tsx`; domain rules, services and contracts use `.ts`.
Network, persisted metadata and iframe inputs enter as `unknown` and are validated before
becoming typed state. Pure history and mutation code does not import React, DOM APIs or a
live Magento service. The application root composes providers instead of owning every
state value and event handler.

Theme authoring remains separate. Existing local themes register through an explicit
`ThemeAdapter`. The [Liquid SDK](../../architecture/liquid-theme-sdk.md) owns theme packages,
templates and runtime behavior. Core editor controls do not evaluate Liquid. The existing
synchronous adapter is a compatibility boundary for current presets; asynchronous
whole-document Liquid rendering requires its own integration and tests.

## Runtime and standards

The project uses Node.js **24.21.0 LTS**, bundled npm **11.19.0**, React **19.2.8**,
TypeScript **5.9.3**, Biome **2.5.13** and esbuild **0.28.2**. Exact dependencies, transitive
tooling and notices are recorded in the product lockfile and third-party inventory. The
project-local Node installation leaves other projects' global Node selection unchanged.

From `product/`, after activating the pinned runtime:

```bash
npm run typecheck
npm run lint
npm run format:check
npm run build
npm run verify
```

`verify` runs strict types, lint, formatting, a production build and behavioral tests.
The compiler covers all maintained editor TypeScript sources. Biome covers the editor and
selected changed build/server/test files; unrelated historical scripts are not silently
included in a formatting migration. Temporary invalid-source probes demonstrated that
each standards command fails on relevant errors. The probes were then removed.

This work changes source organization and preserves current styling. The selected
Tailwind v4 UI design remains a separately reviewed integration scope.

## Verification and correction

The implementation task used an isolated worktree based on commit
`35caa57d63601ffe202e6a209d6df7fb180ebeb7`. PM reviewed the architecture and transferred
161 changed/new/deleted paths into the original checkout only after checking for target
drift and preserving a reversal snapshot. Eleven superseded source/test entries were
removed. SDK work and local draft storage were excluded from the transfer.

The initial original-checkout `npm run verify` passed **147 tests**; all **135 generated
artifact hashes** matched the independently served worktree build. The server was
restarted with the pinned Node runtime and the Daybreak editor mounted its full-page
preview at `http://127.0.0.1:4177/theme?preset=daybreak`.

The connected Silt editor then exposed a real boundary mismatch: the native commerce
provider can return `image: null` for an unavailable category or product image. The new
parser had rejected this legitimate response. The correction normalizes only this image
field to an absent optional property, preserving strict validation of other fields and
rejecting malformed non-null imagery. Synthetic category/product tests cover this contract.
After the two-file correction, the original checkout passed strict checks and **150/150
tests**, with all **135 generated artifacts** matching the corrected worktree build. The
restarted main server runs under the pinned Node runtime. Fresh browser tabs loaded the
connected Silt Home editor and its six current sections, and Daybreak with its 19 sections;
both populated their canvas from header to footer, reported saved drafts loaded and left
Save disabled. These main-browser checks were read-only. All **17 existing draft hashes**
still match the pre-refactor baseline. No original draft save, native apply or restore was
used for acceptance.

The worktree browser suite used disposable draft directories and a fixture-only Silt
service. It covered editable sections, adaptive controls, responsive preview, pointer and
keyboard movement, arrays, images, shared menus, undo/redo, partial-save retry, cancelled
navigation during an acknowledged save, history, unsupported links and legacy conflict
handling. Fixture runs cannot apply or restore Magento. Existing same-origin iframe and
historical favicon warnings were recorded separately; fixture media substitution is not
native media validation.

Evidence is retained locally under `product/.local/source-refactor-review/` in the original
checkout and `product/.local/refactor/` in the implementation worktree. These ignored
receipts, manifests, logs and screenshots are not published documentation assets.

## Ownership and remaining work

- Editor source owner: task `01a08c6f-87f5-78c0-af2e-b337f6d04ed6`, GPT-6 Astra Extra High.
  Its named scope is strict source recovery, state/save ownership and preview trust boundaries.
- Liquid owner: task `01a08c5d-bf41-7720-9a6b-0f44a9e810d5`, working separately in `theme-sdk/`
  and on its scoped existing-INOX validation. Shared product paths require an agreed integration owner.
- PM owns original-checkout integration and preview restart. The earlier editor refactor task
  remains stopped to avoid overlapping writers.

Next work is the explicit asynchronous Liquid preview contract and selected-route Magento
validation, following [ADR 0004](../../decisions/0004-developer-theme-authoring.md) and the
[execution plan](../../roadmap/execution-plan.md). This refactor does not establish an
external theme installer, marketplace, arbitrary-code sandbox, native commerce acceptance,
production deployment or commercial clearance. No commit, push or native apply/restore is
part of this source acceptance.
