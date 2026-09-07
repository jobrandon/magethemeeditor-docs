# Future separate publishing

Status: source delivery is authorized to
[jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs) on `main`.
No hosting project, domain, hosting access configuration, hosting credential, or deployment
workflow is configured. Local builds and preview are available now.

## Decisions to make when hosting is requested

Choose the documentation audience: internal planning, private beta partners, or public product
documentation. The current content includes planning and Linear links that require separate
authorization to view. Review the intended audience before publishing; hiding navigation is not
access control, and search indexes contain page text.

The source repository is selected. Choose a separately owned host/project name, domain or subpath,
access policy, and credentials. Static hosts can consume the generated `site/` directory. Cloudflare Pages is one
possible later host, but it has not been selected or configured by this setup. Do not reuse the
shared documentation site's remote, domain, hosting project, credentials, or access identities.

## Build contract for future hosting

| Setting | Contract |
| --- | --- |
| Source repository root | This standalone `docs/` repository |
| Runtime | Python 3.14; local verification uses 3.14.5 |
| Install | `python -m pip install --require-hashes -r requirements.txt` |
| Build | `python -m mkdocs build --strict` |
| Verify generated output | `python scripts/check_site.py` |
| Artifact directory | `site/` |
| Canonical URL | Set `site_url` in `mkdocs.yml` to the approved URL, including any subpath |
| Source links | `repo_url` points to the approved GitHub repository; source links use `main/content/` |

The build commands assume the selected Python environment is active. Pin that same runtime in
future CI and install the existing lock. Do not copy another project's deployment workflow with
its destination IDs intact. The current repository intentionally has no auto-deploy trigger.

## Authorized publication sequence

1. Review the content, audience, sensitive exclusions, source diff, and generated artifact.
2. Prepare product-specific hosting configuration and access policy for the selected source repository; store credentials
   only in the selected host's secret store. Confirm ownership of the destination.
3. Set the approved canonical URL and any subpath; rebuild and check links under that path.
4. Commit/push/deploy only within the user's explicit authorized scope. Treat a push to a future
   auto-deploy branch as a publishing action.
5. Verify the actual hosted result: landing/deep links, assets, search, Mermaid, mobile navigation,
   HTTPS/canonical URLs, and expected unauthenticated/authenticated access behavior.
6. Record commit, build artifact/release identity, destination, timestamp, results, and rollback path.
   Retain a previous deploy artifact or documented host rollback mechanism.

`site/` is disposable generated output, not authored content. No local build or preview is evidence
of a deployment. Remote diagram assets and any future analytics should be reviewed against the
selected host's privacy, CSP, and availability requirements.
