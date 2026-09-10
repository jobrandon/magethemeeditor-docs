# Theme editor design review

Implementation update · 2026-09-10: the user subsequently requested integration into the actual local product. See [Resource Desk implementation and verification](implementation-2026-09-10.md). The design-phase status and sandbox restrictions below are preserved as historical context.

Status: **proposed UI/UX, compact visual refinement under review**. Observed 2026-09-10. This is a separate design session; Magento development remains paused.

The goal is a commercially presentable editor that lets merchants compose the full storefront, select what they see and edit it with confidence. Preserve the useful outline/canvas relationship of the running editor and introduce a separate contextual inspector. Make drag-and-drop the normal ordering interaction. Preserve every current component and control through progressive disclosure.

This design delivery includes the specifications, control coverage and implementation receipt below. Other workspace documentation remains in separately pending changes; references to those files are recorded as paths until they are delivered.

## Review entry point

Design artifacts live in the workspace folder `uiux/theme-editor/`. Its `README.md` links the current-state captures, three visual directions in displayed order, icon gallery, exact extracted inventory, and these canonical specifications. Generated frames are proposals using fictional store content. They are not screenshots of implemented changes.

The three independent frames were generated with built-in Image Gen and the actual current editor screenshots attached. The original set established three directions; the user is now refining the third frame before an interactive sandbox is built. The sandbox will stay under the review directory and use local sample data only.

The user subsequently annotated the third original frame, Resource Desk, asking for icon-only pencil/trash image actions, a red trash hover, compact indentation and more space for the main canvas. The compact fourth image is followed by `05-resource-desk-bare-icons.png`, which removes the pencil/trash button boxes. The fifth image is the current visual candidate; the original three remain historical alternatives. The icon gallery now demonstrates removal confirmation, Cancel/Escape and Undo.

For the eventual coded refinement, target a 48px activity rail, roughly 220px outline, 268px inspector and 12px indentation per tree level. These are adjustable layout targets, not measured claims about generated-image geometry. Use 32px minimum compact pointer rows/actions, 44px touch targets, 14px readable controls, and recover room through spacing rather than text reduction. Optional-image controls use 16px pencil and trash glyphs on transparent, borderless hit areas; the trash graphic is neutral at rest and red `#c2414a` on hover/focus, with an accessible “Remove image” label. Preserve the keyboard focus ring. This explicit compactness request supersedes the initial 36px desktop-control default for those controls.

