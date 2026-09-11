# Local Magento and native contracts

Read before any Magento source, database or runtime work. User-authorized local development
uses the existing installations only:

| Host | Expected local root; verify before use |
| --- | --- |
| `invictus-staging.test` | `/Users/branorphiano/Projects/s1/invictus-staging` |
| `inox-us-staging.test` | `/Users/branorphiano/Projects/s1/inox-us-staging` |

- Read each installation's instructions and inspect branch, dirty files and runtime first.
  Do not create a new Magento environment, clone an installation or create a fresh database.
  Historical fixtures are evidence, not a reason to recreate or delete environments.
- Necessary local source edits and DB writes are authorized within the assigned scope.
  Record touched files, scoped data changes and practical reversal steps. Prefer dedicated
  test CMS content; preserve existing themes, unassigned routes, drafts and native commerce.
- Never commit, push, open PRs or publish native installation changes. Do not switch branches
  or reset unrelated work. Local permission does not authorize production changes, database
  replacement, real communications or redistribution of client/vendor code and data.
- The initial supported slice is home/CMS. PDP/category and broader native capabilities need
  demonstrated integration criteria. Respect the existing fixed 03F projection and declared
  renderer registry; do not broaden them merely to claim support.
- Execute only declared native renderers. No arbitrary remote PHP/JS, automatic template
  conversion, global resets or copied client assets. Proprietary logic and keys remain hosted.
- Keep schema/semantic validation, safe references, failure states and keyboard behavior
  tested. The portable format stays independent of React or a specific editor library.
- `activate` is a reference model until real persistence proves transaction isolation,
  multi-node coherence, original restoration, cache effects and crash recovery on Magento.
  Local source checks, simulated acknowledgements and storefront proof are distinct.

The PHTML comparison is a bounded comparison artifact, not a second supported product engine.
Coordinate native targets with the existing owner; do not resume unrelated paused batches.
