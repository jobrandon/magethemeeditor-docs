# Original developer section library · 8 September 2026

Initial-lane status: **local implementation and author-to-native notice proof complete**. The
coordinator supplied the accepted package proof and closed independent review as the baseline for
the subsequent [starter foundation](#silt-form-starter-foundation); that review was not rerun.
The original observations below remain a dated record. Owner: task `01a07faf-3e5c-7b91-a0a5-7c52c2684582`, GPT-6 Astra High under the user's
explicit architecture/implementation allocation. Coordinator 2:
`01a07c28-b8ed-78d1-85e2-25f171859b5f`. The user clarified that developer-authored sections/components
are a product purpose, and the coordinator explicitly required the separate narrow native notice
adapter in this batch. No additional execution task or subagent was created.

## Delivered scope

The bounded `component-library/` lane contains original package contracts, presets, validation,
HTML renderers, scoped responsive CSS, fixtures, tests, reference inventory, implementation notes
and a separate native experiment. [Developer package instructions](../architecture/developer-packages.md)
document the working trusted registration entry point and the remaining SDK boundary.

| Component/package | Actual behavior | Native status |
| --- | --- | --- |
| `mte-studio/banner` | Heading, eyebrow, body, media reference/alt, named CMS link, alignment, height, surface/spacing/width presets and missing-image state | Native adapter outstanding |
| `mte-studio/rich-text` | Ordered paragraph/emphasis, heading, list and quote blocks; block controls, limits and empty state | Native adapter outstanding |
| `mte-studio/image-text` | Story/media split, image position/fit, CMS reference and narrow-screen stacking | Native adapter outstanding |
| `mte-studio/cards` | Ordered nested image/text/link cards; 1–4 desktop columns, responsive stacking, block bounds and empty state | Native adapter outstanding |
| `mte-studio/faq` | Ordered questions/answers with default-open state, native keyboard disclosures and empty state | Native adapter outstanding |
| `author-example/notice` | Independently authored heading/message/tone package; catalog registration, generated controls, save/reload/export data and preview | Separate native registry/schema/escaped PHP renderer proved on dedicated INOX page 239 only |

Every component uses a stable namespaced type, versioned package pin and component version. The
five Studio components were preserved while extracting their definitions/renderers into a package.
The independent author example registers through `component-library/packages.mjs`; it has no type
switch or control implementation in editor core. Executable package code stays separate from
merchant JSON. Both packages are original; no third-party dependency was installed or upgraded.

The [complete reference inventory](section-library-reference-inventory-2026-09-08.md) covers the
supplied local reference's self-declared Flux 2.7.1 by Mana Themes. It contains 76 Liquid section
files: 44 strictly parsed/locally structure-checked preset-bearing candidates, 22 fixed/no-preset
sections, seven fragments with no schema and three malformed JSON schemas (`footer`, `info-cards`,
`main-product`). Two section-group JSON files are groups, not addable sections. The census includes
1,408 section setting entries, 122 block definitions, 710 block setting entries and 155 top-level
global settings plus their nested color-scheme definitions. Setting counts include editor metadata.
Preset presence is not full Shopify schema or runtime certification. Trailing-comma recovery is
an inventory-only shadow parse; malformed sources remain classified as malformed.

No Liquid, reference JavaScript/CSS, schemas, options/defaults, translations, assets, icons or fonts
were copied, translated or imported. Reference SHA-256 identities were checked against the starting
snapshot. Mapping similar capabilities is explicitly partial; additional reference effects, sliders,
timers, collection/product components and providers remain outstanding. Product, category, media,
form, review and account concepts map only to Magento-owned services or declared provider gaps.
There is no checkout imitation, remote package system or marketplace implementation.

## Product and browser validation

Environment: macOS arm64, Node 22.22.0, npm 10.9.4. The pre-existing reviewed package graph and
original ceramics asset remain unchanged. The cached Playwright CLI 0.1.19/Playwright
1.63.0-alpha-2026-08-31 was used as existing development tooling, with no install, upgrade or
redistribution. The product's existing dependency and notice guards pass; this is not commercial
clearance for the product, reference theme or client installation.

| Exact check | Result / boundary |
| --- | --- |
| `cd product && npm run verify` | **95 tests pass**, including the prior 84 and 11 new contract/renderer/package/handoff tests; build, dependency identities, notices and existing asset checks pass |
| `node component-library/scripts/build-schema.mjs` | Generates original JSON Schema and package/preset inventory; validates all section/block presets |
| `cd product && npm run validate -- content ../component-library/fixtures/home.json` | Valid five-section portable document |
| `cd product && npm run validate -- content ../component-library/fixtures/author-home.json` | Valid six-section document including independent author package |
| `python3 component-library/scripts/inventory-reference.py` | Complete reproducible capability census; reference read-only |
| `php component-library/native/test/validator.php` | **19 native validator assertions pass**: target, package/type/version, fields, malformed/duplicate wire data, limits, safe text handling |
| Browser editor at loopback 4176 with separate draft storage | Author example added from catalog, generated controls edited, saved as revision 3, reloaded with exact heading `Registered from package files` and package/component IDs intact |
| Browser nested controls | FAQ block reorder/duplicate/undo, invalid-answer save denial and native Enter/Space disclosure pass |
| Browser responsive library | 390px/768px checks have no library/document horizontal overflow; direct 390px preview has six sections, document width 390 and one 350px card column |
| Browser imagery | Three referenced original images decode successfully; empty cards render explicit unavailable-image states |
| Browser native notice | Exact authored heading, native CSS tint and no notice overflow at 390px; scoped notice width 1040 at desktop |

Browser traces, original scripts, snapshots, response facts and screenshots are ignored under
`product/.local/section-library/`. CLI used the cached executable
`node ~/.npm/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js` with named sessions
`mte-library` and `mte-native-package`. `browser-author.js`, `browser-library.js`,
`browser-mobile-result.log`, `browser-images-result.log` and `native-browser-result.log` record
the exact executed interactions. Full-page iframe screenshots were clipped by the outer canvas;
the verified library image uses the same preview renderer in its own tab, after image decoding.
This distinction avoids treating a clipped screenshot as layout failure or full-page visual proof.

The existing editor server on 4173 was restarted from its verified original command/cwd so its
server validators and newly built browser files agree. Its manual saved draft files remained
byte-identical across restart. The existing home draft was read back successfully. The authored
collection/demo evidence lives separately at 4176 in `.local/section-library/drafts/`; it does not
replace the user's manual home/studio drafts. Existing imported/saved content and the 03F projection
retain their prior behavior. The editor remains an illustrative preview with manual local native
handoff, not a connected authenticated storefront editor.

## Exact native registration and local runtime

Verified existing root: `/Users/branorphiano/Projects/s1/inox-us-staging`; branch
`fix/INOXUS-creative-assets-fpc`; HEAD `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
Local PHP 8.3.28. The local bootstrap verifies the existing INOX database identity before use;
credentials are consumed without printing. No environment, database or theme was provisioned.

The added module is `app/code/MageThemeEditor/SectionLibraryExperiment/`, copied from the original
`component-library/native/SectionLibraryExperiment/` source. Its trusted local mapping is generated
in `etc/local-target.json`: exact INOX root, store 1, page 239 and `Magento/luma`. It exposes only
the layout handle for identifier `mte-package-library`, additionally checking host/route/store/page/
theme/non-cacheable layout inside the block. The native registry accepts only the author's notice
identity/version and maps it to installed original PHP. Its schema equals the portable author's
schema. The payload cannot supply code, a PHP class, template path, renderer or service endpoint.

Actual commands from the INOX root:

```sh
php bin/magento module:enable MageThemeEditor_SectionLibraryExperiment
php /Users/branorphiano/Projects/jobrandon/MageThemeEditor/component-library/native/scripts/create-page.php
php bin/magento setup:di:compile
php bin/magento cache:clean config layout
```

The first compile identified a property name colliding with Magento Template's inherited validator;
renaming it to `contentValidator` resolved it, and the complete compile passed. The standard
`module:enable` command reported cache and generated-class cleanup. Generated DI/interceptors and
the module's static CSS were then generated locally. Cache types were never disabled, but cache
contents were invalidated by normal local module enablement and the explicit config/layout clean.
No `setup:upgrade`, Composer operation or remote deployment was run.

The saved editor section crossed the new independent fixed handoff:

```sh
# From MageThemeEditor:
node component-library/native/scripts/stage-notice.mjs \
  product/.local/section-library/drafts/home.json \
  product/.local/section-library/notice-stage.json

# Copy those validated bytes only to INOX var/mte-section-library/inbox.json.
# From the verified INOX root:
php /Users/branorphiano/Projects/jobrandon/MageThemeEditor/component-library/native/scripts/select.php select
php /Users/branorphiano/Projects/jobrandon/MageThemeEditor/component-library/native/scripts/select.php restore
```

The stage preserves the exact author section, including its generated stable section ID, package
pin and settings; only the outer document/scope/state are mapped to the fixed local experiment.
It requires exactly one author notice and the matching saved illustrative home identity. No target
argument is accepted by native selection. The existing 03F bridge remains unchanged and continues
to reject these new types.

`python3 component-library/native/test/runtime.py` records 13 local checks and restores the
original state in `finally`. It refuses an already active selection. The initial author notice
selection returned `200 text/html` at `/mte-package-library`, with exact edited heading, native
package marker, original region absent, neighboring native CMS region retained and `no-store`.
Foreign package/type/store and unknown-template inboxes rejected, leaving active bytes identical.
Malformed and oversized active bytes retained the original region and neighbor. Authored script-like
text was escaped in actual HTML. Restore removed the active file and returned original output.

Controls `/`, `/en/mte-batch03c`, `/mte-batch03d` and `/mte-batch03d-control` remained native HTML
with no new package output. The homepage and unassigned 03D control retained public cache headers;
dedicated experiments retained their existing `no-store` boundaries. The first runtime script tried
the 03C page without its `/en/` store prefix and got the expected 404; using its registered exact
URL completed the controls. The test's `finally` restored the new selection even on that first run.

Native limitation: the existing local Magento serializer warning remains visible above the Luma
page and can widen the full page at 390px. The new notice itself has no horizontal overflow.
This batch does not fix or claim full-page accessibility/CSP/theme health; it records scoped
native package rendering amid that pre-existing environment issue. The illustrative editor's
pre-existing `data:,` favicon produces a CSP console warning; no new package script errors were found.

## Touched paths and database preservation

| Scope | Exact authored/local changes |
| --- | --- |
| Library | New `component-library/AGENTS.md`, README/implementation notes, package list, two original packages, generic registry/render/helper/CSS, generated contracts, fixtures, tests, inventory script/data and separate native module/scripts/tests |
| Product | `contracts/v1/component.schema.json`; `src/contract.mjs`, `src/build-editor.mjs`, `src/demo-server.mjs`; `editor/model.mjs`, `app.mjs`, new `library-controls.mjs`, preview HTML/JS/CSS and editor CSS; new `test/section-library.test.mjs`; README; regenerated ignored `dist/` |
| Canonical docs | Developer package guide, this evidence, complete reference census, navigation and targeted execution/decision/home/roadmap links |
| Existing INOX source | New `app/code/MageThemeEditor/SectionLibraryExperiment/` including local-only target JSON; one added `MageThemeEditor_SectionLibraryExperiment => 1` key in already-dirty `app/etc/config.php` |
| Existing INOX data | New `cms_page` row **239** (`mte-package-library`) and `cms_page_store` row **239:1**; no existing CMS page/block/store row changed; no `core_config_data` row changed |
| Native private state | New `var/mte-section-library/inbox.json`; transient `active.json`/`active.tmp` during tests; active selection absent at handoff |
| Local generated artifacts | Normal Magento compiled/generated metadata and module static CSS, product `dist/`, docs `site/`, ignored evidence and dedicated local demo drafts |

Before/after hashes cover every existing row of `core_config_data`, `cms_page`, `cms_page_store`,
`cms_block` and `cms_block_store`, plus all pre-existing MageThemeEditor module/state files. They
show only the two added CMS records above and the single source config-file change. The config
array diff contains only the new module key. Config/layout/block_html/full_page remain enabled.
These scoped checks do not claim a complete all-table database audit. No catalog/customer/order,
active-theme, homepage assignment or existing CMS content was authored by this work.

The old 03C/03D module and selection/inbox source hashes remain unchanged. The historical research
document and Flux reference hashes remain unchanged. Product/library source has no task-owned Git
commit; docs remain on `main` at baseline `b9704c423a6a1065b58252aace9fa8492caa5171` with preserved
pre-existing changes. No commit, push, PR, source publication or production change occurred.

## Practical reversal and next boundary

The native selection is already restored. To repeat only the proof, stage the saved local author
document, copy to the fixed inbox, run `select.php select`, verify the dedicated page, then run
`select.php restore`. Do not overwrite an unrelated active selection. Restore never touches 03F.

To remove this experiment later, first restore. Through the Magento CMS repository, delete page
239 only after checking its identifier is still `mte-package-library`, store membership is still
`[1]`, and its content has not been subsequently authored by the user. This also removes its
store association. Disable only `MageThemeEditor_SectionLibraryExperiment`, remove that module's
directory/private state if no longer wanted, and rebuild Magento DI with the normal local commands.
Remove only its added config key; do not replace the entire already-dirty config with the backup.
Clean the necessary local config/layout caches. Preserve all other modules, CMS records and cache
configuration. The ignored before snapshot is evidence, not authorization for bulk rollback.

For source-only reversal, remove the new lane, reverse the listed product integration hunks and
rebuild/restart the demo while retaining `.local/demo-drafts/`. Export any newly saved package
documents first: old validators deliberately reject those capabilities. Remove only this batch's
docs/navigation additions after checking for later edits; preserve unrelated dirty documentation.

Remaining work: native adapters for the five Studio components and their data/media references;
generic native package registration/version compatibility; richer field/asset/preset support;
hosted ownership/permissions, signed publishing, durable recovery/cache invalidation, theme/version
matrix, independent review, merchant validation and commercial release evidence. The existing
SOL-501/512 criteria and statuses are not completed by this bounded proof. No new marketplace or
provider issue is created, and no seller, commission or payout workflow is implemented.

## Documentation and existing Linear scope

`cd docs && make verify` passes: **33 source pages, 34 HTML pages and 2,665 local links**,
including anchors, assets, navigation and source/output separation. The existing pinned docs
runtime prints its upstream MkDocs-2 advisory; the strict build/check itself succeeds. Documentation
validation does not establish native Magento behavior.

Evidence-only comments were added to existing SOL-501 and SOL-512 after reading their current
criteria and dependencies. Comment IDs: `6d96daac-2864-4d7a-b37e-05b247760993` and
`b0ff193b-b0ae-4c7f-8259-a2aee2d8114a`; returned bodies were verified. SOL-501 remains In Progress,
SOL-512 remains Backlog; no acceptance text, status or dependency was changed. No new issue or
marketplace/provider task was created.

The developer guide and long reference inventory were inspected in the local docs browser.
At 390px, document width remains 390px; all 197 rendered inventory tables scroll within their
containers, and its 94 section/global subsection headings are present. Navigation/headings and
rendered content were inspected. Ignored screenshot: `output/playwright/docs-inventory-mobile.png`
under the batch evidence folder. The local docs preview remains on loopback 8017.

## Silt Form starter foundation

Observation date: **8 September 2026**. Implementation owner
`01a07ff1-5997-7f42-86e8-85ed3e7ce0f8`, Astra High under the explicit section/theme architecture
allocation; sole source/docs/local-INOX writer for this batch. Coordinator 2 supplied SOL-526–529
for the foundation and SOL-531–537 for the full catalog sequence. The milestone is **Flux component
catalog and working demo theme**, `c75032a6-70a2-4830-9c8d-f8d3129639e5`. The accepted notice/package
implementation and closed review were reused, without another reference crawl or review rerun.

### Delivered merchant flow and native support

The [starter package guide](../architecture/developer-packages.md#silt-form-starter-theme-package)
describes the actual extension points. Open
[the separate local editor](http://127.0.0.1:4177/?page=silt-home), select a page and starter, edit,
Save draft, Apply/Update local page, then Open Magento page. Restore original removes the selected
page content while retaining its saved draft. No merchant terminal or manual JSON transfer is needed.

| Page | Existing local target | Original populated composition | Saved content at handoff |
| --- | --- | --- | --- |
| Home | `https://inox-us-staging.test/mte-silt-home`, CMS 240, store 1 | Banner, rich text, image/text story, three cards, FAQ | Independent Home copy/media/link/alignment edits; scoped accent setting |
| About | `https://inox-us-staging.test/mte-silt-about`, CMS 241, store 1 | Banner, multi-block story/list/quote, image/text invitation | Independent About heading and saved content |
| FAQ | `https://inox-us-staging.test/mte-silt-faq`, CMS 242, store 1 | Introduction, two FAQ groups, image/text invitation | Independent question text and saved block order |

All use the existing default-store **Magento/luma** theme. The scoped Silt & Form masthead,
three-page navigation, section content and colophon live inside the opted-in content area. Native
Magento header/footer/commerce and a dedicated native CMS neighbor remain outside it. This is an
original hybrid content-theme package, not a Magento theme replacement.

| Supported native capability | Actual field coverage |
| --- | --- |
| `mte-studio/banner@1.0.0` | Heading, eyebrow, body, image/alt/decorative state, real CMS reference and link label, alignment, height, surface/width/spacing |
| `mte-studio/rich-text@1.0.0` | Ordered paragraph/emphasis, heading, list, quote/credit blocks; empty story state; common appearance fields |
| `mte-studio/image-text@1.0.0` | Story/media, image start/end, cover/contain, link fields, alt/decorative state and common appearance |
| `mte-studio/cards@1.0.0` | Ordered bounded cards with heading/body/image/link, 1–4 desktop columns, responsive stacking and empty state |
| `mte-studio/faq@1.0.0` | Ordered bounded questions/answers, initial-open setting, native keyboard disclosure and empty state |
| Theme tokens | Scoped accent border and section rhythm from accent/spacing; original package shell CSS and system fonts |
| Media/page references | Actual local Magento media image and active dedicated CMS pages with exact store membership; absent media/link states |
| Registration | Package-owned schema/presets/generated controls/preview; trusted native DI `RendererInterface` registry and generated native schema |

This is support for the **current original schema**, not full Flux field/behavior equivalence. The
[complete coverage/dependency map](silt-form-catalog-coverage-2026-09-08.md) assigns 76 section stems,
1,408 section settings, 122 blocks/710 block settings, two groups and 155 globals plus seven nested
color settings to named follow-on owners. Five base types do not close SOL-531 or final SOL-530.

### Verification evidence

Environment: existing macOS arm64, Node 22.22.0/npm 10.9.4 and PHP 8.3.28. INOX root
`/Users/branorphiano/Projects/s1/inox-us-staging`, unchanged branch
`fix/INOXUS-creative-assets-fpc`, HEAD `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
Invictus’s existing root and local HTTP runtime were inspected; no Invictus source or DB was written.
Docs remain on `main`, baseline HEAD `b9704c423a6a1065b58252aace9fa8492caa5171` with prior edits preserved.

| Check | Actual result |
| --- | --- |
| `cd product && npm run verify` | **98 tests pass**: prior 95 plus template-isolation/identity, native schema parity and unsafe-native-input groups; reviewed dependency/asset guards and browser build pass |
| `node component-library/native/silt-form/build.mjs` | Generates native schema from installed original package registry and copies the original scoped CSS |
| `node component-library/native/silt-form/runtime.mjs` | **26 checks pass** on local Magento: foreign scope/document/package/type/version, executable field, missing references/alt, invalid block, stale restore, cross-origin/missing-origin/command injection requests, unsaved draft rejection, interrupted staging, malformed/oversized active fallback, appearance/order/settings, escaped text, empty states, restore and five unassigned controls |
| Browser Home | Template choice; heading/media/alt/CMS-link/alignment edit; image-empty state; invalid-alt save denial; section reorder; save/apply/reload preserved the exact edit |
| Browser About and FAQ | Independent template/edit/save/apply/reload; FAQ block order/duplicate/undo/redo/remove; page switching preserved Home, About and FAQ independently |
| Native/preview comparison | All 12 saved sections across the three pages have matching semantic DOM after normalizing the existing native image-optimizer picture/source wrappers and their whitespace; actual applied revision, native header/footer, neighbor and scoped H1 verified |
| Browser restore/update | Each page restored through editor controls to original native output and then reapplied from the retained saved draft; Home also saved and updated through its Update local page control |

Ignored evidence is under `product/.local/silt-form/`, including `runtime-results.json`,
`browser-foundation.js/.log`, `browser-pages.js/.log`, `browser-parity.js/.log`,
`browser-restore.js/.log`, responsive checks and `output/playwright/` screenshots. Browser commands
use the already installed cached Playwright CLI at
`~/.npm/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js`, with sessions `mte-silt`
and `mte-silt-native`. No browser tool/dependency was installed or upgraded.

The initial root control returned its existing 302 redirect to `/en/`; the corrected control
followed that redirect and verified native HTML. Native HTML’s existing image optimizer wraps
images with a local WebP source; this is why the browser comparison is semantic and explicitly
normalizes those wrappers. Initial raw-DOM equality was not reported as passing.

The local Magento serializer warning observed during the foundation work was remediated on the same
local INOX installation on 8 September. The triggering value was raw block HTML in Magento CSP block cache
(`BLOCK_2933c6560b8829dc9423056aec4b39ad5632046fe3b00600b55999a0cc02f0a0`, 113 bytes, SHA-256
`55acca3ce4b4661c9db2d1304a4150e6097fd44e9429a937b6c4cfd152a88952`), not Silt & Form content,
CMS data or drafts. PHP 8.3 raises an `E_WARNING` for that raw value; the installed serializer only
converted `E_NOTICE` to its existing invalid-value exception, preventing CSP's raw-block fallback
from taking effect and leaking the warning before the HTML document.

The local compatibility change is one expression in
`vendor/magento/framework/Serialize/Serializer/Serialize.php`: its existing temporary error handler
now covers `E_NOTICE | E_WARNING`. It does not suppress errors: invalid serialized input becomes the
serializer's existing `InvalidArgumentException`; callers that deliberately support raw CSP block
HTML retain their fallback, while uncaught invalid data still fails normally. A scoped
`cache:clean block_html` and removal of that ID were performed during diagnosis, but normal reads can
legitimately recreate the same raw entry; cleanup is not the durable remedy. No CMS, draft, Silt module,
03C/03D/03F state or configuration was changed. Exact HTTPS checks on Home, About and FAQ each returned
`200` with no warning or local filesystem path before `<!doctype html>`.

This edit is a local Magento vendor compatibility workaround, not an upgrade-safe or commercial delivery
mechanism. It must be re-evaluated against the installed Magento/PHP version and carried through an
appropriate upstream-supported patch or upgrade before any distribution. Reversal is to restore
`E_NOTICE` in that one serializer handler and clean `block_html` again; it does not require database
restoration.

Native CSP/plugin console messages and the illustrative editor’s existing favicon CSP warning remain
outside this foundation. No full-site accessibility, CSP health, production performance or broad
theme-support claim follows.

Native responsive checks cover all three pages at **390, 768 and 1200 pixels**. Their content-shell
width/scrollWidth pairs are respectively **360/360**, **738/738**, and **1160/1160**. Home cards have
one, two and three columns at those viewports. All eight page-image instances decode from the
local Magento-generated WebP rendition. The test explicitly requested lazy images before inspecting
full-page output. Native FAQ Enter and Space toggle disclosures and return them to their initial
state. The foundation capture predates the serializer remediation: it recorded a 488px document
caused by the warning while the new shell remained 360px. The clean-document mobile recheck is
recorded separately with this remediation; neither result is a whole-site audit.

### Installation, local changes and reversal

Developer setup used the existing installation only:

```sh
# From MageThemeEditor, generate the native schema/CSS and copy the new original module
# to the existing INOX app/code/MageThemeEditor/SiltFormDemo directory.
node component-library/native/silt-form/build.mjs

# From /Users/branorphiano/Projects/s1/inox-us-staging:
php bin/magento module:enable MageThemeEditor_SiltFormDemo
php /Users/branorphiano/Projects/jobrandon/MageThemeEditor/component-library/native/silt-form/install-pages.php
php bin/magento setup:di:compile
php bin/magento cache:clean config layout

# From MageThemeEditor, after building product:
node component-library/scripts/silt-demo.mjs
```

The original reviewed `product/editor/assets/ceramics.png` was copied to the new dedicated Magento
media directory. No new software package, vendor asset, font, image-generation request or service
was adopted. The existing optimizer generated `ceramics.webp` from that image. No Composer change,
setup:upgrade, fresh installation/database or active theme/homepage assignment occurred. Normal
module enablement cleared local caches/generated classes; complete DI compilation passed. All four
checked cache types (`config`, `layout`, `block_html`, `full_page`) stayed enabled.

| Scope | Exact change / preservation evidence |
| --- | --- |
| Theme package | New `component-library/themes/silt-form/theme.mjs`, `shell.css` and `src/starter.mjs` export |
| Native source | New `component-library/native/SiltFormDemo/` with DI registry, renderer interface, validator, native CMS/media references, selection service, scoped block/layouts and generated schema/CSS |
| Local bridge/setup/tests | New `component-library/native/silt-form/` build, install-pages, command, validator harness and runtime test; `component-library/scripts/silt-demo.mjs` |
| Product | `src/silt-local-bridge.mjs`, `src/demo-server.mjs`, `src/build-editor.mjs`; `editor/model.mjs`, `app.mjs`, `library-controls.mjs`, `preview.mjs`, `preview.html`, `editor.css`; new `test/silt-form.test.mjs` and the existing UI-race harness’s browser-location mocks |
| Coverage | New `component-library/reference/delivery-coverage.json` and `scripts/plan-coverage.py`; accepted census/reference bytes preserved |
| INOX source | New `app/code/MageThemeEditor/SiltFormDemo/`, including installation-only `etc/local-targets.json`; only new config entry is `MageThemeEditor_SiltFormDemo => 1` |
| INOX database | Added CMS rows **240, 241, 242** and store associations **240:1, 241:1, 242:1**; no prior `cms_page`, `cms_page_store`, `cms_block`, `cms_block_store`, or `core_config_data` row changed or removed |
| INOX media/state | New `pub/media/mte-silt-form/ceramics.png` and generated `.webp`; `var/mte-silt-form/{home,about,faq}.json`, selection lock, local receipt history and transient atomic-write files |
| Local drafts/evidence | Dedicated `product/.local/silt-form/drafts/`; before/source/config snapshots, database row hashes/diff, response evidence and browser scripts/screenshots under `.local/silt-form/` |
| Canonical docs | This evidence, developer guide, new catalog coverage plan/navigation and concise linked execution/README additions |

Before/after row hashes prove the scoped table changes above, not an all-table database audit. The
already-dirty config file was compared as a PHP module map; its only additional key is the new module.
All pre-existing MageThemeEditor module/state files captured at start and both prior manual draft
locations retain their hashes. 03C/03D/03F and the accepted author-notice selection remain unchanged.
The normal homepage/control routes return native HTML without Silt & Form output. Root’s existing
redirect is followed to `/en/`. No catalog/customer/order data was authored, and no real message sent.

**Reversal through the UI:** choose each demo page, Refresh local status, then Restore original.
This removes only its active selection and records the transition. Saved page drafts remain. Restore
was proved on all three pages, followed by reapply so the populated demo remains usable. The final
Home draft/selection is revision **3** with accent `#456452`; About and FAQ are revision **2**.

**Source/database removal, if later requested:** first restore all three selections. Verify CMS
IDs 240/241/242 still have identifiers `mte-silt-home`, `mte-silt-about`, `mte-silt-faq`, membership
`[1]` and no subsequent user changes, then delete only those pages through the CMS repository.
Disable only `MageThemeEditor_SiltFormDemo`; remove only its module key/directory and dedicated
media/state directory if no longer referenced; rebuild local DI and clean config/layout caches.
Do not replace the entire already-dirty config file or perform a bulk database restore. The baseline
snapshot is evidence, not authorization to overwrite unrelated work.

For source-only reversal, reverse the listed product integration hunks and remove the new theme/
native/coverage files after checking for later owners, then build/restart the affected demo server.
Preserve/export new saved drafts first. Keep old manual drafts and accepted experiments. No commit,
push, PR, production operation or public deployment occurred. Final foundation review is separately
owned by the coordinator; the full catalog, hosted publication, generic SDK, Hyvä/Porto, native
catalog/PDP/search/cart/account/provider families and commercial clearance remain open.

Final additional checks: the editor and preview have no horizontal overflow at 390px; the editor
also fits 768px, with its 390px preview retained. Preview FAQ Enter/Space works. During an actual
editor-process stop, Magento rendered the correct Home r3 (five sections), About r2 (three) and FAQ
r2 (four), with native chrome and neighboring CMS content; native PNG bytes matched the original
image, and both PNG/WebP returned their correct image content types. The editor was restarted and
left running on 4177. Evidence: `editor-offline-content.json`, `editor-offline-results.json`.

An actual missing-media test temporarily renamed only the new original PNG. The native reference
catalog returned unavailable, apply rejected without changing active bytes, and the native page
showed its readable unavailable-image state. The image was restored in `finally`. Evidence:
`media-failure.mjs` and `media-failure.json`. No unrelated media or CMS page was changed by this test.

`cd docs && make verify` passes: **34 source pages, 35 HTML pages and 2,818 local links** checked,
including anchors/assets/navigation/source boundaries. The existing pinned docs tooling emits its
upstream MkDocs-2 advisory; the strict build and validation succeed. This is documentation proof,
separate from the Magento/browser checks above.

The final package-owned shell extraction also passed native/preview semantic DOM comparison on
Home r3, About r2 and FAQ r2, in addition to their 12 sections. Presentation copy/navigation now
comes from the theme package and generated native metadata. Magento DI was rebuilt successfully
for the injected `ShellRenderer`; the product suite remains 98/98. All three changed docs render
at 390px with document width 390. The 76 accepted reference-section hashes and historical research
hash remain unchanged; 03C/03D inbox/lock identities match their accepted earlier receipt.

Evidence comments were posted after reading current criteria to SOL-526–529 and SOL-531, with
returned bodies verified. IDs respectively: `ae5b20a2-2803-423d-bf01-242865b92abe`,
`b67639b5-9eb8-49e7-9ae8-5cdd5cf64e48`, `99e5534f-5516-4c11-a7c2-3e55088c77e7`,
`d12fa667-4fb4-4d25-8f03-afe282fc0262`, `9205a4c6-c757-45b2-b985-384e3a6d26c3`.
All five remain In Progress; source is ready for coordinator-owned foundation review, and SOL-531
still has later template/behavior work. Parent criteria/statuses/dependencies, later family statuses
and SOL-530 were not changed. No separate marketplace/provider task was created.
