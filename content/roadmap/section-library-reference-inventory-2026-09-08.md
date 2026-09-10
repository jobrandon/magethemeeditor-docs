# Reference capability inventory · 8 September 2026

This is a factual census of the supplied local Flux reference, self-declared Flux 2.7.1 by Mana Themes. The reference files remain untouched. No Liquid, CSS, JavaScript, schemas, option/default values, fonts, icons, translations or demo assets are imported into the original library.

Classification means strict JSON parsing plus bounded structural checks (identity, default bounds and preset block references). A preset-bearing section is a candidate for Add section, subject to recorded template/group restrictions; this is not a complete Shopify schema validator or a Shopify runtime test. Fixed sections have no preset. Fragments have no schema. Malformed schemas remain malformed even when a trailing-comma-only shadow parse permits an inventory.

The reproducible machine census is `component-library/reference/capability-inventory.json`; run `python3 component-library/scripts/inventory-reference.py` from the workspace. It records every section setting, nested block setting, global setting and nested color-scheme definition with an original Magento mapping and status. Identifiers/types are lookup facts, not adopted schemas. See [implementation and evidence](section-library-evidence-2026-09-08.md).

## Coverage summary

76 Liquid section files; 7 fragment-no-schema, 3 malformed-json-schema, 22 valid-fixed-no-preset, 44 valid-preset-bearing; 2 section-group JSON files.

Only five section concepts have partial original equivalents. Partial means the first bounded library implements essential functionality, not every reference setting or option. All native integration remains outstanding for these five. Additional effects, timers, sliders, commerce, external providers and global theme settings remain outside this delivery.

