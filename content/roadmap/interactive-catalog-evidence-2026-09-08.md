# Interactive catalog evidence · 2026-09-08

SOL-533 delivers **ten original interactive/media component subsets** in two populated, independently
saved local templates. All ten render through a trusted native adapter on existing INOX Luma.
SOL-533 remains **In Progress**: reference field gaps, remote/provider substitutions, exact
preset/snippet/countdown behavior and independent substantive review remain outstanding. Neither
this family nor SOL-530, SOL-512 or the full catalog milestone is closed.

The [299-entry field ledger](interactive-field-coverage-2026-09-08.md) records every assigned census
setting and block field. `component-library/reference/interactive-coverage.json` is the machine-readable
overlay; `scripts/plan-coverage.py` preserves it when regenerating the full
[catalog map](silt-form-catalog-coverage-2026-09-08.md). No Flux source was recrawled or copied.

## Ownership and environment

Coordinator 2 assigned task `01a080ae-e86c-7a82-8309-ab3678f886d7` sole source/docs/local-INOX ownership
for SOL-533 under milestone `c75032a6-70a2-4830-9c8d-f8d3129639e5`. Astra High was authorized for the
scoped interactive architecture, native trust boundary and implementation. No additional agents,
new execution tasks, environments or databases were created.

- Existing INOX root: `/Users/branorphiano/Projects/s1/inox-us-staging`.
- Branch `fix/INOXUS-creative-assets-fpc`; HEAD `046d6e87866e7f6c5172e9c63f90097ac8b08295`.
- Existing local database guard, store 1 and `Magento/luma` remain in force. No branch/theme replacement.
- Docs: `main`, baseline `b9704c423a6a1065b58252aace9fa8492caa5171`; pre-existing dirty work preserved.
- Product/component-library have no separate product Git baseline; no source commit SHA is claimed.
- Node 22.22.0 and PHP 8.3.28. No dependency installation, upgrade, Composer operation, new module
  enablement or module-config change. DI compilation and scoped local cache cleaning were performed.

## Open the populated demos

| Surface | Working content |
| --- | --- |
| `http://127.0.0.1:4177/?page=silt-media` | Media studio: story slider, comparison, image gallery, hotspots and tabs |
| `http://127.0.0.1:4177/?page=silt-motion` | Motion & voices: simple slider, scrolling messages, authored testimonials, video and video backdrop |
| `https://inox-us-staging.test/mte-silt-media` | Dedicated CMS page **246**, final saved/applied revision **4** |
| `https://inox-us-staging.test/mte-silt-motion` | Dedicated CMS page **247**, final saved/applied revision **2** |

Both pages retain visible populated content and selected JSON. The browser test temporarily edited
a section and nested slide heading, saved/reloaded/applied it, verified it on Magento, restored the
original region, then saved and reapplied the original populated demo copy. Media's revision increase
is from that real merchant flow. Motion retains its initially saved populated revision.

Pages 240–242, SOL-532 pages 243–245, original manual drafts, previous experimental selections,
ordinary routes and the accepted serializer workaround remain preserved. Existing Silt navigation
stays unchanged; only the two new pages show navigation to the expanded collection.

## Implemented behavior

`mte-interactive@1.0.0` registers original schema/default/control definitions and renderers. Merchant
JSON contains only bounded declarative values and opaque references. The native DI registry names
installed `InteractiveRenderer`; JSON cannot name a PHP class, file, JavaScript module, provider URL,
remote player or executable template. No general SDK/provider capability was introduced.

The package supports CMS links, new-tab announcements, Magento image references and alternatives,
mobile image selection, scoped surface/panel tokens, responsive heading/text sizing, spacing,
width and media sizing. Theme-owned template availability and capability checks restrict interactive
sections to the new media pages, where their content-hashed assets are loaded. Existing template
choices remain available there; editorial CSS is included only where needed for those choices.

