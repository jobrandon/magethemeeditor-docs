# Authoring documentation

Write durable product documentation in this project's `docs/content`. Edit sources through the
canonical path; `.docs` is a convenience symlink. Read the repository's root `README.md` and
`AGENTS.md` for local commands and ownership rules.

## Content conventions

Use descriptive lowercase filenames and a single page title. Date research, audits, and evidence
snapshots with `YYYY-MM-DD`. Put the page's status and evidence scope near the top. Product plans
must distinguish confirmed direction, proposed implementation, open choices, and verified results.

Use relative Markdown links such as `../requirements/hybrid-adoption.md`, including heading anchors
when useful. Add new pages to their folder's `.pages` ordering. Diagrams use fenced `mermaid` blocks.
Prefer small diagrams and readable tables; keep procedural detail near the decision it supports.

## Sources and updates

Cite primary sources near external factual claims. Preserve the original links and research date
when summarizing the [baseline](../architecture/theme-editor-research-2026-09-07.md). Claims in that
copy are historical research findings, not refreshed vendor or licensing guarantees. Verify unstable
facts when they affect a new implementation or distribution decision.

Keep the research copy unchanged and write corrections or later decisions separately. For Linear
summaries, read live records, verify pagination, record observation time and links, and explicitly
state that the snapshot will age. User instructions may confirm direction without completing work
or updating the issue tracker.

## Verify changes

From the documentation repository, run:

```bash
make setup    # first use or dependency changes
make verify   # strict build and local generated-link checks
make serve    # browser inspection at http://127.0.0.1:8017/
```

Inspect the affected pages, navigation, search, long tables, and diagrams. Generated `site/` is
ignored; source files and repository instructions must not leak into it. The checker does not
validate external websites or product runtime behavior.

Keep local scratch artifacts outside `content/`, in ignored `.local/`. Do not store secrets,
customer data, or raw production exports. Publication exclusions are filters, not access control.
See [future publishing](publishing.md) before preparing a hosted site.

## Commit conventions

Use Conventional Commits to make historical changes easy to scan:

```text
type(scope): imperative summary
```

The scope is optional; include a meaningful area such as `architecture`, `site`, or `workflow`
when it adds context. Without a scope, use `type: imperative summary`.

| Type | Use |
| --- | --- |
| `docs` | Product documentation, authoring guidance, or architecture records |
| `build` | Documentation dependencies and build tooling |
| `ci` | Continuous integration or authorized delivery automation |
| `chore` | Repository maintenance that fits none of the above |
| `fix` | Corrections to broken behavior, such as the site link checker |

Keep each commit focused on one coherent outcome. Describe the change with an imperative verb,
for example `docs(workflow): define commit conventions`. Add a body explaining why the change
was needed and relevant validation or limitations when useful. Use real issue references only
when relevant; do not invent issue IDs or use a closing reference for unfinished work. Mark an
intentional breaking change with `!` and explain it in a `BREAKING CHANGE:` footer when applicable.

Commit and push only when the user authorizes that scope. The source repository is
[jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs), using `main`.
Inspect remote history before integration, preserve existing files/commits, and never force-push
without separate authorization. Stage authored content/configuration/tooling only; `site/`,
virtual environments, caches, and secrets stay excluded. A source push does not itself authorize
a separate hosting deployment.

Tooling references: [MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/),
[Material Mermaid support](https://squidfunk.github.io/mkdocs-material/reference/diagrams/),
[Awesome Pages 2.10.1](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/tree/v2.10.1).