| Reference file | Classification | Original Magento equivalent | Coverage / dependency |
| --- | --- | --- | --- |
| `sections/advanced-slider.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/anchor-link.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/announcement-bar.liquid` | valid-preset-bearing | Existing theme-owned registered region | outside-home-cms-scope; Theme adapter and explicit region registration |
| `sections/apps.liquid` | valid-preset-bearing | Allowlisted native widget/provider reference | unsupported-executable-content; Named trusted Magento integration; arbitrary Liquid/app execution excluded |
| `sections/banner-two-columns.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/cart-drawer.liquid` | fragment-no-schema | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/cart-icon-bubble.liquid` | fragment-no-schema | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/cart-live-region-text.liquid` | fragment-no-schema | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/cart-notification-button.liquid` | fragment-no-schema | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/cart-notification-product.liquid` | fragment-no-schema | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/collapsible-content.liquid` | valid-preset-bearing | mte-studio/faq | partial-original-equivalent; Portable library; native adapter outstanding |
| `sections/collection-list.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/collection-tabs.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/comparison-slider.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/contact-form.liquid` | valid-preset-bearing | Magento-owned consent-aware form or notification adapter | adapter-outstanding; Magento form controller, form key, validation, consent and rate limits; no hosted imitation |
| `sections/custom-liquid.liquid` | valid-preset-bearing | Allowlisted native widget/provider reference | unsupported-executable-content; Named trusted Magento integration; arbitrary Liquid/app execution excluded |
| `sections/email-signup-banner.liquid` | valid-preset-bearing | Magento-owned consent-aware form or notification adapter | adapter-outstanding; Magento form controller, form key, validation, consent and rate limits; no hosted imitation |
| `sections/ep-reviews-carousel.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/events-calendar.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/featured-blog.liquid` | valid-preset-bearing | Magento CMS or separately registered blog provider | provider-outstanding; Installed provider capability; Magento core is not assumed to own a blog |
| `sections/featured-collection.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/featured-collections.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/featured-product.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/footer.liquid` | malformed-json-schema | Existing theme-owned registered region | outside-home-cms-scope; Theme adapter and explicit region registration |
| `sections/header.liquid` | valid-fixed-no-preset | Existing theme-owned registered region | outside-home-cms-scope; Theme adapter and explicit region registration |
| `sections/heading-with-images.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/image-banner-with-collections.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/image-banner-with-featured-collection.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/image-banner.liquid` | valid-preset-bearing | mte-studio/banner | partial-original-equivalent; Portable library; native adapter outstanding |
| `sections/image-gallery.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/image-hotspots.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/image-with-text.liquid` | valid-preset-bearing | mte-studio/image-text | partial-original-equivalent; Portable library; native adapter outstanding |
| `sections/info-cards.liquid` | malformed-json-schema | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/location-map.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/main-404.liquid` | valid-fixed-no-preset | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/main-account.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-activate-account.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-addresses.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-article.liquid` | valid-fixed-no-preset | Magento CMS or separately registered blog provider | provider-outstanding; Installed provider capability; Magento core is not assumed to own a blog |
| `sections/main-blog.liquid` | valid-fixed-no-preset | Magento CMS or separately registered blog provider | provider-outstanding; Installed provider capability; Magento core is not assumed to own a blog |
| `sections/main-cart-footer.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-cart-items.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-collection-banner.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/main-collection-product-grid.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/main-list-collections.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/main-login.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-order.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-page.liquid` | valid-fixed-no-preset | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/main-password-footer.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-password-header.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-product.liquid` | malformed-json-schema | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/main-register.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-reset-password.liquid` | valid-fixed-no-preset | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/main-search.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/multicolumn.liquid` | valid-preset-bearing | mte-studio/cards | partial-original-equivalent; Portable library; native adapter outstanding |
| `sections/newsletter.liquid` | valid-preset-bearing | Magento-owned consent-aware form or notification adapter | adapter-outstanding; Magento form controller, form key, validation, consent and rate limits; no hosted imitation |
| `sections/page.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/pickup-availability.liquid` | fragment-no-schema | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/popup.liquid` | valid-preset-bearing | Magento-owned consent-aware form or notification adapter | adapter-outstanding; Magento form controller, form key, validation, consent and rate limits; no hosted imitation |
| `sections/predictive-search.liquid` | fragment-no-schema | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/promotion-cards.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/quick-info-bar.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/quick-order-list.liquid` | valid-preset-bearing | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/recently-viewed-products.liquid` | valid-preset-bearing | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/related-products.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/rich-text.liquid` | valid-preset-bearing | mte-studio/rich-text | partial-original-equivalent; Portable library; native adapter outstanding |
| `sections/scrolling-text.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/separator.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/slick-slider.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/sticky-add-to-cart.liquid` | valid-preset-bearing | Magento native commerce/account service | native-owned-out-of-scope; Magento customer/session/quote/order services; preserve existing theme |
| `sections/subcollections.liquid` | valid-fixed-no-preset | Magento catalog/category/search reference renderer | adapter-outstanding; Store-scoped catalog/category/search services; current price/stock/customer context from Magento |
| `sections/tabs.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/testimonials.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/two-images-text.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/video-background.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |
| `sections/video.liquid` | valid-preset-bearing | Original CMS composition or specialized native provider | coverage-outstanding; Original implementation and adapter proof; maps/video/reviews require separate provider and rights review |

## Section and block settings

Every setting below lists its factual reference identifier/type and the proposed original destination. “Outstanding” is not implemented support. Metadata entries are editor labels/help, not merchant values. Values, defaults, options and reference display copy are deliberately omitted.

### advanced-slider

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `auto_rotate` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `slider_direction` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `slider_loop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `slider_interval` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `slider_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `adapt_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_slider_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_slider_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `content_layout_mode` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `content_position` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `content_anchor` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `content_align` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `content_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `caption_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-26` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-29` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mobile_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_heading_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_caption_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-37` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `slide` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_mobile` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `slider_heading` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_advanced` | `inline_richtext` | Original escaped text/emphasis; no raw HTML | outstanding |
| `highlight_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `word_animation_color` | `color` | Original scoped style token | outstanding |
| `caption` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `apply_link_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### anchor-link

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `anchor` | `text` | Bounded escaped text on an original component/provider | outstanding |

### announcement-bar

valid-preset-bearing.

Reference availability metadata: `{"enabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `announcement_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_only` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `make_bar_thiner` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_announcement_bar_desktop_sticky` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_announcement_bar_mobile_sticky` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_social` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_country_selector` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `vertical_position` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `announcement_text_color` | `color` | Original scoped style token | outstanding |
| `show_countdown` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `countdown-text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-text-position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-date` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-date-time-style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown_finished_message` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-24` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

Block `announcement` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `slider-text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `slider_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

### apps

valid-preset-bearing.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `include_margins` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `@app` → Named trusted Magento integration; arbitrary Liquid/app execution excluded; outstanding.

No block settings; native/app content still requires a registered provider.

### banner-two-columns

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `banner_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `animate_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `slide` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `subheading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_text_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### cart-drawer

fragment-no-schema.

No section settings.

### cart-icon-bubble

fragment-no-schema.

No section settings.

### cart-live-region-text

fragment-no-schema.

No section settings.

### cart-notification-button

fragment-no-schema.

No section settings.

### cart-notification-product

fragment-no-schema.

No section settings.

### collapsible-content

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `layout_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | mte-studio/faq: settings.eyebrow | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | mte-studio/faq: settings.heading | partial-equivalent |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `open_first_collapsible_row` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `open_all_collapsible_row` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `background_color` | `color` | Original scoped style token | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `collapsible_row` → Ordered mte-studio/faq content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | mte-studio/faq: settings.heading | partial-equivalent |
| `icon` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `row_content` | `richtext` | mte-studio/faq: question.settings.answer | partial-equivalent |
| `page` | `page` | Magento CMS page reference/resolver | outstanding |

### collection-list

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}, "max_blocks": 32}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `collection_list_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_title_background_color` | `color` | Original scoped style token | outstanding |
| `ep_title_background_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `title_under` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `featured_collection` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `card_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |

### collection-tabs

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `description_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `collection_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `products_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `product_card_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `ep_show_product_type` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_show_subscription_price` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_quick_view_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_quick_view_trigger` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_quick_view_sticky_footer` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_subscription_accent` | `color` | Original scoped style token | outstanding |
| `ep_media_background` | `color` | Original scoped style token | outstanding |
| `ep_card_border_color` | `color` | Original scoped style token | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_rating` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_buy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_buy_button_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `always_use_plus_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_variant_swatches` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `variant_swatches_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `variant_swatches_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `quick_add_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `use_first_image_in_product_card` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-40` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-43` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-47` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `collection` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `tab_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |

