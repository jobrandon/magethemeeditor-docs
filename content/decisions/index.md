# Decision register

Updated: 7 September 2026. A direction can be confirmed without having a verified implementation.
The original [research](../architecture/theme-editor-research-2026-09-07.md) remains a dated
recommendation; the user's later instructions confirm the directions below.

| Topic | Status | Basis / next step |
| --- | --- | --- |
| Independently owned documentation | Accepted and locally set up | [ADR 0001](0001-independent-documentation.md) |
| Hosted editor with private publishing services and generic Magento connector/runtime | Confirmed product direction | [System boundaries](../architecture/system-boundaries.md); integration proof outstanding |
| Magento retains commerce behavior; versioned JSON and Luma/Hyvä adapters | Confirmed product direction | Final schema, support versions, and runtime behavior unverified |
| Keep active theme; opt in selected pages or regions | Confirmed product direction | [Hybrid acceptance criteria](../requirements/hybrid-adoption.md); detailed Linear synchronization outstanding |
| Free compatible reference theme | Recommended complete editing path | Foundation, distribution licenses, and exact support matrix still need a decision |
| Liquid or another general template engine | Optional future exploration | Not required for initial JSON/template architecture; no engine selected |
| React/TypeScript, API/worker, PostgreSQL, object storage | Research recommendation | Pin versions and validate during the technical spike |
| CDN versus local asset mirror | Research recommendation to support both | Document independent outage guarantees and prove cold-cache behavior |
| Assignment precedence and atomic restore semantics | Open design detail | Implement the observable hybrid requirements; resolve overlap and concurrency before publication |
| Subscription expiry/data export policy | Proposed | Validate commercial policy while preserving merchant content and last local publication |
| Documentation source remote and branch | Authorized | [jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs), `main`; follow the [commit conventions](../contributing/authoring.md#commit-conventions) |
| Separate docs host, domain, access policy | Unconfigured | Follow the [publishing preparation](../contributing/publishing.md) when authorized |

Add a numbered decision record when a meaningful choice is made. Include status, date, context,
decision, consequences, evidence, and superseded records. Do not label a proposal accepted merely
because it appears in research or an issue title.
