# Interactive field coverage · 2026-09-08

SOL-533 accounts for all **299** field entries in the accepted ten-stem census. This ledger is generated from `component-library/reference/interactive-coverage.json`; it never reads Flux source.

A mapped original field is an independently designed subset, not proof of exact reference values, markup, presets or supporting behavior. Material substitutions and exclusions below remain **unaccepted**; SOL-533 and the full catalog milestone stay open. See [implementation evidence and reversal](interactive-catalog-evidence-2026-09-08.md).

| State | Entries |
| --- | --- |
| metadata-only | 36 |
| mapped-original-subset | 233 |
| open-field-gap | 19 |
| mandatory-accessibility-behavior | 4 |
| open-provider-gap | 3 |
| open-scope-gap | 2 |
| local-substitution-provider-gap | 2 |

## Scope decisions

**IM-01 — implemented-local-substitution-review-pending.** Original accessible carousel, native range/details/dialog/tabs and local HTML video replace vendor-specific runtimes; no Flux source, schema, assets or libraries imported.

**IM-02 — material-exclusion-not-accepted.** Remote video URLs/player providers, Shopify-hosted media selection, mobile video switching and product-backed hotspots/testimonials remain open. Local video playback is a working scoped alternative, not proof of remote-provider parity.

**IM-03 — safety-accessibility-boundary-review-pending.** Automatic motion always has pause/start, stops on interaction/hidden document, and never starts with reduced motion. Always retain keyboard controls and focusable alternatives; hover-stop or mobile-arrow removal cannot disable those safeguards.

**IM-04 — scope-gap-not-accepted.** Sticky announcement placement belongs to SOL-535. Vendor preset/word/highlight animations, exact decoration styling, opacity/font numeric parity and advanced content-height variants remain partial/open. No catalog/family closure is claimed.

**IM-05 — scope-gap-not-accepted.** The census contains no countdown block in these ten stems. The issue asks to include related countdown/snippet behavior wherever present: that behavioral parity remains unproven and requires explicit cross-family review with SOL-536; no countdown is simulated.

## advanced-slider

Original destination: `mte-interactive/advanced-slider`. Populated template: **media**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `advanced-slider/settings/0:@metadata-1` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/1:auto_rotate` | `settings/autoRotate` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/2:slider_direction` | `settings/direction` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/3:slider_loop` | `settings/loop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/4:slider_interval` | `settings/interval` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/5:slider_height` | `settings/height` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/6:adapt_to_image` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/settings/7:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/8:hide_slider_desktop` | `settings/hideDesktop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/9:hide_slider_mobile` | `settings/hideMobile` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/10:@metadata-11` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/11:content_layout_mode` | `settings/contentLayout` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/12:content_height` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/settings/13:content_position` | `settings/contentPosition` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/14:content_anchor` | `settings/verticalAlignment` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/15:content_size` | `settings/contentWidth` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/16:content_align` | `settings/alignment` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/17:content_box` | `settings/textBox` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/18:content_opacity` | `settings/overlay` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/19:@metadata-20` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/20:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/21:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/22:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/23:caption_size` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/settings/24:caption_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/25:@metadata-26` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/26:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/27:color_scheme_1` | `settings/panelSurface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/28:@metadata-29` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/29:mobile_height` | `settings/mobileHeight` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/30:mobile_content_height` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/settings/31:mobile_content_size` | `settings/mobileContentWidth` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/32:mobile_heading_size` | `settings/mobileHeadingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/33:mobile_caption_size` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/settings/34:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/35:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/36:@metadata-37` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `advanced-slider/settings/37:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/38:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/settings/39:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/0:image` | `blocks/slide/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `advanced-slider/blocks/0/1:image_mobile` | `blocks/slide/settings/mobileImageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `advanced-slider/blocks/0/2:slider_heading` | `blocks/slide/settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/3:heading` | `blocks/slide/settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/4:heading_advanced` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/blocks/0/5:highlight_option` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/blocks/0/6:word_animation_color` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `advanced-slider/blocks/0/7:caption` | `blocks/slide/settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/8:button_label` | `blocks/slide/settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/9:link` | `blocks/slide/settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `advanced-slider/blocks/0/10:open_new_tab_1` | `blocks/slide/settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/11:button_style_secondary` | `blocks/slide/settings/linkStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `advanced-slider/blocks/0/12:apply_link_to_image` | `blocks/slide/settings/linkImage` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## comparison-slider

