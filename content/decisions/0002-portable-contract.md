# ADR 0002: Portable contract and explicit scoped activation

Status: **accepted for the Batch 01 local prototype; Magento realization remains unverified**.
Date: 2026-09-07. Owner: execution task `01a07ad8-3911-78d1-b5a4-28ba37eba5d7`, GPT-6 Astra.
Issues: [SOL-491](https://linear.app/solventech/issue/SOL-491) and
[SOL-492](https://linear.app/solventech/issue/SOL-492). Supersedes no historical research file.

## Context

Hybrid adoption requires an explicit switch for selected content surfaces while keeping the
merchant's active theme and native commerce. An editor library's internal tree would make native
rendering and future tooling depend on that library. Whole-store releases would unnecessarily
couple two independent page edits. Implicit page/region priority could hide one owner's output.

## Decision

Use JSON Schema 2020-12 with exact contract version `1.0.0`, stable opaque IDs and ordered section
arrays. Schemas are original product source under `product/contracts/v1/`, with a separate semantic
validator. The standard supports reusable references and validation vocabularies; Ajv provides its
2020-12 implementation. [JSON Schema 2020-12](https://json-schema.org/draft/2020-12),
[Ajv schema support](https://ajv.js.org/json-schema.html)

The content vocabulary contains semantic hero, product-grid, CMS-block reference and registered
widget reference settings. It cannot carry arbitrary scripts, template paths, CSS, catalog prices,
customer data or editor engine state. Versioned native Luma/Hyvä renderers own escaped output,
commerce resolution and lifecycle. Those renderers are not implemented in this batch.

Assignments identify an exact store and connector-mapped entity plus content surface or registered
region. No URL routing, wildcards or global inheritance take effect implicitly. Page content and
any region on that same entity cannot both have active editor ownership in v1. Two distinct
declared regions can coexist. This conservative rejection avoids guessed nesting rules; a later
adapter contract can add a proven containment model through an explicit contract change.

Default-scope documents are reusable draft sources. A publisher materializes a complete store
document with provenance before activation. Store overrides replace complete sections/token values;
there is no runtime deep-merge or live default propagation. Every published assignment stays bound
to exact immutable document bytes until the merchant explicitly republishes that target.

Use per-assignment optimistic revision checks, including a null expectation for first activation.
A bounded change set switches its routing/content references together or rejects all changes.
Untouched assignments remain unchanged. Original content and renderer metadata are retained before
activation; restore is a new revision selecting an earlier compatible editor document or the
preserved original, not a destructive overwrite of history.

Sign exact UTF-8 manifest bytes with a detached Ed25519 envelope, a protocol-specific prefix and
key ID. Hash documents/assets with SHA-256. This avoids inventing cross-language JSON
canonicalization and forces transport to preserve bytes. Node's existing crypto API implements the
local signature experiment; PHP verification and key lifecycle integration remain to be proved.
[Node 22.22.0 crypto API](https://nodejs.org/download/release/v22.22.0/docs/api/crypto.html)

## Dependency decision

Adopt Ajv **8.17.1** with four pinned transitive runtime packages solely for local contract
development. The complete reviewed inventory and original MIT/BSD notices are in
`product/third-party/`; no UI dependency, hosted provider or Magento package is selected.
Node 22.22.0/npm 10.9.4 are existing local tools. The review covers this use, not a browser bundle,
distributed toolchain or commercial release. See the
[third-party requirements](../requirements/third-party-compliance.md) and
[Batch 01 evidence](../roadmap/batch-01-evidence-2026-09-07.md#dependency-evidence).

## Consequences and unresolved proof

The exact-version handshake deliberately rejects unsupported versions rather than guessing.
Migration must produce a new validated document and revision while preserving the source.
Component schemas are compiled from trusted product files; the editor cannot upload executable
schemas. The initial IDs and limits can be revised through explicit versioned migration evidence.

The pure transition model demonstrates algorithmic rejection and isolation, not database atomicity,
distributed activation, cache invalidation or durable availability. The connector must implement a
transaction or equivalent coherent local snapshot, then prove crash/concurrency behavior. Asset
hash verification does not establish media safety; image decoding, MIME validation, limits and
sanitization remain service/runtime work. Original PHP/extension restoration compatibility must be
checked against the actual installed theme, never assumed from a stored hash.

Unresolved hypotheses: entity mapping across store views, original renderer snapshot representation,
Page Builder coexistence, PHP signature parity, multi-node activation, cache tags/private content,
native image validation and CSS/JS lifecycle on Luma and Hyvä. The
[contract](../architecture/content-contract.md) and [fixture plan](../architecture/integration-fixtures.md)
name the required evidence. No UI demonstration can validate Magento behavior.

## Amendment after independent review · 2026-09-07

The independent reviewer found three local prototype defects after the original 45-test result:
asset IDs could be rebound despite immutable content, numeric rounding could hide non-integral
values, and the internal definitions schema could be selected as a public validator kind.
The implementer reproduced all three failures before making the following corrections.

- Bind asset IDs across an installation's store views/releases to an immutable digest, byte
  length and MIME declaration. Retain identity history on successful transitions and original/editor
  restore; identical reuse remains valid. Changed bytes/metadata require a new ID and content
  revision. Nonempty older model state without that history requires reset or verified reconstruction.
- Require canonical base-10 integer wire tokens within the safe integer range before JSON number
  parsing. Reject fractions, exponents and negative zero, including integral forms such as `1.0`
  and `1e0`. This intentionally narrows previously accepted serializations; schemas still impose
  field bounds, and external bytes must enter through the decoder, not a lossy caller parser.
- Allow exactly the six advertised public document kinds. Keep `common` available only for trusted
  schema references, rejecting it at public entry points with `UNKNOWN_KIND`.

These are corrections to the unreleased `1.0.0` prototype, not a silent guarantee that earlier
accepted payloads remain valid. Existing canonical fixtures require no change; no persisted product
deployment exists to migrate. The [contract amendment](../architecture/content-contract.md#review-corrections-2026-09-07)
defines exact scope, errors and serialization examples. Package adoption, notices, schemas and
hosting/Magento scope remain unchanged. Local regression/repro results belong to the
[later evidence record](../roadmap/batch-01-evidence-2026-09-07.md#independent-review-and-focused-corrections);
the implementer does not claim the independent recheck has occurred.
