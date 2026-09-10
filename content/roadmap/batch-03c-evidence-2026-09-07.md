# Batch 03C: existing local CMS integration · 7 September 2026

Status: **bounded local implementation verified; independent review next**. Owner:
`01a07c23-85af-7181-a1a7-6a10e74db601`. Current coordinator:
`01a07c28-b8ed-78d1-85e2-25f171859b5f`; former coordinator references remain historical.
No commit, push, PR, deployment, fresh installation, database replacement or new environment.

## Current target and baseline

The latest user directive supersedes isolated-copy/fresh-fixture plans. Both existing checkouts
were inventoried using current config, native environment emulation and verified local HTTPS.
Database rows alone were insufficient: deployed local config overrides old remote URL/search values.
Neither old remote URL nor remote search service was used as the test target.

| Scope | Observed current local identity |
| --- | --- |
| INOX, selected | `inox-us-staging.test`, root `/Users/branorphiano/Projects/s1/inox-us-staging`; branch `fix/INOXUS-creative-assets-fpc`, SHA `046d6e87866e7f6c5172e9c63f90097ac8b08295`; baseline untracked `.docs` and `html` preserved |
| Invictus, inventory only | `invictus-staging.test`, root `/Users/branorphiano/Projects/s1/invictus-staging`; branch `feature/INV-497-authorizenet-address-limit`, SHA `717d005ceb332570fa840299b818f7b0d414f823`; pre-existing dirty `.htaccess` hash unchanged |
| Database/service | Separate existing `inox-us-staging` / `invictus-staging` databases on local MySQL 8.0.40, `127.0.0.1:6033`; existing PHP-FPM 8.3.28 via Valet83 socket; no runtime/service changes |
| Magento locks | INOX 2.4.6-p13, Page Builder 2.2.4-p13, Blank/Luma 100.4.6-p13; Invictus 2.4.6-p15, Page Builder 2.2.4-p15, Blank/Luma 100.4.6-p15 |
| INOX effective stores | English 2, French 7 and Spanish 8 use `SalesOne/InoxUS → Smartwave/porto → Magento/blank`; default 1 uses Luma; outlet 6 inactive. Test scope is English 2, website 2, en_US/USD, guest |
| Invictus effective stores | English 5, French 6, Spanish 7 and default 1 use `SalesOne/InvictusEnglish → Smartwave/porto → Magento/blank`; no Hyvä claim |
| HTTP baseline | Both roots 302 to local `/en/`; both English homes 200 `text/html` with expected title and public cache headers; no initial document-level HTTP failure |
| Cache | INOX Redis default/page caches on local 6380 DB 0/1; global `full_page` and `block_html` enabled. Effective FPC application is Varnish, but direct Valet HTTP provides no Varnish HIT/age evidence |

INOX was healthy and preferred as instructed. Theme identity was checked through native environment
emulation and actual asset output, not inferred from a hostname. No merchant homepage/theme/store
config, prices, stock, customer/order data or unrelated source was changed. Normal runtime cache,
session, generated-code/static and log activity is not a whole-filesystem/database identity claim.

The accepted 03B product baseline contains 103 authored files, aggregate
`a8aff8bfe56a96549b2495161d0836b9b063db73b3505618dae617efd1979937`.
Entry comparison found only the expected coordinator change to `product/AGENTS.md`;
root instructions also intentionally changed for existing-store work and coordinator ownership.
No product Git repository/history was created. Prior fixtures/evidence and editor drafts/dist remain intact.
Final authored source: 106 files, aggregate `bdfc0dae4850dca051472e677a287d551c30002e9984fe5622cfc434f737b276`;
12 existing files changed and three were added after the expected instruction amendment. All 19
deployed original-module files match source; all 12 existing draft/dist files match their entry hashes.
Documentation verification is recorded in the ignored `docs-verify.log`; affected rendered pages
are inspected locally. The historical 03A heading anchor is retained after a strict-build check
caught the initial renamed-heading link. A documentation build is separate from Magento proof.

