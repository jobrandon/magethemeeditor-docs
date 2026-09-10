# Editor interaction specifications

Implementation update · 2026-09-10: the user subsequently requested integration into the actual local product. See [Resource Desk implementation and verification](implementation-2026-09-10.md). The design-phase status and sandbox restrictions below are preserved as historical context.

Status: **proposed**, 2026-09-10. These behaviors are implementation requirements for the selected isolated prototype, not claims that the running editor supports them. [Review overview](index.md).

## Main editing journey

Navigation refinement · 2026-09-10: the user requires a working storefront with the editor available
as a layer, normal link navigation and confirmation before leaving unsaved work. The
[interactive storefront specification](storefront-navigation.md) defines Browse/Select behavior,
guarded navigation and saved-versus-unpublished states. It refines the earlier Edit/Preview design
below; this new flow is not yet implemented.

Choose a page, inspect the full Header / Template / Footer outline, select the storefront element, edit its focused settings, preview at a device width, then save the named draft resource. Show one primary save action appropriate to the active scope. History and resource reload live in supporting controls. The account/bag of the fictional storefront never open real Magento in the sandbox.

Use a page switcher containing all current choices: Home, About, FAQ, Editorial collection, Stories & details, Media studio, Motion & voices, Catalog discovery, Product, Search, Commerce examples, Contact studio, Studio letters and Studio invitation. Search matches display names. Display page title, template and draft state in each row. Switching the page preserves each resource's in-memory edits, selection and scroll position. It is navigation, not a save or template replacement.

“Change template” is a separate page-level action with a preview of the replacement sections. Show a concrete count of sections to be replaced and retain the page metadata. Apply the change to the current draft only as one undoable command. Do not let clicking another page change its template. Head title and meta description live in Page settings, away from the section list.

## Synchronized selection

The outline is a navigation tree with stable resource/node IDs; the canvas has matching selectable boundaries. Click once to select a section and open its inspector. Click a child block boundary to select the block; the breadcrumb exposes its parent. Clicking a nested link in Edit mode selects its owning block instead of navigating. Preview mode removes editor interception and outlines, uses safe local sample navigation, and has an obvious Return to editing action.

Selection uses a restrained tinted outline row, 2px canvas border and a small component label. Hover uses a lighter boundary that cannot be confused with selection. Selection changes do not mark a draft dirty, append history or move keyboard focus unexpectedly. Outline selection scrolls only the canvas region into view; canvas selection expands relevant ancestors in the outline. Manual inspector entry keeps focus and caret stable while the preview updates.

An empty canvas says “Start with a section” with Add section as the single primary action. An unselected canvas inspector shows concise page context and a selection hint. A selected missing-reference section remains selectable and preserves its settings; show the precise unresolved reference next to its field.

## Searchable component library

Open Add section from the outline or a contextual canvas insertion point. Retain that intended placement and neighboring node IDs while searching. Focus search on open; Escape closes and returns focus to the opener. The library is an overlay/flyout with a two-column thumbnail grid, flat category navigation and a details pane only when a card is selected. On constrained widths the inspector temporarily collapses; the canvas retains enough visible area to place a section.

Default filter: eligible sections for the current target. Categories cover Studio (5), Editorial (14), Interactive (10), Commerce (19), Shell (13), Forms (4), Author example (1). All components exposes all 66; the template insertion scope has 52 eligible types. Search spans human name, package, purpose and aliases such as hero/banner, collection/category, accordion/FAQ and phone/mobile. Distinguish equivalent-looking Studio and Editorial types with package labels and controls summary. No results offers Clear filters; it does not invent an unknown type.

Each card has a meaningful miniature layout based on its [preview brief](coverage/index.md), its title, package and placement. A selected card shows its purpose, block types and relevant data availability. Missing catalog data is “Needs store data”; a non-delivering form is “Validation preview”; an account component is “Opens native account”; the author example is “Not available in this theme.” Keep unsuitable cards discoverable in All components, with a focusable explanation and an unavailable insert action. Do not make a disabled card the sole explanation.

Create preview images from safe local samples after visual selection. Use actual reviewed media or generated raster assets, not improvised vector thumbnails. Do not extract commercial theme screenshots/assets. A component's sample thumbnail does not establish its runtime capability.

## Drag and drop

| Phase | Pointer behavior | Visible and announced state |
| --- | --- | --- |
| Ready | Drag starts only from an explicit grip or library card drag region, after 6px movement; text fields remain selectable | Accessible grip name: “Move Image with text” |
| Lift | Capture stable source ID, source resource, parent, position and full before-state | Small ghost with name and preview; original location remains occupied; announce item and position |
| Hover | Hit-test eligible insertion boundaries using section/block level and registry placement | 2px line with endpoint markers and “Insert after Banner / hero”; not color alone |
| Nested hover | Enter only a valid parent accepting that registered block kind | Indented target, parent highlight and “Move into Multi-column cards, position 2 of 3” |
| Auto-scroll | Within 48px of canvas/tree edges, scroll that region proportionally, capped around 600px/sec | Keep insertion label visible; never scroll a background document instead |
| Collapsed parent | Hover a valid collapsed container for approximately 600ms | Expand without committing; still respect allowed depth/kinds |
| Commit | Release on eligible boundary; normalize index after removal | One atomic undoable command, same node ID; update outline/canvas and keep moved node selected |
| Cancel | Escape, pointer cancellation, invalid drop or release outside an eligible target | Restore exact before-state, selection and relevant focus; no dirty/history change |
| Invalid | Reject wrong placement, max blocks, self/descendant cycles or resource boundary | “This block belongs inside a Story slider” or specific limit; no silent conversion |

