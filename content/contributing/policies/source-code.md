# Source code policy

Read for authored editor code, source refactors or code review. Paths are relative to the
workspace root. Read the relevant [development skill](../project-skills.md#task-routing)
and affected package README; do not load unrelated skills.

## Types and responsibilities

- Use strict TypeScript: `.tsx` for maintained React components/providers/hooks and `.ts`
  for models, controllers, services and contracts. This does not migrate Magento/PHP,
  external theme packages or unrelated Node scripts.
- Validate external values as `unknown` before use. Do not suppress errors with blanket
  `any`, disabled strictness, `@ts-nocheck` or unexplained assertions.
- Keep the application root as readable composition. Separate UI, reusable controls,
  state/history, network/persistence and preview communication. Pure domain logic must
  not depend on React, the DOM or a live Magento installation.
- Give components narrow APIs, hooks focused responsibilities and contexts explicit scope.
  Do not relocate a monolith into one giant hook or catch-all state provider.
- Keep theme-specific registration behind adapters. Portable theme JSON, packages and
  contracts must remain independent of React, editor libraries and Tailwind class names.
- Maintain named, formatted source, never hand-packed render trees or minified code.
  Generated bundles belong only in ignored build output. Explain non-obvious invariants,
  especially draft/save races, history ownership and iframe trust checks.

## Spacing

- Group imports at the top. Use one blank line after imports, between definitions and
  individual hooks, after guards, between distinct steps, and before a final return after
  preparation logic. Keep related statements and object properties together.
- Use multiline braced conditional and loop bodies, including early-return guards.
  Keep closing braces and dependency arrays visible. Name intermediate expressions when
  nesting obscures control flow; avoid blank lines after every statement or stacked blanks.
- Review logical grouping as well as running Biome. Formatting alone does not enforce it.
  Apply to new/touched source; keep broad reformats scoped and separate from behavior changes.

## Component ownership and verification

- Shared UI belongs in `product/editor/components/<Component>/`; feature UI belongs in
  `product/editor/features/<feature>/components/<Component>/` or its existing boundary,
  such as `product/editor/liquid/`. Colocate exclusively owned hooks, types and justified
  custom CSS. Shared services/state keep their own boundaries; `talons/` is not required.
- An `index.ts`, story, test folder or CSS file is optional. Add only useful files supported
  by the existing tooling; avoid repository-wide re-export barrels and cycles.
- Follow [Tailwind-first styling](styling.md) for visual changes. The optional
  [component template](templates/component.md) illustrates ownership and spacing.
- Activate exact reviewed Node 24 LTS/npm pins from `product/.nvmrc` and `package.json`.
  Preserve other projects' runtime defaults. Maintain real type checking; esbuild only transpiles.
- `npm run verify` must cover types, lint, formatting, tests and build failures. Keep focused
  `typecheck`, `lint`, `format:check`, `build` and `test` commands available. Use meaningful
  behavior tests, including positive/negative contract cases, and browser checks where needed.
  Do not add tests solely for file sizes or private implementation structure.
- File moves must update imports, entry points, emitted assets and served routes together.
  Keep the source map and contributor commands current. Use disposable drafts for save tests;
  a folder split or passing formatter is not proof of maintainability or working runtime.
