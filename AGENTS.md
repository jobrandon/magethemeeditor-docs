# MageThemeEditor documentation

Inherit the workspace AGENTS. Read `README.md`, affected pages and
`content/contributing/policies/documentation.md` before documentation work.

- This independent Git repository owns `content/`; the workspace `.docs` points here.
  It overrides ancestor/shared-project-docs routing and automatic commit defaults.
  Never borrow the shared repository's remote, host, credentials or publishing workflow.
- Keep product implementation outside docs. Preserve unrelated changes and the byte-identical
  historical research baseline; add corrections separately.
- Use lowercase Markdown paths, relative `.md` links and explicit `.pages` navigation.
  Separate decisions, proposals, dated evidence and current execution status.
- Keep secrets, customer data and raw exports out. Ignored `.local/` holds scratch;
  generated `site/` is never authored source.
- Run `make verify` after content changes and inspect affected pages locally. A successful
  docs build is not runtime or deployment proof.
- Commit/push/publish only when requested; use Conventional Commits and stage only scoped
  sources. Verify actual branch/remote/account; the source destination is
  `jobrandon/magethemeeditor-docs`, `main`. Hosting is separate authorization.

Read development skills only for matching implementation work, not ordinary Markdown/status.
Keep detailed authoring and verification guidance in the documentation policy and README.
