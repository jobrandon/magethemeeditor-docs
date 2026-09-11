# Storefront navigation implementation receipt

Observed: 2026-09-11. Scope: local Theme Studio navigation only; no Magento route, draft, apply or restore state was changed.

## Implemented

- Browse is the initial canvas mode. Theme menus, tabs, sliders and other non-link interactions remain owned by the preview. Same-tab link intents are validated by the parent before an editor transition; modifier/new-tab links retain their browser semantics.
- Select captures component/menu selection and records a selected link. The compact **Follow link** control performs the same validated parent navigation path.
- `theme-studio-navigation.mjs` resolves declared editor pages, same-page anchors and the local catalog search; unsupported, external and unsafe destinations stay honest handoffs rather than becoming editable pages.
- Dirty page/shared resources are named before a page change. The dialog starts at **Stay here** and Escape stays; it also offers save-and-continue and continue-without-saving. Browser `beforeunload` remains conditional on dirty state and is subject to browser limitations documented in the specification.
- Save acknowledgements now advance the saved baseline without overwriting content changed after the submitted snapshot. Multi-resource save stops on a validation, network or revision failure, retains remaining dirty buffers and does not navigate.

## Verification

`npm run verify` from `product/` passed: 133 tests. New focused coverage verifies declared-route resolution, unsafe handoffs, resource-risk scope and acknowledgement of a newer edit during save. `git diff --check` passed.

Browser acceptance is **not complete** in this receipt: `http://127.0.0.1:4177/theme` returned `404 Not Found` at the check time. No service was restarted because this task must not disturb existing drafts. The required browser flow remains to verify Browse/Select, keyboard Follow link, Stay/Escape focus, save/failure dialog behavior and clean versus dirty navigation once an isolated local preview is available.

This is local editor behavior only. It does not add Magento preview support, native commerce/catalog routes, arbitrary page editing, draft publication or a guarantee that every browser exit is interceptable.