| Stem | Working original behavior | Explicit limit |
| --- | --- | --- |
| `advanced-slider` | Ordered image/copy/link slides; previous/next, Home/End/arrows, touch swipe, bounded timed rotation, loop or bounded ends, horizontal/vertical input axis, split/overlay copy and mobile layout | Vendor-specific animation/highlight/preset and some content-height/typography settings remain open |
| `slick-slider` | Original carousel runtime with simple overlay/split presets, controls, timed rotation, image/copy/CMS links | No Slick dependency or imported vendor animation; source typography/visibility details remain partial |
| `comparison-slider` | Two real, distinct original images; native accessible range, percentage/clipping, labels, instructions and optional sweep | Exact source animation/preset behavior remains unproven |
| `image-gallery` | Responsive overflow gallery, keyboard and touch scrolling, optional timed movement, native modal enlargement, arrow navigation, Escape and focus restoration | Original layout/range choices; no claim of exact continuous vendor marquee behavior |
| `image-hotspots` | Positioned native disclosures, keyboard expansion/Escape, safe CMS links and mobile list/overlay choices | No product provider; palette tokens substitute only partially for arbitrary tooltip color settings |
| `scrolling-text` | Ordered real messages, optional original images/CMS links, keyboard/touch overflow, timed scrolling with pause, separators and type-size choices | Global sticky announcement placement belongs to SOL-535; exact vendor decoration/layout semantics remain open |
| `tabs` | Native-readable fallback stories enhanced into ARIA tabs, roving focus, arrow/Home/End selection, panels, images and links | Bounded plain text rather than exact source rich-text formatting |
| `testimonials` | Authored quote grid/carousel, optional images and authored star count, attribution and conspicuous fictional-source disclosure | No real review, product, aggregate-rating or remote provider integration |
| `video` | Real registered local WebM; native controls, keyboard play/pause, poster, description and text alternative, stack/split layouts | Remote video URL players and Shopify media APIs remain unimplemented |
| `video-background` | Real muted local playback, native controls, optional start/loop, readable content panel, mobile stacking and text alternative | No remote provider, independent mobile video selection or full vendor backdrop effects |

Automatic motion has an explicit start/pause control. Hover, focus or direct input stops motion;
hidden documents and reduced-motion changes also stop it. Automatic starts are suppressed under
reduced motion. Manual carousel, range, tab and scroll controls remain usable. Automatic scrolling
suppresses repeated position announcements. Carousel slides and tab stories remain readable when
JavaScript is unavailable; native disclosures and video controls remain available.

## Original media and dependency boundary

No library, remote service, copied font, icon pack, music, customer data, Flux image or provider
was adopted. Existing reviewed React/Ajv tooling and the original ceramics demonstration image
are reused. The local WebM uses the browser's native HTML video player; no player package is shipped.

`scripts/create-original-motion.mjs` authors simple geometry directly with Canvas 2D and records
an approximately three-second silent VP8 WebM with the already installed browser's MediaRecorder.
It has no input image or footage. The two original stills show one shape and a two-shape composition,
so the comparison changes real content. The generated files are `study-before.png`, `study-after.png`
and `motion-study.webm`, copied into `pub/media/mte-silt-form/` in the existing local installation.
Their exact hashes/byte sizes and generating source hash are in ignored `product/.local/sol-533/`.

These authored demonstration assets are accepted for this bounded local development use after
visual/playback inspection. This is not a commercial codec, browser-distribution, provider, asset
or full-product release clearance. Follow the [adoption requirements](../requirements/third-party-compliance.md)
before adding any remote player/library/service or changing distribution. The existing local
serializer workaround remains unchanged and has not become an upgrade-safe product dependency.

## Verification

| Check | Observed result |
| --- | --- |
| `npm --prefix product run verify` | **104 tests pass**; generated contracts, dependency/notice/asset checks and editor build pass |
| `node --test component-library/test/*.test.mjs` | **18 tests pass**; includes exact ten-type coverage, all templates, PHP/preview markup parity across field choices/bounds, semantic/native rejection, media trust boundaries and all 299 coverage destinations |
| `node component-library/native/silt-form/build-interactive.mjs` | Generates trusted schema/theme metadata and content-hashed CSS/JS only on the two media handles; no interactive assets on earlier pages |
| PHP lint and INOX `php -d memory_limit=2G bin/magento setup:di:compile` | Pass; installed renderer resolves through real compiled DI |
| `node component-library/native/silt-form/interactive-runtime.mjs` | **43 native/API checks pass**: exact saved application/order, empty media/blocks, layout/token variants, unsafe/foreign/unsaved data, stale/cross-origin restore, corrupt/oversized selection fallback, interrupted staging and original restoration |
| Media browser flow | **22 assertions pass**: actual timed/keyboard/touch carousel behavior, range clipping, gallery dialog/keys/focus, hotspots, tabs, reduced motion and 390px overflow/list behavior |
| Motion browser flow | **14 assertions pass**: slider/quote change, real scrolling/pause, live-announcement behavior, decoded 640px video playback via keyboard, pause, muted backdrop and reduced-motion change |
| Editor merchant flow | **11 assertions pass**: interactive iframe, schema-driven section/block edit, save/reload, native apply, browser-observed edited output and original restore, draft retention and populated reapplication |
| Progressive enhancement/failure flow | **9 assertions pass**: all slide/tab stories and both comparison images without JS, intrinsic disclosure/video controls, retained text alternatives and actual failed video requests showing both native error states |
| Existing-route and byte preservation | Included in native receipt: prior five rendered Silt pages contain no new runtime assets/markup; ordinary and existing experiment route controls return HTML; prior manual/foundation/editorial draft and selection hashes match the before snapshot |
| Docs `make verify` | Strict build and local-link/navigation verification recorded in the final docs receipt |

