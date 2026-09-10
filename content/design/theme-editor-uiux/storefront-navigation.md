# Interactive storefront navigation and unsaved changes

Status: **user-required experience; interaction design documented 10 September 2026**.
The implementation details below are proposed. This document does not claim they are integrated
into the current editor or resume Magento development.

## Experience

The merchant should feel that the editor is a layer over a working storefront. Menus, accordions,
sliders, buttons and links retain their normal behavior while browsing. Following a supported
storefront link loads its destination and updates the editor's page context while keeping the
editor available. The theme remains responsible for storefront interactions; the editor owns
selection, draft state and navigation protection.

Use two explicit interaction states, with **Browse** as the proposed initial state:

| State | Canvas behavior |
| --- | --- |
| Browse | Ordinary link activation follows the destination; component interactions work normally. Keep a compact editor toolbar and an obvious Select tool. |
| Select | Click a component to open its settings. A link inside that component selects it instead of navigating. Offer a visible, keyboard-accessible Follow link action, routed through the same navigation guard. |

Switching Browse/Select preserves edits, selection, viewport and history. Do not require an
undiscoverable modifier key or double-click to follow a link. An implementation can retain an
isolated storefront iframe: the visual experience does not require shipping the private editor
application into the public theme. Editor CSS and theme CSS remain isolated.

## What counts as unsaved

An unsaved change is a difference from the last successfully acknowledged draft save, including
invalid or partially typed values and shared header/footer/menu/settings edits. Selecting a
component, opening a menu, scrolling or changing the preview viewport does not create a content edit.

A **saved but unpublished draft is safe to leave**. Do not warn that it will be lost merely because
it has not been published. Saving a draft never publishes or applies it to Magento.

Check the resources affected by leaving, not only the field currently visible in the inspector:

- Changing the storefront page checks the outgoing page and shared draft. Preserve other page
  buffers and their separate save/history state.
- Leaving the theme/editor session checks every unsaved resource in that session.
- Moving between inspector resources without navigating the storefront keeps buffers in place.

## Navigation behavior

| Action | Required behavior |
| --- | --- |
| Follow an internal page link, use the page picker or editor Back/Forward | Resolve the destination and check relevant unsaved resources before changing page/context. Keep the editor shell for supported pages. |
| Navigate with unsaved changes | Pause navigation and show the named-resource confirmation below. Do not load the destination behind the dialog. |
| Navigate with all affected drafts saved | Continue without a loss warning. Show the destination's actual saved/draft status. |
| Open a same-page anchor or use a menu, accordion, tab or slider | Perform the interaction; it does not leave the editing page and needs no navigation confirmation. |
| Open a link in a new tab | Preserve normal target/modifier behavior where supported; keep the original editor session intact. Do not discard its edits or warn about losing a session that remains open. |
| Leave the editor in the same tab | Guard all unsaved resources. An external site does not acquire our editor controls or preview privileges. |
| Reload, close the tab or leave through browser navigation | Use the browser's native leave warning when there are unsaved edits; browser-controlled exits have limitations described below. |
| Refresh only the preview | Re-render existing buffers without discarding or navigating them. Keep this distinct from reloading saved resources. |

Back/Forward must reconcile the visible destination, editor page selector and actual preview.
Cancelling a navigation must not leave the URL or outline showing a different page. Keyboard link
activation follows the same rules as pointer activation.

## Confirmation and save handling

Use a dialog such as **Leave this page with unsaved changes?** List the affected resource names,
for example “Home page and Shared navigation”, and the intended destination.

Offer three actions:

1. **Stay here** — cancel navigation, retain every value and return focus to the initiating control.
   This is the initially focused action; Escape also stays.
2. **Save drafts and continue** — validate and save the listed resources, then navigate only after
   successful acknowledgements. Use the singular label when only one draft is affected.
3. **Continue without saving** — perform the requested navigation without saving or publishing.
   Do not silently discard resources that the editor can retain.

The explanation must match what will actually happen. For an internal page change, say that
unsaved edits are retained only in the current editor session. For an exit that destroys those
buffers, say that the named unsaved changes will be lost. Saved drafts remain available in both cases.

If validation, connectivity, storage or revision conflicts prevent a save, stay on the current
page, preserve all edits and show the error with a route back to the affected field/resource.
Multiple resource saves are not necessarily atomic: if Home saves but Shared fails, acknowledge
Home accurately and keep Shared dirty. Do not navigate or claim everything was saved. Prevent
duplicate navigation/save submissions and recheck for newer edits before continuing.

## Browser and preview boundaries

The application can provide its own three-action dialog for navigation it controls. Browser tab
closure, reload and document exits use `beforeunload`, whose message and buttons are browser-owned.
It requires prior user interaction and is not reliably fired on every mobile shutdown. Attach the
listener only while unsaved changes exist; do not promise that every browser exit can be intercepted.
See [MDN's beforeunload behavior and limitations](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event).

One editor-level navigation controller should handle canvas links, page selection and supported
history actions. A storefront preview bridge sends a navigation intent; the parent validates the
message origin/source, destination and preview scope before approving the transition. Keep draft
preview credentials out of external links and public caches. Supported destination resolution must
preserve the intended store view, theme, entity and draft context.

Unassigned Magento pages, unsupported routes and external destinations need an explicit handoff
or a separate browsing view; they must not appear editable without a compatible assignment/adapter.
Working storefront interactions do not imply that a sample form sends email or a fictional cart
places orders. Retain declared capability boundaries until those integrations are implemented.
See [CMS delivery and assignment ownership](../../architecture/cms-page-delivery.md).

## Current source and acceptance gap

Source inspection on 10 September 2026 found:

- `product/editor/theme-studio-frame.mjs` intercepts clicks for selection in Edit mode. Preview
  mode sends link intents to the parent; sample interactions remain theme-owned.
- `product/editor/theme-studio-app.mjs` starts in Edit mode, switches known local page contexts,
  presents handoffs for unavailable destinations and already checks dirty resources on browser
  unload. Internal `switchPage` preserves buffers without the new confirmation flow.
- The [Resource Desk receipt](implementation-2026-09-10.md) records bounded local navigation and
  draft behavior. It does not prove arbitrary storefront browsing with persistent editor controls.

The new default interaction state, unified navigation guard and save-before-continuing dialog
remain implementation work. This documentation pass changes no product or Magento runtime.

## Acceptance for the next UI batch

Verify with isolated local drafts before extending Magento preview integration:

1. Ordinary links and keyboard activation navigate; menus, sliders and tabs still work. Select and
   Follow link remain distinct, usable by keyboard and consistent with their labels.
2. A clean page and a saved-unpublished draft navigate without warnings. A dirty page, shared draft
   or combination prompts with the correct resource list and destination.
3. Stay/Escape preserves values, selection, page, URL and focus. Continue without saving retains
   internal buffers and does not issue save/apply calls; a destructive exit explains its loss scope.
4. Save-and-continue waits for acknowledgements. Validation failure, stale revision, interrupted
   saves, partial multi-resource success and edits made during save never silently lose work.
5. Page picker, canvas links, editor history and supported browser history use consistent guards.
   Browser reload/close warnings occur only for unsaved work, subject to browser limitations.
6. Same-page interactions, preview refresh, device changes and opening a separate tab preserve
   drafts. Unsupported destinations retain honest handoffs and never receive preview credentials.

Record actual browser/test evidence separately from this specification. Existing navigation and
resource rules in the review documents are refined by this page; historical receipts stay unchanged.
