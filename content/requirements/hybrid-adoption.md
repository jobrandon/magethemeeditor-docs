# Hybrid adoption requirements

Status: **confirmed product direction; detailed acceptance criteria proposed for delivery planning**.
Updated: 7 September 2026. Source: the user's explicit product direction, the
[research baseline](../architecture/theme-editor-research-2026-09-07.md), and
[nine live-read Linear issues](../roadmap/linear-baseline-2026-09-07.md#hybrid-adoption-coverage-gap).
These criteria are not implemented, runtime-verified, or fully synchronized into Linear.

## Intended outcome

A merchant keeps the active storefront/theme and adopts the editor only where selected:
home/CMS pages, particular product detail pages (PDPs), category pages, or registered regions.
The rest of the storefront remains under its existing renderer. Installing the connector alone
does not opt in pages, replace a theme, or rewrite content.

## Assignment and renderer contract

Each assignment must explicitly identify the store view or inheritance scope, target entity/page
or registered region, selected renderer/adapter and supported version, published release,
activation state, and restoration reference. Expose the effective inherited/overridden assignment
to the merchant before preview and publication. URLs alone are not a sufficient entity identity.

Default to the original renderer for unassigned targets. Prevent ambiguous overlapping page and
region assignments from publication until a documented precedence rule resolves them. The exact
schema and precedence algorithm remain design work; this page specifies the required observable
behavior without inventing a finalized API.

One renderer owns a selected page surface or region at a time. A page-content assignment does
not implicitly replace the surrounding header, footer, cart, or checkout. Declared region adapters
must define the wrapper and lifecycle they own. Custom templates/extensions require explicit
capabilities and compatibility declarations.

## Acceptance criteria

| ID | Requirement | Evidence needed before completion |
| --- | --- | --- |
| HYB-01 | Installation preserves the active theme, original content, and all existing assignments | Compare configuration, content, rendered output, and key flows before/after installation |
| HYB-02 | Merchants select supported home/CMS, PDP, category, or registered-region targets in an explicit store scope | Demonstrate each allowed target and clear unsupported-target feedback on both adapters |
| HYB-03 | Renderer selection is deterministic, visible, and version/capability checked | Exercise inherited and overridden targets; block ambiguous overlap; confirm exactly one output owner |
| HYB-04 | Draft save and preview are isolated from publication | Anonymous requests never see drafts; parallel editor/store-view previews do not leak state |
| HYB-05 | Publish a selected assignment independently | Publish page/region A while B remains on its prior assignment/release; record exact affected targets |
| HYB-06 | Preserve original content and its renderer metadata before conversion/activation | Dry-run conversion reports supported/preserved/unsupported structures; retain a restoration reference |
| HYB-07 | Restore or disable one assignment independently | Return A to a compatible earlier editor release or original renderer/content without changing B; restore routing and content coherently |
| HYB-08 | Scope CSS, tokens, JavaScript initialization, and teardown to opted-in surfaces | Before/after checks show no global reset, token leakage, duplicate widgets, or changed unassigned layout |
| HYB-09 | Limit publication/cache effects to intended scopes while respecting commerce context | Check release/assignment invalidation, FPC behavior, store views, currency, and customer groups on warm and cold caches |
| HYB-10 | Preserve untouched pages and shared commerce surfaces | Check untouched home/CMS/PDP/category pages plus header, footer, search/navigation, account, mini-cart, cart, and checkout after publish and restore |
| HYB-11 | Declared adapters expose supported behavior without treating arbitrary markup as editable | Unsupported custom templates/extensions retain originals and produce a clear integration requirement; incompatible publication is blocked |
| HYB-12 | Failure and outage preserve the last valid state | Interrupt transfer/activation and lose SaaS connectivity; confirm no partial routing/content switch and prove local-mode assets on cold cache |

These criteria apply to each declared adoption mode. They do not extend support to every Magento
version, product type, theme override, or extension. The support matrix must name the tested scope.

## Minimum integration scenarios

1. On a Luma fixture, opt in the homepage while keeping a legacy CMS page and commerce templates.
   Publish and restore the homepage; check untouched shared surfaces.
2. On a Hyvä fixture, opt in one PDP and one category while adjacent products/categories remain
   original. Verify supported configurable-product selection, prices, and add-to-cart.
3. Register a single content region inside an existing template. Edit it without changing siblings
   or initializing their JavaScript twice. Restore only the region.
4. Convert supported Page Builder content while preserving a CMS block, widget, and unsupported
   structure. Verify opt-in activation never renders both original and converted page content.
5. Combine two assignments and two store views. Publish/restore only one target, test conflicts,
   and verify original content remains retrievable through a connector disable/uninstall policy.

Record fixtures, exact versions, initial state, changed targets, original snapshots, release IDs,
commands, screenshots, commerce results, and limits in future evidence pages. None of these
scenarios have been run by this documentation setup.

## Linear planning gap

SOL-491/492/493/496/503/509/510/511/513 cover related scope, assignments, regions, migration,
and regression work. The audit found partial coverage, not the complete contract above.
The [coverage table](../roadmap/linear-baseline-2026-09-07.md#hybrid-adoption-coverage-gap) identifies
where future issue updates should record the missing criteria. Updating this document does not
change those issues.
