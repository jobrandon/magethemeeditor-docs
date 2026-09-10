# Batch 02 editor concept evidence

Date: **2026-09-07**. Owner: task `01a07b0a-53c4-7382-aea4-79c44a2ca13a`, local Astra High.
Scope: original local home/CMS editor concept, candidate comparison, targeted docs and authorized
Linear updates. Product has no Git branch/SHA; no code upload, commit, push, PR, visibility change
or public hosting. Existing dirty docs and all Batch 01 review/remediation evidence are preserved.

## Foundation and decision

Before edits, this task independently matched the 36-file source aggregate
`bb1ba5807c9ed533bc1519de80ddabbe35867d889d1f48db8e3edf2165bec3a2` and read the independent
recheck report. F1/F2/F3 were resolved; coordinator acceptance was only for this local spike.
The [Batch 01 appendendum](batch-01-evidence-2026-09-07.md#independent-recheck-acceptance) preserves
that scope and the original historical observations.

[ADR 0003](../decisions/0003-local-editor-choice.md) selects custom React for the small flat
contract. The [comparison](../architecture/editor-concept.md#candidate-assessment) reviews exact
GrapesJS core 0.23.6, Puck 0.23.0 and Craft 0.2.12 documentation/package identities. Those three
were not installed or executed. Custom React alone ran both original documents; no four-engine
benchmark, native renderer parity or merchant preference was established.

## Implemented source and dependencies

Added `product/editor/` with original UI, browser-safe document commands, iframe illustration,
styles and generated ceramics asset; `src/build-editor.mjs`, `src/demo-server.mjs` and
`test/editor.test.mjs`. Updated product README/scripts/lock and third-party records/notices.
Existing v1 schemas, contract validator, CLI, foundation tests and fixtures remain unchanged.
No server crypto/filesystem or signing material is imported by browser code.

Exact added graph: React 19.2.8, React DOM 19.2.8, scheduler 0.27.0. All three MIT licenses,
artifact identities, transitive edge, React DOM's bundled Modernizr attribution and actual local
browser use were reviewed; original notices are served at `/THIRD_PARTY_NOTICES.txt`. Existing
five Ajv packages remain server-only. No new bundler, framework template, external font, icon
package, Magento/theme dependency, paid SDK or hosting provider. One original AI-generated image
has retained provenance/hash and local-use review; its model revision is not exposed by the tool.
The build verifies exact dependency/notice and image identities. This is not commercial clearance.

## Automated verification

Environment: Node **22.22.0**, npm **10.9.4**, local macOS arm64. Product commands run from
`MageThemeEditor/product`. Logs/manifests are in ignored `product/.local/batch-02/`.

| Command/check | Observed result |
| --- | --- |
| `npm install --ignore-scripts --no-audit --no-fund` after exact review | Three packages added; no lifecycle/audit upload |
| `npm run verify` | 71 tests pass: existing 53 foundation tests plus 18 editor/service checks; eight-package identity/notice guard and asset hash guard pass |
| `npm run build` | Fixed four-file production vendor graph, 570,688 bytes raw / 102,809 gzip; original MIT and bundled attribution retained |
| `node --check` on authored modules | Syntax checks pass |
| HTTP service tests | Both valid documents, exact round trip, invalid/lossy/duplicate JSON, reference/capability rejection, persistent revisions, competing writes, stale-save conflict, explicit rebase, restart recovery and untouched second page pass |
| Exposure tests | Loopback binding; foreign/missing mutation Origin, rebinding Host, non-JSON and oversized request rejection; exact static routes; workspace/contract/evidence/directory paths unavailable |
| Model tests | Stable IDs through settings/add/order/remove/undo; 100-section limit; identity/revision restrictions; undo after save; unsupported inherited sources rejected |

The single-process service atomically renames local draft files. These checks do not prove durable
fsync/crash recovery, multi-process transactions, authenticated tenancy or production storage.
The optional download uses a browser Blob; its event was not confirmed in the in-app browser.
Validated copyable JSON export and exact reimport are the observed successful path.

## Observed browser interactions

Codex in-app browser at `http://127.0.0.1:4173/`, with actual actions and DOM/AX verification:

- Empty selection; list-to-settings and iframe-to-settings selection, including keyboard Enter.
  Preview selection keeps focus on its section and retains the same stable ID.
- Hero heading/alignment/image controls; grid columns and selected product references; immediate
  iframe updates. HTML-looking heading rendered as plain text with zero injected `<strong>` nodes.
- Add, duplicate, remove, undo/redo; Move up/down and Alt-arrow order changes. Existing identities
  survive. Empty heading produces a visible contract error and disables Save.
- Manual save advanced the local revision; browser reload recovered edits. Home and CMS retained
  independent documents while switching and saving the other page.
- Export exposed exact validated JSON; same-document reimport retained IDs and was a clean no-op.
  Invalid `1.0` numeric import rejected with NUMBER_FORMAT without replacing the current draft.
  Empty valid CMS import showed the empty-region prompt and undo restored the prior document.
- Competing-save exercise showed local/saved revisions and both headings plus expandable complete
  documents. Keep my edits rebased, then a deliberate save succeeded. Use newer draft loaded the
  competing saved version. Neither path silently reported a publication.
- Region picker and scope dialog show home content, registered CMS story, unsupported hardcoded
  booking, untouched shared surfaces, and unavailable PDP/category adapters. About this demo
  explains future connection/preview/publication/restoration and fixed demo editor role.
- Wide **1440×1000** and narrow **390×844** inspected. Narrow Sections/Preview/Settings panels work,
  text/controls fit, and the document has no horizontal overflow. Tablet/mobile iframe widths
  measured **768/390 CSS px**. Screenshots retained locally.
- Keyboard modal Tab/Shift-Tab wrapping, Escape dismissal and focus return were checked after
  fixing an initial one-button Tab escape. Final tab reports no console errors/warnings.

The first browser tab developed a viewport/zoom raster mismatch. A fresh tab in the same in-app
browser restored exact requested dimensions and clean captures; final evidence uses that tab.
Screenshots: `editor-wide.png`, `editor-mobile-settings.png`, `editor-mobile-preview.png` and
`conflict-mobile.png`, alongside detailed `browser-evidence.md`. This is desktop browser responsive
inspection, not physical-device or screen-reader testing. No merchant usability study was run.

## Documentation, Linear and later steering

At start, exact live reads covered SOL-493/501 and dependencies SOL-491/492/500. Only SOL-493 and
SOL-501 moved from Backlog to In Progress, with comments limiting SOL-501 to prototype work.
Descriptions and relationships were not changed. SOL-491/492 retain open support/customer/runtime
criteria. Exact issue readbacks, not paginated project-wide audit, verify the final changes.

The coordinator's later named-store preflight is appended to the
[fixture plan](../architecture/integration-fixtures.md#named-local-compatibility-targets-later-2026-09-07-steering).
It authorizes considering INOX local Blank/Luma/Porto and B2B local Hyvä compatibility targets,
with state isolation planned before module experiments. INOX HTTP 200 and pre-existing B2B 500
are coordinator observations, not new Magento tests by this batch. No local store was mutated.
The future [custom-module proposal](custom-module-data-integration.md) was read from Linear and
mirrored as documentation only; no provider UI/runtime or portable-contract field was added.

## Handoff and open acceptance

Run instructions and exact loopback URL are in the [concept guide](../architecture/editor-concept.md#run-the-concept).
The preview remains available locally for independent review. Copyable JSON is the reliable export
path in this browser; optional download completion remains unverified. Registered settings are
explicit controls, not a general schema-driven/rich-text engine. Pointer dragging/nesting,
authentication/roles, real store connection, default inheritance, Magento native rendering,
preview isolation, publication/restore, cache/outage guarantees and commercial release remain open.

Stop at Batch 02. Next bounded work should independently review this source/evidence, then preflight
and isolate the named local target for one actual native home/CMS rendering/selection experiment.
Do not infer any real-store safety from the illustrated header/footer or local tests.

## Final preservation and documentation checks

Fresh `npm ci --ignore-scripts --no-audit --no-fund` reinstalled all eight locked packages, then
`npm run verify` again passed all 71 tests and build/notice/asset guards. All ten authored `.mjs`
modules passed syntax checks. The original content CLI fixture exits 0 and the invalid columns
fixture exits 1 with SCHEMA, as expected.

Docs `make verify` passed: 25 source pages, 26 HTML pages, 1,577 local links, with local
anchors/assets/navigation/source boundaries checked. Nine changed/new rendered pages were
inspected at 1280 CSS px; long tables scroll within their Material container. `git diff --check`
passes. The existing pinned Material tool prints its upstream MkDocs 2 notice; MkDocs 1.6.1
builds successfully. External citation crawling and Magento behavior are outside this checker.

Only four of the 36 baseline authored product files changed: README, package.json, package-lock.json
and third-party/inventory.json. New files make 52 authored files in total. The original contract,
schemas, fixtures and 53-test foundation suite remain byte-identical. The aggregate is computed
from compact key-sorted JSON mapping relative filenames to SHA-256, excluding generated/install/
ignored evidence directories. Final source aggregate:

`192fb2d25cdea04592f8143c81d1f18979f571c9c7268c23b381ce2946b4b7e8`.

The full map is retained in `product/.local/batch-02/source-after.json`. Research SHA-256 remains
`541f2c46a99715ea01939e71a4c017e9fd74d4bd271bacdc48dc12de7a41f6b5`; `.docs` still resolves
to canonical `docs/content`. Eight pre-existing content/navigation files received targeted
additions; all other snapshotted content bytes remain unchanged. No original review/remediation
file was edited. Docs and product retain separate ownership; neither repository was committed.

Final Linear comments were saved on SOL-493 and SOL-501 at 09:22:41–09:22:43 UTC, followed by
exact readback. Both remain In Progress, with all eight/four acceptance checkboxes respectively
unchecked and original blocking/blocked relationships intact. SOL-491/492 read back In Progress
with their open criteria. No descriptions were edited by Batch 02. Final comment IDs:
`570954f5-70f1-4d8c-926c-79febc2f509c` and `e3cba689-48cf-4be9-92f6-793525128fe7`.


## F1 save-race correction · 2026-09-07

Independent review returned one P2 defect: overlapping client actions released a shared busy flag,
then a delayed save response overwrote newer edits and marked an older revision clean. Server CAS
was functioning. Original implementer `01a07b0a-53c4-7382-aea4-79c44a2ca13a` owns this focused
correction. The review report, original repro/helper and browser evidence remain unchanged under
`product/.local/reviews/batch-02/`; correction evidence is separate under
`product/.local/remediation/batch-02/`. No additional task, batch or Magento work was started.

The app now uses a synchronous operation owner carrying the page and cloned request document.
Competing operations and stale edit/page callbacks cannot clear or bypass that owner. Save
acknowledgement verifies identity, base revision and exact response/request content; it advances
the saved base while retaining the current buffer and undo/redo history. Post-request edits remain
dirty. Import/reload reject replacement if the buffer changed. Conflict choices are tied to the
displayed operation/page, and known newer revisions survive switching between independent buffers.
Simulation now opens the comparison immediately instead of leaving a known older revision clean.

Permanent checks: **82/82 pass**, comprising the previous 71 plus seven model/operation regressions
and four actual App-handler regressions. Deferred-response checks cover edit/undo during saves,
duplicate/stale/wrong-document acknowledgements, exclusive ownership, import/reload guards and
independent pages. A small deterministic hook/transport harness executes unchanged production
handler bodies and invokes stale Save/tools/import/reload/edit/page/conflict callbacks directly,
even when the rendered control is disabled. It is not a React DOM/focus test; the actual browser
run supplies that separate evidence. No test or browser dependency was added.

The unchanged reviewer `race-model-repro.mjs` failed before the fix (exit 1) and passes afterward
(exit 0): B remains dirty and undo/redo retains it. Its two-argument `markSaved` invocation remains
supported; the real app additionally supplies the explicit request snapshot. This is not a rewritten
review assertion. `npm run verify` passes existing package/asset/notice guards and server CAS tests.

Actual browser writes use only loopback **4177**, correction-owned PID **9209**, and separate
`product/.local/remediation/batch-02/drafts/`. The helper delays only home-save HTTP response end
by 20 seconds; storage and response bytes are unchanged. During both observed delays, Draft tools,
page selection, fields and undo remain disabled. Attempting Draft tools times out on its disabled
control, no dialog opens, and no second write reaches the server. Save A completes at its stored
revision; subsequent B edits remain dirty and recover through conflict choices. An independent
Studio save and returning to Home preserve the Home buffer and known newer revision. Browser
snapshots, blocked-action diagnostics and the request log are retained in the correction directory.

Only `editor/app.mjs`, `editor/model.mjs`, `test/editor-race.test.mjs` and
`test/editor-ui-race.test.mjs` differ from the reviewed source. The portable contract, service CAS,
schemas, original fixtures, dependencies and assets are unchanged. There is still no product Git
branch/SHA. The compact key-sorted relative filename/SHA-256 map excludes `.local`, `node_modules`,
`.git`, `dist` and Finder `.DS_Store` metadata. Corrected **54-file** aggregate:

`3aafd62c93c72e6514339e1c1dfbffac50deebacd5eb3ab60ee5adefa7c5406e`.

The existing user preview PID **7682** on `127.0.0.1:4173` and its manual draft files remain
untouched. Browser assets have been rebuilt; the user's existing tab still runs its loaded version
until the user reloads after saving/exporting any unsaved work. No user tab was reloaded. Original
review evidence, unrelated dirty documentation and Finder metadata remain preserved. Research
retains its recorded checksum and `.docs` retains its canonical target.

SOL-501 remains In Progress with all four criteria unchecked and existing relationships intact.
This is local correction evidence only. **Independent recheck by the original reviewer remains
pending**, followed by coordinator acceptance before any native integration. Magento, merchant,
publication/restoration, outage/cache and commercial-release criteria remain open. No Git commit,
push, PR, upload, visibility change or deployment occurred.


Correction closeout checks: Node 22.22.0/npm 10.9.4 on macOS arm64; all 12 authored JavaScript
modules pass syntax checks. The final built browser also passes undo/redo, explicit reload,
validated JSON export/reimport, Use newer draft and unchanged Studio saved-buffer controls, with
no warning/error console entries. `make -C docs verify` passes **25 source pages, 26 HTML pages,
1,581 local links**, and `git -C docs diff --check` passes. The three changed pages were inspected
in the existing loopback docs preview. These are documentation checks, not Magento runtime proof.