### comparison-slider

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `animate_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `before_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `after_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `disable_before_after` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `accessibility_info` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-24` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### contact-form

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `contact_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_phone_field` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `all_fields_required` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-27` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_height_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### custom-liquid

valid-preset-bearing.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### email-signup-banner

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `newsletter_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_terms` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `terms_label` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `caption` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `heading` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `paragraph` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `email_form` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

No block settings; native/app content still requires a registered provider.

### ep-reviews-carousel

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `store_id` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `language` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `review_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `desktop_columns` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `maximum_reviews` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_desktop_carousel` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mobile_columns` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_mobile_swipe` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_overall_stars` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_popups` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `popup_close_behavior` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `auto_scroll` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `auto_scroll_speed` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `show_pause_button` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `star_color` | `color` | Original scoped style token | outstanding |
| `disabled_star_color` | `color` | Original scoped style token | outstanding |
| `base_font_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `review_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-28` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### events-calendar

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `banner_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `animate_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_animation` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `event` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `event_date` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `event_month` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `hide_date` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `event_time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `event_price` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `event_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `event_description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `event_location` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_text_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### featured-blog

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `ep_home_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `blog` | `blog` | Registered Magento CMS/blog provider | outstanding |
| `blog_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `post_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `show_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_date` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_author` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_excerpt` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_view_all` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-25` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### featured-collection

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `show_description` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `description_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `collection_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `products_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_view_all` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `view_all_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_buy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `always_use_plus_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_variant_swatches` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `variant_swatches_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `variant_swatches_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `quick_add_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `use_first_image_in_product_card` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-31` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-34` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-38` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `slide` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `subheading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_text_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### featured-collections

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}, "max_blocks": 6}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `featured_collection_1` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `featured_collection_2` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_collections_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `heading` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `caption` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |

Block `countdown-timer` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `countdown-text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-text-position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-date` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-date-time-style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown_finished_message` | `text` | Bounded escaped text on an original component/provider | outstanding |

Block `button` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### featured-product

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `ep_home_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `product` | `product` | Store-scoped Magento product reference/resolver | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `product_gallery_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `media_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `media_fit` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_zoom` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `autoplay_video` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_video_looping` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `@app` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

No block settings; native/app content still requires a registered provider.

Block `spacer` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `text` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_text_background` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

Block `image` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `vendor` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `enable_vendor_link` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `title` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `price` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `price_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `inventory` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `inventory_threshold` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `show_inventory_quantity` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `sku` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `quantity_selector` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `variant_picker` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `picker_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `keep_swatches` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `swatch_shape` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hide_unavailable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `countdown-timer` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `countdown-text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-text-position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-date` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-date-time-style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown_finished_message` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown_timer_tag` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `buy_buttons` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `show_dynamic_checkout` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_gift_card_recipient` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `description` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `custom_liquid` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |

Block `delivery_estimator` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `delivery_estimator_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `earliest_delivery` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `latest_delivery` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `complementary` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `block_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `product_list_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `waiting_list` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `waiting_list_title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_tagline` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_notice` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_button` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `dynamic_card_icons` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `card_metafield_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `card_metafield_key` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `card_metafield_image_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_image_size_custom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `card_metafield_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_icon_title_font_weight` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_border` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_enable_border_radius` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `icons_tooltip` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### footer

malformed-json-schema.

Strict parse error: Illegal trailing comma before end of object; line 272, column 65. trailing-comma-only shadow parse; source still malformed.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_follow_on_shop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_country_selector` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_language_selector` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `payment_enable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_powered_by_link` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_policy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_terms` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `terms_label` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `back_to_top_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `back_to_top_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `back_to_top_right` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `back_to_top_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `centered_content` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-24` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `footer_background_color` | `color` | Original scoped style token | outstanding |
| `footer_text_color` | `color` | Original scoped style token | outstanding |
| `apply_scheme_footer_bottom` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `footer_border` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-30` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-33` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-36` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `make_columns_even` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `@app` → Theme adapter and explicit region registration; outstanding.

No block settings; native/app content still requires a registered provider.

Block `link_list` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `menu` | `link_list` | Magento-owned navigation provider | outstanding |

Block `brand_information` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `brand_headline` | `inline_richtext` | Original escaped text/emphasis; no raw HTML | outstanding |
| `brand_description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `brand_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `brand_image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `newsletter_enable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_social` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `social_icons_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `subtext` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |

Block `image` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_headline` | `inline_richtext` | Original escaped text/emphasis; no raw HTML | outstanding |
| `image_description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### header

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `menu` | `link_list` | Magento-owned navigation provider | outstanding |
| `menu_type_desktop` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `all_items_mega` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_links` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `desktop_header_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_search_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_header_full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `sticky_header_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `sticky_logo_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `sticky_vertical_padding` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_fixed_header_type` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_fixed_header_type_collection` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_fixed_header_type_all` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `transparent_menu` | `link_list` | Magento-owned navigation provider | outstanding |
| `enable_fixed_header_transparent` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `transparent_text_color` | `color` | Original scoped style token | outstanding |
| `transparent_logo` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `fixed_header_type_margin` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `fixed_header_type_margin_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `image_1` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `button_label_one` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_one` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_additional_links` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_mobile_menu_links` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-33` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_item_highlight` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `item_highlight_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `item_highlight_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `adjust_item_highlight_position` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-38` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_country_selector` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-40` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_language_selector` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-42` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_customer_account_modal` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `customer_account_menu` | `link_list` | Magento-owned navigation provider | outstanding |
| `@metadata-45` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `header_icons_decoration` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-47` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `item_highlight_background_color` | `color` | Original scoped style token | outstanding |
| `item_highlight_color` | `color` | Original scoped style token | outstanding |
| `@metadata-51` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-54` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_country_selector_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_language_selector_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `featured_collection_1` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `featured_collection_2` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `mobile_desktop_header_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `mega_promotion` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `mega_promotion_item` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_promotion_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_promotion_caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_promotion_title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_promotion_link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_promotion_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

