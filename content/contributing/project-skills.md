# Project development skills

Status: accepted for project-local development guidance on 10 September 2026.
The user authorized the five selected skills after reviewing the research shortlist.
This is a tooling adoption record, not commercial product release clearance.

## Installed scope

The workspace uses `.agents/skills/` for these five standalone skills. Personal and system
skill directories are unchanged. Invoke a skill by its name or let Codex select it when
the task matches its description. Read individual rules as needed instead of loading
every complete guide into every task. The project root `AGENTS.md` provides explicit
paths for tasks whose nested Git repository limits automatic discovery.
[Codex skill discovery](https://developers.openai.com/codex/skills/)

| Skill | Use in MageThemeEditor | Source revision |
| --- | --- | --- |
| `vercel-react-best-practices` | React editor rendering, subscriptions, loading and bundle performance | Vercel `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `vercel-composition-patterns` | Reusable inspector controls and component APIs | Vercel `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `nodejs-backend-patterns` | Node service boundaries, validation, errors and API design | wshobson `a30778f8c4e6b0a87567941b7cca4f534bf642b6` |
| `tailwind-design-system` | Tailwind v4 CSS-first tokens, component variants and responsive styling | wshobson `a30778f8c4e6b0a87567941b7cca4f534bf642b6` |
| `web-design-guidelines` | Interface accessibility, focus, forms and interaction review | Vercel `063bee94c3f4df8453406c830b0a7df0f2860278`, with pinned guidelines below |

The exact repository paths, original and installed SHA-256 file hashes, and local changes
are recorded in `.agents/skills.lock.json`. The two Vercel React directories use their
declared skill names. Upstream instruction/rule files remain unchanged except for the
web-design entrypoint: it reads a bundled snapshot instead of fetching mutable rules
before every review. Its original entrypoint is retained under `.agents/third-party/`.

## Third-party adoption review

Reviewed by the installing Codex task on 10 September 2026 against the
[third-party adoption requirements](../requirements/third-party-compliance.md).

| Source and authoritative terms | Intended use and coverage | Outcome and obligations |
| --- | --- | --- |
| [Vercel agent skills at the pinned revision](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278), [README license declaration](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md#license) | Three selected skill directories, including their Markdown rules, compiled guides, metadata and README files. The repository declares MIT; both React entrypoints additionally declare MIT. | Accepted for local development guidance. Retain the source declaration, authorship metadata and MIT permission text. The pinned repository supplies no separate LICENSE file; do not invent a copyright attribution. |
| [wshobson agents MIT license](https://github.com/wshobson/agents/blob/a30778f8c4e6b0a87567941b7cca4f534bf642b6/LICENSE) | Two selected directories, including their detailed and advanced pattern references. | Accepted for local development guidance. Preserve the complete MIT license and Seth Hobson copyright notice in both installed directories. |
| [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines/tree/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1), [MIT license](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/LICENSE) | The web-design skill's transitive `command.md` rules, bundled locally at revision `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`. | Accepted for local development guidance. Preserve the complete Vercel Labs copyright and MIT license; record the local entrypoint adaptation. |

The installed payload contains instruction/reference text and JSON metadata, with no
executable helper scripts, package installations, hooks, remote connectors, telemetry or
hosted-service enrollment. The upstream repositories' build tooling is not installed.
Libraries mentioned in examples are recommendations, not installed or accepted dependencies.
External documentation links are references, not part of the pinned local payload.
Optional suggestions to consult other skills do not install those skills.

No skill subscription, seat/store limit or service fee was introduced. Installation reads
public GitHub content and does not upload project files. Subsequent LLM use follows the
existing agent/account arrangements; these skills introduce no separate data processor.
Preserve applicable notices if substantial example code or skill material is later copied
into distributed software. Any actual product dependency still needs its own adoption review.

## Applying the guidance

Project requirements, the approved UI direction and installed library versions take precedence
over generic examples. Apply React guidance to the merchant editor; Alpine remains the
shopper interaction layer. Next.js, TypeScript, Express, Fastify, Zod, state libraries and
extra UI packages are not adopted merely because a skill uses them. Use the existing Ajv
contract where appropriate. Keep theme JSON independent of the editor framework and CSS classes.

Installation does not resume paused Magento work or authorize commits, deployment or publication.
Skill README build commands describe upstream maintenance and are not this project's build commands.

## Verification and maintenance

Verify five unique skill names and their required local rule/reference files, compare file
hashes with the lock, and run the documentation checks after changes to this record.
Successful installation establishes discoverable files, not measured coding-quality gains.

For upgrades, resolve a new immutable revision, inspect the relevant file and terms changes,
then update the lock and this record. Do not bulk-refresh the entire upstream repositories.
The web-interface snapshot is updated through the same review, not fetched automatically.

For removal, delete only the five named skill directories and remove their routing entries
from the root `AGENTS.md`. Retain or intentionally retire the corresponding lock and review
record; preserve any other skills added to the workspace later.
