# MageThemeEditor documentation

This is MageThemeEditor's independently owned documentation project and local Git repository.
It contains product direction, research, architecture, requirements, decisions, and delivery plans.
Product implementation remains outside this directory.

**Source of truth:** `/Users/branorphiano/Projects/jobrandon/MageThemeEditor/docs/content`.
The workspace's `.docs` symlink points to this source. The earlier shared research is preserved;
new product documentation belongs here.

Research was completed on 7 September 2026. Merchant interviews, implementation, and Magento
runtime validation remain outstanding. Start at [the documentation home](content/index.md).

## Structure

```text
docs/
  README.md                 Local setup and repository guide
  AGENTS.md                 Agent ownership and operating rules
  mkdocs.yml                Material site; content/ in, site/ out
  requirements.in           Pinned direct dependencies
  requirements.txt          Generated complete dependency lock with hashes
  .python-version           Python version used for setup verification
  Makefile                  setup, build, verify, serve
  scripts/check_site.py      Generated-site validation
  content/
    index.md                Documentation home
    product/                Outcomes and adoption paths
    architecture/           Boundaries, original research, provenance
    requirements/           Hybrid adoption and validation criteria
    roadmap/                Delivery stages and dated Linear baseline
    decisions/              Decision register and records
    contributing/           Authoring and future hosting guidance
  site/                     Generated output; ignored
  .venv/                    Local runtime; ignored
  .venv-tools/              Dependency lock tooling; ignored
  .local/                   Local QA artifacts; ignored
```

## Local setup

Use Python 3.14, `venv`, and Make. This setup was verified on macOS with Python 3.14.5.
The commands also target Linux, but Linux and other Python versions were not exercised here.
Initial installation needs network access to PyPI. No system-wide Python packages are changed.

```bash
cd /Users/branorphiano/Projects/jobrandon/MageThemeEditor/docs
make setup
make verify
make serve
```

Open [the local preview](http://127.0.0.1:8017/). Stop it with Ctrl-C. It binds only to loopback.
For a different interpreter, use `make setup PYTHON=python3.14`. For an occupied port, run
`.venv/bin/python -m mkdocs serve --strict --dev-addr 127.0.0.1:8018`.

Without Make:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python -m mkdocs build --strict
.venv/bin/python scripts/check_site.py
.venv/bin/python -m mkdocs serve --strict
```

`make build` creates `site/`. `make verify` also checks every generated HTML page's local links,
anchors and linked assets, authored-page coverage, navigation, and source/output separation.
These checks do not crawl external research citations or validate the Magento product.
Inspect changed pages in a browser, including diagrams and search. Material supplies Mermaid
support; its diagram runtime may be fetched from a third-party CDN by the browser. This setup
disables remote font loading but does not promise an entirely offline browser experience.

## Reproducible dependency updates

Normal installation uses the exact transitive versions and hashes in `requirements.txt`.
Edit direct pins in `requirements.in` only when intentionally updating tooling, then regenerate:

```bash
python3 -m venv .venv-tools
.venv-tools/bin/python -m pip install 'pip-tools==7.6.1'
.venv-tools/bin/pip-compile --generate-hashes --strip-extras --resolver=backtracking \
  --output-file=requirements.txt requirements.in
make setup
make verify
```

Use Python 3.14 to regenerate the lock. Review the dependency diff and browser output. For a new
Python/platform target, verify installation in a fresh virtual environment before documenting it
as supported. Awesome Pages 2.x is retained intentionally for the shared site's `.pages` convention;
a move to the renamed Awesome Nav plugin is a separate tooling migration.

## Authoring

Write Markdown under `content/`, update the relevant `.pages`, and use relative `.md` links.
See [authoring conventions](content/contributing/authoring.md) and read `AGENTS.md` before agent work.
Keep status and sources explicit. Date snapshots and link to current Linear records for current work.

The imported research is byte-for-byte preserved. Its [provenance page](content/architecture/research-provenance.md)
records the source and SHA-256. Add updates in separate pages rather than editing the baseline.
Material features, validation, and navigation configuration follow the
[MkDocs configuration guide](https://www.mkdocs.org/user-guide/configuration/),
[Material diagrams guide](https://squidfunk.github.io/mkdocs-material/reference/diagrams/), and the
[Awesome Pages 2.10.1 source](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/tree/v2.10.1).

## Git and future publishing

Run Git commands from this `docs/` directory. It has its own `.git`; the parent workspace routing
file and `.docs` symlink are outside this repository. Local setup does not authorize a commit,
push, or deployment. Commit only on an explicit user request. Stage specific source/config files;
keep `site/`, environments, scratch output, and unrelated changes out of commits.

The source repository is [jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs),
with `origin` pointing to `https://github.com/jobrandon/magethemeeditor-docs.git` and delivery to `main`.
This checkout uses the authenticated personal GitHub CLI account through an HTTPS credential helper;
credentials are not stored in authored files. Verify the active account and remote before pushing.
Follow the [Conventional Commits standard](content/contributing/authoring.md#commit-conventions)
for focused commits with imperative summaries and useful rationale/validation bodies.

No hosting identity is configured. [Future publishing](content/contributing/publishing.md)
describes preparing a separate static host, selecting visibility/access control, setting the
canonical URL, running the same verification, and deploying only after authorization.
Do not reuse the sibling shared docs repository's remote, domain, Cloudflare project, or credentials.

## Setup verification · 7 September 2026

- Fresh isolated installation from the hashed lock and `pip check` passed on macOS/Python 3.14.5.
- `make verify` passed: 13 source pages, 14 HTML pages (including 404), and 615 local links;
  anchors, linked assets, rendered navigation, and source/output boundaries were checked.
- Browser checks passed for desktop home/navigation, both Mermaid diagrams, search and result
  navigation, dark mode, and the 390px mobile drawer/table layout. Page width remained 390px;
  the wide requirements table scrolled within its own container. Temporary viewport overrides
  were reset. A browser-control timeout was recovered through the documented browser API.
- The research copy is 32,592 bytes and matches the original's recorded SHA-256. `.docs` resolves
  to this project's `content/`, and the same research bytes are reachable through both paths.
- At initial local setup, the standalone repository had no commits or remotes; source delivery
  was subsequently authorized to the GitHub repository above. `site/`, environments, and scratch
  output remain ignored.
- The shared repository's pre-existing changed navigation and untracked research folder were
  preserved. Initial local setup performed no Linear mutation, push, or deployment. The subsequent
  GitHub delivery authorization covers commits and pushes, without a separate hosting deployment.

Limitations: external citations were not exhaustively crawled or revalidated; Linux, Magento
runtime behavior, and a hosted deployment were not tested. The Material package prints an upstream
notice about future MkDocs 2; this site is pinned and verified against MkDocs 1.6.1.
