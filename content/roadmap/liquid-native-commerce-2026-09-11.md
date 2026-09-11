# Liquid native commerce evidence — 11 September 2026

Status: **bounded local commerce checkpoint accepted by PM after independent review**.
The active goal remains complete Liquid implementation. This checkpoint does not close full
reference-theme/editor parity, PHTML comparison, broader extension compatibility or release readiness.
See the [SDK guide](../architecture/liquid-theme-sdk.md) and [execution plan](execution-plan.md).

## Scope and identities

The existing INOX installation remains on `fix/INOXUS-creative-assets-fpc`, commit
`046d6e87866e7f6c5172e9c63f90097ac8b08295`, Magento 2.4.6-p13 and local PHP 8.3.28.
No new environment, setup upgrade, global theme assignment, checkout-policy change, commit,
push or production deployment ran. Existing editor drafts and earlier Silt/Daybreak work remain separate.

The original Atelier 1.1.0 package remains unchanged. The separate original **Atelier Commerce 1.0.2**
package in `theme-sdk/examples/commerce-theme/` owns home/product Liquid templates and a native
product form. Its digest is `fb014b5f8ebe5fab2c76609adf5fdb9cbf16f3b788a429f7619fb6c5519a4b84`.
Store 1's isolated `mte-liquid` assignment selects it; other routes retain their original renderers.
The first editor adapter still uses its clean Atelier installation and fictional catalog.

The staged module contains **241 files**, recorded in
`theme-sdk/.local/native-validation/staged-files.json`, SHA256
`227df60ab706ea71fbbea67a350c1d33bab68c5c55762a85699f67622d4543c3`.
Native runtime digest is `4906d600854ffae72156916ae378c4eb0d396568312b8d567754439f08998fa1`.
The SDK uses Node 24.21.0/npm 11.19.0 and reviewed keepsuit/liquid 0.12.0; no new dependency was adopted.

## Verification

| Layer | Observed result |
| --- | --- |
| SDK source | Required strict types, lint, formatting, PHP syntax, build and **34 tests** pass: 23 PHP and 11 Node |
| Native contract probes | Six pass: hidden-child exclusion, native prices/options, permitted response/result passthrough and denied-policy callback suppression |
| Final route isolation | Seven HTTP checks pass: home/product 200, hidden child/missing page/unassigned store 404, original product/Silt home 200 without Liquid renderer |
| Configurable product | Black option 4 is $28; Gold option 7 is $34; native attribute 93, set 9, website/store 1 |
| Native cart | Gold quantity 2 persists at $68; Black quantity 1 adds $28; native cart contains two lines, three units, subtotal/grand total $96 |
| Rejected requests | Invalid form key returns 302; invalid option and excessive stock return native 200 failure responses. None has an acknowledgement. Before/after quote item IDs, selected children, quantities, prices and totals match exactly |
| Analytics | After explicit consent, the local collector receives one real confirmed `cart:item-added` and one `cart:updated`. No production transport or customer data is sent |
| Guest checkout | Original policy remains enforced: native checkout returns to cart with “Guest checkout is disabled.” |
| Authenticated handoff | One synthetic customer signs in through native login; the same quote reaches `/default/checkout/#shipping`, loading masks finish, first-name/address fields are visible and all three units/$96 remain. No address, order or payment is submitted |
| Responsive UI | Product page at 390px has no horizontal overflow; desktop/native cart and shipping screenshots inspected |
| Cleanup | Logout completed; exact five test quotes and synthetic customer deleted. Fresh counts show zero matching quotes/items/customer and zero orders. Temporary credentials/session files removed |

The package's 1.0.2 change from tested 1.0.1 is manifest formatting/version only; template/module
bytes are unchanged. Final negative-preservation requests and collection-to-product browser navigation exercise 1.0.2; Gold remains $34, analytics defaults denied and no JavaScript error occurs. Evidence lives in the
ignored `theme-sdk/.local/native-validation/` directory: `native-contracts.json`,
`commerce-browser.json`, `commerce-followup.json`, `negative-preservation.json`,
`checkout-browser.json`, `auth-checkout.json`, `final-read-check.json`, `cleanup-plan.json` and `cleanup-complete.json`.
Screenshots live in `theme-sdk/output/playwright/`.

PM's independent receipt is
`product/.local/source-refactor-review/liquid-native-independent/commerce-acceptance.json`.
PM reproduced six native probes, seven HTTP isolation cases and fresh collection-to-product/Gold
price/denied-analytics browser checks without JavaScript errors. It independently verified all 241
staged files, extension hashes, native identity, five-quote/customer cleanup, three retained products,
17 prior drafts and clean main Atelier revision 1. Its 239-file SDK snapshot matched at that review;
subsequent standalone menu source changes are a separate checkpoint and are not in native staging.

PM reviewed the writer's cart, rejected-request, consent-event and authenticated shipping evidence
and code without repeating those transactions. Acceptance reaches the visible empty shipping address
form, with no shipping method, address, payment or order acceptance. The native review hold is released;
this does not authorize unrelated native work or establish broader extension compatibility.

The first native display attempt used a listing API that applies category visibility filtering,
which hid configurable children. Exact product reads now use the native repository/render collector,
with explicit current-website, enabled-status and individual-visibility checks. The catalog listing
retains its native listing path. Scoped native stock/price and product-category indexes were refreshed
only for the three owned product IDs.