## Implemented behavior

The generic renderer now injects `Model/LocalTarget` to separate the trusted local installation
mapping from the portable content document. Its historical Luma fixture defaults remain guarded.
A separate, unshipped local DI module pins INOX root, `.test` host, English store code/ID, effective
theme, numeric page ID, `mte-` block/directory, document/scope and a small opaque product allowlist.
Foreign host/store/page/theme/route and a cacheable CMS layout retain original rendering.

The original `mte-batch03c` CMS page (235), control `mte-batch03c-control` (236) and original CMS
block `mte-batch03c-hero` (142) were created through native repositories, assigned only to store 2.
Their prior identifiers were checked absent. They contain only original test text and a native CMS
block directive. The neighboring region stays native. The real `porto_home_14` homepage is unchanged.

Validated contract 1.0.0 content renders one hero and two native simple-product references. Two
existing public PDPs return HTML and their links match the grid. INOX requires guest sign-in for
prices: the grid and both native PDPs show the same “Sign In to view price” policy, with no numeric
price amounts. No authenticated account was used, no private price was exported and no merchant
price/stock was changed. Existing-store grids use native PDP links only; no cart action, quote item,
checkout, payment, order or real communication was submitted.

The local test page alone has an explicit `cacheable="false"` layout boundary. Original, selected,
fallback and restored requests return `max-age=0, must-revalidate, no-cache, no-store`. The unassigned
control and real homepage retain public cache headers, and global cache flags remain unchanged.
This deliberately avoids caching selected experimental output. It does **not** implement scoped
publication invalidation, cache identities, warm/cold Varnish proof or a production caching solution.

## Focused evidence and tests

Runtime artifacts are ignored under `product/.local/batch-03c/`; the durable report contains no
credentials, raw database export or vendor assets. Raw merchant HTML was not archived wholesale:
HTTP evidence retains response facts/hashes and the original test region with two public references.
Browser snapshots/crops are bounded QA evidence, not product assets or copied theme source.

| Actual check | Outcome |
| --- | --- |
| `npm run verify` in `product/` | 82 tests pass; unchanged generated editor dist and manual drafts checked separately |
| PHP 8.2 `integration/tests/native.php` | 57 existing hero/validator/storage/plugin/template assertions pass with explicit target injection |
| PHP 8.2 `integration/tests/grid-domain.php` | 27 existing portable grid boundary checks pass |
| PHP 8.2 `integration/tests/local-target.php` | 26 focused scope/host/page/theme/cache, registry and storage checks pass |
| PHP 8.3 actual Magento CLI | Valid mapped selection and restore succeed with existing global caches enabled; malformed/wrong-store/unknown-reference/extra-price/draft inputs reject without replacing active bytes |
| `python3 product/.local/batch-03c/verify-runtime.py` | 71 assertions over 10 real responses: repeat selection, one owner, same neighbor, malformed/unreadable active fallback, same-block control, home cache policy and exact test-content restoration |
| Actual browser | Selected hero/grid, native guest-price gates, link click to correct PDP, unassigned control, malformed fallback, restoration, scoped screenshots; anonymous state checked at zero cookies |
| 390px browser | Region 360px, one grid column, document width 390px; no observed horizontal overflow |
| Installation | Two module-enable lines only; config/layout cache clean; no setup upgrade, schema migration, theme switch or infrastructure rebuild |

A real installation check caught Magento's inability to generate an interceptor with a newly
constructed object as a default constructor value. The correction uses required constructor
injection; Magento then generated/loaded the command and live rendering normally. No vendor or
cache-framework code was patched, and no global compile/reset was used to hide the failure.

## Native limitations and evidence boundaries

- Browser requests show PHP `unserialize()` warnings from Magento's existing serializer, including
  on the native PDP when active selection is absent. The selected grid also displays those native
  warnings. Curl's anonymous response checks do not reproduce them. This is not clean-store QA;
  the warning source is not repaired by this batch.