Block `mega_image_menu` → Theme adapter and explicit region registration; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `mega_image_menu_item` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_columns` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_1` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_2` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_3` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_3` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_4` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_4` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-28` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_5` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_5` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_5` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_5` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_5` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-34` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_6` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_6` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_6` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_6` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_6` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-40` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_7` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_7` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_7` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_7` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_7` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-46` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mega_image_menu_image_8` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `mega_image_menu_caption_8` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_title_8` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_label_8` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `mega_image_menu_link_8` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

### heading-with-images

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["footer", "header"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `text` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_size_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `image` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `mobile_image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### image-banner-with-collections

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width_banner` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `adapt_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `inline_richtext` | Original escaped text/emphasis; no raw HTML | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `highlight_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `word_animation_color` | `color` | Original scoped style token | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `richtext_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `button_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_label_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_2` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-29` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `desktop_margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `mobile_margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-39` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-43` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_mobile` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_overlay_opacity_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_height_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-50` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

Block `featured_collection` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `show_content_manually` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

### image-banner-with-featured-collection

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width_banner` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `adapt_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_collection` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `collection_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `products_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `desktop_margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_buy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `always_use_plus_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_variant_swatches` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `variant_swatches_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `variant_swatches_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `quick_add_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `use_first_image_in_product_card` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-31` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-34` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-38` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_mobile` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_overlay_opacity_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_height_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-45` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `heading` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `inline_richtext` | Original escaped text/emphasis; no raw HTML | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `highlight_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `word_animation_color` | `color` | Original scoped style token | outstanding |

Block `caption` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `buttons` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_label_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_2` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### image-banner

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | mte-studio/banner: settings.imageAssetId + alt/decorative | partial-equivalent |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_border_radius` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_text_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_mobile` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_text_below` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `heading` → Ordered mte-studio/banner content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `inline_richtext` | mte-studio/banner: settings.heading | partial-equivalent |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `highlight_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `word_animation_color` | `color` | Original scoped style token | outstanding |

Block `caption` → Ordered mte-studio/banner content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | mte-studio/banner: settings.eyebrow | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Ordered mte-studio/banner content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | mte-studio/banner: structured text block or settings.body | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `countdown-timer` → Ordered mte-studio/banner content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `countdown-text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-text-position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-date` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-date-time-style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `large-countdown` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `countdown_finished_message` | `text` | Bounded escaped text on an original component/provider | outstanding |

Block `buttons` → Ordered mte-studio/banner content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `apply_link_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_label_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_2` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### image-gallery

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `scroll_direction` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `scroll_speed` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `scroll_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hover_stop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `scroll_height_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `text` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

### image-hotspots

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `tooltip_background_color` | `color` | Original scoped style token | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `layout_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `Tooltip` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `product` | `product` | Store-scoped Magento product reference/resolver | outstanding |
| `content` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `left` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### image-with-text

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `ep_home_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image` | `image_picker` | mte-studio/image-text: settings.imageAssetId + alt/decorative | partial-equivalent |
| `video_url` | `video` | Magento-owned media provider; video renderer outstanding | outstanding |
| `caption` | `text` | mte-studio/image-text: settings.eyebrow | partial-equivalent |
| `desktop_image_width` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `heading` → Ordered mte-studio/image-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | mte-studio/image-text: settings.heading | partial-equivalent |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `caption` → Ordered mte-studio/image-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | mte-studio/image-text: settings.eyebrow | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Ordered mte-studio/image-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | mte-studio/image-text: structured text block or settings.body | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `image` → Ordered mte-studio/image-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | mte-studio/image-text: settings.imageAssetId + alt/decorative | partial-equivalent |
| `position_image_relative` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `mobile_disable_image_animation` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `mobile_disable_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `button` → Ordered mte-studio/image-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label` | `text` | mte-studio/image-text: settings.linkLabel | partial-equivalent |
| `button_link` | `url` | mte-studio/image-text: settings.pageId via Magento CMS resolver | partial-equivalent |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### info-cards

malformed-json-schema.

Strict parse error: Illegal trailing comma before end of array; line 129, column 6. trailing-comma-only shadow parse; source still malformed.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `cards_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `infocard` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `product` | `product` | Store-scoped Magento product reference/resolver | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `infocards_background_color` | `color` | Original scoped style token | outstanding |
| `infocards_color` | `color` | Original scoped style token | outstanding |

### location-map

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_contact_form` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_phone_field` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `api_key` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `zoom_level` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `address` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `marker_content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-25` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-404

valid-fixed-no-preset.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-account

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-activate-account

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-addresses

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-article

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `@app` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

No block settings; native/app content still requires a registered provider.

Block `featured_image` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `title` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `blog_show_date` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `blog_show_author` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `content` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

No block settings; native/app content still requires a registered provider.

Block `tags` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

No block settings; native/app content still requires a registered provider.

Block `buttons` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

No block settings; native/app content still requires a registered provider.

Block `share` → Installed provider capability; Magento core is not assumed to own a blog; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `share_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `@metadata-3` | `paragraph` | Editor help metadata; no merchant value | metadata-only |

