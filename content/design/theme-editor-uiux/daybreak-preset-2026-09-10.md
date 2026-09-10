# Daybreak Market theme preset

Observed 10 September 2026. Owner: Resource Desk task `01a08b2d-21a8-7f53-a51b-09b853c71451`, continuing the assignment reconciled by Development Coordinator 2. The older Flux writer remains cancelled. This receipt covers an original local theme preset, not a Magento deployment or a completed independent theme SDK.

## Open and edit

Run `npm --prefix product run build`, then `node component-library/scripts/silt-demo.mjs` from the workspace root. Open `http://127.0.0.1:4177/theme?preset=daybreak`, or use **Choose theme → Daybreak Market** in the Resource Desk editor. Theme selection opens a separate editor tab so existing draft buffers remain available.

The versioned developer resource lives in `component-library/themes/daybreak/`: `theme.mjs` owns identity, package pins, default portable content, references, shell and presentation metadata; `style.css` owns storefront appearance; `runtime.mjs` owns Alpine lifecycle, navigation and card enhancements. `components.mjs` registers 19 semantic `daybreak-market/*` component variants using the existing package schemas and render primitives; portable `section.type` preserves each variant when instance IDs change. Identity is `daybreak-market/full`, version `1.0.0`. Existing registered Studio, Editorial, Interactive, Commerce and Forms packages remain pinned to `1.0.0`. There are 19 editable sections composing the 17 reference families and the newsletter.

