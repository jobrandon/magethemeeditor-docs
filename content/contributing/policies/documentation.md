# Documentation policy

Read for durable documentation, navigation or MkDocs work. The independent `docs/` repository
owns `docs/content/`; `.docs` resolves there. This overrides shared-project-docs infrastructure:
do not write new product docs to the sibling shared repository or borrow its host, domain,
remote, credentials or publishing workflow. The skill's auto-commit default does not apply.

## Authoring

- Read `docs/AGENTS.md`, `docs/README.md`, affected pages and the
  [decision register](../../decisions/index.md). Preserve unrelated changes and keep product
  implementation outside docs. Use [authoring conventions](../authoring.md).
- Write publishable Markdown under `content/`, using descriptive lowercase paths and relative
  `.md` links. Maintain explicit `.pages` ordering. Do not use local `/Users/...` website links.
- Date research, audit and evidence snapshots `YYYY-MM-DD`; state their scope and evidence
  date. Distinguish confirmed direction, proposal, historical report and verified behavior.
  Cite primary sources near claims and recheck unstable claims when making new decisions.
- Preserve `architecture/theme-editor-research-2026-09-07.md` byte-for-byte. Add corrections
  in separate pages; a deliberate replacement requires updated provenance. Shared originals
  remain untouched. Prior research and Linear synchronization are not current runtime proof.
- For imported Linear data, read live state and record timestamp, pagination completeness,
  identifiers and links. Do not infer completion from titles or update Linear without authority.
- Report branch/SHA, environment, commands, outcomes and limits for runtime evidence. Keep
  changing status in the execution ledger, not instructions or undated assertions.
- Keep secrets/customer data/raw exports out of docs. `.local/` is ignored scratch outside
  `content/`; publication filters are not access controls. Review documentation dependencies
  and assets under the [third-party requirements](../../requirements/third-party-compliance.md).

## Verification and delivery

- Use the hashed `requirements.txt` and README setup/lock commands. Run `make verify` after
  changes; it checks strict build, links, anchors, assets, coverage, navigation and separation.
  Edit sources, never generated `site/` output.
- Inspect changed pages in the local preview. For configuration/theme changes, check narrow
  layout and both color schemes. Check headings, navigation, search, long tables and diagrams
  where affected. Verify `.docs` and research checksums after routing/import changes.
- Report actual limits: a successful docs build is not Magento or hosted deployment proof.
- Follow [delivery rules](delivery.md) and [commit conventions](../authoring.md#commit-conventions).
  Stage only scoped sources, never generated site/environments or unrelated changes.
  The authorized source destination is `jobrandon/magethemeeditor-docs`, branch `main`;
  verify the actual remote/account/history before delivery. Source delivery does not authorize
  hosting; follow [publishing preparation](../publishing.md) for separate infrastructure.