### main-blog

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `blog_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `make_first_post_featured` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `tags` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `tag_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `tag_default` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `show_page_title` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_date` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_author` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-13` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-cart-footer

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_left` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_right` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `subtotal` → Magento customer/session/quote/order services; preserve existing theme; outstanding.

No block settings; native/app content still requires a registered provider.

Block `buttons` → Magento customer/session/quote/order services; preserve existing theme; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `show_dynamic_checkout` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `custom_liquid` → Magento customer/session/quote/order services; preserve existing theme; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |

Block `text-with-image` → Magento customer/session/quote/order services; preserve existing theme; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `centered_content` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `@app` → Magento customer/session/quote/order services; preserve existing theme; outstanding.

No block settings; native/app content still requires a registered provider.

### main-cart-items

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_left` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_right` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### main-collection-banner

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `show_collection_description` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_breadcrumbs` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `collection_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_for_all` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `fallback_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-collection-product-grid

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `products_per_page` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `pagination` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `load_button` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `product_card_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `ep_show_product_type` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_show_subscription_price` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_quick_view_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_quick_view_trigger` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_quick_view_sticky_footer` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_subscription_accent` | `color` | Original scoped style token | outstanding |
| `ep_media_background` | `color` | Original scoped style token | outstanding |
| `ep_card_border_color` | `color` | Original scoped style token | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `contain_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_rating` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_buy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_buy_button_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_per_unit_price` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `always_use_plus_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_variant_swatches` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `variant_swatches_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `variant_swatches_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `hide_unavailable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_add_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `use_first_image_in_product_card` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `list_color_variants_in_collection` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `list_size_variants_in_collection` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-35` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_filtering` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_switcher` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `filter_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `open_filter` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_sorting` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `product_count` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-42` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-45` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-48` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `promo_row` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `promo_row` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `banner_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `subheading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `show_text_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_overlay_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### main-list-collections

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `sort` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-login

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-order

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-page

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-password-footer

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### main-password-header

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### main-product

malformed-json-schema.

Strict parse error: Illegal trailing comma before end of object; line 3337, column 82. trailing-comma-only shadow parse; source still malformed.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `layout_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_subscription_accent` | `color` | Original scoped style token | outstanding |
| `ep_buy_box_color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `ep_nutrition_header_background` | `color` | Original scoped style token | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `ep_recharge_font_role` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_recharge_title_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ep_recharge_price_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ep_recharge_badge_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_sticky_info` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `sticky_content` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `product_gallery_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `gallery_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `media_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `media_fit` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `thumbnail_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_zoom` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `hide_variants` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `autoplay_video` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_video_looping` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-25` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `quantity_selector` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-27` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `in_stock_background_color` | `color` | Original scoped style token | outstanding |
| `in_stock_color` | `color` | Original scoped style token | outstanding |
| `@metadata-31` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `under_gallery` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `mobile_thumbnails` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `mobile_gallery_arrow_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-35` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `@app` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

No block settings; native/app content still requires a registered provider.

Block `payment_enable` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `spacer` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `text` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_block_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_text_background` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `pin_to_top` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `image` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `vendor` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_vendor_link` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `pin_to_top` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `title` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `pin_to_top` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `price` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `price_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `ep_compare_price_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ep_compare_price_weight` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_compare_price_gap` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `badge_discount` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `waiting_list` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `waiting_list_title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_tagline` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_notice` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `waiting_list_button` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `product-meta` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_product_inventory` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `inventory_threshold` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `show_inventory_quantity` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_product_sku` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `sku` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `delivery_estimator` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `delivery_estimator_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `earliest_delivery` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `latest_delivery` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `inventory` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `inventory_threshold` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `show_inventory_quantity` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `countdown-timer` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-text-position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown-date` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-time` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown-date-time-style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `countdown_finished_message` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `countdown_timer_tag` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `buy_buttons` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_dynamic_checkout` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `force_unbranded_button` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_gift_card_recipient` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_native_purchase_options` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `purchase_options_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `one_time_purchase_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `savings_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `default_purchase_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `stack_buttons_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `stacked_buttons_width` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `picker_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swatch_shape` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hide_unavailable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_quantity_input` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_variant_picker` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `description` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_view_description_mode` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `quick_view_description` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `show_quick_view_details` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_view_pack_size` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `quick_view_product_type` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `quick_view_machine` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `quick_view_caffeine` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `quick_view_ingredients` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `pin_to_top` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `share` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `share_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-3` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `@metadata-4` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `custom_liquid` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `collapsible_tab` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `icon` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `no_padding` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `page` | `page` | Magento CMS page reference/resolver | outstanding |
| `custom_liquid` | `liquid` | Unsupported executable content; named native widget/provider only | outstanding |
| `open_first_collapsible_row` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_spacer` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-15` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `ingredient_details` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `left_column_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `right_column_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `alternative_formatting` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `open_first_collapsible_row` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `popup` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `popup_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `popup_content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `popup_page` | `page` | Magento CMS page reference/resolver | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `dynamic_card_icons` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `card_metafield_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `card_metafield_key` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `card_metafield_image_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_image_size_custom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `card_metafield_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_icon_title_font_weight` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_border` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_enable_border_radius` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `icons_tooltip` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `complementary` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `block_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `product_list_limit` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `columns` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `icon-with-text` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `icon_with_text_columns` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `icon_with_text_columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `icon_with_text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `icon_1` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_1` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `icon_2` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `icon_3` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_3` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading_3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `icon_4` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_4` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading_4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `icon_with_text_padding` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `tabs` → Store-scoped catalog/category/search services; current price/stock/customer context from Magento; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `column` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `row_content_1` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `row_content_2` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `row_content_3` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `centered_tabs` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `remove_border_tabs` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `hide_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### main-register

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-reset-password

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### main-search

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_filtering` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `filter_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_sorting` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `article_show_date` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `article_show_author` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_article_posts` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `show_page_posts` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### multicolumn

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `ep_home_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `multicolumn_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_card_background` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `caption` | `text` | mte-studio/cards: settings.eyebrow | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title` | `text` | mte-studio/cards: settings.heading | partial-equivalent |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_width` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `columns_desktop` | `range` | mte-studio/cards: settings.columns | partial-equivalent |
| `column_alignment` | `select` | mte-studio/cards: settings.alignment | partial-equivalent |
| `button_label` | `text` | mte-studio/cards: settings.linkLabel | partial-equivalent |
| `button_link` | `url` | mte-studio/cards: settings.pageId via Magento CMS resolver | partial-equivalent |
| `open_new_tab_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-25` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `column` → Ordered mte-studio/cards content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | mte-studio/cards: settings.imageAssetId + alt/decorative | partial-equivalent |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `video_url` | `video` | Magento-owned media provider; video renderer outstanding | outstanding |
| `disable_autoplay` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `title` | `text` | mte-studio/cards: settings.heading | partial-equivalent |
| `text` | `richtext` | mte-studio/cards: structured text block or settings.body | partial-equivalent |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### newsletter

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_terms` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `terms_label` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-4` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `heading` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `paragraph` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |

Block `email_form` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

No block settings; native/app content still requires a registered provider.

Block `@app` → Magento form controller, form key, validation, consent and rate limits; no hosted imitation; outstanding.

No block settings; native/app content still requires a registered provider.

### page

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `page` | `page` | Magento CMS page reference/resolver | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### pickup-availability

fragment-no-schema.

No section settings.

### popup

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `enable_popup` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `popup_test` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `fadein` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `popup_count` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `trigger_link` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `popup_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `image_alt` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `popup_title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `header_font_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `popup_message` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `message_font_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `submit_button_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `success_message` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `show_social` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_terms` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `terms_label` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `terms_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `subs_form` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `apply_link_to_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-28` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |

### predictive-search

fragment-no-schema.

No section settings.

### promotion-cards

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `promotion_cards_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-11` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `column` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### quick-info-bar

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image-1` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading-1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `caption-1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image-2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading-2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `caption-2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image-3` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading-3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `caption-3` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-13` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image-4` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading-4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `caption-4` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `add_border` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `full_width_background` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-24` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-28` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### quick-order-list

valid-preset-bearing.

Reference availability metadata: `{"enabled_on": {"templates": ["product"]}, "limit": 1}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `show_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_image_hover_effect` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_sku` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### recently-viewed-products

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `products_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_quick_buy` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_per_unit_price` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `always_use_plus_icon` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `quick_add_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `use_first_image_in_product_card` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-25` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-31` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `disable_quick_add` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### related-products

valid-fixed-no-preset.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `products_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `show_secondary_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_rating` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### rich-text

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `ep_home_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `desktop_content_position` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `content_alignment` | `select` | mte-studio/rich-text: settings.alignment | partial-equivalent |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `rich_text_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `mobile_content_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `image` → Ordered mte-studio/rich-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | mte-studio/rich-text: settings.imageAssetId + alt/decorative | partial-equivalent |

Block `heading` → Ordered mte-studio/rich-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `inline_richtext` | mte-studio/rich-text: settings.heading | partial-equivalent |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `highlight_option` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `word_animation_color` | `color` | Original scoped style token | outstanding |

Block `caption` → Ordered mte-studio/rich-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | mte-studio/rich-text: settings.eyebrow | partial-equivalent |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Ordered mte-studio/rich-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | mte-studio/rich-text: structured text block or settings.body | partial-equivalent |

Block `button` → Ordered mte-studio/rich-text content block (partial); partial-equivalent.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label` | `text` | mte-studio/rich-text: settings.linkLabel | partial-equivalent |
| `button_link` | `url` | mte-studio/rich-text: settings.pageId via Magento CMS resolver | partial-equivalent |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_label_2` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_2` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary_2` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### scrolling-text

