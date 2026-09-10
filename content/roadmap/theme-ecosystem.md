# Future theme ecosystem and marketplace

Status: **confirmed future product direction; delivery sequence and implementation proposed**.
Updated: 7 September 2026. The user requested third-party theme creation and sales, then explicitly
placed this capability on the future roadmap. No marketplace delivery date, commission rate,
template engine, seller tooling, or payment provider is selected. This direction does not expand
the initial editor MVP. It now has a separate Linear project containing plans and documents only;
see [planning status](#planning-status) for the verified project and artifact links.

## Intended outcome

Developers, agencies, and merchants with development skills can create themes using MageThemeEditor's
published standards, including their own sections, blocks/elements, presets, settings, and assets.
Creators can eventually register as sellers and distribute free or paid themes through the platform.
Merchants discover compatible themes, preview them, obtain a license where required, and customize
them in the same hosted editor. A commission on theme purchases is a possible platform revenue model;
the commercial terms remain open.

A seller role is distinct from the role that connects and manages a Magento store, although an
organization may hold both. Theme purchases are separate from shoppers' purchases on Magento stores.

## Proposed sequence

| Stage | Scope | Evidence needed to advance |
| --- | --- | --- |
| Initial editor foundation | Versioned component identities and settings; separate theme defaults from merchant content; declared runtime capabilities | Our reference components use the same contracts intended for future authors |
| Developer authoring pilot | Documented theme package format, starter theme, local preview, validation, and a small invited creator group | An external developer builds an original section and theme without modifying the editor core; preview, publication, upgrades, and restoration work |
| Curated theme catalog | Reviewed submissions, author profiles, demos, compatibility declarations, release history, and free distribution | Merchants install supported themes and receive updates without losing their settings or changing unassigned surfaces |
| Paid marketplace | Seller onboarding, paid listings, licenses, commissions, payouts, refunds, and support ownership | Commercial policy, payment flows, package review, and merchant recovery are ready for the supported launch scope |

Marketplace screens, seller accounts, billing, and payout infrastructure are future work. The first
concept UI remains focused on editing, previewing, publishing, and restoring selected storefront
content. No speculative marketplace infrastructure is required for that proof.

## Standards to preserve and decisions to make later

Keep component IDs namespaced and versioned, define settings and allowed nesting, and separate
immutable theme package versions from merchant-owned content and overrides. Components should declare
their supported page/region contexts, runtime dependencies, and adapter requirements. Theme updates
must have a migration and restoration strategy; replacing a theme must not silently discard content.

Before promising a public authoring SDK, select and prove a template execution model. Liquid or a
restricted alternative is a candidate. A format that only composes our existing components does
not yet fulfill the goal of authors creating original renderers. Native PHP extensions would remain
explicit Magento package installations; marketplace uploads must not become unrestricted remote
PHP execution. Template isolation, browser scripts, package review, and upgrade compatibility need
their own evidence before third-party installation is enabled.

The public authoring contract must expose controlled Magento data and commerce capabilities without
requiring access to private editor services. Installed templates, browser assets, and rendered output
remain inspectable; marketplace licensing is not a guarantee against copying.

## Hybrid adoption remains a requirement

Authors must declare whether a package supports a complete compatible theme, selected page content,
or reusable regions/sections. A complete theme is not automatically compatible with every existing
Luma/Hyvä customization. Reusing a component from another author's theme requires compatible
contracts and assets; it is not automatic. Preview and activation must identify affected targets and
preserve the [hybrid adoption requirements](../requirements/hybrid-adoption.md).

## Reference model and limits

Shopify themes organize templates, sections, blocks, settings, translations, and assets using a
standard structure. Theme blocks can define settings and support reuse and nesting. This is a
reference for our authoring experience, not a claim of Shopify theme compatibility.
[Shopify theme architecture](https://shopify.dev/docs/storefronts/themes/architecture),
[theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/quick-start?framework=liquid).

Liquid has platform-specific variations; Shopify adds its own objects, tags, and filters. Choosing
Liquid alone would not supply Magento integrations or make Shopify themes directly installable.
[Liquid variations](https://shopify.github.io/liquid/basics/variations/).

Shopify's Theme Store demonstrates selling creator themes with platform revenue sharing. Our
commission, license scope, update entitlements, support, refunds, seller responsibilities, and payout
terms require separate decisions; no Shopify rates or terms are adopted here.
[Shopify theme revenue sharing](https://shopify.dev/docs/storefronts/themes/store/revenue-share).

## Planning status

The user requested a separate project with artifacts and plans, and no tasks. Created under the
Solventech team:
[MageThemeEditor — Theme Ecosystem & Marketplace](https://linear.app/solventech/project/magethemeeditor-theme-ecosystem-and-marketplace-f118322e5577).
Project ID: `ec46d17c-f646-4216-9461-009c93d25804`.

The project contains three planning documents:

- [Theme Ecosystem — Product vision and scope](https://linear.app/solventech/document/theme-ecosystem-product-vision-and-scope-5da3e0ac8c69).
- [Theme Ecosystem — Authoring and compatibility proposal](https://linear.app/solventech/document/theme-ecosystem-authoring-and-compatibility-proposal-d4e80c9ca67c).
- [Theme Ecosystem — Phased roadmap and open decisions](https://linear.app/solventech/document/theme-ecosystem-phased-roadmap-and-open-decisions-d44a1a599b40).

Live verification on 7 September 2026 at 07:07 UTC found Planned status, three documents, two
reference links, no issues, no milestones, and no start or target dates. The document and issue
listings were complete (`hasNextPage: false`); issues were checked including archived items.
This is an observation, not an automatically refreshed dashboard.

The [core MageThemeEditor project](https://linear.app/solventech/project/magethemeeditor-f2f58b04b098)
and its existing issues were not modified or moved. Its
[dated M6 discovery baseline](linear-baseline-2026-09-07.md) remains historical evidence. Converting
the future project's plans into issues or execution milestones requires a later user request.

## Later planning observation · 2026-09-07

The coordinator added and read back a fourth artifact,
[Theme Ecosystem — Custom module data integration](https://linear.app/solventech/document/theme-ecosystem-custom-module-data-integration-4607c4e9c89d),
created at 09:09 UTC. The [local mirrored proposal](custom-module-data-integration.md) records
registered typed providers, reuse of approved native/API services and future visual field binding.
The authoring and phased-roadmap Linear documents link to it. The coordinator separately verified
zero future issues; no new milestones or core issue criteria were created for this idea. Batch 02
read the exact new document and mirrored it; it did not repeat the whole project listing.
The earlier three-document observation remains historical. Portable 1.0.0 and the current editor
concept remain unchanged by this future-only direction.
