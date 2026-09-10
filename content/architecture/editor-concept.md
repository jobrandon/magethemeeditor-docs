# Local editor concept and candidate comparison

Observed: **2026-09-07**. Original fictional Silt & Form store. Local home/CMS spike only;
[ADR 0003](../decisions/0003-local-editor-choice.md) records the reversible choice.
The [portable 1.0.0 contract](content-contract.md) remains authoritative and unchanged.

## Candidate assessment

Exact npm metadata and SHA-512-verified candidate tarballs were inspected on the observation date.
Only custom React was implemented and executed. GrapesJS/Puck/Craft rows below are documentary
assessments and engineering inferences, not measured browser behavior or complete adoption reviews.
Live vendor docs may evolve independently of these pinned packages; version-pinned package
metadata is retained in `product/.local/batch-02/package-review/`.

| Candidate / exact edition | Contract fidelity and identities | Controls, order and history | Native preview fit and effort |
| --- | --- | --- | --- |
| GrapesJS **core 0.23.6**, BSD-3-Clause; Studio SDK excluded | Uses its own component/project JSON. Needs explicit v1 mapping, stable semantic IDs and strict rejection of arbitrary styles/scripts/HTML; HTML export is insufficient for editor restoration | Component types/traits, ordering, UndoManager and keymaps exist. Must constrain the general HTML model to the registered vocabulary | Its iframe hosts the GrapesJS canvas. A native Magento preview and selection bridge remain separate integration work. Most adaptation overhead for this flat semantic contract |
| **@puckeditor/core 0.23.0**, MIT; Cloud/AI services excluded | Puck Data has content/root and component props IDs, with slots replacing older zones. Requires reversible v1 mapping and preservation of document/scope/version metadata outside Puck Data | Configurable fields, outline, permissions, viewports and history hooks offer a strong ready-made shell | React component canvas is a useful accelerator, but its iframe configuration does not prove control of authenticated, externally rendered PHTML. Mapping plus preview bridge needs a spike before claiming fit |
| **@craftjs/core 0.2.12**, MIT | SerializedNodes retain node IDs/props and resolver type information. Translate v1 sections explicitly; never make that node graph the stored contract | Node actions, selection connectors, move/delete and history are building blocks; settings and finished UI are ours | React node composition is not a native Magento renderer. Still requires a custom shell and native preview bridge, while adding a second graph |
| **Custom React 19.2.8 / React DOM 19.2.8** | Direct edits to the canonical document; stable IDs unchanged through settings/order/save/export/reimport. No mapping layer | First-party flat commands, registered controls, bounded undo/redo, native form/button keyboard operations | First-party same-origin illustrative iframe and origin/source-checked selection messages. Highest ownership of UI details, lowest semantic translation cost for this deliberately small spike |

