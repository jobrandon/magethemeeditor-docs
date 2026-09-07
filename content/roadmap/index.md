# Delivery roadmap

Status: planned delivery, not a dated release commitment. Baseline: 7 September 2026.
The [Linear snapshot](linear-baseline-2026-09-07.md) records 34 issues in six milestones.
The live project was Planned with no start or target date at inspection.

| Milestone | Intended outcome | Evidence required to progress |
| --- | --- | --- |
| M1 · Product scope and architecture | Validated user outcome, support matrix, content/UX contracts | Research baseline plus customer validation and explicit compatibility choices |
| M2 · Magento integration proof | Luma/Hyvä fixtures, connector, renderer/adapters, end-to-end proof | Edit, preview, publish, restore, and local-mode shopping during SaaS outage |
| M3 · Hosted editor and publishing | Tenancy, editor, scoped drafts/preview, assets, publication/history | Merchant flow through acknowledged, recoverable publication |
| M4 · Existing content and free theme | Inventory, CMS/widgets, supported migration, adapter SDK, theme/library | Preserved originals, deliberate adoption, and supported reference-theme behavior |
| M5 · Private beta readiness | Commerce/security/recovery proof, packaging, operations, policy, pilot | Support matrix, operational runbooks, merchant measurements, go/no-go decision |
| M6 · Ecosystem discovery after beta | Locator, app blocks, template/headless options, assisted editing | Customer pull and bounded compatibility/support cost for each expansion |

Research capture is the sole Done issue in this baseline. Merchant validation is Todo; 32 issues
are Backlog. Milestones and issue creation are planning evidence, not delivery evidence.

## Immediate planning follow-through

Merchant discovery and an explicit support matrix should inform the integration proof. Carry
[hybrid adoption](../requirements/hybrid-adoption.md) through scope, schema/UX, local rendering,
publication/restoration, migration, adapters, and regression work. The detailed routing/isolation
criteria still need authorized issue updates; this setup does not synchronize them.

Use the [decision register](../decisions/index.md) for open architecture choices and the
[validation plan](../requirements/validation-plan.md) for proof requirements. Set dates and
estimates after scope and the first integration results.