valid-preset-bearing.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `layout_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `scroll_direction` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_scroll_decoration` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `scroll_decoration` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `scroll_speed` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `scroll_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `scroll_text_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_block` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_stencil_text` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hover_stop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `keep_small_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `border` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_announcement_bar_desktop_sticky` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `enable_announcement_bar_mobile_sticky` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `text` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |

### separator

valid-preset-bearing.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `separator_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `spacer_color` | `color` | Original scoped style token | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_top_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `margin_bottom_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### slick-slider

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `auto_rotate` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `slider_interval` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `opacity_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_slider_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_slider_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `heading_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `caption_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `link_size` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-16` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `slide` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_mobile` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `caption` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `show_link_button` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### sticky-add-to-cart

valid-preset-bearing.

Reference availability metadata: `{"enabled_on": {"templates": ["product"]}, "limit": 1}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `enable_section` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `layout_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_sheet_heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `hide_desktop` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `hide_img` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_quantity_input` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `hide_select_variant` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `btn_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### subcollections

valid-fixed-no-preset.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `subcollection_list_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `title_under` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `image_ratio` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `collections_to_show` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-21` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `columns_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### tabs

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `tabs_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

Block `tab` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `tab_image_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `row_content` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `button_style_secondary` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### testimonials

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `testimonials_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `remove_testimonial_border` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `columns_desktop` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `enable_desktop_slider` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `rating_stars_color` | `color` | Original scoped style token | outstanding |
| `@metadata-18` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `swipe_on_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_arrow_mobile` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

Block `column` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `rating` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `rating_stars` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `title` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `title_one` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `hide_image` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `product` | `product` | Store-scoped Magento product reference/resolver | outstanding |

### two-images-text

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}, "max_blocks": 6}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `image_2` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-6` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-10` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `layout_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `heading` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `heading` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `caption` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

Block `text` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |

Block `image` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |

Block `image_1` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `image_1` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |

Block `button` → Original implementation and adapter proof; maps/video/reviews require separate provider and rights review; outstanding.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### video-background

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `video_url` | `video` | Magento-owned media provider; video renderer outstanding | outstanding |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-12` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `video_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width_background` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `background_height` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `box_align` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `box_vertical_align` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_align` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ignore_box` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `content_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `blur` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-23` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-26` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-30` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `video_url_mobile` | `video` | Magento-owned media provider; video renderer outstanding | outstanding |
| `background_height_mobile` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### video

valid-preset-bearing.

Reference availability metadata: `{"disabled_on": {"groups": ["header", "footer"]}}`.

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `caption` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `heading_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_tag` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_label_1` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `button_link_1` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `open_new_tab_1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `cover_image` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `video_url` | `video_url` | Registered media provider; embed origin/privacy review outstanding | outstanding |
| `description` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `video_layout` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `full_width` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-17` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `color_scheme` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `color_scheme_1` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-20` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `padding_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `padding_bottom` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ignore_spacing` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-24` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `margin_spacing` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `margin_top` | `range` | Bounded numeric setting on an original component/provider | outstanding |

## Global theme settings and groups

Global reference settings are inventoried for remaining coverage. Existing Magento theme globals stay owned by that theme; the first library styles only its own section. A matching field name does not grant a global override.

### t:settings_schema.logo.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `logo` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `logo_h1` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `logo_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `logo_width_mobile` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `favicon` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |

### t:settings_schema.breadcrumbs.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `show_breadcrumb_nav` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_breadcrumbs_on_pages` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `breadcrumbs_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `advanced_breadcrumbs` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.animations.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `deactivate_animation` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `page_scroll_indicator` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `scroll_indicator_color` | `color` | Original scoped style token | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `page_loader_enable` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `loader_background_color` | `color` | Original scoped style token | outstanding |
| `loader_text_color` | `color` | Original scoped style token | outstanding |
| `page_loader_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `page_loader_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

### t:settings_schema.colors.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `color_schemes` | `color_scheme_group` | Original scoped surface token definitions; no reference palette imported | outstanding |
| `color_schemes.background_color` | `color` | Original scoped style token | outstanding |
| `color_schemes.background_gradient` | `color_background` | Unmapped reference field; requires explicit original design | outstanding |
| `color_schemes.text_color` | `color` | Original scoped style token | outstanding |
| `color_schemes.button_primary_background_color` | `color` | Original scoped style token | outstanding |
| `color_schemes.button_primary_text_color` | `color` | Original scoped style token | outstanding |
| `color_schemes.button_secondary_color` | `color` | Original scoped style token | outstanding |
| `color_schemes.color_link` | `color` | Original scoped style token | outstanding |

### t:settings_schema.colors_add.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `@metadata-2` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `accent_background_color_1` | `color` | Original scoped style token | outstanding |
| `accent_color_1` | `color` | Original scoped style token | outstanding |
| `accent_color_2` | `color` | Original scoped style token | outstanding |
| `accent_text_color_2` | `color` | Original scoped style token | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `border_color_1` | `color` | Original scoped style token | outstanding |
| `@metadata-9` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `button_quick_add_background_color` | `color` | Original scoped style token | outstanding |
| `button_quick_add_text_color` | `color` | Original scoped style token | outstanding |
| `button_quick_add_background_color_hover` | `color` | Original scoped style token | outstanding |
| `button_quick_add_text_color_hover` | `color` | Original scoped style token | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `countdown_background_top` | `color` | Original scoped style token | outstanding |
| `countdown_text_top` | `color` | Original scoped style token | outstanding |
| `countdown_background_bottom` | `color` | Original scoped style token | outstanding |
| `countdown_text_bottom` | `color` | Original scoped style token | outstanding |
| `opacity_color` | `color` | Original scoped style token | outstanding |

