# Batch 03A native hero evidence · 2026-09-07

Status: **bounded local Luma experiment verified by the implementer; independent review pending**.
Owner: task `01a07b5a-dbf4-7e31-a3b3-d63d2f58d3ab`, local, GPT-6 Astra, sole implementation and
documentation writer. Coordinator: `01a07a34-9a91-7160-8ff1-835cfc8011f3`. No additional agent/task.

One explicitly registered home hero now renders through actual Magento PHP after a deliberate
local selection. Installing the module without an assignment preserves the fixture's original
output; removing selection restores it. This is a small native rendering experiment, **not** the
complete connector, secure handshake, Luma adapter, publication protocol or product support promise.

## Accepted foundation and source identity

The coordinator accepted the Batch 02 save-race correction after independent recheck. This batch
freshly reproduced the corrected **54-file** authored source aggregate SHA-256:
`3aafd62c93c72e6514339e1c1dfbffac50deebacd5eb3ab60ee5adefa7c5406e`.
The reviewer algorithm hashes compact key-sorted JSON mapping product-relative filenames to file
SHA-256, excluding `.local`, `node_modules`, `.git`, `dist` and `.DS_Store`.

The original portable schemas, Node contract/activation model, editor/service code, fixtures,
dependencies, notices and tests remain unchanged. New native code is in
`product/magento/NativeHeroExperiment/`; original local fixture tooling is in `product/integration/`.
The product README adds navigation to this work. Prior review/remediation files and both manual
drafts were snapshotted before work. There is no product Git repository/commit baseline or source
delivery in this batch. The independently owned docs repository remains on `main` with its existing
dirty/untracked work preserved; no commit/push/PR/visibility change/public upload or hosting deploy.

## Refreshed named-store preflight

Read the SalesOne ancestor instructions and searched the exact INOX checkout for root/nested
instructions before runtime access. Environment detection returned `local`. Read-only Git/config
inspection and a read-only SQL transaction established:

| Item | Observation |
| --- | --- |
| Named source | `/Users/branorphiano/Projects/s1/inox-us-staging` |
| Branch and SHA | `fix/INOXUS-creative-assets-fpc`, `046d6e87866e7f6c5172e9c63f90097ac8b08295` |
| Existing dirty state | Untracked `.docs` and `html`; preserved |
| Magento package identity | Open Source/base 2.4.6-p13; Page Builder 2.2.4-p13 and Blank/Luma 100.4.6-p13 present |
| Effective local DB | `inox-us-staging`, prefix `s1_`, loopback port 6033, MySQL Community 8.0.40; server datadir is the user's local `Projects/LocalDB` |
| English active theme | Store id 2 / code `en`, theme id 4 `SalesOne/InoxUS`, parent `Smartwave/porto`, then `Magento/blank` |
| Search/cache/session | Effective env override selects local OpenSearch 2.12.0 port 19200; shared local Redis 6.2.22 port 6380, cache databases 0/1 and session database 2. Stored DB search settings include an older remote endpoint; none was copied |
| Local HTTP | Valet maps the named hostname to the exact source `pub/`; default socket resolves to `valet83.sock` (installed PHP-FPM 8.3.28). Certificate-verified loopback HTTPS GET `/en/` returned 200 |

The first read-only query missed the configured table prefix and failed before returning rows;
it was corrected using `env.php`'s exact prefix. No source DB writes or dump/import were performed.
The current INOX page is **not Luma evidence**. No Porto/client theme code or content was adopted.

The B2B/Hyvä installation was not accessed or repaired by this batch. Its earlier coordinator-observed
500 remains historical baseline information, not a fresh health or compatibility result.

## Isolation before Magento bootstrap

The fixture lives only under ignored `product/.local/batch-03a/`. The 181-package dependency
closure was copied from the named installation's open-source packages and base package layout;
client `app/code`, themes, media, env/config, auth files and databases were excluded. Exact package
versions/source references/notice hashes are in `package-inventory.json` and `package-plan.json`.
The source copies are **as installed**, not claimed pristine upstream. The generated subset lock is
runtime metadata, not a clean full-distribution Composer resolution or a redistributable product lock.
The CLI does not identify a full distribution version; the table below uses verified package versions.

| Fixture component | Actual scope |
| --- | --- |
| Magento | Base 2.4.6-p13, CMS 104.0.6-p13 and selected native modules; Page Builder and commercial/client packages excluded |
| Active theme | Explicitly selected `Magento/luma` 100.4.6-p13, registered theme id 3, parent Blank 100.4.6-p13 |
| PHP | Existing native PHP 8.2.29 CLI/server, macOS 26.6.2 arm64; no global PHP/Valet change |
| Database | Separate MySQL Community 8.0.40 process, new private datadir, `mte_batch03a` database and schema-scoped generated user, 127.0.0.1:19306 |
| Search | OpenSearch 2.12.0, cached arm64 image digest `sha256:7096045a3c30007d5b3c59c19a3a7cef41a399ea45f3c3290db82df3da2cece9`, dedicated container/network/storage; Docker server 29.4.0 |
| Search access | Internal Docker network with no external gateway; a loopback relay at 19210 verifies ownership and forwards only to that container. OrbStack's internal-network port publishing was unavailable |
| HTTP | Task-owned PHP development server, only 127.0.0.1:4180 |
| Cache/session/static | Independent local files and paths; `full_page` and `block_html` disabled consistently before comparisons; config/layout cache local; separate session/generated/static/media/temp directories |
| Other workers/services | No cron, queue consumers, Redis, Varnish or shared mail service used by the fixture |
| Dataset | Original `mte-` CMS identifiers/text, two pages/two blocks, one simple product at USD 12, one category; zero customer and order rows; no client content/media or database import |

