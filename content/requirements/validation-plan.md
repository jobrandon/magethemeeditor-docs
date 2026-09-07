# Validation plan

Status: proposed evidence plan; execution outstanding. Updated: 7 September 2026.
Derived from the [research validation sequence](../architecture/theme-editor-research-2026-09-07.md#opportunity-map-and-validation-sequence)
and [hybrid adoption requirements](hybrid-adoption.md).

| Stage | Evidence to collect | Decision enabled |
| --- | --- | --- |
| Merchant and agency discovery | Recent real change requests, effort/cost, editor comparisons, adoption constraints, willingness to pay | Scope the outcome and support matrix; proposed sample is five merchants and two agencies |
| Integration proof | Reproducible Luma/Hyvä fixtures, hero/product grid, original mixed content, preview, publication, restoration, local-mode outage | Validate the hosted-editor/local-renderer architecture and theme-specific effort |
| Hybrid routing and isolation | HYB-01 through HYB-12 across declared page/region scopes and untouched surfaces | Validate partial adoption without requiring theme replacement |
| Private beta readiness | Permissions, signing, tenant isolation, recovery, upgrades, commerce/cache tests, CSP, accessibility, performance | Approve only the tested compatibility matrix and operational behavior |
| Merchant pilot | Time to first preview/publish, routine changes without help, mismatch and failure rates, restoration time, support effort | Decide whether the product works for its intended users and what to expand |

## Technical evidence boundaries

Use exact versioned fixtures with hardcoded templates, Page Builder content, CMS blocks, and
widgets. Test supported simple/configurable products, store views, currencies, customer groups,
mobile and desktop widths, and warm/cold caches. Preserve FPC and private-content behavior.

Preview, source validation, staging, activation acknowledgement, and live result are distinct
observations. Report each accurately. A successful HTTP response or cached page alone does not
prove renderer, commerce, or origin health.

For hybrid work, capture unaffected pages/header/footer/cart/checkout before the change and compare
them after both publication and restoration. Exercise two independent assignments to prove the
second remains unchanged. Include incomplete transfer, conflicts, unsupported capabilities, and
lost service/CDN connectivity under the declared asset mode.

## Recording results

Future evidence pages should give date, owner, repository/branch/SHA, fixture/version matrix,
commands, target assignment and release IDs, expected and observed behavior, links to safe artifacts,
failures, and unresolved limits. Summarize sensitive evidence without copying production records.

Set numerical success targets after measuring a baseline. No customer savings, conversion lift,
runtime compatibility, production readiness, or interview completion is claimed yet.