The first commerce script attempted registration after top-level asynchronous loading, which the
synchronous registration contract rejected. The readable theme entry now registers immediately;
asynchronous helper loading happens within `mount` and honors cancellation and cleanup.

## Named installed extension correction

**SalesOne_CustomerGroupCatalog 1.0.0**, from its existing local Composer manifest, is proprietary.
Its local source is not redistributed in MageThemeEditor. The exact affected file is
`app/code/SalesOne/CustomerGroupCatalog/Plugin/Cart/CartAddControllerBlockPlugin.php`.
Its original SHA256 was `6ca162753c366e75bd8876abeaf7ebdf66d571c746cc545844416cfe7d086163`;
corrected SHA256 is `295b90d6efea48e7830869e3171547d366f53c3a32497af688bcd436da11ddb6`.

The plugin declared only `ResultInterface`, but Magento's native AJAX cart controller returns
`ResponseInterface`. Native persistence succeeded before the plugin raised a return-type error.
The local correction adds the response interface to its import, return union and DocBlock. The
access-policy branch is byte-for-byte unchanged. An allowed response and redirect result both pass;
a synthetic denied policy never invokes the native action. No customer group or policy setting changed.

Failed HTTP 500 requests are explicitly separate from later successful acknowledgements. The browser
reported uncertainty and emitted no success. It did not automatically retry. This correction is
limited to the controller return contract: price hiding, account/menu behavior and the module's wider
frontend restrictions still need an explicit Liquid adapter and acceptance. It does not establish
compatibility with arbitrary Magento extensions.

## Owned data and reversal

| Scope | Recorded identity and handling |
| --- | --- |
| Product fixtures retained | Parent 9738 `mte-liquid-configurable-cup`; simple children 9736 `mte-liquid-variant-black`, 9737 `mte-liquid-variant-gold`; existing color 93/options 4 and 7/set 9 reused, no new attribute or option |
| Stock | Native legacy stock item rows: children quantity 30/in stock/manage stock; parent in stock without managed quantity. Native MSI tables are absent; no MSI service was assumed |
| Failed-response quotes | 61431 and 61432 each held Gold2/$68; 61433 held Black1/$28. All had HTTP 500 after persistence and no success event |
| Successful probe quotes | 61434 held Black1/$28. Browser quote 61435 held Gold2 plus Black1/$96 and became owned by synthetic customer 20142 during native login; no new merged quote was created |
| Synthetic identity | Newly created customer 20142, website/store 1, existing group 1, original synthetic name and non-deliverable address. Created through repository/password hash, without the account welcome-email API |
| Deleted test data | Quotes 61431–61435 were individually checked and deleted through native repositories; customer 20142 was deleted after logout. Zero orders were verified. This was an exact ID list, not a range deletion |
| Credentials | Ignored 0600 credential and browser-session files removed after cleanup |

Cleanup initially removed the five quotes, then the customer repository's CLI area guard refused
deleting the synthetic customer. A scoped resume verified all quotes absent and the exact customer
identity, enabled Magento's operational secure-area registry only around that deletion, and restored
it immediately. Final database checks confirmed completion. No real customer was reused or reset.

To revert the commerce demo, first restore only store 1's `var/mte-liquid/assignment.json` value to
`atelier`, preserving other assignments. The pre-commerce assignment/runtime/staging manifests are
under `theme-sdk/.local/native-validation/pre-commerce/`. Keep wanted packages and merchant settings;
never overwrite a newer assignment or entire configuration blindly.

After verifying each retained product ID/SKU and absence of new quote/order references, delete only
parent 9738 and then children 9736/9737 through the native product repository. Their stock, website,
option relationships and index rows belong to those products. Existing attribute 93, options 4/7,
set 9, Silt products 9734/9735 and all unrelated content must remain.

The extension backup is ignored local evidence at
`theme-sdk/.local/native-validation/customer-group-catalog/CartAddControllerBlockPlugin.before.php`.
Revert only the import/DocBlock/return union after matching the current corrected hash; if the file
has later edits, apply the inverse patch without replacing them. Full SDK/module installation reversal
is documented in the [SDK guide](../architecture/liquid-theme-sdk.md#native-magento-checkpoint-and-reversal).

## Separate editor acceptance and remaining work

PM independently accepted the first local HTTP-v1 editor adapter: 160 required tests, 18 HTTP cases,
29 source paths, 141 identical generated artifacts and 239 SDK snapshot matches. Main Liquid/Silt/
Daybreak canvases load, with 17 original drafts preserved. Complete-state CAS save, conflicts,
stale-preview protection, whole-document frames and lifecycle disposal have bounded browser proof.
This is separate from the native commerce checkpoint above, which still needs PM review.

The basic Liquid editor has ordering arrows. Reviewed shell/polish, drag/drop, menus, richer schema
controls, multipage browser proof and full Silt/Daybreak migration remain open. So do a broader
extension/custom-provider example, same-design PHTML comparison, cache/performance/outage,
store-wide analytics/external SDK policy, migration/uninstall tooling, independent author acceptance
and release support/dependency inventory. No broad Linear issue or active goal is marked complete.