The supplied [Flux preview](https://19a08oqc5qmf99gy-24806554.shopifypreview.com/) was inspected for capability and layout coverage. The implementation does not import its source, assets, fonts or schemas. Copy, product illustrations and the coffee still life are original; the market, prices, testimonials and events are fictional.

## Family coverage

| Family | Registered composition | Editable content and behavior |
| --- | --- | --- |
| Opening banner with products | Editorial image banner + Commerce featured collection | Image, caption, heading, text and CTA; overlapping product row on desktop, stacked on phone |
| Collection list | Commerce collection list | Ordered category references and labels; keyboard/button horizontal browsing on phone |
| Rich text | Editorial rich text | Heading and ordered text blocks |
| Image and text | Editorial image with text | Media, caption, heading, text, CTA and layout |
| Collection tabs | Commerce collection tabs | Ordered category references and labels; actual sample product groups, arrow-key switching |
| Story slider | Interactive slick slider | Three ordered media/text/link slides, previous/next, keyboard movement, optional motion controls |
| Information cards | Editorial info cards | Four original cards; theme-owned native disclosure enhancement |
| Promotions | Editorial promotion cards | Ordered image/text/link cards; phone horizontal controls |
| Image hotspots | Interactive image hotspots | Image, position, label, text and link; click/keyboard disclosure and Escape |
| Testimonials | Interactive testimonials | Ordered quotes, names and roles; explicit fictional disclosure |
| Featured product | Commerce featured product | Product reference, heading and display settings; sample detail dialog and price, no purchasing |
| Two-image story | Editorial two images with text | Two media blocks and ordered editorial content |
| Articles | Editorial multicolumn | Authored image/title/summary/link cards; no native blog-provider claim |
| Events | Editorial multicolumn | Three ordered cards with editable date caption, title, time/venue text and action |
| Featured collection | Commerce featured collection | Category and product presentation; linked fictional product details |
| Benefits | Editorial multicolumn | Five editable values/captions and descriptions |
| Closing banner | Editorial image banner | Editable image, heading, text and CTA |

The shared shell contains a wordmark, announcement, named navigation menus, Search/Account/Bag actions and footer menus/note. The closing editorial callout and newsletter form compose the lower page with that footer. Search filters the fictional catalog and opens product details. Account/Bag explain that the local preset has no account or checkout service. Newsletter validates locally without storing or sending an address. Event dates and times are authored text, not typed calendar/timezone fields or a booking integration.

## Persistence and boundaries

`product/src/theme-preset-store.mjs` resolves preset IDs from a trusted map and writes only `product/.local/theme-presets/daybreak.json`. Reading an untouched preset does not create its file. Page and shared resources have independent optimistic revisions; stale writes receive HTTP 409. Exact resource shape, theme/document/scope identity, registered component eligibility and preset-owned references are checked before writes. Requests require the loopback origin and JSON content type; unknown actions, duplicate JSON keys, oversized input and symlink destinations are rejected.

The compare/write/rename operation is atomic in the single local Node process. It is not proof of a multi-process hosted database, authenticated tenant isolation, publication or crash recovery. Editor history and sidecar metadata use the distinct key `mte:resource-desk:daybreak-market:demo:v1`; Silt retains its existing key. Merchant values remain JSON, without executable code, filesystem paths or Tailwind class names.

Native Silt status was read before and after the work and remained identical, including draft and applied data. No native save/apply/restore action was called. Existing legacy draft sentinels also remained unchanged in isolated HTTP tests. Browser QA changed only Daybreak hero copy, wordmark, footer label, an event caption and block order. Those values were saved/reloaded successfully, then restored to the original preset through its own API. Final Daybreak revisions after restoration: shared 4, home 8. Its history retains the reversible QA revisions.

## Verification

`npm --prefix product run verify` passed **130 tests**, covering the existing product/native-contract suites plus seven new preset tests. New coverage includes independent factories, family/default validity, theme identity and reference rejection, independent page/shared saves, stale revision handling, fresh store reload, symlink rejection, escaped sample prices, native catalog output preservation and HTTP origin/action/size/strict-JSON boundaries. A focused variant test duplicates hero/events, checks independent IDs with unchanged semantic type, label and wrapper, then saves/reloads those copies. Silt native eligibility explicitly rejects these browser-only variants.

In-app browser checks passed:

- Hero, shared wordmark, footer menu label and event-date edits persisted after save/reload; ordered event blocks retained their saved order.
- Section insertion and duplication each produced 20 sections; undo returned to the original 19 without a new save.
- Tabs switched product groups by click and arrow key; slider Next showed the second authored slide; hotspots opened and closed with Escape.
- Information cards expanded; sample search filtered Sunrise and opened its detail dialog; required signup fields and consent were enforced, then local success confirmed nothing was sent or subscribed.
- Phone menu reported the correct `aria-expanded` state and closed with Escape. Promotion Next and collection End scrolled the intended tracks.
- Desktop preview followed browser resizing. At 1920, 2560 and 1100 browser widths, preview content widths were 1814, 2454 and 994 pixels, respectively. Tablet and Phone retained 768/390 CSS-pixel frames, with 753/375 content pixels after their scrollbars. Document scroll width equalled client width in each case; no section escaped the phone document. The browser size was restored.

Local evidence lives under `product/.local/daybreak-preset/`: `verify.log`, `browser-saved-status.json`, `restored-status.json`, `native-before.json`, `native-after.json`, `preservation.json`, `responsive.json`, `duplicate-variants.json`, `duplicate-saved-status.json`, and desktop, phone, tablet, event and footer screenshots. Runtime is Node 22.22.0 on macOS. Source changes remain uncommitted on root `main` after `e82efbe`; the documentation repository is independent.

## Remaining architecture and acceptance work

The intended product boundary is **generic editor → developer-owned theme/component contract → generic Magento connector/providers**. Daybreak is a consumer of that contract. React controls, draft/history and movement remain in the editor; theme visuals and interaction enhancement remain in its package; native commerce remains with Magento/providers.

This local proof still has explicit coupling: the application context and preset store register known theme imports; Daybreak reuses the earlier Silt shared-resource validator/menu renderer; its eligible components now come from declared package pins in the shared registry; frame selection still recognizes Silt shell hooks and known component markup. Sample catalog dialogs live in the application, and the current shared settings schema is fixed. A separately installable, theme-neutral manifest/SDK, generic shell-slot annotations, portable provider contracts, theme-defined shared settings and a verified Magento adapter remain future work. Adding a production third-party theme without touching editor application registration is not established by this preset.

The product build regenerated native source capability hashes and package runtime artifacts after extracting reusable interaction helpers. These are source/build outputs only: nothing was copied to a Magento installation or deployed. The existing React 19.2.8 and Alpine CSP 3.17.2 pins remain unchanged. The Tailwind v4 review workspace pins and styling boundary remain unchanged; Daybreak storefront CSS is isolated from editor styling. Asset provenance, hashes and local-use scope are recorded in `product/third-party/daybreak-assets-2026-09-10.md` and the asset manifest. Commercial release review remains open.

Independent read-only acceptance review passed the populated page, desktop/phone visuals, tabs, slider, hotspots, mobile menu, theme chooser and Silt preservation. It found P2: specialized presentation used original instance IDs and was lost on duplication. The writer replaced that identity dependency with registered semantic component variants. Browser duplication, save and reload preserved both hero/events labels and identical computed heading sizes/backgrounds on new IDs; the original 19-section draft was then restored. Focused independent recheck passed: the reviewer ran the semantic regression, regenerated all 19 variant IDs, confirmed labels/wrappers and native rejection, checked the fresh editor/library, and reconfirmed every Silt baseline digest. P2 is closed, with no further actionable finding in this bounded local preset review. Review evidence: `product/.local/flux-reference-review/review-2026-09-10.md`. Documentation verification passed 62 source pages, 63 HTML pages and 7,054 local links; the rendered receipt navigation and coverage table were inspected. No commit, push, publication, environment provisioning, Linear mutation or broad automation resumption belongs to this preset delivery.