Original destination: `mte-interactive/comparison-slider`. Populated template: **media**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `comparison-slider/settings/0:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/1:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/2:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/3:title` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/4:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/5:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/6:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/7:image` | `settings/beforeAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `comparison-slider/settings/8:image_2` | `settings/afterAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `comparison-slider/settings/9:animate_slider` | `settings/autoSweep` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/10:height` | `settings/height` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/11:before_text` | `settings/beforeLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/12:after_text` | `settings/afterLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/13:disable_before_after` | `settings/showLabels` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/14:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/15:@metadata-16` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `comparison-slider/settings/16:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/17:@metadata-18` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `comparison-slider/settings/18:accessibility_info` | `settings/instructions` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/19:@metadata-20` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `comparison-slider/settings/20:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/21:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/22:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/23:@metadata-24` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `comparison-slider/settings/24:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/25:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `comparison-slider/settings/26:mobile_height` | `settings/mobileHeight` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## image-gallery

Original destination: `mte-interactive/image-gallery`. Populated template: **media**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `image-gallery/settings/0:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/1:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/2:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/3:title` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/4:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/5:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/6:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/7:scroll_direction` | `settings/direction` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/8:scroll_speed` | `settings/speed` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/9:scroll_height` | `settings/height` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/10:hover_stop` | — | mandatory-accessibility-behavior | Hover/focus/input stops automatic motion and keyboard/touch controls remain available. These safeguards are not merchant-disableable. |
| `image-gallery/settings/11:@metadata-12` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-gallery/settings/12:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/13:@metadata-14` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-gallery/settings/14:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/15:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/16:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/17:@metadata-18` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-gallery/settings/18:scroll_height_mobile` | `settings/mobileHeight` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/19:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/settings/20:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-gallery/blocks/0/0:image` | `blocks/image/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `image-gallery/blocks/0/1:image_link` | `blocks/image/settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |

## image-hotspots

Original destination: `mte-interactive/image-hotspots`. Populated template: **media**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `image-hotspots/settings/0:image` | `settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `image-hotspots/settings/1:image_size` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `image-hotspots/settings/2:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/3:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/4:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/5:heading` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/6:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/7:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/8:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/9:layout` | `settings/hotspotLayout` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/10:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/11:@metadata-12` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-hotspots/settings/12:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/13:tooltip_background_color` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `image-hotspots/settings/14:@metadata-15` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-hotspots/settings/15:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/16:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/17:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/18:@metadata-19` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `image-hotspots/settings/19:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/20:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/settings/21:layout_mobile` | `settings/mobileLayout` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/blocks/0/0:product` | — | open-provider-gap | No product/review provider is bound; authored information and explicit fictional quotes do not substitute for catalog/review data. Owner: SOL-534 / SOL-537 |
| `image-hotspots/blocks/0/1:content` | `blocks/hotspot/settings/body` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/blocks/0/2:top` | `blocks/hotspot/settings/y` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `image-hotspots/blocks/0/3:left` | `blocks/hotspot/settings/x` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## scrolling-text

Original destination: `mte-interactive/scrolling-text`. Populated template: **motion**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `scrolling-text/settings/0:layout_style` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `scrolling-text/settings/1:scroll_direction` | `settings/direction` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/2:enable_scroll_decoration` | `settings/decoration` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/3:scroll_decoration` | `settings/decoration` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/4:scroll_speed` | `settings/speed` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/5:scroll_height` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `scrolling-text/settings/6:scroll_text_size` | `settings/messageSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/7:padding_block` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `scrolling-text/settings/8:enable_stencil_text` | `settings/stencil` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/9:hover_stop` | — | mandatory-accessibility-behavior | Hover/focus/input stops automatic motion and keyboard/touch controls remain available. These safeguards are not merchant-disableable. |
| `scrolling-text/settings/10:keep_small_mobile` | `settings/mobileMessageSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/11:border` | `settings/border` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/12:enable_announcement_bar_desktop_sticky` | — | open-scope-gap | No sticky global announcement placement in these scoped CMS components. Owner: SOL-535 |
| `scrolling-text/settings/13:enable_announcement_bar_mobile_sticky` | — | open-scope-gap | No sticky global announcement placement in these scoped CMS components. Owner: SOL-535 |
| `scrolling-text/settings/14:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/15:@metadata-16` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `scrolling-text/settings/16:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/17:@metadata-18` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `scrolling-text/settings/18:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/settings/19:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `scrolling-text/blocks/0/0:text` | `blocks/message/settings/text` | mapped-original-subset | Bounded escaped plain text, not imported HTML or exact rich-text formatting. Formatting parity remains partial. |
| `scrolling-text/blocks/0/1:image` | `blocks/message/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `scrolling-text/blocks/0/2:image_link` | `blocks/message/settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |

## slick-slider

Original destination: `mte-interactive/slick-slider`. Populated template: **motion**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `slick-slider/settings/0:@metadata-1` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `slick-slider/settings/1:auto_rotate` | `settings/autoRotate` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/2:slider_interval` | `settings/interval` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/3:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/4:image_opacity` | `settings/overlay` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/5:opacity_mobile` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `slick-slider/settings/6:hide_slider_desktop` | `settings/hideDesktop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/7:hide_slider_mobile` | `settings/hideMobile` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/8:@metadata-9` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `slick-slider/settings/9:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/10:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/11:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/12:caption_size` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `slick-slider/settings/13:caption_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/14:link_size` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `slick-slider/settings/15:@metadata-16` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `slick-slider/settings/16:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/17:@metadata-18` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `slick-slider/settings/18:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/19:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/20:@metadata-21` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `slick-slider/settings/21:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/22:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/settings/23:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/blocks/0/0:image` | `blocks/slide/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `slick-slider/blocks/0/1:image_mobile` | `blocks/slide/settings/mobileImageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `slick-slider/blocks/0/2:heading` | `blocks/slide/settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/blocks/0/3:caption` | `blocks/slide/settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/blocks/0/4:button_label` | `blocks/slide/settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `slick-slider/blocks/0/5:link` | `blocks/slide/settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `slick-slider/blocks/0/6:show_link_button` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `slick-slider/blocks/0/7:open_new_tab_1` | `blocks/slide/settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## tabs

Original destination: `mte-interactive/tabs`. Populated template: **media**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `tabs/settings/0:tabs_style` | `settings/tabsStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/1:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/2:@metadata-3` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `tabs/settings/3:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/4:color_scheme_1` | `settings/panelSurface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/5:@metadata-6` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `tabs/settings/6:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/7:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/8:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/9:@metadata-10` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `tabs/settings/10:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/settings/11:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/0:heading` | `blocks/tab/settings/label` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/1:image` | `blocks/tab/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `tabs/blocks/0/2:tab_image_width` | `blocks/tab/settings/imageWidth` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/3:hide_image` | `blocks/tab/settings/hideImage` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/4:row_content` | `blocks/tab/settings/body` | mapped-original-subset | Bounded escaped plain text, not imported HTML or exact rich-text formatting. Formatting parity remains partial. |
| `tabs/blocks/0/5:button_label` | `blocks/tab/settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/6:button_link` | `blocks/tab/settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `tabs/blocks/0/7:open_new_tab_1` | `blocks/tab/settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `tabs/blocks/0/8:button_style_secondary` | `blocks/tab/settings/linkStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## testimonials