Browser artifacts and exact check names are retained under ignored `product/.local/sol-533/`:
`browser-media.log`, `browser-motion.log`, `browser-editor.log`, `browser-fallbacks.log`, screenshots,
`runtime-results.json`, product/library logs, DI log and final hashes. Chromium was exercised through
the existing Playwright CLI. This is focused keyboard/accessibility/responsive evidence, not a formal
WCAG certification or proof for every browser/assistive technology. Safari/Firefox and Hyvä are untested.

Browser QA found and corrected the Luma root-font sizing mismatch and a dialog-close focus race.
The editor still reports its pre-existing blocked empty `data:,` favicon under its existing CSP;
that message is not an interactive script failure. Native requests retain the existing unrelated
store warning. No remote-provider or production performance proof is claimed.

## Touched local state and reversal

Before source/native mutations, `product/.local/sol-533/before/` captured component-library,
product editor/src and the installed `SiltFormDemo` module. `preservation.json` records the pre-existing
manual/foundation/editorial draft and selection bytes. `touched-native-files.json` lists exact
installation files; final manifests include hashes and media byte sizes.

| Area | Scoped mutation |
| --- | --- |
| Original component source | New interactive package/runtime/style, theme factories, trusted package registration, native adapter/validation/DI, additive schema/metadata and coverage/test/build/setup scripts |
| Product | Fixed preview runtime/style imports, dedicated-page template/capability handling, exact original media routes and existing field-control integration; no generalized hosted provider or SDK |
| INOX source | Matching `app/code/MageThemeEditor/SiltFormDemo/` files plus installation-only `media` and `motion` target-map entries |
| INOX database | Created only `cms_page` identities **246** (`mte-silt-media`) and **247** (`mte-silt-motion`) with store-1 associations; no existing CMS content, theme assignment or database replacement |
| INOX media | Three newly authored files in `pub/media/mte-silt-form/`; existing ceramics file preserved |
| Selected state and drafts | New `media.json`/`motion.json` selections in `var/mte-silt-form/`, independent `silt-media.json`/`silt-motion.json` drafts, appended shared receipt log |
| Generated state | DI compilation and local `layout`, `block_html`, `full_page` cache clean; hashed assets allow current merged/static requests to load correct bytes |

A normal reversible content action is **Restore original** on either new editor page. It removes only
that page's selected content while retaining its saved draft. Both populated selections are deliberately
left applied at handoff.

For complete scoped removal, first snapshot any later user edits. Restore the two selections using
the existing local bridge and current selection hashes. Verify original-region HTML. In the existing
INOX root, use Magento's page repository to delete **only** 246/247 after rechecking identifiers and
store-1 associations; remove only the matching two target-map keys. Restore the changed existing
module files from `before/native/`, remove only new interactive renderer/layout/hashed assets from
`touched-native-files.json`, and preserve unrelated modules and the earlier editorial/foundation files.
Recompile DI and clean the same local cache types. Restore only changed product/library files from
the before snapshot if reverting implementation. Remove or archive only the two new drafts and three
new media files after checking for later edits/references. Keep receipts; do not rewind the shared
receipt log, reset branches, copy databases, disable other experiments or edit the accepted serializer.

## Handoff and open criteria

All ten assigned stems have working original local evidence. Their **299 fields** include 233 mapped
original-subset entries, 36 metadata entries, 19 open field gaps, three open provider entries, two open
scope entries, two local-video substitutions with provider gaps, and four mandatory accessibility
behaviors. Mapping is not exact field/preset/snippet parity. The explicit IM-01–05 decisions in the
field ledger distinguish implementation choices from **unaccepted** material exclusions.

Source/docs/local-INOX ownership returns to Coordinator 2 for an independent substantive review.
Do not dispatch another family from this implementation task. SOL-533's parent, milestone,
dependencies and acceptance checklist remain unchanged; evidence-only Linear progress does not
accept exclusions or close this task. No commit, push, PR, production/remote publication, new theme,
marketplace action or customer communication was performed.
