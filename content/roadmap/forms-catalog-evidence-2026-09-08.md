# Forms and promotions evidence · 8 September 2026

SOL-536 remains **In Progress: original non-delivering local subset implemented; full acceptance open**.
Four original components render on three populated dedicated INOX Luma pages. Entered field values
remain in the browser. A fixed Magento endpoint checks the session form key and current selected
section, then returns a validation receipt. It cannot send contact email, subscribe anyone or start a
campaign. **No controlled visitor capture or real delivery provider has been implemented.**

The [103-entry field ledger](forms-field-coverage-2026-09-08.md) covers the exact four assigned stems
and eight reference blocks from the existing census. The [canonical catalog map](silt-form-catalog-coverage-2026-09-08.md)
and `component-library/reference/forms-coverage.json` preserve explicit unaccepted gaps. None of the
material substitutions below waives the issue criteria or establishes full Flux support.

## Ownership and environment

Coordinator 2 assigned this task sole source/docs/local-INOX ownership for SOL-536. Astra High is
authorized for this scoped form architecture and Magento trust boundary. No additional agent was
started. The accepted inventory was reused without opening or recrawling Flux source; no reference
code, schema, CSS, assets or snippets were translated or distributed.

- Existing local installation: `/Users/branorphiano/Projects/s1/inox-us-staging`.
- Branch `fix/INOXUS-creative-assets-fpc`, SHA `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
- Existing store 1 / website 1 / `Magento/luma`; bootstrap verifies the exact local root and database.
- New CMS/store rows: contact 254, signup 255 and promotions 256, assigned only to store 1.
- Pages 240–253, store/theme configuration, website assignments, previous selections/drafts and 03F
  remain intact. The pre-existing serializer file and `app/etc/config.php` retain their hashes.
- No environment provisioning, remote/production operations, customer communications, newsletter
  submission, contact submission, dependency adoption, commit, push, PR or publication.

## Populated demonstrations

Open the existing local editor on port 4177. Three independent saved drafts remain applied for review.
The 4173 manual editor and its prior draft files remain intact.

| Demo | Editor target | Native path | Current behavior |
| --- | --- | --- | --- |
| Contact studio | `?page=silt-contact` | `/mte-silt-contact` | Edited contact heading, original media, required name/email/message, optional telephone, consent and disabled delivery example |
| Studio letters | `?page=silt-signup` | `/mte-silt-signup` | Signup banner, newsletter block composition, simulated provider failure and empty form-block state |
| Studio invitation | `?page=silt-promotions` | `/mte-silt-promotions` | Manual optional dialog, registered CMS link, email preview and disabled popup example |

The Contact heading **A conversation starts here.** was edited, saved, reloaded, applied to Magento,
restored to original native output through the editor, and reapplied. Signup and Promotions were
saved and applied independently. The signup flow initially rejected an empty settings object after
the PHP associative-array bridge serialized it as an array. The original form block now has a
meaningful editable validation-button label. The existing serializer workaround was not modified.

## Contracts and exact boundaries

Only the forms package and its three templates are selectable on the dedicated form targets;
other packages cannot silently render without their required assets. Canonical coverage regeneration
retains all 103 mapped/gap entries and preserves every other family unchanged.

All four stems have original registered `mte-forms/*` definitions, generated exact schemas,
automatic editor controls, version pins, presets, safe media/CMS references, browser validation and
native DI registration through `FormsRenderer`. No renderer class, template, executable expression,
form action, external endpoint or arbitrary merchant URL is accepted in portable JSON.

| Stem | Working original capability | Remaining or substituted capability |
| --- | --- | --- |
| `contact-form` | Original stack/image-start/image-end layouts; heading/caption/body; image dimensions and visibility; optional phone; required fields; consent; CMS information link; paired surfaces, spacing and responsive preview | No contact email submission, recipient/transport configuration, server validation of entered values, custom arbitrary fields or stored capture |
| `email-signup-banner` | Original single-image layout, ordered caption/heading/paragraph/email-form blocks, labels, required email and consent choices, empty/error/disabled states | Second image, rich inline markup, exact vendor layout/values and actual subscriber creation are open |
| `newsletter` | Original ordered blocks, per-form validation button label, independent empty block list, required/optional/hidden consent, visible validation result | Arbitrary `@app` blocks, campaign provider, newsletter confirmation and subscription success remain open |
| `popup` | Enabled/disabled, manual/delayed opening, native modal dialog, focus trap, Escape/close and return to opener, responsive image/panel, optional signup, CMS link, visit/session/day frequency | Social provider content, vendor test mode, exact animation/count semantics, global theme popup placement and real promotional subscription behavior remain open |

Decision records FO-01–FO-05 label the local privacy boundary as review-pending and the capture,
provider and reference-equivalence substitutions as **not accepted**. Plain text replaces rich HTML;
three bounded size choices replace arbitrary typography values. Required consent is never prechecked.
The sample-fill control uses only `Demo Visitor`, `demo@example.invalid`, `0000000000` and
`Local demonstration only.` and leaves consent unchanged. These strings are browser-only fixtures.

## Security and data ownership

Inputs are inside an accessible `role="form"` region with a fieldset, labels, required indicators,
per-field error descriptions and a polite status. There is no HTML form action or named input to
accidentally submit when JavaScript fails. Buttons use `type="button"`. Empty or invalid fields focus
the first error and produce no request. The editor preview runs validation locally without Magento.

On the dedicated native pages, the browser may POST only `form_key`, `page`, `section` and `revision`
to the installed `/mteforms/preview/check` route. It does not serialize any field or checkbox value.
The controller requires POST, exact HTTPS Origin/host, store 1, native form-key/session validation,
an active dedicated page and form, and the current SHA-256 selection identity. It rejects additional
request fields, including `email`, and checks bounded identifiers and body size. The only session
write is an integer last-check timestamp enforcing a two-second local throttle. No payload is logged,
no customer/subscriber service is injected, and no email transport is called. GET cannot execute it.

A valid response means **the native selected preview exists**, not that Magento validated visitor
text. Client validation and native selection validation are separate proofs. A malicious caller can
bypass client field validation, but cannot obtain a delivery or capture operation from this endpoint.
A future real-delivery adapter must validate all submitted fields and consent on the server; this
preview is not that adapter. All results prefix immutable **nothing sent/saved/subscribed** wording.
The error scenario returns HTTP 503 with an explicitly simulated provider error, not a fake success.

Form-key pages are dedicated noncacheable layouts and return private/no-cache headers. Ordinary
contact/newsletter routes, native behavior and page layout assignments are untouched. Popup storage
contains only an opaque page/section key with `shown` or a timestamp, never visitor text or identity.
Automatic open is suppressed when a field has focus, another dialog is open, the viewport is hidden,
or storage is denied. Manual reopen remains possible. No page-global tracking or campaign is installed.

## Real delivery prerequisites

A separately authorized native adapter must decide store-scoped contact recipients, sender identity,
approved transport and templates; newsletter enablement, subscriber ownership and confirmation policy;
consent wording, retention and evidence; native form-key/session handling; server-side field checks,
request-size and abuse protection; failure/retry behavior; and a controlled capture/test delivery
fixture before any real send is authorized. Provider terms and installed edition/version require the
[third-party review](../requirements/third-party-compliance.md). No provider has been selected, adopted,
enabled or accepted as an exclusion. This work does not claim hosted, provider or full-forms support.

## Verification and limits

Local evidence is in `product/.local/sol-536/`; images are in `output/playwright/sol536-*`.
Runtime: Node 22.22.0 / npm 10.9.4 / PHP 8.3.28, existing macOS installation and Playwright CLI.

| Check | Result |
| --- | --- |
| `npm run verify` from product | 104 passing tests, reviewed inventory/notices and browser build |
| `node --test component-library/test/*.test.mjs` | 39 passing tests, including six new forms tests |
| Form schema/native parity | Positive presets; unsafe fields, foreign scope/media/targets and multiple form blocks rejected; every enum/boolean/numeric bound renders equivalently in PHP/browser after excluding native token metadata |
| Native DI | `php bin/magento setup:di:compile` passed; config/layout/block/full-page cache types cleaned |
| `forms-lifecycle-check.mjs` | 67 passing assertions: selected output, invalid browser/native apply, unchanged failure bytes, empty content, stale hash, alternate surface/consent, escaping, restore, corrupt fallback, exact restoration, private cache and prior/native route controls |
| `forms-request-check.py` | 12 passing real HTTP checks: valid session token, throttle, forged/missing token, unexpected visitor data, foreign page/section/origin, stale revision, disabled section, GET exclusion and private page headers |
| Editor/browser | Contact edit/save/reload/apply/restore/reapply; independent Signup/Promotions save/apply; required/email/consent validation; no visitor data in native requests; simulated error and empty/disabled states |
| Accessibility/responsiveness | Explicit labels and error associations; 390px contact/signup without horizontal overflow; dialog initial close focus, reverse-Tab containment, Escape, opener restoration, manual reopen and mobile internal width; visual screenshots inspected |
| `forms-frequency-check.mjs` | Session/day delayed display, reload suppression, manual reopen and marker-only storage passed; exact selected bytes restored. The test waits for the prior page timer before clearing its marker to avoid a test navigation race. |
| Documentation | `make -C docs verify`: 44 source pages, 45 HTML pages and 4079 local links, with anchors/navigation/assets/source separation checks |
| Preservation | 30 protected files unchanged; page/store rows 240–253 and five configuration/assignment table hashes unchanged; exact local target-map change included in 13-file native manifest |

The focused checks do not certify full WCAG compliance, production rate limiting, server field
validation, customer/subscriber data retention, email deliverability, multi-node cache coherence,
Hyvä/Porto support or commercial release readiness. The native store cookie banner is retained in
screenshots. Its existing warning and the editor's existing favicon CSP warning are outside this package.

## Changed paths, reversal and review handoff

New original sources: `packages/forms/`, `themes/silt-form/forms.mjs`, native `FormsRenderer`, fixed
`Controller/Preview/Check`, route configuration, three generated layouts and hashed form CSS/JS,
forms test/coverage/build/install/snapshot/request/lifecycle/frequency scripts. Shared edits register
the package and targets, enforce the dedicated form boundary, import the trusted runtime/style,
expand generated schemas/theme metadata and update the existing starter target-combination test.
No new third-party code, asset, font, service or dependency was adopted; existing reviewed React/Ajv,
original ceramics media and installed Magento services are reused within their prior local scope.

`native-changed.json` records every installed changed file and before/after hash, including
`etc/local-targets.json`. `native-before/` holds the selective pre-change comparison source.
`preserved-hashes.json`, `preservation.json`, `db-before.json` and `db-after.json` retain the reversal
and preservation evidence. Only CMS/store rows 254–256 and the three target-map keys were added;
new draft/selection files and append-only local receipts belong to this family. Session throttle and
browser frequency markers are the only request/runtime state introduced.

Use **Restore original** separately on Contact, Signup and Promotions to remove their selections
while preserving their drafts. For complete removal, verify identifiers `mte-silt-contact`,
`mte-silt-signup` and `mte-silt-promotions` and store 1 ownership before deleting only pages 254–256.
Remove only `contact/signup/promotions` from the current local mapping, using its manifest entry and
backup for comparison. Remove the family's route/controller/renderer, DI items, layouts, hashed
assets, product registration/targets and wanted new drafts selectively; rebuild schemas/browser/DI
and clean affected cache types. Remove `mte-form-popup:` markers for these three demo paths and the
`mte_forms_last_check` session timestamp if complete runtime-state removal is required. Do not restore
an old whole module over later work or delete previous pages, selected JSON, drafts or serializer files.

Source/docs/local-INOX ownership returns to Coordinator 2 for independent substantive review.
Prioritize non-delivery and request boundaries, field/schema/native parity, exact gap classifications,
modal/frequency behavior, preservation and reversal. SOL-536, SOL-530 and the catalog milestone remain
open; no material exclusion or provider substitution is accepted by this report.
