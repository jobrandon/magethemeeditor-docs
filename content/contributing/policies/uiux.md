# Separate UIUX review workspace

Read when working in `uiux/theme-editor/`. The reviewed concept is separate from product
integration. Its README and package/lock files define the local specimens and toolchain.

- Own this review directory and scoped design docs. Use `product/` and `component-library/`
  as read-only references. Inspect current editor behavior and the component registry; cover
  current controls without displaying every type on one screen.
- Preserve the useful layout; prioritize component discovery, direct drag/drop, clear
  selection/drop feedback, progressive settings, accessibility and undoable interactions.
  Ordering arrows must not remain the primary interaction.
- Use local sample data. Never call Magento apply/restore bridges, mutate native data or
  import server modules that can. Clearly distinguish prototype state from publication
  without exposing implementation detail in the merchant UI.
- Use a separate free loopback port. Do not replace or stop the main editor on 4177, install
  dependencies into product or resume old goals/automation. Integration is separate scope.
- The user's design task uses Astra Extra High for the named problem of coherent extensible
  interaction across the catalog, nested drag/drop and page/shared revision states. Its one
  authorized icon sub-agent completed; reuse reviewed assets and do not spawn replacements.
- Icons cover selection, phone/tablet/desktop, back, restore/history, save, draft, reload,
  undo/redo and visibility. Keep labels/tooltips, focus/active/disabled states and consistent
  style; restore, reload and undo have distinct semantics. Preserve reviewed sources/notices.
- Use the relevant Product Design workflow and [task-specific skills](../project-skills.md#task-routing).
  The target/outcome are known; do not repeat intake. Static specimens need no React/backend
  skills merely to be styled or served. Report artifacts and remaining design choices.

## Styles and viewport

Follow [Tailwind-first styling](styling.md). This workspace's reviewed toolchain uses Node
22.22.0/npm 10.9.4 and Tailwind/CLI 4.3.3; read `third-party/tailwind-review.md` before changing
it. Do not silently replace this separate toolchain with product's Node 24 pin. Use
`npm ci --ignore-scripts`, `npm run build` and `npm run verify:css` when appropriate.

Keep shared tokens in `styles/tokens.css`, entries under `styles/`, and generated CSS under
`compiled/`. Use `source(none)` and exact specimen source paths. Existing entries omit
Preflight intentionally; preserve base styles, adaptive controls, focus and notices.
Colocate small scoped plain-CSS exceptions with their specimen and import through its entry.
No Sass, duplicate Tailwind entries or framework migration merely to match folder conventions.

Desktop preview fills available canvas at actual CSS-pixel size: `width: 100%`, `max-width: none`,
no fixed width or scaling. Resize without reload or loss of edits. Tablet/Phone remain
768px/390px with workspace scrolling as needed. Preserve theme content-width settings and
editor/storefront document isolation. The review specimen is `viewport.html`.