Original destination: `mte-interactive/testimonials`. Populated template: **motion**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `testimonials/settings/0:title` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/1:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/2:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/3:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/4:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/5:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/6:button_label` | `settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/7:button_link` | `settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `testimonials/settings/8:open_new_tab_1` | `settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/9:testimonials_style` | `settings/display` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/10:remove_testimonial_border` | `settings/border` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/11:columns_desktop` | `settings/columns` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/12:enable_desktop_slider` | `settings/display` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/13:@metadata-14` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `testimonials/settings/14:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/15:color_scheme_1` | `settings/panelSurface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/16:rating_stars_color` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `testimonials/settings/17:@metadata-18` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `testimonials/settings/18:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/19:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/20:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/21:@metadata-22` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `testimonials/settings/22:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/23:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/settings/24:swipe_on_mobile` | — | mandatory-accessibility-behavior | Hover/focus/input stops automatic motion and keyboard/touch controls remain available. These safeguards are not merchant-disableable. |
| `testimonials/settings/25:disable_arrow_mobile` | — | mandatory-accessibility-behavior | Hover/focus/input stops automatic motion and keyboard/touch controls remain available. These safeguards are not merchant-disableable. |
| `testimonials/blocks/0/0:rating` | `blocks/quote/settings/rating` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/blocks/0/1:rating_stars` | `blocks/quote/settings/rating` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/blocks/0/2:text` | `blocks/quote/settings/quote` | mapped-original-subset | Bounded escaped plain text, not imported HTML or exact rich-text formatting. Formatting parity remains partial. |
| `testimonials/blocks/0/3:title` | `blocks/quote/settings/name` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/blocks/0/4:title_one` | `blocks/quote/settings/role` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/blocks/0/5:image` | `blocks/quote/settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `testimonials/blocks/0/6:hide_image` | `blocks/quote/settings/hideImage` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `testimonials/blocks/0/7:product` | — | open-provider-gap | No product/review provider is bound; authored information and explicit fictional quotes do not substitute for catalog/review data. Owner: SOL-534 / SOL-537 |

## video-background

Original destination: `mte-interactive/video-background`. Populated template: **motion**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `video-background/settings/0:video_url` | `settings/videoAssetId` | local-substitution-provider-gap | Working registered local WebM with native controls/text alternative; external URL players and Shopify media APIs are not implemented. Owner: SOL-533 / provider review |
| `video-background/settings/1:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/2:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/3:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/4:heading` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/5:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/6:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/7:text` | `settings/body` | mapped-original-subset | Bounded escaped plain text, not imported HTML or exact rich-text formatting. Formatting parity remains partial. |
| `video-background/settings/8:button_label` | `settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/9:link` | `settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `video-background/settings/10:open_new_tab_1` | `settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/11:@metadata-12` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video-background/settings/12:video_style` | `settings/textBox` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/13:full_width_background` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/14:background_height` | `settings/height` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/15:box_align` | `settings/contentPosition` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/16:box_vertical_align` | `settings/verticalAlignment` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/17:text_align` | `settings/alignment` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/18:ignore_box` | `settings/textBox` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/19:content_opacity` | `settings/overlay` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/20:blur` | — | open-field-gap | No equivalent field with native behavior is implemented for this setting. Owner: SOL-533 |
| `video-background/settings/21:opacity` | `settings/overlay` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/22:@metadata-23` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video-background/settings/23:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/24:color_scheme_1` | `settings/panelSurface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/25:@metadata-26` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video-background/settings/26:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/27:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/28:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/29:@metadata-30` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video-background/settings/30:video_url_mobile` | — | open-provider-gap | Separate mobile video resolution is not implemented. Owner: SOL-533 / provider review |
| `video-background/settings/31:background_height_mobile` | `settings/mobileHeight` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/32:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video-background/settings/33:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |

## video

Original destination: `mte-interactive/video`. Populated template: **motion**.

Exact vendor presets/snippet behavior and countdown-related requirements remain open; census mapping alone is not parity proof.

| Census field | Original field | State | Evidence boundary / dependency |
| --- | --- | --- | --- |
| `video/settings/0:caption` | `settings/caption` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/1:text_style` | `settings/captionStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/2:text_size` | `settings/textSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/3:heading` | `settings/heading` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/4:heading_size` | `settings/headingSize` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/5:heading_style` | `settings/headingStyle` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/6:heading_tag` | `settings/headingLevel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/7:text` | `settings/body` | mapped-original-subset | Bounded escaped plain text, not imported HTML or exact rich-text formatting. Formatting parity remains partial. |
| `video/settings/8:button_label_1` | `settings/linkLabel` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/9:button_link_1` | `settings/pageId` | mapped-original-subset | Registered local Magento CMS destination and mandatory link label; arbitrary URLs/providers are excluded. |
| `video/settings/10:open_new_tab_1` | `settings/newTab` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/11:cover_image` | `settings/imageAssetId` | mapped-original-subset | Magento-owned opaque image identity with independently authored alternative text; source/vendor assets are not copied. |
| `video/settings/12:video_url` | `settings/videoAssetId` | local-substitution-provider-gap | Working registered local WebM with native controls/text alternative; external URL players and Shopify media APIs are not implemented. Owner: SOL-533 / provider review |
| `video/settings/13:description` | `settings/description` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/14:video_layout` | `settings/videoLayout` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/15:full_width` | `settings/width` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/16:@metadata-17` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video/settings/17:color_scheme` | `settings/surface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/18:color_scheme_1` | `settings/panelSurface` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/19:@metadata-20` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video/settings/20:padding_top` | `settings/paddingTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/21:padding_bottom` | `settings/paddingBottom` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/22:ignore_spacing` | `settings/spacingMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/23:@metadata-24` | — | metadata-only | Editor grouping/help metadata has no merchant runtime value. |
| `video/settings/24:margin_spacing` | `settings/marginMode` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
| `video/settings/25:margin_top` | `settings/marginTop` | mapped-original-subset | Original bounded declarative field; exact vendor values, presets and numeric ranges are not claimed. |
