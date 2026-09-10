# Batch 03F: local editor hero handoff · 8 September 2026

Status: **bounded local handoff independently reviewed**. Owner: this Batch 03F task, GPT-5.6 Terra Medium. Coordinator: `01a07c28-b8ed-78d1-85e2-25f171859b5f`. No commit, push, PR, deployment, remote access, new environment, service, package, catalog, customer, order, theme, homepage, base-URL or global-cache change occurred.

## Observed local flow

The saved illustrative editor home draft remained in its ignored local location, unchanged. Its validated export was copied into ignored Batch 03F evidence and passed through a new local-only projection. That projection has one fixed destination: INOX root `/Users/branorphiano/Projects/s1/inox-us-staging`, store `default`/1, Luma page 237, block `mte-batch03d-hero`, state directory `var/mte-batch03d`, document `doc-mte-luma-integration` and scope `store-mte-luma`. None of those values come from editor input or command arguments.

Only `tokens.accent`, `tokens.spacing`, `hero.heading`, and `hero.alignment` cross the deliberate projection. The existing home draft keeps its description/image and other known demo sections; they do not become Magento content. Foreign document/store, inheritance, unknown hero settings and unsupported section types reject before staging. The local Magento validator also rejects a foreign staged document and retains its existing state. This is a handoff stage document, not a hosted publish, activation receipt, persistence protocol, permission check, signed release or remote API.

With the valid stage selected through the fixed `mte:luma:select` command, exact local HTTPS `/mte-batch03d` returned Luma HTML and the native hero heading `Quiet rituals, lasting forms.`; the original region marker was absent and the same page's neighboring native Luma region remained. The narrow browser restoration check visibly showed the original region plus the unchanged neighbor. Malformed active bytes safely retained the original marker and neighbor. A foreign staged document was rejected as `DOCUMENT_TARGET`. Restore removed the active selection. The historical 03D inbox bytes were then restored too; Batch 03C and 03D active selections are absent.

## Focused checks

| Check | Outcome |
| --- | --- |
| `npm run verify` in `product/` | 84 assertions/tests pass, including two fixed-bridge projection/rejection tests |
| `node src/luma-local-bridge.mjs INPUT OUTPUT` | Existing saved home export stages one target-bound 362-byte native hero document |
| PHP `integration/tests/local-target.php` | 26 target/registry/storage assertions pass |
| PHP 8.3 `setup:di:compile` | Pass; fixed local `mte:luma:select` command is registered alongside historical 03C command |
| Actual local CLI/HTTPS | Valid select, malformed fallback, foreign `DOCUMENT_TARGET` rejection and restore all pass |
| Browser restoration | Original Luma region and unchanged neighbor visible; existing native serializer warning remains outside this work |
| Cache headers | Selected, malformed and restored dedicated-page responses are `200 text/html` with `no-store`; config/layout/block_html/full_page remain enabled |
| Docs `make verify` | Recorded after this page and the execution ledger update; documentation validation is not Magento proof |

## Limits and selective reversal

This is one trusted, manually run local draft export/stage/select/restore path only. It is not connected to hosted authentication, roles or permissions, live publication, scheduling, signing, draft persistence/inheritance, multi-node recovery, remote services, Magento content authoring, cart/checkout, product data, cache invalidation, Hyvä/Porto-wide support or commercial readiness. The page's `no-store` boundary avoids claiming Varnish/FPC invalidation behavior.

At handoff, restore is already complete. To repeat or reverse only this path: confirm both active files are absent; retain the fixed 03D page/control/block; restore the saved 03D inbox if a test changed it; then use `mte:luma:select --restore`. The only new INOX source is the command mapping inside the existing ignored `MageThemeEditor_LocalCmsExperiment/etc/di.xml`; remove that mapping and clean only config/layout caches after review if the local command is no longer desired. Do not remove Batch 03C mappings, the 03D CMS records, user changes, or shared caches.

Ignored, secret-free command output, response facts, source/deployed identities and restoration checks are in `product/.local/batch-03f/`.

Independent Terra Medium review found no actionable finding within this bounded flow. Its ignored
report, `product/.local/reviews/batch-03f/report.md`, independently confirmed fixed target ownership,
selective projection, valid selection, malformed fallback, foreign rejection and exact restoration.
The local-only limits above remain unchanged.
