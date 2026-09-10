# Custom module data integration

Status: **future roadmap proposal; artifacts and plans only**. Updated: 7 September 2026.

The user wants heavily customized Magento stores to expose selected data from custom modules and third-party extensions with minimal integration work. They explicitly placed this capability on the future roadmap. It adds no current MVP tasks, milestones, implementation, dates or changes to the reviewed portable 1.0.0 contract.

## Intended merchant outcome

A developer registers an approved data source once. A merchant can then choose that source in the theme editor and connect its typed fields to compatible sections without repeatedly changing templates.

Example: an existing dispatch-time extension exposes an estimated dispatch label. The merchant selects “Connect data → Dispatch estimate → Label” for a text element. The original Magento extension continues calculating the value; the theme package controls presentation.

The differentiator to validate is the complete registration-to-visual-editing experience across supported storefront adapters. This is a product hypothesis, not a claim that data-binding APIs are new, patentable or unavailable elsewhere.

## Reuse existing integration mechanisms

Magento provides PHP service contracts intended for reuse by modules and presentation/API clients. Its web API framework can expose appropriately defined services through REST/SOAP configuration. Existing business logic should remain in its owning module. [Adobe service layer](<https://developer.adobe.com/commerce/php/architecture/layers/service>), [Configure services as web APIs](<https://developer.adobe.com/commerce/php/development/components/web-api/services>)

Magento also allows modules to extend GraphQL schemas and supply resolvers for custom fields. GraphQL is an available transport, not a requirement for every native Magento rendering call. [Extend a GraphQL schema](<https://developer.adobe.com/commerce/webapi/graphql/develop/extend-existing-schema>)

Proposed adapter choices:

| Existing extension surface | Smallest integration to evaluate |
| -- | -- |
| Suitable PHP service/repository | Registered provider calls it through dependency injection inside Magento |
| Suitable existing GraphQL or REST API | Map an explicitly approved operation and typed fields; keep credentials in the appropriate server boundary |
| No stable data API | A separate compatibility module wraps a supported extension service where feasible; document version coupling and maintenance |
| Complex widget or interactive storefront behavior | A registered renderer/action adapter may be necessary; exposing data alone does not reproduce behavior |

Do not force an HTTP/GraphQL round trip back into the same Magento request when a suitable native service can be reused. GraphQL exposure does not automatically supply editor controls, storefront authorization, cache correctness or template compatibility.

## Proposed registration and binding contract

A future provider declaration would describe:

* Stable provider identity/version, required module versions and supported storefront contexts.
* Typed inputs and outputs, field labels, cardinality and allowed section/settings bindings.
* Required store/product/customer context, authorization and data sensitivity.
* Public versus private delivery, cache identity/invalidation, batching and request limits.
* Preview behavior, empty/missing/error fallback, compatibility and deprecation policy.

The editor would discover only registered, approved capabilities. Typed metadata could generate a data-source picker and compatible field controls. Optional scaffold tooling could produce adapter boilerplate and validation reports.

Future content documents would store provider/field references and bounded parameters, not copied live prices, stock, customer data, raw SQL, arbitrary PHP/JavaScript or unrestricted GraphQL query text. Credentials and private response data would not become theme assets or CDN documents. Changes require an explicit future version/migration decision; examples here are not valid 1.0.0 wire objects.

Native preview and the published storefront should call the same provider contract with the correct Magento context. Luma/Hyva may share data semantics while needing separate presentation adapters. Magento’s GraphQL cache behavior already distinguishes cacheable queries and customer context; the bridge must declare and test its own corresponding boundaries. [GraphQL caching](<https://developer.adobe.com/commerce/webapi/graphql/usage/caching>)

## Initial future pilot and limits

Start with read-only public data, such as an original dispatch estimate or store-location summary. Test one original extension with a PHP service and one with an existing API. Measure the actual integration effort before promising configuration-only or near-zero-code adoption.

Later, consider authenticated customer-specific providers and separately declared actions. Reading a label and redeeming loyalty points have different authorization and side-effect requirements; preview must not accidentally execute commerce actions.

Test disabled/upgraded modules, missing fields, incompatible versions, wrong-store access, private-data isolation, cache invalidation, slow providers, bounded collection queries, safe fallback and unchanged neighboring storefront behavior. A provider failure should have an explicit local presentation policy. Third-party service availability cannot inherit the product’s local-only outage guarantee automatically.

No arbitrary module/database auto-exposure, universal extension compatibility, no-code conversion of custom PHP, or redistribution of vendor/client code is promised. Commercial-use and entitlement checks apply to each adopted SDK, package and distribution model.

## Evidence and sequence

Explore alongside the future authoring SDK/creator pilot, after the core editor and actual Magento integration are demonstrated. Theme marketplaces and paid distribution are not prerequisites for validating this bridge.

Expected future artifacts: provider contract proposal, developer guide and original examples, editor binding journey, compatibility/upgrade matrix, privacy/cache model and measured pilot findings. Observe time to first working binding, source changes required, adapter reuse across Luma/Hyva, upgrade breakage and merchant task success; set targets after measuring a baseline.

The current concept UI remains focused on its existing home/CMS scope. Existing core issues and the future project’s no-task/no-milestone status remain unchanged. Turning this proposal into executable work requires later user direction.

## Source and observation

Mirrored from the coordinator-authored [Linear proposal](https://linear.app/solventech/document/theme-ecosystem-custom-module-data-integration-4607c4e9c89d) after an exact document read on 2026-09-07. Document ID: `2c087f0a-3b75-4f25-9f33-22c49b7f1669`; future project `ec46d17c-f646-4216-9461-009c93d25804`. This is the fourth planning document; the earlier three-document observation remains historical. The coordinator separately verified zero future issues and no added milestones. This batch read the exact document, not a complete project listing. No UI, provider implementation, dependency, current acceptance criterion or portable 1.0.0 field changed for this proposal.
