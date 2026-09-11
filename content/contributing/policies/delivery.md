# Dependencies, Git and status delivery

Read the matching section before adopting dependencies or performing authorized Git/Linear work.
This policy adds no permission to publish, purchase, accept contracts or start marketplace tasks.

## Third parties

Follow the [adoption and commercialization requirements](../../requirements/third-party-compliance.md)
before adding/upgrading dependencies, SDKs, themes, assets or hosted services. Record exact
version/edition, authoritative terms, intended use, direct/transitive coverage, obligations and
review outcome. Include copied code, fonts/images and service terms; distinguish browser delivery,
hosted use, Magento distribution and development-only tooling. Preserve notices and reassess
changed versions, editions, uses and release inventories. Resolve unclear rights with qualified
review when needed; routine clear terms do not require an extra approval or universal legal sign-off.
A scanner or license-name match is not proof of compliance with all laws.

`theme-flux/` is untouched third-party capability reference material. Do not copy or translate
its code, schemas, templates, behavior, CSS, icons, fonts or assets, or import it at build/runtime.
Create original implementations within the approved contracts.

## Git and publication

- Commit, push, open PRs or publish only with user authority. Inspect repository root,
  branch/SHA, status, remote visibility, authenticated identity and remote history first.
  Resolve visibility explicitly before pushing proprietary source to a public remote.
- Stage only scoped reviewed files and preserve unrelated changes. Never force-push without
  explicit authority. Keep generated output, credentials, customer data, raw exports and
  client licenses out of source and reports; ignored `.local/` holds disposable evidence.
- Use Conventional Commits: `type(scope): imperative summary`. Choose `feat`, `fix`, `test`,
  `docs`, `build`, `ci` or `chore` as appropriate; scope is optional. Explain intentional
  breaks with `!` and a `BREAKING CHANGE:` footer. Add useful rationale/verification details,
  reference only real relevant issues and do not imply open acceptance criteria are closed.
- Documentation is a separate Git repository; never absorb its working tree, `.git` or
  generated site into product. Native installation source must remain uncommitted locally.

## Linear and acceptance

Read live issues and dependencies before authorized updates. Preserve acceptance text and
ownership; mark only started work active and use Done only when all applicable criteria have
evidence. Separate source/tests, local runtime, browser checks, native commerce and production
release proof. Do not treat a queued task or a preview as completion. Use the optional
[change receipt](templates/change-receipt.md) when durable evidence is needed.