Sources: [GrapesJS project persistence](https://grapesjs.com/docs/modules/Storage.html),
[traits](https://grapesjs.com/docs/modules/Traits.html),
[UndoManager](https://grapesjs.com/docs/api/undo_manager.html),
[keymaps](https://grapesjs.com/docs/api/keymaps.html),
[Puck Data](https://puckeditor.com/docs/api-reference/data-model/data),
[Puck component API](https://puckeditor.com/docs/api-reference/components/puck),
[Puck viewports](https://puckeditor.com/docs/integrating-puck/viewports),
[Craft editor API](https://craft.js.org/docs/api/useEditor),
[Craft overview](https://craft.js.org/docs/overview),
[React state logic](https://react.dev/learn/extracting-state-logic-into-a-reducer).

Keyboard support must be tested in the resulting integration. GrapesJS keymaps are not an
accessibility certification. Puck's supplied controls/history reduce implementation work but do
not establish screen-reader, focus or cross-frame behavior for our app. Craft exposes primitives;
we would own accessible settings and reordering. Custom React's native controls, explicit order
buttons/Alt-arrow commands and dialog focus handling were exercised here. No WCAG conformance or
screen-reader validation is claimed. No merchant preferred one engine in a study.

The same original home hero/grid/CMS-block and studio hero/widget documents informed all four
mapping assessments. Custom React executed both and retained exact document semantics. The other
three did not render those documents, so there is no observed cross-engine visual-parity result.
A second implementation was unnecessary: no material unresolved question justified another full
editor for this flat proof. Revisit Puck if a wider library/nested composition becomes required.

## Dependency and commercial implications

| Package graph | Observed implication | Use/review outcome |
| --- | --- | --- |
| GrapesJS 0.23.6 | Eight declared dependency edges, including Backbone, CodeMirror and Underscore; tarball unpacked size 12,448,906 bytes | Core license permits source/binary redistribution with notices and non-endorsement obligations. Complete transitive graph and delivered bundle were not adopted/reviewed. Studio SDK is a separate commercial product |
| Puck 0.23.0 | 36 declared dependency edges, including DnD Kit, Tiptap, Radix, Zustand and happy-dom; unpacked size 2,654,160 bytes | Core declares MIT. Npm tarball inspected here lacks a standalone LICENSE file; upstream repository supplies MIT text. Resolve exact-release notice coverage and full transitives before adoption. Cloud/AI terms are separate |
| Craft 0.2.12 | Four declared dependency edges: lodash, debounce, @craftjs/utils, tiny-invariant; unpacked size 482,847 bytes | Core tarball includes MIT license. Full transitives and browser output not adopted/reviewed |
| React/DOM/scheduler | Three added locked packages; React DOM's one runtime edge resolves to scheduler 0.27.0 | Accepted for this local browser prototype after tarball identity, manifest, original-license and bundled-code review. Four production files yield 570,688-byte vendor JS, 102,809 bytes gzip |

Declared edge counts and unpacked archive sizes are **not installed graph counts or comparable
browser bundle measurements**. Puck/Craft require React too. No four-way performance benchmark was
run. Sources: [GrapesJS exact metadata](https://registry.npmjs.org/grapesjs/0.23.6),
[Puck exact metadata](https://registry.npmjs.org/@puckeditor/core/0.23.0),
[Craft exact metadata](https://registry.npmjs.org/@craftjs/core/0.2.12),
[React exact license](https://github.com/react/react/blob/v19.2.8/LICENSE),
[Puck license](https://github.com/puckeditor/puck/blob/main/LICENSE),
[GrapesJS Studio documentation](https://app.grapesjs.com/docs-sdk/configuration/projects).

The actual eight-package inventory (five unchanged Ajv dependencies plus three React packages),
lock, original notices, exact-use review and asset record live in `product/third-party/`.
The React DOM bundle includes its original Modernizr custom-build MIT attribution; both this
attribution and full React MIT grants survive browser packaging. Node/npm and docs tooling remain
at their previously reviewed versions. The first-party build uses no new compiler package.

One original AI-generated ceramics photograph is stored in `product/editor/assets/ceramics.png`.
Only fictional art instructions were sent through the existing built-in OpenAI image tool. No
client art, customer data, external font, paid SDK or hosted editor service is used. The tool does
not expose an exact image-model revision; the service/asset identity limitation is recorded.
System UI/Georgia fonts resolve locally and are not redistributed. Output rights, non-uniqueness,
account data controls and final commercial re-review are recorded in the exact-use review.
[OpenAI content terms](https://openai.com/policies/row-terms-of-use/)

## Run the concept

From `MageThemeEditor/product` using the existing Node 22.22.0/npm 10.9.4:

```bash
npm ci --ignore-scripts --no-audit --no-fund
npm run verify
npm run dev
```

`verify` builds the fixed browser graph, verifies package/notice identities and runs Node tests.
Open `http://127.0.0.1:4173/`. An alternate loopback port uses `MTE_DEMO_PORT=4174 npm run dev`.
Only exact authored routes/assets are served, never the workspace directory. Restart after server
changes; rerun `npm run build` and reload after browser-source changes. No hot-reload dependency.

Manual saves persist separately in ignored `product/.local/demo-drafts/home.json` and `studio.json`.
Unsaved buffers and up to 100 undo entries per visited page are in browser memory. Page switching
retains that tab's buffers; reload loses unsaved edits after the browser's unload warning. There
is no autosave, durable recovery history, multi-process locking or fsync/crash guarantee.

Draft tools exposes validated copyable JSON and an optional file-download request. The copyable
route was verified end to end; the in-app download event could not be confirmed. Import accepts
only the matching page/store draft and current saved revision, preserving stable IDs and typed
settings. Unknown references, assets and unresolved inherited sources are rejected in this demo.
A conflict compares both complete documents. Keep my edits rebases the full local document,
then requires another explicit save; Use newer draft replaces the local buffer. No field merge.

Following the Batch 02 F1 correction, asynchronous draft actions have one synchronous owner.
Save, import, reload, export, file reading and conflict simulation cannot overlap; page changes
and edits are guarded while an action is pending. Save acknowledgements identify their page and
request snapshot, advance the saved revision and retain any newer local edits/history as dirty.
Reload/import reject a changed request buffer. Conflict choices belong to the displayed page and
operation; known newer revisions remain visible across page switches. Simulation opens that
comparison immediately. These protections are local client behavior, not a hosted concurrency claim.

## Scope and next evidence

Home uses its main content surface. Our studio uses the registered story region and displays
surrounding original content plus unavailable hardcoded booking. CMS blocks/widgets are registered
references with illustrative copy. Header/footer/commerce and product/category routes are excluded.
The local fixture labels a hypothetical Luma adapter 1.0.0; it is not an installed Luma package.

Onboarding and unavailable publish/restore steps are explained in About this demo. English/store
override and demo editor role are fixed; no connection, authorization or inheritance resolution
is implemented. Controls are explicit for registered v1 types, not a generic schema-generated
settings engine. Plain text is intentional because rich text is absent from v1. Pointer dragging,
nesting, image uploads, price rendering, storefront navigation and live actions remain outside
this proof. There is one demo context, not a successful fake connection or publication.

Next: independent review, then a bounded native home/CMS renderer/selection proof after the
[named local-store preflight and isolation](integration-fixtures.md#named-local-compatibility-targets-later-2026-09-07-steering).
That must establish real renderer ownership, escaping and unaffected surrounding commerce before
broader hosted persistence or publication. Merchant-task, accessibility, authentic capability,
store/theme/version, outage/cache and commercial-release criteria remain open.
