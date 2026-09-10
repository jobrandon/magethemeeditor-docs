# Content, assignment and publication contract

Status: **v1 local executable prototype, not a released API or Magento integration**.
Date: 2026-09-07. [ADR 0002](../decisions/0002-portable-contract.md) explains the routine choices;
[Batch 01 evidence](../roadmap/batch-01-evidence-2026-09-07.md) records actual checks and limits.

## Source and responsibility

Authoritative executable files are `product/contracts/v1/*.schema.json` and
`product/src/contract.mjs` in the sibling product workspace. This page specifies behavior beyond
single-document schema validation. The CLI validates one document; the activation model also
validates signature, capabilities, all referenced bytes, current revisions and original snapshots.
Neither executes Magento. The contract uses
[JSON Schema 2020-12](https://json-schema.org/draft/2020-12), independent of any editor engine.

| Artifact | Required identity and role |
| --- | --- |
| Content | Contract version, document ID/revision, draft/published state, scope, bounded tokens, ordered sections; optional immutable source provenance |
| Component | Stable section ID, semantic type, exact component version and bounded settings |
| Assignment | Stable assignment ID/revision, exact store ID and target, selected mode, release ID, original snapshot; editor mode adds exact renderer and content reference |
| Capabilities | Trusted installation/store identity, exact contract versions, runtime version, registered renderers/components/targets, asset modes and resolvable fixture commerce references |
| Release | Immutable release ID for one installation/store, minimum runtime, delivery mode, bounded changes with expected revisions, exact document digests and assets |
| Signature | Contract version, Ed25519 algorithm, trusted key ID, manifest SHA-256 and detached signature |

Contract version is exactly `1.0.0`; `v1` in paths groups this initial major. No implicit acceptance
of unknown fields, versions or components occurs. Namespace IDs use lowercase ASCII letters,
digits, hyphens and underscores, beginning with a letter, at most 64 characters. IDs are stable
opaque connector mappings, not merchant URLs, display labels, SKUs or raw Magento numeric IDs.
Production generators must avoid collisions and preserve mappings across exports/restores.
The fixture's `luma@1.0.0`/`hyva@1.0.0` identify hypothetical adapter protocol versions, not actual
Magento/Hyvä package versions or a support claim.

## Content and limits

Array order is render order; reordering retains section IDs. Duplicate section IDs fail.
Settings are complete typed values, not arbitrary HTML or engine metadata. Hero text is plain
text and must be escaped by a renderer even if it contains markup characters. `product-grid`
contains product IDs and columns only. CMS blocks/widgets are references to registered native
behavior; their inner arbitrary markup is not structurally editable.

| Bound | v1 value |
| --- | --- |
| Wire document | 1 MiB UTF-8; 32 nesting levels; duplicate object keys and malformed Unicode rejected |
| Sections | 0–100; hero heading 1–160 characters, body up to 2,000 |
| Product grid | 1–24 distinct product references; 1–4 columns |
| Tokens | Hex accent color and compact/comfortable/spacious spacing; scoped to the assigned wrapper |
| Revisions | Integer 1–2,147,483,647; no skipped revisions on draft save or assignment transition |
| Release | 1–100 changes, at most 100 referenced content documents and 200 assets |
| Assets | PNG/JPEG/WebP declared types; 10 MiB each, 50 MiB total; exact bytes and SHA-256 |
| Capability fixture | At most 1,000 explicit targets and 1,000 IDs per commerce reference category |

The capability ID arrays are a bounded local fixture abstraction, not a mandate to export an entire
catalog in a production handshake. The connector needs an authenticated scoped reference-resolution
API and opaque capability generation/expiry before integration. No prices, stock, tax, customer
groups or session values are copied into a design release. Magento resolves live commerce data at
request time and contributes proper cache/private-content behavior. Missing/deleted references at
render time require a safe native omission/error presentation, not a stale copied price or broken
commerce control; the exact adapter behavior remains a runtime hypothesis.

## Draft, inheritance and preview

A draft uses `scope.kind = default` or an exact store scope. `saveDraft` compares the current
revision and stable document/scope identity. It returns a new draft only; published assignments
are a different store of state. A stale save receives `REVISION_CONFLICT`, never silently overwrites.
Retain both revisions for a user-visible comparison in the future UI.

A publisher resolves default inheritance before release assembly. Start from one immutable
default source revision, apply explicit store overrides by stable section ID or whole token value,
then write a complete store document with `inheritedFrom` identifying its source digest/revision.
Reset removes the override and re-materializes from the deliberately selected source revision.
Section deletions/order are explicit edits to the resulting full array. No implicit deep merge,
cycle, self-reference or propagation from later default edits is allowed. The batch rejects
published default scopes and self-inheritance; the full override resolver and provenance-chain
validation are specified here but remain SOL-503 implementation work.

Preview must select an authenticated tenant/store/draft revision and use the same native Magento
renderer as publication. Preview responses bypass shared public caches; private customer context
cannot enter a public release. Anonymous requests see only activated documents. The JSON state
separation test does not prove sessions, iframe messages, authentication or cache isolation.

## Assignment ownership and precedence

The target tuple is `(pageType, entityId, surface, regionId?)` inside an exact store. Page types
are home, CMS, PDP and category; `surface` is content or region. Regions require a registry ID.
The capability provider must certify that this tuple maps to a supported local renderer boundary.
Unassigned targets retain the existing renderer. Installation alone creates no assignments.

One stable assignment owns each exact store/target even after restoration. An active content
assignment and any active region assignment for the same entity conflict and fail publication.
Distinct declared regions can coexist; duplicate owners and ambiguous overlap fail. There are no
wildcard, website-wide or global assignment rules in v1. Inherited intent must first become a
visible exact-store assignment. The UI must show source inheritance, effective scope, renderer,
affected targets and unsupported capabilities before preview/publish.

Content ownership excludes the shared header/footer and native commerce surfaces. Adapter CSS,
tokens, scripts, initialization and teardown must stay within the registered wrapper. The
reference model cannot prove those DOM/runtime boundaries. PDP/category targets remain future
rollout capabilities, while home/CMS is the first [MVP scope](../requirements/mvp-support-matrix.md).

## Immutable release and activation protocol

1. Authenticate the requested operation and authorize tenant/store/target access in the private
   service. Resolve inheritance, validate settings/references and assign new published revisions.
2. Assemble the exact UTF-8 manifest bytes and complete immutable asset/document set. Sign
   `MageThemeEditor/release/1.0.0\n` + key ID + `\n` + those bytes using Ed25519. The detached
   envelope includes SHA-256 of the same bytes. Do not parse/reserialize bytes in transport.
3. The connector stages without changing live routing. It verifies the envelope against its
   locally trusted active key, installation/store binding, contract/runtime compatibility, exact
   renderer/component/target capabilities, every document and asset hash/length and references.
4. Verify locally retained original content and renderer metadata hashes and scope. Compare every
   assignment's expected revision (`null` for new; current revision otherwise). Require next
   revision = expected + 1. Identity and original provenance cannot change under an existing ID.
5. Validate the entire resulting assignment set, including unchanged targets. Publish all changes
   atomically, persist the idempotency receipt with that transaction and retain old documents/assets.
   Invalidate only affected scopes while respecting Magento context and dependencies.
6. Return an acknowledgement with installation/store/release/digest, affected targets and durable
   activation state. Verify the actual storefront separately before exposing a verified-live state.

The implemented `activate` is a pure in-memory reference for steps 3–5. Its receipt is explicitly
`model-activated`; it is not the production acknowledgement API. Authorization, transfer, durable
transaction, cache invalidation and live verification are absent. Production acknowledgement must
distinguish accepted, staged, activated, failed and verified-live; a queued job cannot report live.

Release IDs are unique inside installation/store scope. Retrying identical bytes returns the same
receipt without switching again, including after a later release; different bytes under that ID
fail. Published document ID/revision pairs retain an immutable digest. Disjoint target changes can
proceed independently; conflicting changes return current revision information through an
authorized error response. Retry transient transfer errors with bounded backoff and the same
immutable bytes/ID. Validation, signature or revision errors require correction/new intent, not
infinite retry. The service scheduler and durable receipts remain SOL-505 work.

## Restoration, keys and failure

Restore is a new signed release with a new assignment revision. Select retained compatible editor
documents and their complete assets, or `mode = original` with retained original content and
renderer/routing metadata. A restoration of A must leave B exactly unchanged. If the original
adapter/theme is no longer compatible, reject the restore while retaining the last working state;
do not route a partial content snapshot through guessed metadata. Uninstall/disable recovery needs
a tested explicit policy before the connector ships.

Trust is connector-local and bound to installation authorization, never supplied by a manifest.
Key rotation first provisions the new public key through an authenticated administration channel,
then overlaps acceptance while in-flight releases finish; future releases use the new key. Revoked
or unknown keys cannot activate. Previously active publications continue serving locally without
needing to recontact SaaS. Restore old content through a newly authorized release when its old
signing key is retired. Provisioning, overlap deadlines, revocation propagation and emergency
recovery require security design and PHP parity tests; ephemeral test keys prove no operational
key management.

`ContractError` provides a stable code and path. Wire/schema failures include `JSON_SYNTAX`,
`DUPLICATE_KEY`, `JSON_LIMIT` and `SCHEMA`; publication failures distinguish signature/integrity,
scope, capability, overlap and revision errors. Never echo secret documents or credentials in errors.
Any preflight failure leaves the supplied model state unchanged. Real crashes between stage,
transaction, cache effects and acknowledgement must be tested on the Magento fixture.

## Asset delivery guarantees and limits

Assets have immutable IDs/digests, lengths and MIME declarations; no arbitrary download URL or
filesystem path is accepted. A future connector derives locations from a configured trusted origin
and digest path, forbids path traversal/redirect-based SSRF, and validates actual media bytes before
staging. The current prototype tests byte integrity only, using opaque original test bytes; it does
not decode images or establish that a MIME claim is safe.

Local mode must retain all required assets, documents, original snapshots and installed renderer
dependencies in durable merchant-local storage outside disposable Magento static build output.
Activation cannot depend on a warm cache. After staging, loss of SaaS and vendor CDN must preserve
the last valid local publication on cold cache. Garbage collection must retain active and supported
restore generations and respect in-flight work. This guarantee remains unproved until outage tests.

CDN mode still verifies bytes during staging but public asset reads have a separate external CDN
availability dependency. It makes no local cold-cache outage promise. No provider is selected.
The connector must expose the distinction to merchants before publication. A CDN URL, public 200,
hash-only check or model transition does not prove origin health or a live storefront.

## Review corrections · 2026-09-07

This amendment follows the 08:17–08:22 UTC independent review and supersedes any broader
interpretation of numeric acceptance or immutable asset identity above. The format remains an
unreleased `1.0.0` prototype. These intentional acceptance changes are recorded before Batch 02;
they do not claim a released-client migration or Magento verification. See the
[review and correction evidence](../roadmap/batch-01-evidence-2026-09-07.md#independent-review-and-focused-corrections).

### Immutable asset bindings

An asset ID is immutable **within one installation, across its store views and releases**.
Its binding is `(SHA-256, byte length, MIME declaration)`. The model retains this tuple under
`installationId/assetId` in `state.assetBindings`. Identical reuse is allowed. Changing any member
requires a new asset ID and a new published content revision that references that ID;
otherwise activation fails with `IMMUTABLE_ASSET`, even when the retained content hash is unchanged.
Each installation owns its model state; this is not a multi-tenant persistence implementation.

Bindings survive omission from later manifests, restoration to the original renderer and restoration
of a retained editor document. A release still carries all assets needed by its changed documents.
An unchanged assignment keeps its retained document/assets; publishing or restoring A does not
rebind B's image. New bindings are committed only with a successful whole transition. Failure,
including a late revision conflict, leaves assignments, receipts, document digests and asset
bindings unchanged. The model does not garbage-collect identity history.

A nonempty pre-correction model state without `assetBindings` is rejected for new activation with
`ASSET_HISTORY_REQUIRED`. Reset disposable fixtures or rebuild complete identity history from
verified retained manifests before resuming; do not silently assume an empty map. Historical
idempotent receipt replay does not activate anything. No persistent-state migration is implemented.
The MIME declaration is immutable metadata, not proof that the bytes decode as that image type.

### Lossless integer wire policy

All current numeric fields are integers. Raw JSON numeric tokens must use canonical base-10
integer spelling: `0`, a nonzero unsigned integer, or a minus sign followed by a nonzero integer.
Magnitude must be at most `9007199254740991`; field schemas impose their smaller bounds afterward.
The decoder checks spelling and compares digit strings before parsing numbers, so rounding cannot
turn an invalid setting, revision, expected revision or asset length into a valid integer.

| Wire token | Result |
| --- | --- |
| `4` | Exact integer; accepted when the field allows 4 |
| `4.0000000000000001` | `NUMBER_FORMAT`, never rounded to 4 |
| `1.0`, `1e0`, `1E+0`, `10e-1` | `NUMBER_FORMAT`, even though some represent integral mathematical values |
| `-0`, `01` | `NUMBER_FORMAT`; noncanonical representations are rejected |
| `9007199254740991`, `-9007199254740991` | Lossless parser limits; still subject to the document field schema |
| `9007199254740992`, `-9007199254740992` | `NUMBER_RANGE` |
| `"1.0"`, `"1e999"` | Ordinary strings; their containing field must allow text |

Decimal fractions and exponents are unsupported in this version. This deliberately tightens the
previous prototype, which accepted some decimals/exponents after conversion to a JavaScript
Number. Use plain integer serialization; do not round non-integral input. Any future fractional
field needs a new explicit exact representation/policy decision. No general JSON canonicalization
or new dependency is introduced. `validate` checks already materialized values and cannot recover
precision lost by a caller's parser; all wire input must go through `decode`/`parseJson` first.
JSON Schema alone does not enforce numeric token spelling.

### Public validator kinds

The only public kinds for `validate`, `decode` and the CLI are `component`, `content`, `assignment`,
`capabilities`, `release` and `signature`. `common` is internal schema-definition storage. It and
unknown kinds or schema-fragment names fail with `UNKNOWN_KIND`; no arbitrary registered schema
can report public validation success. `decode` rejects the kind before reading its JSON shape.