All Magento CLI/server invocations use the local sandbox wrapper. It denies outbound network
connections except dedicated loopback ports 19306/19210, denies subprocess execution, restricts
writes to task state, removes inherited integration environment variables and disables PHP sendmail.
Generated SMTP configuration is disabled. Before installation, positive connection tests passed
for the two owned services; shared ports 6033/6380/19200/1025 and external IP connections failed
with permission denial. The search container's external connection test also failed. No copied
payment/email/fulfillment/webhook configuration was booted.

Third-party review is recorded in original `product/integration/third-party-review.md`. Local
notices and source copies are retained. Open Sans WOFF metadata identifies version 1.10 and Apache
2.0; this is local Luma use, with no vendor visuals repurposed as product assets. Package availability
does not create redistribution entitlement. Full shipped-asset/linkage/hosting/commercial review
remains open under the [third-party requirements](../requirements/third-party-compliance.md).
This is a feasibility combination; current Adobe requirements also note MySQL 8.0 end of support.
[Adobe system requirements](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/system-requirements)

## Supported native boundary

Portable target: `store-en/home/page-home/region/hero-region`. Local registration maps it to
store code `default`, configured CMS home `mte-native-home`, actual route `cms_index_index`, CMS
block `mte-native-hero`, and effective theme `Magento/luma`. Reusing the same block in
`mte-native-unassigned` retains original output. Other blocks, routes, stores, homes and themes
are excluded. No arbitrary HTML conversion or caller-selected template/path is implemented.

`prepare-hero.mjs` fully validates the existing original `fixtures/valid/content.json`, projects
its one hero while excluding `grid-1`, validates the result through the unchanged Node contract,
and writes only a fixed local inbox. `hero-projection.json` records both SHA-256 identities and
the exact target mapping. Staging does not select a renderer.

The PHP subset accepts contract/content/component version **1.0.0**, document `doc-home`, explicit
published `store-en` scope, bounded integer revision, `accent`/`spacing` tokens and exactly one
hero with `heading`/`alignment`. It rejects unsupported keys, versions, draft/default/foreign scope,
inheritance, body/images/grid/widget/block content, malformed/duplicate/lossy input and unsafe values.
Its local encoding is minified UTF-8 JSON plus one newline, at most 16 KiB/depth 8: this is narrower
than the portable wire format. It is **not full PHP validation parity**.

`bin/magento mte:native:select` validates the fixed inbox before replacing the fixed local selection;
`--restore` removes selection. There are no HTTP ingestion endpoints or target/file arguments. A
cache-state guard rejects selection/restoration while fixture FPC or block cache is enabled. The
command does not toggle cache state. `MTE_LOCAL_FIXTURE=batch03a` identifies the local launcher;
it is not authentication, tenancy or a merchant permission model.

The frontend plugin reads and revalidates active bytes, uses one registered PHP template, escapes
output and requests one CSS file only within the selected region. Every CSS rule is scoped to its
root; no JavaScript or remote assets. Missing/invalid state preserves original output. A repeated
registered boundary has only one renderer output per request in the focused harness. The module
never overwrites the original CMS content. Restoration returns current native original content;
there are no versioned original snapshots, durable release pointer or rollback guarantees.

Full release/signature/assignment/capability checks, inherited values, overlap handling and immutable
assets still live only in the Node contract/pure activation model. The existing editor iframe remains
illustrative and is not connected to this Magento fixture.

## Actual verification

| Check | Observed result |
| --- | --- |
| `cd product && npm run verify` | **82 tests pass**, no failures/skips; existing editor build/dependency/asset/notice guards pass |
| PHP production-code harness | **57 assertions pass** for positive/negative content boundaries, original/selected/unassigned contexts, duplicate ownership, actual template escaping, local replacement/restoration and symlink rejection; Magento dependency doubles are explicit |
| Real Magento CLI/HTTP negatives | **8 cases pass**: draft, foreign store, version, caller template, unsupported grid and duplicate-wire input rejected without changing active state; real PHP template escapes an HTML-looking heading; corrupted active state falls back to original output |
| Real CLI cache guard | With only fixture FPC enabled, selection rejects and remains unassigned; the original disabled-cache context is restored afterward |
| Syntax and configuration | **13 PHP files** pass syntax checks; **4 XML files** pass the installed Magento XSD checks with local URN resolution; Python helpers parse successfully |
| Documentation | `make verify` passes: **26 source pages, 27 HTML pages and 1,689 local links**; the dated evidence page and seven affected rendered pages inspected |
| Fresh installation | Magento setup finished successfully on the owned empty database; no customer/order dump imported |
| Actual HTTP stage captures | Five routes return **200** at baseline, installed/unassigned, assigned and restored stages |
| State comparison | Captured CMS pages/blocks, themes, stores, selected configuration, product/category identities and customer/order counts are identical across installation, selection and restoration |
| Browser | Baseline Luma layout, native selected hero, same-block unassigned CMS page, restored original, category/product native navigation, USD 12 price, enabled product Add to Cart control, functioning empty mini-cart and empty cart page observed; no order/cart submission |

