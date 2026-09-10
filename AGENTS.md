# MageThemeEditor documentation agents

## Ownership and routing

This standalone repository owns MageThemeEditor documentation. Its source of truth is
`/Users/branorphiano/Projects/jobrandon/MageThemeEditor/docs/content`.
The parent workspace's `.docs` symlink resolves here. The sibling shared docs repository is
only the historical source for the copied research and a setup reference.

The user's product-specific routing overrides the fixed repository paths, remote, domain,
hosting project, and identities in the `shared-project-docs` skill. Reuse authoring conventions,
not that repository's infrastructure. Do not modify the shared original during normal product work.

## Before editing

1. Read the workspace `../AGENTS.md`, this file, `README.md`, the affected pages, and any nearer instructions.
2. Inspect `git status --short --branch`, the repository root, and current remotes before Git work.
3. Preserve unrelated changes. Product code belongs in its application repository, outside this one.
4. Read the decision register and distinguish confirmed direction, proposals, open questions,
   observed evidence, and verified implementation.

## Task-based skills

The canonical task-to-skill map is in `../AGENTS.md`; installed project skills are in
`../.agents/skills/`. Markdown authoring, evidence updates, navigation edits and established
MkDocs checks use the documentation instructions without loading React, Node or Tailwind
skills. Use `web-design-guidelines` for an actual documentation-interface accessibility or
interaction review; use other development skills only if the changed implementation matches
their runtime and scope. Do not introduce React or Tailwind into MkDocs to satisfy a skill.
Document verified skill use and outcomes without treating guidance as implementation evidence.

## Authoring and evidence

- Put publishable Markdown under `content/`; use lowercase, descriptive filenames and folders.
- Use `YYYY-MM-DD` in dated research, audit, and evidence filenames. Give dated snapshots a clear
  observation date and scope; they are not a live task dashboard.
- Maintain explicit `.pages` order when adding pages. Use relative `.md` links between source pages
  and stable heading anchors. Do not link to a local `/Users/...` path as a website destination.
- Cite primary external sources near factual claims, with meaningful link labels. Label assumptions,
  recommendations, historical reports, and unverified vendor capabilities. Recheck unstable claims
  when making a new decision; copying dated research does not refresh its claims.
- When importing Linear data, read live state, record the timestamp, pagination completeness,
  identifiers and direct links. Never infer completion from an issue title. Do not update Linear
  unless the user authorizes that work.
- Keep `architecture/theme-editor-research-2026-09-07.md` byte-identical to the original baseline.
  Put corrections and later decisions in separate linked pages; update provenance for a deliberate
  future replacement. Never silently rewrite the historical baseline.
- Research is completed; Batch 01 adds a local contract/validation prototype. Merchant interviews,
  editor/connector implementation and Magento runtime checks remain outstanding. Hybrid acceptance
  criteria were synchronized into 13 existing Linear issues; see
  `content/roadmap/batch-01-evidence-2026-09-07.md` for exact mappings and verified readback.
  Synchronization and the local model do not complete those runtime criteria.
- Record branch/SHA, environment, command, outcome, and limits when reporting future runtime proof.
- Follow `content/requirements/third-party-compliance.md` when introducing documentation tooling
  or assets and when recording product dependency choices. Capture exact versions/editions, intended
  use and obligations; distinguish proposed candidates from reviewed adoption and release evidence.
- Keep secrets, customer data, raw exports, and credentials out of this repository. Summarize evidence.
  `.local/` is ignored local scratch space, outside `content/`; `exclude_docs` is a publication filter,
  not an access-control boundary.

## Verification

- Install from the hashed `requirements.txt` using `make setup`; follow `README.md` for lock updates.
- Run `make verify` after changes. It performs a strict MkDocs build and checks generated local links,
  anchors, assets, page coverage, navigation, and source/output separation.
- Inspect changed pages in `make serve`: navigation, headings, long tables, search, and Mermaid.
  For configuration/theme changes, check a narrow viewport and both color schemes as appropriate.
- Generated `site/` is disposable and ignored. Edit the sources, never generated HTML.
- Verify the `.docs` destination and copied-research checksum after routing or import changes.
- Report actual checks and their limits. A successful documentation build says nothing about
  Magento integration, commerce behavior, or a public deployment.

## Git and publishing

- Commit only when the user explicitly asks, following the ancestor workspace's Git rule.
  The shared skill's default auto-commit rule does not apply here.
- Require Conventional Commits: `type(scope): imperative summary`, with a meaningful optional
  scope. Omit parentheses when no scope helps, for example `docs: clarify publication boundaries`.
  Use `docs` for documentation, `build` for dependencies/build tooling, `ci` for automation,
  `chore` for repository maintenance, and `fix` for correcting broken behavior. Select the type
  that best describes the change; use scopes such as `architecture`, `site`, or `workflow` only
  when they clarify ownership.
- Keep commits focused on one coherent outcome and write a concise imperative summary. Add a
  body explaining why, relevant validation, and meaningful limitations when useful. Reference
  real issue IDs only when relevant; never invent issue references or imply uncompleted work
  is closed. Mark an intentional breaking change with `!` and explain it in a `BREAKING CHANGE:`
  footer when applicable.
- Stage only scoped source/configuration changes and inspect the staged diff. Never stage `site/`,
  virtual environments, local evidence artifacts, or unrelated edits.
- Push or publish only when explicitly requested. Local setup/preview is not publication authority.
- The authorized source repository is `https://github.com/jobrandon/magethemeeditor-docs`, on `main`.
  Verify `origin`, authenticated account, branch, and remote history before delivery. Preserve
  existing commits and remote files; never force-push without separate explicit authorization.
- No documentation hosting project, domain, hosting credential, or deploy workflow is configured.
  Source delivery to GitHub does not authorize hosting deployment. Use
  `content/contributing/publishing.md` to prepare separately owned hosting infrastructure.
- Do not borrow the shared docs' remote, domain, hosting project, credentials, or access identities.
- Root-level routing instructions and `.docs` are outside this Git repository. If a product repository
  is later created, handle those files there with explicit scope; do not absorb nested docs by accident.
