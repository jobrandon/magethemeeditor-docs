# Batch 01 foundation evidence

Observation date: **2026-09-07**. Scope: local product contract prototype, independently owned
documentation and authorized Linear synchronization. No Magento runtime, UI, deployment, merchant
interview or commercial release is proved. See the [execution ledger](execution-plan.md).

Owner: task `01a07ad8-3911-78d1-b5a4-28ba37eba5d7`, GPT-6 Astra, local macOS arm64.
Product has no Git branch/SHA yet. Documentation baseline is `main` at
`b9704c423a6a1065b58252aace9fa8492caa5171`, with pre-existing uncommitted work preserved.
No commit/push/PR or visibility change was performed by this batch.

## Linear synchronization

The live project and SOL-491–494 were read before mutation, with their direct blocking/blocked
relationships. SOL-490 and the existing implementation issues below were then read with
relationships. Updates appended the complete requirement and evidence text for each mapped HYB
criterion; existing descriptions and dependencies were not replaced. Only SOL-491/492 moved from
Backlog to In Progress. The project received a scope clarification, not a changed completion claim.

Writes completed between 07:52:28 and 07:52:59 UTC. Subsequent exact issue readback on this date
confirmed all 13 original descriptions were preserved, all expected additions were present and
all original relationships were unchanged. These are exact-ID reads, not paginated listings;
there is no issue-list pagination to complete and no claim of a full project-wide dependency audit.
The project read included six milestones and two resource references at the time of inspection.