Insertion and reorder share the same placement model. A new component receives a new unique section ID and unique block IDs. Duplicating also regenerates IDs and resolves package-unique anchors through existing validation. Dropping before/after uses neighboring stable IDs so a simultaneous render does not change the intended position. Refuse a stale target if the parent changed during dragging. A failed command must roll back the whole mutation.

Current sections support one level of typed child blocks; they are not arbitrary nested containers. Permit reordering within a parent. Moving a block to another compatible section requires the same accepted block schema and a valid capacity; otherwise explain the rejection. Never move page content into a shared resource by accidental drag. A future explicit copy-to-resource action requires its own scope UX.

For narrow viewports or limited pointer precision, the contextual “Move…” action provides a destination dialog with parent and position. This is also the non-drag keyboard/touch fallback. Arrow buttons do not remain the main ordering UI.

## Keyboard and assistive technology

Tree rows use a single roving tab stop, standard Up/Down navigation and Left/Right collapse/expand. Home/End jump within the visible tree. Enter selects; Tab proceeds to inspector/tool controls. A focusable drag grip uses Space to lift, Up/Down to choose a sibling boundary, Right/Left to change nesting only where legal, Enter/Space to drop and Escape to cancel. Do not hijack these keys while editing text. Announce changes through a polite live region: “Moved FAQ to position 4 of 6 in Home.” A modal Move dialog provides equivalent functionality without spatial interaction.

Undo uses Cmd/Ctrl+Z outside editable controls. Redo uses Cmd/Ctrl+Shift+Z; native field undo keeps priority while typing. Cmd/Ctrl+S saves the active named resource. Escape dismisses the topmost transient surface, then cancels a drag, then clears canvas selection as appropriate. Tooltips appear on hover and focus; every icon button has an accessible action label, not the icon filename.

Use modal focus trapping only for actual modal surfaces such as destructive template replacement or a destination dialog; ordinary inspectors are nonmodal. Restore focus to the opener or nearest surviving row after removing a node. Menu tree exposes level and expanded state. Disabled actions include an adjacent reason when the cause is not self-evident. Busy operations announce progress once and do not repeatedly speak every rerender.

Target text contrast at least 4.5:1 for normal text, 3:1 for large text and meaningful control boundaries. Measure actual computed colors after coding. Never rely on the generated image as contrast evidence. At 200% zoom, controls remain reachable and panels can collapse. The editing workstation targets desktop/tablet; mobile controls preview a mobile storefront rather than promising a full phone editing UI.

Reduced motion removes smooth scrolling, ghost animation and automatic canvas motion. Keep clear static placement feedback. Previewed sliders/videos follow the package's pause, keyboard and reduced-motion behavior; do not autoplay distracting previews in the library.

## Contextual inspector

Inspector header: human component name, resource scope, visibility, duplicate and More. Under it use a compact breadcrumb for child blocks. Open Content by default; expose Media, Source and links, Layout, Appearance, Behavior, Results and Form and consent only where applicable. Block lists appear in the outline and a concise inspector list; selecting a block swaps the fields rather than expanding every block form at once. Search settings can reveal and focus a field across collapsed groups.

The [coverage appendices](coverage/index.md) map every declared field, default, type, choice, bound and nested block. No unknown HTML, dynamic renderer or executable merchant input is introduced. Grouping metadata is an editor concern; preserve the serialized contract.

| Existing data | Proposed control | Required behavior |
| --- | --- | --- |
| Bounded plain text | Labeled text/multiline field | Retain max length and plain-text semantics; count remaining characters near limit |
| String enum | Adaptive segmented choice or select | Measure actual labels and available field width; preserve exact stored enum values and inherited/default meaning |
| Boolean | Adaptive Enabled/Disabled choice or select | Keep a true boolean value and explicit opposing labels; use meaningful field-specific labels when needed |
| Integer | Numeric input with optional bounded slider | Exact min/max/step; editable number always available; expose source units (4px/8px) clearly |
| Ordered string array | Text-item list with add/remove/grips | Exact min/max item count and each string's bound; multiline paste can create items with preview |
| Asset reference | Searchable picker, thumbnail, alt/decorative controls | Preserve missing asset ID with warning; replacement is undoable; decorative removes required alt without deleting it |
| CMS/category/product reference | Searchable typed picker | Show scope and unavailable source; retain opaque ID; no price/stock/customer snapshots in settings |
| Route binding | Read-only “Current product/category” source chip plus explicit override behavior if supported | Preserve route context; do not silently turn a route-bound template into a fixed product |
| Colors | Swatch + hex field | Validate exact schema and required foreground/background pairing; measured contrast message |
| Typed blocks | Reorderable list + contextual block settings | Enforce permitted kinds, capacity and extra package constraints |