| HTTP stage | Home native renderer count | Home original count | CMS/product/category/cart native counts | Shared and unassigned markup |
| --- | --- | --- | --- | --- |
| Baseline | 0 | 1 | 0 on each route | Captured |
| Module installed, unassigned | 0 | 1 | 0 on each route | Matches baseline |
| Hero selected | 1 | 0 | 0 on each route | Header/footer/sibling and unassigned main markup match |
| Original restored | 0 | 1 | 0 on each route | Matches baseline |

HTTP comparison normalizes per-request form keys, generated link IDs and script text; it does
not claim entire-response byte identity. The first category comparison differed only in its toolbar
JSON form key. Retained raw baseline/installed HTML was reanalyzed with that explicit normalization;
the initial results are preserved. Installed response headers were not retained after that first
assertion failure; body/status evidence and later stage headers remain available.

Browser DOM checks independently found unchanged header/footer text, identical sibling markup and
computed color/font/padding/margin. Assigned hero count was exactly one, original hero count zero;
its border was 4px in the declared accent and alignment was `start`. The unassigned page and restored
home loaded no native hero stylesheet. No external asset declarations or warning/error console entries
were observed on the checked pages. This is not a full CSP/accessibility/performance/network audit.

Initial local setup failures were resolved in the reusable recipe: missing top-level file-cache
package, subset runtime metadata, invalid admin frontname, stale generated autoload entries, fixture
area context and isolated session/temp setup. Their local logs are retained. No shared service reset,
global configuration change or original-store repair was used to recover.

## Evidence, ownership and stop point

Ignored evidence root: `product/.local/batch-03a/evidence/`.

Final authored product source inventory contains **87 files**, aggregate SHA-256
`0aae1808a708a91e476691d12f3636ebd25bd7f3a7f16ccda2a385ebd2f30fd6`.
It excludes `.local`, `node_modules`, `.git`, `dist` and `.DS_Store`. Of the 54 original
source files, only README navigation changed; 53 are byte-preserved. All **188 prior
review/remediation/manual-draft files** are preserved. The final preservation record
also checks deployed module bytes, internal runtime symlinks and original INOX state.

- `source-start.json`, `preservation-start.json` and final preservation/source maps identify authored
  bytes and preserved prior artifacts; the original research checksum and `.docs` routing are checked.
- `inox-preflight.json`, `versions.json`, `package-{plan,inventory}.json`, `staged-package-files.json`,
  `font-notices.json`, `egress-check.json`, install/seed logs and resource owner records describe isolation.
- `http/{baseline,installed,assigned,restored}/` retains actual route bodies, results and comparisons.
  `state-{baseline,installed,assigned,restored}.json` and `state-comparisons.json` retain state evidence.
- `hero-projection.json`, `native-runtime-checks.json`, `cache-guard.json`, `php-tests.log`,
  `npm-verify.log`, PHP/XML checks and docs verification/browser notes record tests and limits.

The fixture is left **unassigned with original rendering**, for independent review. At this stop
point its owned HTTP PID is 10266 (4180), MySQL PID 9965 (19306), search relay PID 10032 (19210), and
container is `mte-batch03a-search`, network `mte-batch03a-internal`. Live owner/PID/container records
under `.local/batch-03a/` are authoritative for cleanup; verify process identity and container labels
before stopping. Stop only those fixture services, preserving data for review. No automatic reset
or shared-resource cleanup is authorized by the setup scripts.

The user editor PID 7682 / port 4173, both manual drafts, existing docs listener PID 5726 / port 8017,
original INOX checkout/resources and all prior review/remediation artifacts remain preserved. The
user's editor tab was not used or reloaded. Only a new background fixture tab was used for Magento.

SOL-494 and SOL-496 remain **In Progress** for this partial preparation/renderer work, with their
original acceptance text and upstream dependencies intact. SOL-495 and SOL-498 remain **Backlog**;
no full handshake or adapter work is claimed. No issue is Done, no duplicate/new issue, and no future
ecosystem project task/milestone is created. This batch stops here for independent review.

Recommended next bounded step after review: complete one repeatable fixture reset/rebuild and add
the missing mixed-content/native-grid scenarios under the existing dependencies. Product decisions
on supported versions and the next handshake/adapter slice remain with the coordinator. No next
batch, Hyvä/Porto implementation, hosted editor connection, distributed cache/outage proof, full
checkout, merchant validation or commercial release clearance starts here.
