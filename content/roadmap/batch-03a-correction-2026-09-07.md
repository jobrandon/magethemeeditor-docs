# Batch 03A F1/F2 correction evidence · 7 September 2026

Status: **Both bounded corrections implemented and locally verified; independent recheck pending**.
This is a correction to the [initial Batch 03A experiment](batch-03a-evidence-2026-09-07.md),
not another batch or completion of the broader integration issues.

Original implementer and sole scoped writer: `01a07b5a-dbf4-7e31-a3b3-d63d2f58d3ab`, GPT-6 Astra.
Coordinator: `01a07a34-9a91-7160-8ff1-835cfc8011f3`. The completed independent reviewer,
`01a07b96-e067-7121-9de3-5e8027eadfb3`, returned two P2 findings. Its original report, repros,
controls and captures remain unchanged under ignored `product/.local/reviews/batch-03a/`.
New correction evidence is confined to `product/.local/remediation/batch-03a/`.

## Scope and source identity

The 11:40 UTC correction baseline exactly reproduced the reviewed **87-file** product source map,
aggregate SHA-256 `0aae1808a708a91e476691d12f3636ebd25bd7f3a7f16ccda2a385ebd2f30fd6`.
The baseline also snapshots 623 existing documentation/review/remediation/draft/build/configuration
files, owned service identities, selection bytes/modes and a read-only fixture state query.

Corrected product source: **90 files**, aggregate SHA-256
`91105e7c183372e4ddeb320a2027e9037e0391ddd0eabdb234c5e4aa367bf9a4`.
The product-relative map uses compact, key-sorted JSON and excludes `.local`, `node_modules`, `.git`,
`dist` and `.DS_Store`. Four existing files changed: native `Model/LocalState.php`, its module README,
`integration/fixture-php.py` and the integration README. Three permanent checks were added under
`integration/tests/`: `storage-read.php`, `isolation.php` and `runtime-fallback.py`.
No schemas, editor code, dependency versions, images or other product behavior changed.

## F1: contain expected selection read failures

The review reproduced an unreadable `active.json` under Magento's actual error handler. Its
warning became a plain `Exception`, bypassing the plugin's intended storage/validation fallback.
HTTP remained 200 while both the hero and its untouched sibling disappeared behind the generic
CMS content error. Readable and malformed controls established that a 200 alone was insufficient.

`LocalState::read()` now installs a warning handler only around the bounded `file_get_contents`
operation. It converts that operation's warning to the storage contract's `RuntimeException`
with the generic code `LOCAL_STATE_READ`, and restores the caller's handler in `finally`.
The plugin's existing narrow catch retains the current original output. No global catch was added;
unrelated Magento warnings still throw. Diagnostics contain neither a raw path nor a chained
filesystem exception.

The new permanent storage regression loads the installed Magento error handler without Magento
bootstrap. It proves a raw unreadable read throws plain `Exception`, checks the normalized failure,
handler restoration after failure/success, unrelated-warning propagation, readable bytes and missing
selection. **Eight assertions pass**. The same new test against the snapshotted old module fails
specifically at storage normalization; that negative control is retained.

The corrected module was copied only to its paired fixture module path. Actual CLI selection and
HTTP requests, plus a new background browser tab, produced:

| Home state | Native hero | Original hero | Untouched sibling | Generic CMS error |
| --- | --- | --- | --- | --- |
| Initially unassigned | 0 | 1 | 1 | Absent |
| Valid selection | 1 | 0 | 1 | Absent |
| Same selected bytes, mode 000 | 0 | 1 | 1 | Absent |
| Same bytes, mode restored to 0600 | 1 | 0 | 1 | Absent |
| Malformed selected bytes | 0 | 1 | 1 | Absent |
| Explicitly restored original | 0 | 1 | 1 | Absent |

Five native routes—home, same-block unassigned CMS, product, category and cart—were captured before
selection, after selection and after restoration, plus the three failure/control responses:
**18 HTTP 200 responses with content assertions**. Other routes retain zero native renderers.
The unreadable and malformed requests emit generic `LOCAL_STATE_READ` and `CONTENT_JSON`
diagnostics. Browser checks independently show identical original hero/sibling markup and
header/footer text during read failure, correct readable recovery, and no native stylesheet after
restoration. No user editor tab, cart submission or checkout was used.

## F2: prevent child creation while allowing initial PHP startup

The original profile denied execution except for the PHP binary used to start the fixture. That
exception also permitted `proc_open([PHP_BINARY, ...])`, which the reviewer observed running a child.
This was a process-creation failure; neither review nor correction claims it escaped inherited
network/write restrictions.

The wrapper now also denies `process-fork`. Its mandatory sandbox, initial PHP execution exception,
two owned outbound destinations, restricted writes and cleared inherited environment remain.
It has no unsandboxed fallback. No PHP functions/extensions were disabled to hide a probe result.
The allowed PHP executable may still replace the current process; child creation is the tested
restriction.

