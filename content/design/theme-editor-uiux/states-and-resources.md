# Draft states and resource scope

Implementation update · 2026-09-10: the user subsequently requested integration into the actual local product. See [Resource Desk implementation and verification](implementation-2026-09-10.md). The design-phase status and sandbox restrictions below are preserved as historical context.

Status: **proposed**, 2026-09-10. This document separates merchant-facing concepts from what the current local editor actually persists. [Review overview](index.md).

## Resource ownership

| Editing context | Draft owner | Current fields / limits | Proposed save label |
| --- | --- | --- | --- |
| Current page | One page buffer | Template, head title, meta description, typed section array | Save page draft |
| Header | Shared global buffer | Wordmark, announcement, header menu assignment, dropdown/mega navigation layout | Save shared draft |
| Footer | Shared global buffer | Footer note, footer menu assignment | Save shared draft |
| Theme settings | Shared global buffer | Accent hex, sans/serif typography preset, compact/comfortable/spacious spacing | Save shared draft |
| Menus | Shared global buffer | Named menus, assignments and nested items | Save shared draft |

Header, Footer, theme settings and all menus currently share one global revision. Present them as understandable editing contexts, but do not imply they can currently be independently committed. Before saving, a scope detail shows all changed shared contexts: for example “Header announcement + Main navigation.” Saving a page must not save shared edits or other page buffers. Switching contexts preserves unsaved buffers.

Show the affected theme/store scope and assigned pages, not an unqualified “whole store” claim. In the sandbox the scope is “Silt & Form sample theme”; there is no real store target. Full header/template/footer composition into arbitrary shell nodes is a proposed extension. The current source uses a fixed shared shell and a separate shell package.

## Distinct commands

| Action | Meaning and result | Unsaved/undo treatment | Backend relationship |
| --- | --- | --- | --- |
| Undo / Redo | Reverse/reapply one local editing command in the active resource | No network. Navigation is excluded. New edit clears the redo branch | Current editor has session-wide snapshots capped near 40; proposed per-resource grouping differs |
| Refresh preview | Re-render current draft buffer at current viewport | Keeps every edit and history entry | Separate from reload; sandbox-only renderer |
| Reload saved resources | Retrieve latest persisted drafts | Clean state: reload. Dirty state: show changed resource list and Keep editing / Discard and reload; never silently discard | Current refresh reloads all resources and resets history; its UI disables reload while dirty |
| Save page/shared draft | Persist the named resource after validation | Acknowledged save becomes the clean baseline; other buffers untouched | Current save API distinguishes page versus global and clears history; redesigned behavior needs deliberate reconciliation |
| History | Browse saved draft snapshots and compare scope/content | Viewing is read-only | No general draft revision archive currently exposed; sandbox uses bounded local sample history |
| Restore as draft | Copy a chosen saved revision into the editable buffer | Preserve current work as a recovery snapshot; one undoable local command; explicitly requires Save to persist | Proposed new draft workflow, not the current previous/original native restore actions |
| Preview | Inspect present draft at selected viewport without editor overlays | Keeps unsaved state; Return to editing restores selection | Local sample route only |
| Return/back | Return to page/theme overview or previous editor context | Internal navigation preserves buffers. Leaving unsaved session offers save scoped draft / leave without saving / keep editing | Does not restore, reload or apply anything |

“Save draft” does not apply the theme. “Saved” means persisted draft, not live storefront. “Applied” is only valid after an actual target acknowledges a complete saved snapshot and the UI identifies that snapshot. No applied state is executed or fabricated in this review. If a later sandbox displays the visual applied-state example, it must say “Sample state” and remain disconnected.

The current live toolbar's **Restore previous** restores a previous complete applied theme/menu/page snapshot. **Restore original** restores original native page output while retaining saved resources. These are materially different from restoring a historical draft. In a future product UI, put them in clearly named applied-theme recovery actions with affected routes and a review step; never wire “Restore as draft” to either native endpoint. Native recovery is outside this review's execution scope.

## Visible states and copy

