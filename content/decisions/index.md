# Decision register

Updated: 11 September 2026 for Liquid developer theme authoring; other rows retain their stated evidence dates.
A direction can be confirmed without having a verified implementation.
The original [research](../architecture/theme-editor-research-2026-09-07.md) remains a dated
recommendation; the user's later instructions confirm the directions below.

| Topic | Status | Basis / next step |
| --- | --- | --- |
| Full-page default theme and shared menus | Required by user, first native local boundary implemented 2026-09-08 | [Full-theme contract](../architecture/full-page-theme.md); historical CMS-region shell is insufficient; broader catalog/commerce acceptance open |
| Alpine CSP for shopper-facing default theme | Selected by user 2026-09-08 | Reviewed @alpinejs/csp 3.17.2 local runtime; independent of RequireJS/Luma JS; React editor remains; Hyvä compatibility unproven |
| Third-party rights before adoption and commercialization | Required by the user | [Adoption and release requirements](../requirements/third-party-compliance.md); exact-use reviews and evidence required; no final product dependency clearance yet |
| Independently owned documentation | Accepted and locally set up | [ADR 0001](0001-independent-documentation.md) |
| Hosted editor with private publishing services and generic Magento connector/runtime | Confirmed product direction | [System boundaries](../architecture/system-boundaries.md); one local Luma hero observed in Batch 03A, full connector/integration criteria open |
| Magento retains commerce behavior; versioned JSON and Luma/Hyvä adapters | Confirmed product direction | [Initial contract prototype](../architecture/content-contract.md); full support versions/adapters unverified; [bounded Luma evidence](../roadmap/batch-03a-evidence-2026-09-07.md) |
| Keep active theme; opt in selected pages or regions | Confirmed product direction | [Hybrid acceptance criteria](../requirements/hybrid-adoption.md); [Linear synchronization verified](../roadmap/batch-01-evidence-2026-09-07.md#linear-synchronization); runtime criteria remain open |
| Free compatible reference theme | Recommended complete editing path | Foundation, distribution licenses, and exact support matrix still need a decision |
| Liquid developer theme authoring | Selected by the user 2026-09-11; PHP SDK and first editor adapter implemented; bounded native commerce evidence, broader parity and production acceptance open | [ADR 0004](0004-developer-theme-authoring.md): readable installable theme packages; SOL-521 active in M1; [SDK implementation](../architecture/liquid-theme-sdk.md) runs alongside editor recovery with separate ownership; native validation and comparison remain open |
| Third-party themes and marketplace | Confirmed future direction; separate planning project created | [Future ecosystem roadmap and project artifacts](../roadmap/theme-ecosystem.md#planning-status); documents and plans only, no issues or milestones; implementation and commercial terms unselected |
| Custom React for the local editor concept | Accepted for Batch 02 only; reversible | [ADR 0003](0003-local-editor-choice.md); portable round-trip and local UI evidence, no Magento proof |
| Developer-authored section packages | Confirmed product requirement; local proof implemented 2026-09-08 | [Trusted authoring contract](../architecture/developer-packages.md): original five-section package, independent author example and one separate local native notice; general SDK/native adapters remain open |
| Custom-module data integration | Future proposal only | [Typed provider and visual binding proposal](../roadmap/custom-module-data-integration.md); no current contract/UI/runtime work |
| React/TypeScript, API/worker, PostgreSQL, object storage | Research recommendation | Pin versions and validate during the technical spike |
| CMS identity and separate MTE publication storage | Proposed production architecture, documented at the user's request 2026-09-10 | [CMS delivery proposal](../architecture/cms-page-delivery.md): preserve native CMS identity/content; add store-scoped assignments and durable published JSON; general connector implementation remains open |
| CDN versus local asset mirror | Proposed store-hosted default with optional CDN delivery | [Availability and publication contract](../architecture/cms-page-delivery.md#publish-restore-and-availability); storage/hosting selection and cold-cache outage guarantees remain unverified |
| Assignment precedence and atomic restore semantics | Accepted for local prototype; runtime proof pending | [ADR 0002](0002-portable-contract.md): explicit store targets, overlap rejection, per-assignment revisions and coherent restore |
| Subscription expiry/data export policy | Proposed | Validate commercial policy while preserving merchant content and last local publication |
| Documentation source remote and branch | Authorized | [jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs), `main`; follow the [commit conventions](../contributing/authoring.md#commit-conventions) |
| Separate docs host, domain, access policy | Unconfigured | Follow the [publishing preparation](../contributing/publishing.md) when authorized |

Add a numbered decision record when a meaningful choice is made. Include status, date, context,
decision, consequences, evidence, and superseded records. Do not label a proposal accepted merely
because it appears in research or an issue title.