| Existing issue | Synchronized criteria | Verified status |
| --- | --- | --- |
| [SOL-491](https://linear.app/solventech/issue/SOL-491/define-mvp-scope-and-the-storefront-support-matrix) | HYB-01, HYB-02, HYB-03, HYB-10, HYB-11 | In Progress |
| [SOL-492](https://linear.app/solventech/issue/SOL-492/specify-versioned-content-component-and-publication-contracts) | HYB-03, HYB-04, HYB-05, HYB-06, HYB-07, HYB-09, HYB-12 | In Progress |
| [SOL-493](https://linear.app/solventech/issue/SOL-493/design-and-validate-the-editor-and-store-onboarding-workflow) | HYB-02, HYB-03, HYB-04, HYB-07 | Backlog |
| [SOL-494](https://linear.app/solventech/issue/SOL-494/create-reproducible-luma-and-hyva-integration-fixtures) | HYB-01, HYB-02, HYB-04, HYB-08, HYB-09, HYB-10, HYB-12 | Backlog |
| [SOL-496](https://linear.app/solventech/issue/SOL-496/implement-the-local-json-renderer-and-registered-editable-regions) | HYB-01, HYB-02, HYB-03, HYB-11 | Backlog |
| [SOL-503](https://linear.app/solventech/issue/SOL-503/implement-draft-persistence-and-store-view-inheritance) | HYB-03, HYB-04, HYB-05, HYB-09 | Backlog |
| [SOL-509](https://linear.app/solventech/issue/SOL-509/convert-supported-page-builder-content-with-a-restoration-path) | HYB-02, HYB-05, HYB-06, HYB-07 | Backlog |
| [SOL-510](https://linear.app/solventech/issue/SOL-510/document-and-implement-the-adapter-sdk-for-hardcoded-theme-regions) | HYB-08, HYB-10, HYB-11 | Backlog |
| [SOL-511](https://linear.app/solventech/issue/SOL-511/build-the-free-compatible-reference-theme) | HYB-01, HYB-02, HYB-03, HYB-10 | Backlog |
| [SOL-513](https://linear.app/solventech/issue/SOL-513/verify-commerce-cache-isolation-csp-accessibility-and-performance) | HYB-04, HYB-05, HYB-07, HYB-08, HYB-09, HYB-10, HYB-12 | Backlog |
| [SOL-505](https://linear.app/solventech/issue/SOL-505/build-the-validated-publication-and-scheduling-pipeline) | HYB-03, HYB-05, HYB-09, HYB-12 | Backlog |
| [SOL-506](https://linear.app/solventech/issue/SOL-506/add-release-history-restoration-and-publication-audit-trails) | HYB-05, HYB-06, HYB-07, HYB-12 | Backlog |
| [SOL-514](https://linear.app/solventech/issue/SOL-514/verify-publication-recovery-and-saascdn-outage-behavior) | HYB-07, HYB-12 | Backlog |

The [core project](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098) also now states:
preserve active Luma/Hyvä themes; explicit selected home/CMS/PDP/category/region opt-in; unchanged
native commerce and untouched routes; home/CMS first; free theme optional; editor/provider choices
still candidates; local validation does not complete runtime criteria. The full requirement and
evidence text remains on each issue and in [HYB-01–12](../requirements/hybrid-adoption.md).
No new issues, tasks or marketplace implementation were created. The older Linear snapshot was
preserved as the historical observation; this page records the later synchronization.

## Product checks

Commands ran from `MageThemeEditor/product` with Node 22.22.0/npm 10.9.4. The verified code consists
of seven schema files, a bounded JSON decoder, semantic checks, a pure activation/draft model,
CLI, original valid/invalid fixtures and targeted tests. First test run: 43 passed. A subsequent
review added immutable document identity protection; final verification is recorded below.

Final verification, completed around 08:15 UTC (16:15 Asia/Manila):

| Check | Observed outcome |
| --- | --- |
| `npm ci --ignore-scripts --no-audit --no-fund` | Fresh lock-based install of all five reviewed packages passed |
| `npm run verify` | 45 tests passed, 0 failed; exact dependency identity and original notice SHA-256 checks passed for five packages |
| `node --check` on every authored `.mjs` | All four modules passed syntax checks |
| CLI valid content | Exit 0 with explicit document-only evidence label |
| CLI invalid columns fixture | Exit 1; `SCHEMA` at `/sections/1/settings/columns`, must be <= 4 |
| Docs `make verify` | Strict build passed; 21 source pages, 22 HTML pages, 1,198 local links; anchors/assets/navigation/source separation passed |
| Docs browser inspection via `make serve` | Six new pages and five changed existing pages inspected at 1280px; navigation/headings/tables readable; search returned the new contract section and navigated to its anchor; existing Mermaid rendered |
| Preservation | Research remains byte-identical to the shared original; `.docs` resolves to this workspace's `docs/content`; earlier Linear baseline and unrelated dirty content unchanged |
| Git whitespace | `git -C docs diff --check` passed |

The product contains 36 authored files outside installed dependencies. No UI/configuration theme
change required a new color-scheme or mobile test; those variants were not re-exercised here.
The existing Material tooling emits its upstream MkDocs 2 notice; the pinned MkDocs 1.6.1 strict
build completed successfully. External citations and dynamically loaded assets are not covered
by the site checker.

The tests use ephemeral local Ed25519 keys and synthetic content. They verify malformed/unsupported
documents, settings/limits, capability/store checks, live-reference allowlists, exact byte hashes,
signature/key rejection, revision conflicts, page/region overlap, all-or-nothing model transitions,
independent A/B publication/restoration and retained document identity. No key is persisted.
The asset test uses opaque original bytes with a MIME declaration, so it proves hash/length
validation only and explicitly does not decode or certify an image.

## Dependency evidence

Before installation, exact npm tarballs for Ajv 8.17.1, fast-uri 3.1.0, fast-deep-equal 3.1.3,
json-schema-traverse 1.0.0 and require-from-string 2.0.2 were downloaded and verified against
published SHA-512 identities. Full license texts and complete runtime dependency edges were
inspected. The product retains original notices, exact versions, artifact URLs, integrity values,
use/reviewer/date/outcome and dependency coverage in `product/third-party/` and `package-lock.json`.

Four packages are MIT; fast-uri is BSD-3-Clause with its upstream uri-js attribution. This review
accepts local contract-development use with the original notice obligations retained. It clears
no Magento distribution, browser bundle, hosted deployment, toolchain container or commercial
release. [Ajv license](https://ajv.js.org/license.html),
[fast-uri v3.1.0 license](https://github.com/fastify/fast-uri/blob/v3.1.0/LICENSE)

Node 22.22.0 and npm 10.9.4 were already installed and are used unmodified locally. Their upstream
license files were read, including Node's bundled-component notices and npm's Artistic-2.0 and
separate-dependency terms. Toolchain redistribution requires a separate exact inventory review.
No new docs dependencies, fonts, client code, Magento/Hyvä package, editor library or paid service
was introduced. The public registry was used for public package retrieval, without product/customer
data uploads or new account creation. [npm open-source terms](https://docs.npmjs.com/policies/open-source-terms/),
[npm privacy policy](https://docs.npmjs.com/policies/privacy/)

Python's initial HTTPS fetch failed certificate verification; the read-only package review was
retried with the system `curl` trust store and verified package integrity. TLS verification was
never disabled. All npm installation lifecycle scripts and automatic audit uploads were disabled.

## Documentation and preserved state

New durable pages are the execution plan, this evidence page, contract specification, fixture
plan, scope matrix and ADR 0002. Targeted additions update navigation, current status and links.
Existing independent documentation edits remain intact; the shared docs repository was not edited.
The historical research checksum and `.docs` destination are checked in final verification.
Generated `site/`, local QA evidence and dependency installs remain ignored.

Preserved research SHA-256:
`541f2c46a99715ea01939e71a4c017e9fd74d4bd271bacdc48dc12de7a41f6b5`.

## What remains open

SOL-491 requires customer-informed exact support versions and final beta scope. SOL-492 remains
partial because inheritance resolution, authenticated handshake/reference resolution, PHP signature
parity, operational key rotation, actual atomic persistence, durable acknowledgements, cache effects,
media validation and Magento restoration/outage behavior have not been implemented or observed.
SOL-493/494 remain Backlog. Documenting the future fixture recipe does not create those fixtures.

The selected product remote is known but its reported public visibility conflicts with the planned
private source delivery; the coordinator is resolving that decision. No source push was attempted.
Next: coordinator review, then the bounded concept UI/editor comparison task and independent
fixture access preparation described in the [execution plan](execution-plan.md).

## Independent review and focused corrections

Later observation, 2026-09-07. The original 08:15 results above remain historical evidence.
Independent review task `01a07af0-aa4e-7b33-a6d5-553840d6d6e9` examined the original source from
08:17–08:22 UTC. It reproduced 45 passing tests but found three failing desired-behavior repros;
nine companion controls passed. Review recommendation: correct F1/F2/F3 before Batch 02.

| Finding | Original behavior | Focused correction |
| --- | --- | --- |
| F1 · P2 | Same asset ID could acquire different bytes/metadata while document ID/revision/hash stayed fixed | Installation-scoped immutable digest/length/MIME bindings, identical reuse allowed, changed binding rejected, retained history and failure atomicity |
| F2 · P2 | `4.0000000000000001` rounded to integer 4 and passed a settings bound | Canonical integer token and exact digit-range checks before JSON numeric conversion; decimals/exponents/negative zero rejected explicitly |
| F3 · P3 | `common` definitions schema accepted arbitrary JSON and CLI exited 0 | Six-kind public allowlist; internal/unknown/schema-fragment kinds return `UNKNOWN_KIND` |

The original report/repros and all reviewer-owned files remain under
`product/.local/reviews/batch-01/`, unchanged. The implementer resumed at 08:25 UTC, captured a
separate preservation manifest, confirmed the original source identity and reproduced all three
failures before editing. Remediation logs/manifests are separate under
`product/.local/remediation/batch-01/`; this directory is not reviewer-owned evidence.

Original 36-file source aggregate SHA-256:
`38cb20f461d430197614fb63aa20c6d89941d83f6db30b66ffa8832653356174`.
The aggregate is the SHA-256 of the compact key-sorted JSON relative-filename-to-SHA-256 map,
excluding `.local`, `node_modules` and `.git`. There is still no product Git baseline.

Only `product/src/contract.mjs` and `product/test/contract.test.mjs` changed in product source.
Related decoder, CLI, schema-selection and asset/document-reference paths were inspected for the
same defects. Trusted package/schema-file reads continue using ordinary JSON parsing; all public
wire document paths use the corrected decoder. The schema/settings/revision/length bounds and
dependency inventory remain unchanged. The intentional acceptance policy changes are specified
in the [contract amendment](../architecture/content-contract.md#review-corrections-2026-09-07) and
[ADR amendment](../decisions/0002-portable-contract.md#amendment-after-independent-review-2026-09-07).

Permanent regressions cover changed digest/length/MIME, identical reuse across releases/stores,
new asset IDs, independent original/editor restore, late-failure map preservation, missing legacy
history, exact integer/safe-range boundaries, settings/revision/expected-revision/length wire
tokens, quoted numeric text, malformed controls and every allowed/forbidden public kind.
All three original repro assertions now pass in the implementer's run, together with nine controls;
the permanent suite passes 53 tests. This is not an independent recheck or Magento evidence.

### Correction verification

Implementer checks on 2026-09-07 after the 08:25 UTC remediation start, using the same existing
Node 22.22.0/npm 10.9.4 environment:

| Command/check | Observed outcome |
| --- | --- |
| `npm run verify` | 53/53 tests pass; all five dependency identities and notice hashes pass |
| `node --test .local/reviews/batch-01/repro.test.mjs` | 12/12 pass, including all three originally failing assertions; reviewer file unchanged |
| `node --check` on all four authored `.mjs` files | Exit 0 for each |
| Actual npm CLI cases | Eleven cases match expected exits: ordinary/maximum-column content exit 0; bounded-invalid, unsupported-version, malformed, common/unknown kind and lossy settings/revision/length/exponent cases exit 1 |
| Docs `make verify` | Strict build and local link/anchor/asset/navigation/source checks pass; 21 source pages and 22 HTML pages |
| Changed-page browser inspection | Contract/ADR/evidence/ledger inspected locally, including numeric policy table, headings, navigation and linked correction anchors |
| Preservation | Reviewer-owned file set/hashes unchanged; only two product source files and four specified documentation pages changed during remediation; original research unchanged |

The normal preview port 8017 was already occupied. The documented alternative command
`.venv/bin/python -m mkdocs serve --strict --dev-addr 127.0.0.1:8018` served this inspection without
stopping the existing listener. Only the correction task's temporary preview is stopped afterward.
No diagrams or theme/configuration changed; no new Magento, mobile/color-scheme, media decoding or
commercial-release result is inferred from these checks.

Corrected 36-file source aggregate SHA-256, using the same filename/hash algorithm as the review:

`bb1ba5807c9ed533bc1519de80ddabbe35867d889d1f48db8e3edf2165bec3a2`.

Individual changed source identities:

- `src/contract.mjs`: `d8a3525b66ebc403ffb38cf5d313e2562cfc0d1ab2b4a9149bb8b0ae87b6ac0a`.
- `test/contract.test.mjs`: `42c8851239a26e9cb94719d9873b3e129dd42db86d623c792511aeb3aa9fbe60`.

The exact file map is retained at `product/.local/remediation/batch-01/source-after.json`; command
logs and CLI/syntax results sit beside it. No dependencies, fixtures or schema files changed.
SOL-492 remains In Progress. The coordinator should request recheck from the existing independent
review task before accepting Batch 02. The implementer's successful rerun does not supply that
independent acceptance, Magento proof or source-delivery authorization.

## Independent recheck acceptance

Later observation, 2026-09-07, 08:38–08:41 UTC. Independent reviewer task
`01a07af0-aa4e-7b33-a6d5-553840d6d6e9` resolved F1/F2/F3 and found no newly introduced
actionable regression in the bounded recheck. It independently reproduced 53 permanent tests,
12 unchanged original review checks, six additional checks and 20 CLI cases. Both source
manifests matched the corrected 36-file aggregate above. Original review evidence and docs
remained unchanged during recheck. Report: `product/.local/reviews/batch-01/recheck.md`.

The coordinator accepted this only as the local foundation for Batch 02, owned by task
`01a07b0a-53c4-7382-aea4-79c44a2ca13a`. SOL-491/492 remain In Progress with customer,
support and integration criteria open. No Magento behavior, commercial release or delivery
authority was accepted. Earlier pending-recheck statements are preserved as history.