| State | UI and copy | Allowed next actions |
| --- | --- | --- |
| Clean saved draft | “Draft saved · 11:24” with resource name available in status details | Preview, edit, history, reload; save disabled because unchanged |
| Unsaved | “Unsaved changes” with readable dot + text; affected-resource count in details | Save active scope, undo, navigate while buffers remain |
| Another resource dirty | “Home saved · Shared changes unsaved” | Jump to that resource; never show a globally clean status |
| Saving | “Saving Home draft…”; disable duplicate save only for involved scope | Maintain readable preview; prevent conflicting commands in that scope |
| Saved acknowledgment | “Home draft saved” then quiet timestamp | Keep other buffers and independent undo stacks intact if implemented |
| Validation failure | “Check 2 fields before saving” with links | Focus first error; maintain all text and selection |
| Storage/network failure | “Draft could not be saved. Your edits are still here.” | Retry or continue editing; no false success transition |
| Storage unavailable in sandbox | “Browser storage unavailable. Changes last for this session.” | Keep session editing and explicit limitation |
| Stale saved revision | “A newer draft is available” with compare/reload choices | No silent overwrite; sandbox may demonstrate using a local fixture |
| Reload with dirty buffers | Dialog names every draft to be discarded | Keep editing is default; explicit Discard and reload |
| History selection | Timestamp, resource and short change summary; current saved entry marked | Read-only compare, then Restore as draft |
| Restore-as-draft result | “Revision restored to draft. Save when ready.” | Undo restore, edit, save; never claim live change |
| Missing source | “Selected category is unavailable” at source picker and canvas block | Replace source or keep editing; ID preserved |
| Provider unavailable | “Pickup information is not connected” | Inspect visual settings; no inventory or success fabrication |
| Applied example | “Sample state · Saved revision applied” only inside an explicit state specimen | No executable apply/restore bridge |

Timestamps in specimens use 2026-09-10. Actual browser save events in the eventual local prototype should use real local time and retain a “Design draft” context marker. Do not render invented revisions as received Magento acknowledgments.

## Nested menu editing

Menu selection sits in Shared resources; assignment chips show Header or Footer usage. Display named resources and Add/Duplicate menu actions. Current limits: 1–12 menus, maximum three levels of items and maximum 100 items across the global resource. Duplicate recursively regenerates all item IDs. Prevent removal of an assigned menu and of the last remaining menu.

Selecting a menu item exposes Label, Destination type, Destination, Optional image, Short description, Audience (everyone/guest/customer/hidden) and Open in new tab. Destination types currently include theme page, native route, CMS page, category, product and external HTTPS. Changing type clears incompatible selection with a visible prompt rather than carrying an invalid old ID. Reference controls preserve unavailable destinations so the merchant can repair them. External targets retain existing safe-HTTPS and no-credentials rules.

Menu drag supports before, after and within. Horizontal target indentation only appears for legal parents; reject descendants/cycles and subtrees that would exceed three levels. Maintain stable IDs and menu ownership. Keyboard Move… offers the same legal parent and position choices. The current product only drags siblings and uses Indent/Outdent buttons for nesting; this richer interaction is a prototype proposal.

Show “Used by Header” beside shared editing controls. An item's eye/visibility indicator must distinguish hidden from audience-restricted; a customer-only menu link is not globally hidden. The sandbox provides fictional audience preview states without fetching any customer session. Visiting a native account/cart destination shows a local handoff explanation and does not authenticate, submit a form or call Magento.

## Review scenarios

| Scenario | Before | Interaction | Expected visible result |
| --- | --- | --- | --- |
| Insert then undo | Home has 6 sample sections | Drag Multi-column cards after Hero; undo | 7 then 6 sections; exact prior IDs/order restored |
| Reorder nested block | Cards: Morning, Table, Keep | Move Keep before Morning using grip; Escape on second attempt | Keep/Morning/Table after first commit; cancel changes nothing |
| Select and edit | Hero unselected | Click headline, edit heading, blur | Hero selected in tree/canvas; inspector retains caret; Home dirty |
| Hide and preview | FAQ visible | Hide FAQ; enter Preview; exit; undo | Hidden in preview, muted/selectable in tree; restored by undo |
| Page versus shared | Home heading dirty | Edit Header announcement; save shared; switch About then Home | Shared clean, Home still dirty; both edits preserved |
| Nested menu | Journal under Studio | Drag into Shop; undo; attempt depth 4 | Legal move reflected in menu preview; undo exact; depth 4 rejected |
| Reload versus refresh | Home heading dirty | Refresh preview, then request Reload | Refresh keeps change; Reload prompts with dirty resource name |
| Save and restore | Two saved local revisions | Inspect older, Restore as draft, undo | Older content in dirty buffer; no publication; undo returns current content |
| Missing reference | Featured products points to missing category | Open source picker | Missing selection retained; no empty-string replacement |
| Keyboard placement | Library open, focus on FAQ | Insert using destination dialog | Valid location announced and selected; focus returned correctly |
| Responsive view | Desktop fills available container | Resize browser, hide/show panels, Tablet 768, Phone 390, then Desktop | Actual viewport follows available space without a cap or scaling; edits, selection and resource unchanged |

These scenarios define later browser acceptance; they have not been executed against an interactive redesign in this visual-selection phase.