The unchanged reviewer `isolation-probe.php` now reports no process created for either same-PHP or
`/usr/bin/true`. Its output was captured in the new correction directory. The permanent regression
adds `pcntl_fork`, direct FFI `posix_spawn` against PHP/another executable/the shell, a `popen`
control, allowed/denied connection probes, a denied write outside fixture state, an allowed
temporary write inside it, and inherited environment checks: **19 assertions pass**.
Direct fork/spawn failures return EPERM and create no child PID; probes wait for any unexpected
child so a regression cannot leave one running.

Darwin's `popen` can return a pipe even when `posix_spawn` fails, then report exit 127 on close.
The first test incorrectly assumed a pipe meant a child existed; that failed result is retained.
The corrected test records pipe/output/exit separately and corroborates denial with direct spawn
return codes. This matches [Apple's libc implementation](https://github.com/apple-oss-distributions/Libc/blob/main/gen/FreeBSD/popen.c).
This source was consulted; no Apple source code or dependency was adopted.

Both owned ports 19306/19210 accept connections. Shared ports 6033/6380/19200/1025 and external
test destination 192.0.2.1:443 return EPERM. The outside write fails with an observed permission
error; the parent sentinel and unrelated inherited environment variables are absent. Existing
CLI FFI/pcntl availability is part of this pinned local regression context.

The old HTTP PID **10266** was verified against its owner record, command, cwd and loopback
listener, then gracefully stopped. Only that fixture service was restarted, using the corrected
mandatory wrapper: **PID 11517 / 127.0.0.1:4180**. Recorded sandbox SHA-256 is
`f10f4f609aa2619b0f83025b62d43cf282c8612623fefb4cf94eb25d8c03c497`.
A read-only macOS `sandbox_check` against that actual server PID reports `process-fork` denied;
an unsandboxed caller control reports allowed. Normal Magento CLI/HTTP/browser operations above
also ran after restart. MySQL 9965/19306, relay 10032/19210, search container/network and all
unrelated services were left intact. No setup/reset/reinstall occurred.

## Verification, preservation and handoff

| Check | Observed result |
| --- | --- |
| Existing Node verification | **82 tests pass**, no failures/skips; full `npm run verify` in a correction-owned source copy using existing dependencies; no install |
| Original editor build | All **10 generated files** from that isolated build equal the existing product `dist`; user preview files were not rebuilt |
| Existing PHP harness | **57 assertions pass** in the isolated source copy, with the existing explicit Magento doubles |
| New correction regressions | **8 storage assertions, 19 isolation assertions**, actual warning handler and OS denial controls as described above |
| Actual Magento | **18 HTTP captures**, valid select/restore, real permission-denied/readable/malformed controls and generic diagnostics |
| Syntax | Three changed/new PHP files pass syntax checks; two changed/new Python files parse |
| Documentation | `make verify` passes: **27 source pages, 28 HTML pages and 1,775 local links**; correction page and ledger rendered/navigation checked without horizontal overflow |
| Fixture state | Read-only snapshots of the named CMS/config/theme/store/catalog/customer/order fields are equal; `full_page` and `block_html` remain disabled |
| Files and ownership | Exact inbox/lock/env bytes and modes restored, active selection absent; current deployed module bytes match authored source |

The first HTTP runner used the CMS block identifier instead of its HTML sibling ID in a count
assertion. It failed on the original baseline before selection. Its body/results and runner copy
are retained; the corrected permanent check uses the observed `mte-original-sibling` ID. The original
reviewer's failing repro/report was never edited or overwritten.

Key local correction records: `source-{start,end}.json`, `preserved-{start,end}.json`,
`baseline-{start,end}.json`, `state-{start,end}.json`, `state-comparison.json`,
`storage-read.json`, `storage-read-before.log`, `original-isolation-probe.json`,
`isolation-complete.json`, `live-server-policy.json`, `http-restart.json`,
`runtime-final/results.json`, `browser-{notes.md,cleanup.json}`, `npm-verify.log`,
`php-harness.log`, syntax/build checks, documentation verification and Linear readback.
The runtime runner requires a new evidence directory and restores exact initial files in `finally`.

Historical implementation/review/remediation reports, both manual drafts, original editor output,
historical research and `.docs` routing are preserved. The current operational sandbox and HTTP
PID record intentionally reflect the correction. The docs listener **5726/8017** remains running.
Editor PID **7682** was already absent from the first correction process snapshot at 11:40 UTC;
port **4173** is currently unbound. This correction did not stop/restart it or use its tab. Its
absence is an observation, not a diagnosed cause; both manual drafts and editor files remain
byte-preserved. Only correction-owned browser tabs are closed. Original INOX/B2B
resources were not used for correction runtime work; their state was not repaired or changed.

SOL-494 and SOL-496 remain **In Progress**, with their original unchecked criteria and dependencies.
SOL-495 and SOL-498 remain **Backlog**. Progress evidence records only these corrections; no issue
is marked Done and no future ecosystem task is started. The same reviewer must independently
recheck the corrected source before coordinator acceptance.

The original limits remain: minimal local package subset, no full adapter, authentication/handshake,
signature or PHP contract parity, FPC/distributed-cache/outage guarantee, full checkout, Hyvä/Porto
support, merchant validation or commercial clearance. No commit, push, PR, upload, visibility change,
deployment, new dependency/image or next batch is part of this correction.
