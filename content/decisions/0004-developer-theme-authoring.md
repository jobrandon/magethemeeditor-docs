# ADR 0004: Liquid theme authoring and Magento validation

Date: 11 September 2026.
Status: Liquid is the user-selected developer theme authoring direction. The user subsequently authorized completing implementation. The standalone SDK now uses reviewed keepsuit/liquid 0.12.0 in PHP; the first local editor adapter is accepted and native configurable cart/shipping handoff has bounded evidence; full theme/editor parity, complete dialect support and production acceptance remain open. See the [SDK implementation record](../architecture/liquid-theme-sdk.md).

## Decision

MageThemeEditor must support independently authored, readable and installable developer themes. A developer must be able to create original layouts, sections, blocks and snippets; modify HTML, CSS and JavaScript; add reviewed third-party scripts such as Mixpanel; and package a theme without editing MageThemeEditor core.

The user selected Liquid as the developer theme authoring direction. PM - Autonomous Dev confirmed the newer user instruction, "we decided to use liquid", while this document was being prepared. Use a clean native PHTML implementation as a comparison baseline to validate integration cost, behavior and developer experience. This comparison validates the chosen direction; it does not silently reopen the authoring-language choice. The current SDK uses reviewed keepsuit/liquid 0.12.0 in PHP, including the isolated native Magento adapter. The supported dialect matrix and readiness for broader migration remain under validation; see the [SDK implementation record](../architecture/liquid-theme-sdk.md). This supersedes the earlier deferral of all Liquid evaluation until after beta. It does not commit to Shopify or Jumpseller theme compatibility, a hosted headless storefront, or supporting two production rendering engines.

The existing React/strict TypeScript maintainability and navigation/save work retains its sole editor owner. The subsequent implementation goal permits the independent Liquid SDK work alongside that refactor; shared editor integration follows its acceptance and explicit file coordination. The current sample themes are useful internal presets; their coupled JavaScript factories and dense source are not acceptance of a public developer theme SDK.

The [same-design native PHTML baseline](../roadmap/liquid-phtml-comparison-2026-09-11.md) is independently accepted for matching home/product structures, route isolation, source diagnostics and controlled renderer timing. Native cart authority and consent events were accepted from reviewed writer evidence without repeating the transaction. Liquid remains selected; wider migration/support requirements remain open.

## What developers must receive

- A versioned manifest describing identity, runtime compatibility, entry points, declared dependencies/assets and capabilities.
- Predictable directories for layouts, page templates, sections, blocks, snippets, assets, global settings and translations. Choose and document the final schema through the validation work; the earlier illustrative folder tree is not an implemented contract.
- Readable maintained source with descriptive names, focused responsibilities and enforced formatting. Minified bundles belong only in generated output.
- Theme source and default presets separated from each merchant's saved settings, page instances and draft history.
- An install/validate/preview/package workflow that does not require hardcoded theme-name imports in product source.
- Errors that identify the template or asset file and line, source maps for compiled JavaScript, documented data contracts and reproducible debugging.
- An independent author exercise that creates an original section and installs a theme using only the documented public interfaces.

The editor remains responsible for controls, selection, history and persistence. The theme owns the selected full page from head through footer. Magento remains responsible for catalog, prices, taxes, stock, customer context, sessions, cart, checkout and orders. The optional existing-theme/registered-region adoption path remains available; unassigned routes retain their original renderer.

## Liquid validation against the PHTML baseline

Use the same design, content, data and acceptance criteria for both candidates:

1. An editable full-page header/navigation, hero, product collection and footer.
2. A product journey covering a configurable product, variant selection, quantity, Magento-calculated pricing and availability, add-to-cart and the existing checkout handoff.
3. One named extension already installed in an approved local Magento installation. Record its exact version, frontend/data behavior, compatibility changes and remaining gaps. Select it by read-only inventory; do not install a new extension just to satisfy the example.
4. Theme-derived editor controls; section insertion, ordering, duplication, save/reload and matching storefront output.
5. A small custom Magento data-provider example exposed through documented APIs without core edits.
6. A tracking integration example with observable lifecycle behavior and a local collector or mock transport. No real customer data or production analytics traffic is required.

Use only the existing local installations, with current instructions and environment preflight. Preserve Silt/Daybreak drafts and applied state, unrelated edits and existing storefront behavior. Use disposable persistence and controlled local test data. Record scoped changes and reversal steps. Do not create another environment or resume unrelated Magento batches.

Report the following for each candidate; mark untested cells explicitly:

| Area | Required evidence |
| --- | --- |
| Authoring and maintenance | Hands-on changes, time spent, files touched, platform internals needed, independent developer feedback |
| Debugging | Missing data, malformed template and script failure traced to source; actionable errors |
| Editor parity | Desktop/mobile output, shared and page settings, repeatable save/reload and preview |
| Commerce | Correct price/customer/store context, configurable options, cart/session behavior and checkout handoff |
| Extension support | Named extension/version, preserved backend behavior, adapted frontend behavior and ownership of adapter |
| Performance and caching | Comparable cold/warm requests, server rendering cost, asset size and browser timings; no unsupported universal speed claim |
| Isolation and availability | Draft/private-data separation, CSP and asset lifecycle, cache invalidation, last published local output with editor unavailable |
| Distribution and upgrades | Install validation, explicit dependencies, export, upgrade without overwriting merchant changes, disable/restore |
| Adoption cost | Merchant benefit, agency delivery/maintenance burden, migration scope and support obligations |

Record the exact Liquid engine/dialect and render location, with a proceed/defer decision for migration or production rollout based on the evidence. A .liquid extension does not itself decide whether rendering is inside Magento or in a separate service. Retain the existing store-hosted publication and outage requirements unless separately changed. A second rendering engine is a comparison artifact, not an automatic product commitment.

## Third-party scripts and extension boundaries

Trusted developer packages may declare bundled JavaScript dependencies or external SDK URLs. Ordinary merchant content remains declarative and cannot choose arbitrary server code or module paths.

Define script load location, ordering, initialization, teardown, section remount behavior, consent state, preview mode and failure handling. Initialization and event delivery must not duplicate when the editor re-renders a section. Store-wide analytics configuration should survive theme switching; browser-visible project tokens must be distinguished from server-side credentials. Real third-party transport or live account setup requires the actual integration context; the comparison uses a local test transport.

Expose stable documented storefront events for the example. Events representing successful commerce actions must reflect confirmed Magento results, not merely button clicks. Document how CSP sources are derived and reviewed.

Media-upload rejection of executable files remains intact. Trusted theme code has a separate, explicit package-installation path. This is not unrestricted code execution through saved content and does not require opening the future marketplace project.

## Licensing and technical facts

Liquid's original implementation and LiquidJS publish MIT licenses permitting commercial use subject to their notices. Exact release selection, dependencies, distribution model and notices still require the project's adoption review before installation. A license name is not a completed product inventory review.