### t:settings_schema.typography.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `type_header_font` | `font_picker` | Reviewed font token; system fonts used by first collection | outstanding |
| `type_header_weight` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `heading_scale` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-5` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `type_body_font` | `font_picker` | Reviewed font token; system fonts used by first collection | outstanding |
| `body_scale` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `navigation_font` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `text_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `navigation_scale` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `subnavigation_scale` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### t:settings_schema.layout.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `page_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `spacing_sections` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `@metadata-4` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `spacing_grid_horizontal` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `spacing_grid_vertical` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### t:settings_schema.buttons.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `buttons_border_thickness` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `buttons_radius` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `button_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `button_shadow_opacity` | `color` | Original scoped style token | outstanding |
| `show_button_arrow` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.global_design.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `global_border_radius` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-3` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `global_shadow_opacity` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `global_shadow_horizontal_offset` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `global_shadow_vertical_offset` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `global_shadow_blur` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `@metadata-8` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `exclude_drawer` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `exclude_popup` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `exclude_inputs` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.cards.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `card_text_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `card_metafield_key` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `card_icons_size` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `enable_tooltip` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.quick_view.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `quick_view_product_gallery_width` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `quick_view_height` | `range` | Bounded numeric setting on an original component/provider | outstanding |

### t:settings_schema.blog_cards.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `blog_card_text_alignment` | `select` | Allowlisted token/choice on an original component/provider | outstanding |

### t:settings_schema.badges.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `badge_discount` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_badge_discount` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-4` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `ep_discount_badge_background` | `color` | Original scoped style token | outstanding |
| `ep_discount_badge_text` | `color` | Original scoped style token | outstanding |
| `@metadata-7` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `@metadata-8` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `custom_badge_text` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `custom_badge_tag` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `custom_badge_color` | `color` | Original scoped style token | outstanding |
| `custom_badge_background` | `color` | Original scoped style token | outstanding |

### t:settings_schema.social-media.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `open_in_new_tab` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `social_facebook_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_instagram_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_youtube_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_tiktok_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_twitter_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_snapchat_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_pinterest_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_vimeo_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_tumblr_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_whatsapp_link` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `social_linkedin_link` | `text` | Bounded escaped text on an original component/provider | outstanding |

### t:settings_schema.search_input.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `predictive_search_enabled` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `predictive_search_show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `predictive_search_show_price` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.currency_format.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `@metadata-2` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `currency_code_enabled` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### t:settings_schema.cart.name

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `cart_type` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `cart_drawer_style` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_cart_promo_background` | `color` | Original scoped style token | outstanding |
| `ep_cart_progress_track` | `color` | Original scoped style token | outstanding |
| `ep_cart_progress_fill` | `color` | Original scoped style token | outstanding |
| `cart_icon` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `cart_icon_custom` | `image_picker` | Magento-managed media reference + accessible alternative text | outstanding |
| `show_vendor` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `show_cart_note` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `cart_discount` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `cart_note_open` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `custom_color_scheme` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `color_scheme_cart` | `color_scheme` | Original scoped surface tokens; reference scheme not imported | outstanding |
| `@metadata-14` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_free_shipping_message` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `free_shipping_message` | `textarea` | Bounded escaped multiline text on an original component/provider | outstanding |
| `free_shipping_amount` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `free_shipping_success` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `@metadata-19` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_promo_message` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `promo_message` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-22` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_cross_sell` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-24` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `cross_sell_collection` | `collection` | Store-scoped Magento category reference/resolver | outstanding |
| `cross_sell_label` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `disable_quick_view` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `@metadata-28` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_terms` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `terms_label` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `@metadata-31` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `enable_empty_cart_message` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `empty_cart_message` | `richtext` | Original structured text blocks; no raw HTML | outstanding |
| `button_link` | `url` | Named Magento route/CMS reference; arbitrary external URL input not supported | outstanding |
| `@metadata-35` | `header` | Editor organization metadata; no merchant value | metadata-only |
| `disable_cart_button` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `disable_checkout_button` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

### Mixpanel analytics

| Reference identifier | Type | Original destination | Status |
| --- | --- | --- | --- |
| `@metadata-1` | `paragraph` | Editor help metadata; no merchant value | metadata-only |
| `ep_mixpanel_enabled` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_mixpanel_project_token` | `text` | Bounded escaped text on an original component/provider | outstanding |
| `ep_mixpanel_api_region` | `select` | Allowlisted token/choice on an original component/provider | outstanding |
| `ep_mixpanel_autocapture` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |
| `ep_mixpanel_replay_percent` | `range` | Bounded numeric setting on an original component/provider | outstanding |
| `ep_mixpanel_customer_profiles` | `checkbox` | Typed Boolean setting on an original component/provider | outstanding |

- `sections/footer-group.json`: section-group-not-addable-section; references footer, popup.
- `sections/header-group.json`: section-group-not-addable-section; references announcement-bar, header.