Choice fields now have a separate working specimen in `uiux/theme-editor/controls.html`. Short option sets use segmented toggles only when their rendered labels fit the available inspector width; many or long options use a select. Resizing or changing labels preserves the selected value. The [interaction specification](interactions.md#adaptive-choice-presentation) defines the shared renderer rule. This is isolated sample behavior; the actual editor is unchanged.

Desktop preview now follows the available container without a fixed width cap or scaling, per the 2026-09-10 user instruction. The isolated `viewport.html` example lets the reviewer resize the browser, hide editor panels and compare fixed Tablet/Phone widths. See [viewport behavior](interactions.md#viewports-and-preview).

## What the current screen establishes

Visual inspection at `127.0.0.1:4177/theme` found a forest-green header, white form controls, a 340px source-defined sidebar, and a large warm Silt & Form storefront canvas. Page and resource selectors are useful foundations. The toolbar gives save, apply, two different restores, reload and preview similar visual weight. Section/block ordering uses arrow buttons. Selecting a section appends its fields below the full outline and insertion dropdown, forcing extensive sidebar scrolling. The rendered image remains visible while its selector says unavailable; that mismatch was captured, not repaired by this design pass.

The current editor has 14 page/template choices. It has separate page and shared buffers, a fixed shared Header/Footer model, named menu resources, local undo/redo, page/shared save actions and a consistent-snapshot apply/restore bridge. The design pass inspected source and UI; it did not execute that bridge or revalidate native functionality.

## Design direction invariants

- Header / Template / Footer remain visible as a hierarchy for the current page. Shared scope is explicit; page content stays independent.
- A searchable library uses useful rendered previews, package names and placement filtering. It does not flatten the entire catalog into permanent screen chrome.
- Canvas selection, outline selection and inspector selection share one stable identity. Editing mode selects links/components; Preview mode exercises sample navigation.
- An action changes one named resource or an explicit set. Saving, session undo, preview refresh, resource reload and history restore have distinct meanings.
- The component registry remains extensible. Existing Studio and Editorial variants stay distinct. No silent conversion, raw-code editing requirement or arbitrary merchant module loading is introduced.
- Readable grouped controls and accessible alternatives are part of the core journey. Hide, duplicate, remove and reorder are undoable draft commands.

## Review documents

| Document | Purpose |
| --- | --- |
| [Interaction specifications](interactions.md) | Selection, library insertion, nested drag-and-drop, inspector controls and accessibility |
| [States and resources](states-and-resources.md) | Page/shared scope, menus, save/reload/undo/history distinctions and sample scenarios |
| [Implementation handoff](handoff.md) | Existing capability versus proposal, local sandbox boundary and acceptance checks |
| [Current element coverage](coverage/index.md) | All 66 types, fields, blocks, limits, preview briefs and placement/capability caveats |

The user selected Tailwind CSS v4 for editor styling on 2026-09-10. The review now has exact 4.3.3 pins, a lockfile, CSS-first tokens and four locally compiled stylesheets. See the [styling/build handoff](handoff.md#selected-editor-styling-standard). The adaptive and icon specimens consume those stylesheets; this does not integrate the complete editor or migrate the storefront.

## Proposed visual system

Evolve existing forest/sage/warm-neutral colors. Initial candidates: primary forest `#163b2d`, accent `#31584b`, canvas ground `#edf0ec`, panel white `#ffffff`, selected tint `#e8efea`, text `#25362e`, muted text `#526058`, separator `#d6ded7`. Color values are starting tokens, not a completed accessibility audit.

Use system sans at 14–16px for controls, 12px only for nonessential metadata, 20px contextual headings and a restrained 4/8px spacing system. Controls use 6px corners, surfaces remain mostly flat, and shadows only explain actual overlays. Storefront typography stays visually separate from editor typography. Generated frames sometimes render an inspector field in serif; the implementation should keep every editor input in system sans.

Editor buttons target 36px minimum height and 44px on touch. Use 16px icons in compact outline rows, 20px in toolbar controls, 24px in the catalog/gallery; preserve each SVG's 24px viewBox and stroke geometry. Active state must combine tint with selected/pressed semantics. Focus uses a visible 2px ring with 2px offset. See the local icon mapping for per-action labels and restore/reload/undo distinctions.

The icon sub-agent delivered 55 Lucide Static 1.44.0 assets with a semantic map, gallery, upstream ISC/Feather MIT notices and a dated review accepted for this local asset set only. Generated icon approximations are directional placeholders to be replaced with those exact assets during the selected prototype build. No product dependency was installed.

## Visual review findings to carry into the build

Generated frames establish useful hierarchy and style, but do not substitute for a coded/accessibility review. The three mockups have slightly different copy, icon shapes and sampled prices; these are fictional. Use the documented registry names and exact icon set in the prototype. Do not copy the extra abstract logo/Media navigation in the third frame as newly approved product features. Restrict shared impact text to pages assigned to this theme in the selected store; the mock's broad “across your store” wording must be corrected. Preserve 52 eligible template insertions within the 66-type catalog count. Keep the whole structure accessible when the library flyout overlays part of the canvas.

## Grounding and ownership

The full-page requirement is confirmed in the [decision register](../../decisions/index.md). This design adds proposals; it does not change those decisions or mark outstanding features complete. Existing full-theme architecture (`content/architecture/full-page-theme.md` in the workspace) and third-party requirements (`content/requirements/third-party-compliance.md` in the workspace) remain authoritative.

Artifacts are authored by the separate Astra Extra High design session for the named problem of coherent component, nesting, resource and revision UX. Exactly one Terra Medium sub-agent owns the bounded icon deliverable. No development coordination was resumed, no remote state changed, and no commit or publication was made.
