# Magento integration environments and historical fixture plan

Status: **existing INOX CMS experiment locally verified; independent review next; fresh provisioning deferred**.
Updated: 2026-09-07. Owner: [SOL-494](https://linear.app/solventech/issue/SOL-494), In Progress.
The [Batch 03A evidence](../roadmap/batch-03a-evidence-2026-09-07.md) records 181 reviewed as-installed
open-source packages from the authorized INOX source, fresh generated data/config, separate MySQL,
search/cache/session/static state and enforced outbound denial. No client app/theme/media, database,
integration credentials or Hyvä entitlement was copied. Actual Luma was explicitly selected.

Batch 03A proves one local CLI-selected home hero and restoration, with installation/unassigned
and untouched-route comparisons. It does not complete the broader matrix below. The original
inventory and full-fixture recipe that follow are historical planning requirements; exact observed
runtime/ownership, exclusions, reproducibility limits and current checks are in the dated evidence.

## Current directive · Batch 03C, 2026-09-07

The user's latest instruction supersedes all provisioning/copy/reset directions below. Use the
existing `inox-us-staging.test` and `invictus-staging.test` installations directly. Do not create
another Magento environment, copy an installation, create a fresh database or replace a database.
The prior 03A/03B fixture and its evidence remain intact; clean rebuild/reset criteria are deferred,
not passed. Earlier B2B/isolated-copy guidance is historical and is not this batch's target list.

Batch 03C inventories both current local roots, services, store/theme scopes and HTTP health;
prefer healthy INOX for one dedicated `mte-` CMS page/registered region. Invictus is inventory-only
unless INOX is unavailable. Preserve current themes, homepages, unassigned content and commerce.
Use existing public catalog references without changing prices/stock/customer data. Local source
and scoped CMS DB changes are authorized, with practical reversal notes. Keep existing branches and
unrelated changes; no commits, pushes, PRs or publication. Do not globally disable storefront caches.
Observed result: INOX English store 2 on `SalesOne/InoxUS` (Porto/Blank) renders the dedicated
hero/grid with native guest-price gates and PDP links. Original output is restored; only that test
page bypasses page caching. Browser-native warnings and broader cache/adapter limits remain open.
See [Batch 03C evidence](../roadmap/batch-03c-evidence-2026-09-07.md) and the [current execution ledger](../roadmap/execution-plan.md#batch-03c-current-execution-2026-09-07).

## Historical bounded fixture · Batch 03A {#current-bounded-fixture-batch-03a}

Original source/tooling is in `product/magento/NativeHeroExperiment/` and `product/integration/`;
actual package/runtime/data copies stay ignored in `product/.local/batch-03a/`. Base/CMS packages
2.4.6-p13, Luma 100.4.6-p13, PHP 8.2.29, MySQL Community 8.0.40 and OpenSearch 2.12.0 were exercised
as a local feasibility subset, not a supported full-distribution release. FPC/block cache are disabled
and selection rejects other cache context. The fixture is left with original output for review.

Complete clean reset/rebuild, Page Builder/hardcoded/widget mixed content, configurable products,
multiple stores/currencies/groups, Hyvä, secure handshake/preview, grid rendering and cache/outage
scenarios remain outstanding. INOX's active client theme inherits Porto and is not the tested Luma
fixture; Porto and B2B/Hyvä remain untested in this batch.

## Historical extension · Batch 03B {#current-extension-batch-03b}

[Batch 03B evidence](../roadmap/batch-03b-evidence-2026-09-07.md) adds six original products and a
finish attribute/options through native APIs, preserving prior CMS/catalog/config data. One simple
and one configured child added through native browser forms to the same USD guest cart; that cart
was emptied natively. Live price changes were observed without design JSON changes and restored.
The necessary reviewed ProductVideo 100.4.6 prerequisite takes the fixture to 182 packages, with
one additive schema table and no unrelated migration. A recovery checkpoint and exact delta are
retained; this is not a second-install/reset proof. The original 181-package report remains historical.
Ownership and the sandbox/service boundaries remain unchanged. Selection is left unassigned for
review. Full PHP/publication/cache/multi-context/Hyvä/Porto and preview-disposal criteria remain open.

## Available local runtimes

Read-only commands in the MageThemeEditor workspace returned:

| Command | Observed result |
| --- | --- |
| `node --version` / `npm --version` | Node 22.22.0 / npm 10.9.4 |
| `python3 --version` | Python 3.14.5 |
| `php -v` | PHP 8.3.28 CLI, NTS |
| `composer --version` | Composer 2.9.2 |
| `docker version --format '{{json .}}'` | Client/server 29.4.0; Linux arm64 engine; orbstack context |
| `make --version` | GNU Make 3.81 |

Host is macOS 26.6.2 arm64. No unrelated containers, databases or package credentials were read.
Docker availability is sufficient to prepare an isolated environment later, not proof that
required images or a specific Magento dependency combination are present or supported.

Consult the exact selected Magento patch's current requirements before building the fixture;
the host PHP/Composer combination is not automatically a supported installation. The official
requirements distinguish version-specific service combinations and may include prereleases, so
also check the linked release notes. [Adobe system requirements](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/system-requirements)

## Exact access and decisions needed

1. A confirmed Magento Open Source patch and independently obtained source/Composer package
   access for that patch, using product-owned repository credentials only if required. Record
   its exact commit/tag, `composer.lock`, package hashes and file-level license notices.
2. Product-owned Hyvä package access and applicable rights for this fixture, exact edition/version,
   dependency packages and permitted use. Do not reuse another merchant's license or repository
   token. Installation instructions and package access must be checked at the time of adoption.
   [Hyvä setup documentation](https://docs.hyva.io/hyva-themes/getting-started/index.html)
3. A reviewed exact container/service inventory for the selected Magento patch: PHP extensions,
   Composer, database, search, cache, Varnish and web server. Pin digests, including arm64 support
   or deliberately reviewed emulation. No image download or toolchain adoption is cleared here.
4. Agreement on the first tested version matrix and simple/configurable product scope, informed by
   SOL-490/491. A feasibility version can be selected before interviews finish if explicitly labeled
   experimental; it must not become a merchant support promise without evidence.

No hosting subscription, production data, payment gateway, real customer or paid contract is
needed for the initial fixture. Use local-only generated test identities and a Magento offline
payment method when an order flow is required. Secure credentials belong in named environment
variables/ignored files, never authored docs or source control.

## Reproducible isolation recipe for the fixture task

Create a dedicated `product/integration/` only when SOL-494 starts. Use Compose project names
`mte-fixture-luma` and `mte-fixture-hyva`, separate networks/volumes, loopback-only ports selected
after checking availability, and no mounts of sibling client projects. No global Valet/PHP changes.
Keep two independently resettable stores with the same original data recipe and locked packages.

The fixture task must deliver:

- `versions.json`: exact Magento/Hyvä/modules, PHP/extensions, DB/search/cache/Varnish/web server,
  OS architecture, image digests, source commit and runtime flags.
- `compose.yaml` plus minimal product-owned configuration and an ignored `.env.example`-style
  template containing names/placeholders only; no live secrets.
- Deterministic seed/reset commands built with Magento APIs/data patches, an original dataset,
  expected entity-to-contract ID mappings and fixture checksums.
- A setup script that refuses non-fixture project/volume names and a reset limited to those
  named resources. A dry run must show exact destructive fixture targets before any reset.
- A baseline and scenario runner recording URLs, target/release IDs, rendered ownership markers,
  browser evidence, cache headers/origin logs and commerce results.

Bootstrap sequence: verify tooling/rights and pins; create isolated resources; install from locked
packages; generate local test configuration; install Magento; seed via the original recipe; set
Luma or Hyvä deliberately; compile/install assets as required; capture baseline before adding the
connector; snapshot only generated fixture state for reset. Repeat from empty fixture volumes to
prove reproducibility. Never use a production dump as a shortcut.

## Original data and scenarios

Create two stores (`store-en`, `store-fr`), two currencies, guest and one synthetic customer group,
simple/configurable products with fixed seed identifiers, two categories and two CMS pages.
Use original fixture text and original/generated media whose provenance is documented.
Include a hardcoded hero region, Page Builder banner, CMS block, product widget and one deliberately
unsupported structure on each representative homepage. Page Builder and widget availability is
verified against the chosen Magento packages before assuming these fixtures can render.

| Scenario | Required observations |
| --- | --- |
| Installation and opt-in | Active theme/config/content and all untouched routes unchanged; no implicit assignment |
| Home/CMS first | Edit hero/grid; actual preview; publish A while B retains exact prior renderer/release; restore A |
| Region boundary | Single owner, scoped tokens/CSS, initialization/teardown, unchanged sibling DOM and behavior |
| Future PDP/category support | Selected versus adjacent native routes; configurable options, live price and add-to-cart |
| Mixed content | Conversion dry run, original retention, supported/reference/unsupported report, no double output |
| Two stores and editors | Inheritance resolution, optimistic conflicts, preview isolation, no draft/customer cache leaks |
| Commerce and cache | Header/footer/navigation/account/mini-cart/cart/checkout before and after publish/restore; warm/cold FPC |
| Failure and outage | Interrupted transfer, bad signature, missing asset, activation crash, duplicate/out-of-order jobs; local cold-cache shopping with SaaS/CDN unavailable |
| Restore and recovery | Original content plus renderer metadata restored coherently; unavailable original fails safely; disable/uninstall policy |

Map results to [HYB-01–12](../requirements/hybrid-adoption.md#acceptance-criteria). Every run needs
branch/SHA, environment, exact versions, command, expected/observed result and limits. Local JSON
tests and an editor mockup do not satisfy these scenarios. PHP signature parity, persistence,
multi-node activation and cache behavior remain actual runtime work.

## Named local compatibility targets · later 2026-09-07 steering

The user subsequently authorized considering the existing `inox-us-staging` (Blank/Luma/Porto)
and `b2b-jewelry.test` (Hyvä) local stores as compatibility targets. This supersedes the earlier
blanket exclusion of unrelated local stores for these two named installations. A clean,
independently reproducible fixture remains useful for installation/reset and version breadth;
it is no longer a prerequisite to every compatibility experiment. Installed-theme testing
creates no right to redistribute vendor/client code or copy package entitlements.

The coordinator reported the following read-only preflight. These are attributed observations,
not independently rerun by Batch 02 and not active-theme/database proof:

| Named local target | Coordinator-observed source/config baseline | Baseline HTTP observation |
| --- | --- | --- |
| INOX, `/Users/branorphiano/Projects/s1/inox-us-staging` | Branch `fix/INOXUS-creative-assets-fpc`, SHA prefix `046d6e878`; untracked `.docs` and `html` preserved. Lock: Magento 2.4.6-p13, Page Builder 2.2.4-p13, Blank/Luma 100.4.6-p13. Smartwave/porto exists and extends Magento/blank. Valet maps `inox-us-staging.test` to this `pub/` | Root redirects to `/en/`; HTTPS GET `https://inox-us-staging.test/en/` returned 200 with certificate verification |
| B2B, `/Users/branorphiano/Projects/jobrandon/b2b-jewelry-inv` | Branch `preview/v2.1-mintforge`, SHA prefix `e0f156b5`; clean at observation. Same locked Magento/Page Builder; Hyvä default theme 1.4.6 and theme-module 1.5.2. Valet maps `b2b-jewelry.test` to this `pub/` and PHP82 socket | HTTPS GET `https://b2b-jewelry.test/` returned 500 before MageThemeEditor installation; cause undiagnosed |

The B2B failure is a baseline-health prerequisite, not a MageThemeEditor failure or compatibility
result. Start future preflight with each repository's current AGENTS/policies, exact branch/SHA,
effective URLs/database/theme, and outbound integrations. Preserve current branches and valuable
content. Prefer INOX for the first Blank/Luma-family experiment, treating Porto as additional
compatibility work, then B2B for Hyvä after diagnosing its baseline health.

Historical Batch 02 proposal, now superseded: isolated local copies/checkouts with separate databases,
cache/search/session/static resources and reviewed outbound-integration settings. A Git worktree
alone does not isolate Magento state. Create only original `mte-`-prefixed CMS/test fixtures;
never copy client storefront design/assets into product source. No further isolation resources are authorized by the current directive.
Remote production, copied private data/services and entitlement redistribution remain outside scope.
No Magento mutation or new integration batch occurred in Batch 02. At that stop point SOL-494 was Backlog; the
coordinator added the preflight comment, which this task did not duplicate. Named-store access
also does not resolve pending repository privacy/source-delivery authority.