- [Original Liquid license](https://github.com/Shopify/liquid/blob/main/LICENSE)
- [LiquidJS license](https://github.com/harttle/liquidjs/blob/master/LICENSE)

Shopify extends Liquid with platform-specific objects, tags and filters. Jumpseller independently combines Liquid, theme packages, assets and a visual editor. These are references for developer experience; neither supplies Magento compatibility or rights to third-party theme code.

- [Liquid variants](https://shopify.github.io/liquid/basics/variations/)
- [Jumpseller theme development](https://jumpseller.com/support/themes-guidelines-v2/)

Magento uses PHTML by default and supports multiple template engines. Its layouts and extensions participate in page rendering; replacing those paths can require compatibility work. Hyva also documents explicit extension adaptation despite retaining PHTML.

- [Magento templates](https://developer.adobe.com/commerce/frontend-core/guide/templates/)
- [Magento layouts](https://developer.adobe.com/commerce/frontend-core/guide/layouts/)
- [Hyva compatibility modules](https://docs.hyva.io/hyva-themes/compatibility-modules/getting-started.html)

LiquidJS execution limits do not sandbox JavaScript. Evaluate template isolation, exposed data, custom filters and render budgets against the actual chosen runtime.

- [LiquidJS security model](https://liquidjs.com/tutorials/security-model.html)

These sources were consulted on 11 September 2026. The Liquid/PHTML adoption assessment is an engineering/product judgment, not completed merchant or agency research.

## Execution sequence and ownership

The later user goal **complete the Liquid implementation** supersedes this record's initial documentation-only scope and sequential waiting requirement. Task `01a08c5d-bf41-7720-9a6b-0f44a9e810d5` now owns `theme-sdk/`, its dependencies/tests, reference themes and implementation evidence. The standalone PHP runtime is executable. The [SDK record](../architecture/liquid-theme-sdk.md) lists actual checks and remaining acceptance. The editor owner retains shared editor/build/server files and will coordinate asynchronous preview integration. No new Magento environment, unrelated batch, commit or push is authorized.

Original planning sequence, amended by that later authorization:

1. Finish the existing editor source refactor and verify strict types, lint, formatting, tests, production build and browser behavior.
2. Complete [SOL-521](https://linear.app/solventech/issue/SOL-521/validate-liquid-theme-authoring-against-the-magento-phtml-baseline)'s Liquid runtime/dialect validation against the PHTML baseline.
3. Incorporate the validated Liquid contracts into rendering, SDK and asset delivery.
4. Package the reference theme and have an independent developer install, customize and debug it.
5. Complete installation/upgrade, commerce, extension, performance and recovery acceptance against the declared support matrix.

PM has transferred editor implementation from task 01a08c1e-a267-7da3-b330-beb2f1eb69e5 to the new task 01a08c6f-87f5-78c0-af2e-b337f6d04ed6, using user-requested GPT-6 Astra Extra High in an isolated worktree. The named problem is recovery of readable strict TypeScript editor architecture while preserving save concurrency, navigation and the future Liquid adapter. PM reports the WIP transfer complete: the old writer is idle/quiescent and the new owner is actively recovering the editor. Refactor acceptance remains open; PM reported 468 strict TypeScript diagnostics in the handed-off baseline, not a passing type check. PM - Autonomous Dev retains instruction ownership and independent acceptance; Coordinator 2 retains broader implementation coordination. Do not restart completed Daybreak/Flux writers or create competing writers. The earlier documentation-only phase has ended. This task now implements the separate SDK; both owners have acknowledged the async preview interface and retained separate file ownership.

The initial request authorized Linear task alignment, a project document and project note; the later active goal additionally authorizes completing Liquid implementation. The first SDK dependency was reviewed and pinned before adoption. The broader comparison and integration remain incomplete; no commit, push, production deployment or broader automation has occurred. Historical completed evidence remains historical; no implementation criterion is marked complete by this decision.

## Task alignment

- [SOL-521](https://linear.app/solventech/issue/SOL-521/validate-liquid-theme-authoring-against-the-magento-phtml-baseline): Promote from post-beta discovery to M1 Liquid validation against a native PHTML baseline; remove its dependency on completed beta. Keep Todo until execution starts.
- [SOL-491](https://linear.app/solventech/issue/SOL-491/define-mvp-scope-and-the-storefront-support-matrix): Update support and adoption promises; distinguish complete themes from optional existing-theme integration.
- [SOL-492](https://linear.app/solventech/issue/SOL-492/specify-versioned-content-component-and-publication-contracts): Add theme manifests, defaults versus saved state, declared data/assets/events, versioning and migrations.
- [SOL-496](https://linear.app/solventech/issue/SOL-496/implement-the-magento-theme-runtime-and-registered-editable-regions): Implement the selected runtime after the comparison; preserve Magento services and existing supported rendering.
- [SOL-510](https://linear.app/solventech/issue/SOL-510/deliver-the-developer-theme-sdk-and-magento-integration-adapters): Extend the developer SDK to independent theme packages, custom providers, scripts and debugging.
- [SOL-511](https://linear.app/solventech/issue/SOL-511/build-the-installable-liquid-reference-theme): Deliver an installable reference theme without theme-specific core edits.
- [SOL-501](https://linear.app/solventech/issue/SOL-501/build-the-section-editor-and-schema-driven-settings-panels): Preserve the current source cleanup, then derive editor behavior from public theme contracts.
- [SOL-504](https://linear.app/solventech/issue/SOL-504/implement-versioned-media-and-asset-delivery-with-a-local-mirror): Define trusted script/dependency delivery and lifecycle separately from media upload.
- [SOL-513](https://linear.app/solventech/issue/SOL-513/verify-commerce-cache-isolation-csp-accessibility-and-performance): Carry comparison and selected-runtime regressions into commerce/cache/CSP/performance acceptance.
- [SOL-515](https://linear.app/solventech/issue/SOL-515/package-installation-upgrades-diagnostics-and-uninstall-behavior): Add theme package installation, upgrade, export and restoration.
- [SOL-530](https://linear.app/solventech/issue/SOL-530/verify-and-hand-over-the-working-starter-theme-demo-end-to-end): Require independent developer authoring and install/debug evidence for final theme handoff.
- [SOL-520](https://linear.app/solventech/issue/SOL-520/design-the-future-app-block-and-capability-extension-model): Retain future marketplace/app discovery; core developer script support is no longer deferred behind it.

## Project artifact and provenance

[Linear decision document](https://linear.app/solventech/document/magethemeeditor-liquid-theme-authoring-and-magento-validation-11-eef498350d73). This record supersedes the decision register's earlier future-only Liquid exploration, while preserving the immutable 7 September research baseline. The 11 September task alignment read all 47 issues in the main MageThemeEditor project with no next page; the separate future ecosystem project had no issues and was not changed. Task mappings above remain a dated snapshot, not live implementation evidence.

[Linear project activity note](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098/activity#project-update-c7b5806d) records the 12 issue updates, three milestone changes and editor handoff. All 12 updated issues were reread on 11 September 2026: SOL-521 is Todo / High / M1, its beta blocker is absent, and its SDK/reference-theme/package dependencies are present. Other changed issue states and unrelated dependencies were preserved. No implementation issue was completed by this alignment.