### Adaptive choice presentation

The user's requested rule applies to enum and boolean choice fields throughout the inspector. Short sets such as Page/Block or Enabled/Disabled use segmented toggles when the complete labels fit in one row. Use a select when there are more than four choices or the labels do not fit. Reference pickers retain their search and source-specific behavior.

Measure the rendered labels using the real font, weight and padding against the field's available width. Equal-width segments must accommodate the longest label in every segment, including gaps and borders. Do not decide from character count or a fixed viewport breakpoint. Never wrap, truncate labels, shrink readable text or overflow the panel to force toggles to fit. Recalculate on inspector resize, label/locale changes and font loading. The local specimen uses two to four choices as the small-set limit; six destination types remain a select even in a wider inspector.

Presentation changes are UI state only: preserve the exact selected value, validation, resource, dirty state and undo history. Keep booleans as true/false, not strings. Native radio groups provide one selected choice and arrow-key behavior; the select exposes the same field label and options. Only the active presentation is visible and tabbable. If a focused field changes presentation during a resize, move focus to the matching selected control without scrolling. Keep 32px pointer targets and 44px touch targets.

An isolated working specimen lives at `uiux/theme-editor/controls.html`, with an inspector-width slider and short/long label examples. Page/Block is illustrative sample data, not a new registered product field. No product renderer or serialization was changed.

### Conditional controls and validation

Conditional controls must preserve hidden values: e.g. custom spacing reveals numeric padding; theme spacing collapses it; decorative image changes alt validation; popup delay appears for delayed behavior and day count for day frequency. Keep one email form per forms section, no more than two image blocks in a two-image story, unique anchors and paired link label/target rules. Unavailable references must not disappear on save/reload.

Edit fields responsively using a local draft value; validate on blur and before save. Group one continuous text editing session or slider gesture into one undo command. Show errors at the specific field and in a concise save error summary with links; preserve focus and entered text. Do not turn temporary half-entered hex values into renderer errors replacing the whole canvas.

## Visibility, duplicate and remove

Generic visibility is a proposed editor contract addition. In the sandbox, keep a local visibility map; hidden sections remain muted in the outline with an eye-off marker and a “Hidden” label. Hide them in Preview; an Edit-mode Show hidden toggle exposes their selectable boundary. Distinguish this from existing popup viewport visibility and menu audience visibility. Do not serialize a new generic field into current strict product contracts.

Duplicate inserts next to the original, selects the new copy, regenerates identities and validates limits. Remove first opens a confirmation dialog naming the target and affected children or association. Cancel receives initial focus; Cancel or Escape leaves the draft unchanged and restores focus to the opener. Confirm removes the target as one undoable draft edit, selects the nearest surviving sibling and offers Undo. Removing a menu with children names its descendant count. Removing a menu assigned to Header/Footer is disabled until reassigned; display its usages. No permanent backend deletion is implied.

Optional-image actions are bare pencil and trash glyphs with transparent, borderless 32px hit areas, 44px on touch, accessible names and hover/focus tooltips. The trash glyph alone turns red on hover/focus; retain the keyboard focus ring. Removing an association opens “Remove image?” with “Remove this image from Journal? The file stays in your media library.” Confirm clears the local association only; Undo restores it. This behavior is implemented in the isolated icon gallery specimen.

## Viewports and preview

The user selected fluid Desktop preview on 2026-09-10. Desktop fills the entire available preview container at its actual CSS-pixel width, with no fixed 1440px viewport, maximum width or transform scaling. Browser resizing and opening/closing editor panels resize the storefront viewport naturally. The theme retains its own responsive breakpoints and intentional content-width settings; the editor must not impose a theme content cap. Show the actual iframe viewport dimensions. Editor panels stay outside the storefront document.

Tablet remains 768px and Phone remains 390px. At insufficient workspace width, keep those device widths and allow horizontal workspace scrolling at 100%. Returning to Desktop restores width:100% and max-width:none and clears obsolete horizontal workspace offsets. Device changes and browser resizing must not recreate/navigate the iframe, reset draft values, switch resources or add undo commands.

The isolated `uiux/theme-editor/viewport.html` specimen demonstrates Desktop/Tablet/Phone, optional editor panels, responsive sample content and a preserved heading edit. Desktop uses a flexible grid column with min-width:0; the iframe fills it without a maximum-width container. This supersedes the original fixed-desktop proposal and does not integrate the actual editor.

Preview is a separate local mode with viewport controls, local sample navigation and Return to editing. Refresh preview rerenders the current buffer without discarding edits. Resource reload is a different action described in [states and resources](states-and-resources.md). External or unavailable native routes show a local handoff explanation in this isolated sandbox; they do not open Magento.
