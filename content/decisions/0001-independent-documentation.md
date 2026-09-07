# ADR 0001: independently owned documentation

Status: accepted by explicit user request. Date: 7 September 2026.

## Context

MageThemeEditor research began in the shared project-docs repository. The product workspace's
`.docs` symlink pointed to that shared folder. The user requested a separate documentation project
inside MageThemeEditor, following useful shared conventions while retaining independent ownership.

## Decision

Use `MageThemeEditor/docs` as a standalone local Git repository and `docs/content` as the authored
source of truth. Configure its own MkDocs Material site, `.pages` navigation, Mermaid, dependency
lock, local preview, and verification. Generate disposable output in ignored `docs/site`.

Preserve the original shared research and copy it exactly into the new architecture area with
recorded [provenance](../architecture/research-provenance.md). New summaries and decisions live here.
Repoint the workspace `.docs` symlink to `docs/content` after verifying the copy and local site.
Root guidance explicitly routes future product documentation to this project.

## Consequences

Documentation can have its own source remote, host, domain, and access policy. None was
configured by the initial setup decision. The user subsequently selected
[jobrandon/magethemeeditor-docs](https://github.com/jobrandon/magethemeeditor-docs) and authorized
source delivery to `main`; hosting remains unconfigured. Shared publishing infrastructure and identities are not inherited.
Commits, pushes, and deployment follow explicit user authorization and current workspace guidance.

The parent routing file and symlink sit outside the standalone docs Git boundary. A later product
repository must explicitly decide how to reference this nested repository. The historical shared
copy remains available but is not the owner of new product documentation.

## Verification

Use the import checksum, strict build, generated-link checks, browser preview, `.docs` resolution,
and Git ignored-path checks. A local docs setup establishes no Magento implementation or hosted
production environment.
