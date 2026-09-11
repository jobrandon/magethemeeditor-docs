# Tailwind-first editor styling

Read for editor CSS, tokens, layout, variants or style review. Use the project-local
`tailwind-design-system` skill; see [skill routing](../project-skills.md#task-routing).

- **Tailwind CSS v4 first.** Keep layout, spacing, typography, colors, responsive rules and
  interaction states in the owning TSX component's utilities/variants. Extract reusable UI
  into components and explicit variants. Do not introduce Sass/SCSS.
- Keep shared CSS-first tokens, base/reset styles and CSS entry points central. A shell's
  layout belongs to its component. Do not create a stylesheet for every component or rebuild
  the utility system as large `@apply` blocks.
- When utilities cannot express a requirement clearly, explain the exception and colocate a
  small plain `<Component>.module.css`. Use local selectors and shared CSS variables;
  avoid global selectors reaching into siblings or the storefront iframe.
- Before introducing CSS Modules, verify actual module scoping, TypeScript declarations,
  esbuild output and HTML loading of emitted CSS. Renaming a global stylesheet is insufficient.
  Prefer shared variables to `@apply`; do not duplicate Tailwind compilation or token imports
  per module.
- Compile locally with exactly pinned reviewed dependencies and a lockfile. No browser/CDN
  Tailwind runtime. Load the editor entry once per document; scope source discovery to the app,
  use complete static utility names and validated CSS variables for dynamic values.
- Keep editor styling isolated from the storefront. Theme packages own storefront styles;
  portable theme JSON contains semantic settings, not Tailwind classes. React is the editor;
  Alpine is the default storefront interaction layer.
- Apply the standard in the separate review workspace and in authorized editor integration.
  It does not itself authorize a storefront migration or rewrite of static specimens.
  Static review components may use adjacent scoped plain CSS through existing entry points;
  see the [UIUX policy](uiux.md) for their build and viewport requirements.
