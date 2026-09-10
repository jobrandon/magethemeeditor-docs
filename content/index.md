# MageThemeEditor

MageThemeEditor is a planned hosted storefront editor for Magento Open Source. The product owns
the editing and publishing services; Magento retains commerce behavior and renders published
designs through a generic connector/runtime and declared Luma or Hyvä adapters.

!!! info "Current evidence · 9 September 2026"
    The [full-page Silt theme](roadmap/full-theme-commerce-evidence-2026-09-09.md) now has coherent
    Home, collection, product and search templates; populated synthetic Magento catalog data; native
    simple-cart mutations/totals; and an authenticated transition to ordinary native checkout.
    Shared menu/settings editing, declared package capabilities and fourteen page resources are local.
    Full catalog/field/provider/account acceptance, exclusive CSP response-header ownership, Hyvä
    compatibility, hosted delivery and commercialization remain open. See the [execution plan](roadmap/execution-plan.md).

## Start here

| Need | Read |
| --- | --- |
| Understand the product and adoption choices | [Product overview](product/overview.md) |
| Author original sections and components | [Developer packages](architecture/developer-packages.md) and [local package/native evidence](roadmap/section-library-evidence-2026-09-08.md) |
| Understand service and storefront ownership | [System boundaries](architecture/system-boundaries.md) |
| Connect existing CMS pages and understand storage, publishing and outages | [CMS pages and storefront delivery](architecture/cms-page-delivery.md) |
| Keep an existing storefront and adopt selected areas | [Hybrid adoption requirements](requirements/hybrid-adoption.md) |
| Check third-party rights before adoption and release | [Third-party compliance requirements](requirements/third-party-compliance.md) |
| Read the completed research and its sources | [Research baseline](architecture/theme-editor-research-2026-09-07.md) and [provenance](architecture/research-provenance.md) |
| See planned delivery and current-state limits | [Roadmap](roadmap/index.md) and [dated Linear baseline](roadmap/linear-baseline-2026-09-07.md) |
| Distinguish confirmed direction from open choices | [Decision register](decisions/index.md) |
| Add documentation or prepare separate hosting | [Authoring](contributing/authoring.md) and [publishing](contributing/publishing.md) |

## Product direction

Merchants can retain their active storefront theme and opt in only home/CMS pages, selected
product or category pages, or registered regions. A free compatible reference theme is the
recommended path to the broadest supported editing experience. Custom templates and extensions
need declared adapters. Liquid is optional future exploration.

Hybrid adoption is confirmed direction. The exact routing, isolation, and independent restoration
criteria are documented here; they were only partially covered in Linear at the recorded audit.
Batch 01 subsequently [synchronized the complete criteria](roadmap/batch-01-evidence-2026-09-07.md#linear-synchronization)
into existing delivery issues without claiming runtime completion.

## Ownership and project links

This documentation source lives in `MageThemeEditor/docs/content`, with its own local Git repository
and MkDocs site. The shared research original remains preserved. Read the
[ownership decision](decisions/0001-independent-documentation.md) before moving documents.

[Linear project](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098) ·
[Linear research document](https://linear.app/solventech/document/magethemeeditor-research-and-architecture-baseline-953f16866313)

The Linear snapshot is dated evidence, not automatic synchronization. No product deployment or
public documentation hosting is established by this local setup.