- The existing native price renderer emits its theme-owned global `.special-price` style. The new
  authored styles are scoped, and the dedicated neighboring region is unchanged, but full native
  theme/widget style isolation is not established by this experiment.
- QA blocks non-local browser hosts. Existing external fonts, Porto CDN styles/images, social
  assets and analytics fail by design; existing jQueryUI compatibility warnings also remain.
  Local MageThemeEditor CSS renders. No external assets were downloaded/mirrored for redistribution.
- No numeric prices for authenticated groups, stock changes, configurable/grouped purchase,
  guest cart/checkout, preview widget disposal, hosted editor connection, signing/auth, publication,
  multi-store inheritance or distributed recovery was tested. Grouped homepage products were
  intentionally excluded from the renderer's existing simple/configurable capability.
- INOX's actual theme is Porto-derived. This is additional renderer feasibility evidence, not
  completion of the Luma adapter or Hyvä/Porto commercial support. Installed commercial theme
  bundle/version/entitlements remain outside product adoption clearance.

## Touched state and reversal

Product source: `magento/NativeHeroExperiment/Model/LocalTarget.php`; validator, local storage,
product resolver, region plugin, select command and grid template adaptations; three existing PHP
harness injection updates and the new local-target harness; module/product/integration READMEs and
the Batch 03C third-party record. Exact changed/added source paths and hashes are retained locally.
The canonical contract, editor code/dependencies/assets, user drafts/dist and old fixture are unchanged.

INOX source: original module copy under `app/code/MageThemeEditor/NativeHeroExperiment/` and four
original local mapping/layout files under `app/code/MageThemeEditor/LocalCmsExperiment/`;
`app/etc/config.php` gains only their two enable entries. `app/etc/env.php`, composer lock,
`.htaccess`, existing theme/client/vendor source and current branch/SHA remain unchanged.
Generated Magento classes for these modules and their original static CSS are ordinary local effects.
Invictus source/config/lock/branch and the initial dirty `.htaccess` are preserved; no DB writes there.

Scoped DB changes: only CMS pages 235/236, CMS block 142 and their English store associations.
`cms-created.json` records IDs; `cms-final-identity.json` records identifiers/content hashes and
store links. No `setup:upgrade`, schema, catalog, customer, order or core-config DB change was made.

Stop state: **no `var/mte-batch03c/active.json`**; original CMS output selected. The validated inbox,
local mapping, original test content and ignored evidence remain for review.

1. From the existing INOX root, use PHP 8.3 `bin/magento mte:native:select --restore` to remove only
   the test selection. This is the current state; reselect reads only its fixed validated inbox.
2. After review, remove only the two known pages and one block using Magento repositories, after
   checking their identifiers/content hashes to avoid deleting later user edits.
3. Remove only the two module-enable entries and those two new module directories; clean config
   and layout caches. Do not restore a whole config backup or overwrite unrelated changes.
4. Optional generated cleanup is limited to owned MageThemeEditor classes/static CSS and
   `var/mte-batch03c/`. Do not flush shared cache services, remove unrelated sessions or touch the
   historical 03A/03B fixture/services. No cleanup is performed at this handoff.

## Linear and review handoff

Live issue descriptions/dependencies were read at entry. Existing SOL-494 received the explicit
scope amendment: fresh provisioning/rebuild/reset criteria are deferred by user instruction,
not passed or erased. Its historical criteria and relations remain intact. SOL-494/496 stay
In Progress for partial preparation/renderer work. SOL-498 remains In Progress from earlier Luma
work; this Porto result does not complete or independently advance its Luma adapter criteria.
SOL-495 remains Backlog. No issue is Done and no future custom-data/marketplace issue was added.

The current coordinator owns independent review and any next batch. This owner stops here;
no task, subagent, further environment, Git delivery or publication is started.
