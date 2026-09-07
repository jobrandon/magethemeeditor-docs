# MageThemeEditor

MageThemeEditor is a planned hosted storefront editor for Magento Open Source. The product owns
the editing and publishing services; Magento retains commerce behavior and renders published
designs through a generic connector/runtime and declared Luma or Hyvä adapters.

!!! info "Evidence status · 7 September 2026"
    Public research is complete. Merchant interviews, product implementation, and Magento runtime
    verification are outstanding. These pages describe direction and acceptance criteria.

## Start here

| Need | Read |
| --- | --- |
| Understand the product and adoption choices | [Product overview](product/overview.md) |
| Understand service and storefront ownership | [System boundaries](architecture/system-boundaries.md) |
| Keep an existing storefront and adopt selected areas | [Hybrid adoption requirements](requirements/hybrid-adoption.md) |
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
See the [coverage gap](roadmap/linear-baseline-2026-09-07.md#hybrid-adoption-coverage-gap).

## Ownership and project links

This documentation source lives in `MageThemeEditor/docs/content`, with its own local Git repository
and MkDocs site. The shared research original remains preserved. Read the
[ownership decision](decisions/0001-independent-documentation.md) before moving documents.

[Linear project](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098) ·
[Linear research document](https://linear.app/solventech/document/magethemeeditor-research-and-architecture-baseline-953f16866313)

The Linear snapshot is dated evidence, not automatic synchronization. No product deployment or
public documentation hosting is established by this local setup.
