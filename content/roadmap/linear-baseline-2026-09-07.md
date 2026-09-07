# Linear baseline · 7 September 2026

Status: dated read-only planning snapshot. Live project and issue records were read in this setup
session on 7 September 2026; this summary was assembled at 06:24 UTC (14:24 Asia/Manila).
No Linear records were changed. Re-read Linear before treating this snapshot as current.

## Source and scope

- [MageThemeEditor project](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098)
- Project ID: `1c14ca75-bc6f-4e7d-8e92-22804035a98d`; team: Solventech (SOL).
- [Research document](https://linear.app/solventech/document/magethemeeditor-research-and-architecture-baseline-953f16866313)
- Project details included all six milestones and its research resource.
- Issue listing included archived records, requested up to 100 items, returned **34 issues**,
  and reported `hasNextPage: false`. Range: SOL-489 through SOL-522, with no missing identifiers.
- The nine hybrid-adoption issues below were fetched individually for full descriptions because
  listing descriptions were truncated. Their acceptance criteria were inspected in full.
- This is a summary of planning metadata and selected descriptions, not a full issue/comment export.

Project status was **Planned**, with no start or target date. **1 issue was Done, 1 Todo,
and 32 Backlog.** SOL-489 records completed research; SOL-490 is merchant validation and remains
Todo. Implementation and runtime verification are outstanding.

## Milestones

| Milestone | Issue range | Recorded progress |
| --- | --- | --- |
| M1 — Product scope and architecture | SOL-489–493 | 20% |
| M2 — Magento integration proof | SOL-494–499 | 0% |
| M3 — Hosted editor and publishing | SOL-500–506 | 0% |
| M4 — Existing content and free theme | SOL-507–512 | 0% |
| M5 — Private beta readiness | SOL-513–518 | 0% |
| M6 — Ecosystem discovery after beta | SOL-519–522 | 0% |

Percentages are Linear's reported milestone progress, not an independent estimate of product
readiness. The [roadmap](index.md) explains intended outcomes and evidence.

## Issue inventory

Titles and statuses below are taken from the live issue listing.

| Issue | Title | Status | Milestone |
| --- | --- | --- | --- |
| [SOL-489](https://linear.app/solventech/issue/SOL-489/capture-the-research-and-architecture-baseline) | Capture the research and architecture baseline | Done | M1 |
| [SOL-490](https://linear.app/solventech/issue/SOL-490/validate-merchant-workflows-and-agency-demand) | Validate merchant workflows and agency demand | Todo | M1 |
| [SOL-491](https://linear.app/solventech/issue/SOL-491/define-mvp-scope-and-the-storefront-support-matrix) | Define MVP scope and the storefront support matrix | Backlog | M1 |
| [SOL-492](https://linear.app/solventech/issue/SOL-492/specify-versioned-content-component-and-publication-contracts) | Specify versioned content, component, and publication contracts | Backlog | M1 |
| [SOL-493](https://linear.app/solventech/issue/SOL-493/design-and-validate-the-editor-and-store-onboarding-workflow) | Design and validate the editor and store-onboarding workflow | Backlog | M1 |
| [SOL-494](https://linear.app/solventech/issue/SOL-494/create-reproducible-luma-and-hyva-integration-fixtures) | Create reproducible Luma and Hyvä integration fixtures | Backlog | M2 |
| [SOL-495](https://linear.app/solventech/issue/SOL-495/implement-the-generic-magento-connector-and-secure-store-handshake) | Implement the generic Magento connector and secure store handshake | Backlog | M2 |
| [SOL-496](https://linear.app/solventech/issue/SOL-496/implement-the-local-json-renderer-and-registered-editable-regions) | Implement the local JSON renderer and registered editable regions | Backlog | M2 |
| [SOL-497](https://linear.app/solventech/issue/SOL-497/implement-the-hyva-adapter-for-the-integration-proof) | Implement the Hyvä adapter for the integration proof | Backlog | M2 |
| [SOL-498](https://linear.app/solventech/issue/SOL-498/implement-the-luma-adapter-for-the-integration-proof) | Implement the Luma adapter for the integration proof | Backlog | M2 |
| [SOL-499](https://linear.app/solventech/issue/SOL-499/prove-edit-preview-publish-rollback-and-offline-storefront-operation) | Prove edit, preview, publish, rollback, and offline storefront operation | Backlog | M2 |
| [SOL-500](https://linear.app/solventech/issue/SOL-500/build-the-hosted-application-tenancy-and-store-permissions) | Build the hosted application, tenancy, and store permissions | Backlog | M3 |
| [SOL-501](https://linear.app/solventech/issue/SOL-501/build-the-section-editor-and-schema-driven-settings-panels) | Build the section editor and schema-driven settings panels | Backlog | M3 |
| [SOL-502](https://linear.app/solventech/issue/SOL-502/build-authenticated-storefront-preview-and-selection-synchronization) | Build authenticated storefront preview and selection synchronization | Backlog | M3 |
| [SOL-503](https://linear.app/solventech/issue/SOL-503/implement-draft-persistence-and-store-view-inheritance) | Implement draft persistence and store-view inheritance | Backlog | M3 |
| [SOL-504](https://linear.app/solventech/issue/SOL-504/implement-versioned-media-and-asset-delivery-with-a-local-mirror) | Implement versioned media and asset delivery with a local mirror | Backlog | M3 |
| [SOL-505](https://linear.app/solventech/issue/SOL-505/build-the-validated-publication-and-scheduling-pipeline) | Build the validated publication and scheduling pipeline | Backlog | M3 |
| [SOL-506](https://linear.app/solventech/issue/SOL-506/add-release-history-restoration-and-publication-audit-trails) | Add release history, restoration, and publication audit trails | Backlog | M3 |
| [SOL-507](https://linear.app/solventech/issue/SOL-507/inventory-existing-themes-content-and-editable-capabilities) | Inventory existing themes, content, and editable capabilities | Backlog | M4 |
| [SOL-508](https://linear.app/solventech/issue/SOL-508/expose-cms-blocks-and-supported-magento-widgets-as-components) | Expose CMS blocks and supported Magento widgets as components | Backlog | M4 |
| [SOL-509](https://linear.app/solventech/issue/SOL-509/convert-supported-page-builder-content-with-a-restoration-path) | Convert supported Page Builder content with a restoration path | Backlog | M4 |
| [SOL-510](https://linear.app/solventech/issue/SOL-510/document-and-implement-the-adapter-sdk-for-hardcoded-theme-regions) | Document and implement the adapter SDK for hardcoded theme regions | Backlog | M4 |
| [SOL-511](https://linear.app/solventech/issue/SOL-511/build-the-free-compatible-reference-theme) | Build the free compatible reference theme | Backlog | M4 |
| [SOL-512](https://linear.app/solventech/issue/SOL-512/ship-the-initial-section-library-and-native-review-presentation) | Ship the initial section library and native review presentation | Backlog | M4 |
| [SOL-513](https://linear.app/solventech/issue/SOL-513/verify-commerce-cache-isolation-csp-accessibility-and-performance) | Verify commerce, cache isolation, CSP, accessibility, and performance | Backlog | M5 |
| [SOL-514](https://linear.app/solventech/issue/SOL-514/verify-publication-recovery-and-saascdn-outage-behavior) | Verify publication recovery and SaaS/CDN outage behavior | Backlog | M5 |
| [SOL-515](https://linear.app/solventech/issue/SOL-515/package-installation-upgrades-diagnostics-and-uninstall-behavior) | Package installation, upgrades, diagnostics, and uninstall behavior | Backlog | M5 |
| [SOL-516](https://linear.app/solventech/issue/SOL-516/prepare-hosted-beta-environments-and-operational-monitoring) | Prepare hosted beta environments and operational monitoring | Backlog | M5 |
| [SOL-517](https://linear.app/solventech/issue/SOL-517/define-pricing-licensing-data-ownership-and-subscription-behavior) | Define pricing, licensing, data ownership, and subscription behavior | Backlog | M5 |
| [SOL-518](https://linear.app/solventech/issue/SOL-518/run-the-private-beta-and-measure-merchant-task-completion) | Run the private beta and measure merchant task completion | Backlog | M5 |
| [SOL-519](https://linear.app/solventech/issue/SOL-519/evaluate-a-free-store-locator-module-and-editable-location-sections) | Evaluate a free store-locator module and editable location sections | Backlog | M6 |
| [SOL-520](https://linear.app/solventech/issue/SOL-520/design-the-future-app-block-and-capability-extension-model) | Design the future app-block and capability extension model | Backlog | M6 |
| [SOL-521](https://linear.app/solventech/issue/SOL-521/evaluate-liquid-authoring-and-a-future-hosted-storefront-renderer) | Evaluate Liquid authoring and a future hosted storefront renderer | Backlog | M6 |
| [SOL-522](https://linear.app/solventech/issue/SOL-522/evaluate-assisted-editing-using-the-component-schema) | Evaluate assisted editing using the component schema | Backlog | M6 |

## Hybrid adoption coverage gap

The user's confirmed direction permits keeping the active theme while opting in selected
home/CMS, PDP, category, or registered-region surfaces. The live issues partially cover this.
SOL-509 is especially explicit about per-page opt-in, original retention, restoration, and avoiding
duplicate renderer output. The audit must not erase that existing coverage.

However, the complete routing and isolation contract is not yet explicit across these issues.
This task adds [local acceptance criteria](../requirements/hybrid-adoption.md#acceptance-criteria);
it does **not** fix or synchronize the Linear gap.

| Issue | Existing coverage | Detail still to record or make explicit | Local criteria |
| --- | --- | --- | --- |
| [SOL-491](https://linear.app/solventech/issue/SOL-491/define-mvp-scope-and-the-storefront-support-matrix) | Content/support categories and surface boundaries | Explicit partial-adoption promise and untouched-surface scope | HYB-01–03, 10–11 |
| [SOL-492](https://linear.app/solventech/issue/SOL-492/specify-versioned-content-component-and-publication-contracts) | Assignments, versions, inheritance, release activation/rollback | Routing identity, overlap handling, independent activation/restoration contract | HYB-03, 05–07 |
| [SOL-493](https://linear.app/solventech/issue/SOL-493/design-and-validate-the-editor-and-store-onboarding-workflow) | Choose store view/page, editable areas, preview/publish/restore | Visible renderer selection and page/region opt-in or restore controls | HYB-02–04, 07 |
| [SOL-496](https://linear.app/solventech/issue/SOL-496/implement-the-local-json-renderer-and-registered-editable-regions) | Registry, local state, registered regions, preserved unsupported output | Deterministic routing and single renderer ownership for each opted-in surface | HYB-01–03, 11 |
| [SOL-503](https://linear.app/solventech/issue/SOL-503/implement-draft-persistence-and-store-view-inheritance) | Scoped page/template drafts and inheritance | Assignment inheritance/conflicts and independent publication state | HYB-03–05, 09 |
| [SOL-509](https://linear.app/solventech/issue/SOL-509/convert-supported-page-builder-content-with-a-restoration-path) | Original retention, per-page opt-in/restoration, no double output | PDP/category/region breadth and independent routing/content restoration beyond conversion | HYB-02, 05–07 |
| [SOL-510](https://linear.app/solventech/issue/SOL-510/document-and-implement-the-adapter-sdk-for-hardcoded-theme-regions) | Region SDK, controlled settings, preserving unrelated template behavior | Scoped style/script lifecycle and explicit untouched-region regression evidence | HYB-08, 10–11 |
| [SOL-511](https://linear.app/solventech/issue/SOL-511/build-the-free-compatible-reference-theme) | Free theme controls and preserved commerce | Compatibility of theme adoption with selected-surface adoption on an existing theme | HYB-01–03, 10 |
| [SOL-513](https://linear.app/solventech/issue/SOL-513/verify-commerce-cache-isolation-csp-accessibility-and-performance) | Page-type support matrix, cache/CSP/accessibility/commerce checks | Named untouched page/header/footer/cart/checkout checks after publish and restore | HYB-04–05, 07–10, 12 |

A future authorized planning update should reconcile these local criteria with current issue
descriptions, assign clear ownership, and avoid duplicating existing work. Independent
publication/restoration and outage behavior also need to be carried into their delivery issues;
this nine-issue audit does not claim to be an exhaustive audit of every issue's acceptance text.

## Evidence limits

This snapshot verifies issue existence, metadata, milestone grouping, and the selected acceptance
text. It does not prove merchant interviews, implementation, runtime tests, publishing, or a
closed planning gap. No issue status was inferred from the existence of documentation.
