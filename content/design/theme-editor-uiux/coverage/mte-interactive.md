# Interactive control coverage

Observed 2026-09-10. Extracted from `component-library/packages/interactive/package.mjs` (1.0.0); source SHA-256 `e79401fd9949585890ad10a1109544fccb9b8f747eae631af2ab64c25fcf2b92`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Story slider

Type: `mte-interactive/advanced-slider`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Story slides with visible pause and next controls.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `autoRotate` / Start automatic rotation | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `interval` / Seconds per slide | Behavior / Numeric input + bounded slider | Integer 5–30 | `7` |
| `loop` / Loop slides | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `direction` / Slide direction | Content / Adaptive segmented choice / select | Choices: horizontal, vertical | `"horizontal"` |
| `height` / Desktop media height (16px units) | Layout / Numeric input + bounded slider | Integer 20–80 | `28` |
| `mobileHeight` / Mobile media height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `20` |
| `hideDesktop` / Hide on desktop | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideMobile` / Hide on mobile | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `contentLayout` / Slide content layout | Layout / Adaptive segmented choice / select | Choices: split, overlay | `"split"` |
| `contentPosition` / Content horizontal position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `verticalAlignment` / Content vertical position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"center"` |
| `contentWidth` / Content width (%) | Layout / Numeric input + bounded slider | Integer 30–100 | `50` |
| `mobileContentWidth` / Mobile content width (%) | Layout / Numeric input + bounded slider | Integer 50–100 | `100` |
| `textBox` / Show content panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `overlay` / Image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `25` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Story slider: Slide block

Block key: `slide`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `heading` / Slide heading | Content / Text input | Text 0–160 characters | `"An everyday ritual."` |
| `caption` / Slide caption | Content / Text input | Text 0–120 characters | `"THE STUDIO"` |
| `body` / Slide text | Content / Plain-text multiline input | Text 0–3000 characters | `"Slow down and notice the familiar."` |
| `linkImage` / Link image to the CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Simple slider

Type: `mte-interactive/slick-slider`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Simple slide sequence with pagination.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `autoRotate` / Start automatic rotation | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `interval` / Seconds per slide | Behavior / Numeric input + bounded slider | Integer 5–30 | `7` |
| `loop` / Loop slides | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `direction` / Slide direction | Content / Adaptive segmented choice / select | Choices: horizontal, vertical | `"horizontal"` |
| `height` / Desktop media height (16px units) | Layout / Numeric input + bounded slider | Integer 20–80 | `28` |
| `mobileHeight` / Mobile media height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `20` |
| `hideDesktop` / Hide on desktop | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideMobile` / Hide on mobile | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `contentLayout` / Slide content layout | Layout / Adaptive segmented choice / select | Choices: split, overlay | `"overlay"` |
| `contentPosition` / Content horizontal position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `verticalAlignment` / Content vertical position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"center"` |
| `contentWidth` / Content width (%) | Layout / Numeric input + bounded slider | Integer 30–100 | `50` |
| `mobileContentWidth` / Mobile content width (%) | Layout / Numeric input + bounded slider | Integer 50–100 | `100` |
| `textBox` / Show content panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `overlay` / Image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `25` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Simple slider: Slide block

Block key: `slide`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `heading` / Slide heading | Content / Text input | Text 0–160 characters | `"An everyday ritual."` |
| `caption` / Slide caption | Content / Text input | Text 0–120 characters | `"THE STUDIO"` |
| `body` / Slide text | Content / Plain-text multiline input | Text 0–3000 characters | `"Slow down and notice the familiar."` |
| `linkImage` / Link image to the CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Image comparison

Type: `mte-interactive/comparison-slider`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Before/after image split with a real slider handle.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `beforeAssetId` / Before Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `afterAssetId` / After Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `beforeAlt` / Before image description | Content / Text input | Text 0–300 characters | `""` |
| `afterAlt` / After image description | Content / Text input | Text 0–300 characters | `""` |
| `beforeLabel` / Before label | Form and consent / Text input | Text 1–80 characters | `"Before"` |
| `afterLabel` / After label | Form and consent / Text input | Text 1–80 characters | `"After"` |
| `position` / Initial before share (%) | Layout / Numeric input + bounded slider | Integer 0–100 | `50` |
| `showLabels` / Show before and after labels | Form and consent / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `instructions` / Comparison instructions | Content / Text input | Text 1–300 characters | `"Drag the handle or use the arrow keys to compare both images."` |
| `height` / Desktop comparison height (16px units) | Layout / Numeric input + bounded slider | Integer 20–60 | `28` |
| `mobileHeight` / Mobile comparison height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `20` |
| `autoSweep` / Start automatic comparison sweep | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Image gallery

Type: `mte-interactive/image-gallery`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Grid opening a single-image dialog.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `columns` / Desktop visible images | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile visible images | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `height` / Desktop image height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `22` |
| `mobileHeight` / Mobile image height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `18` |
| `autoScroll` / Start automatic gallery scrolling | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `direction` / Scroll direction | Content / Adaptive segmented choice / select | Choices: forward, backward | `"forward"` |
| `speed` / Scroll pixels per second | Content / Numeric input + bounded slider | Integer 5–60 | `20` |
| `lightbox` / Enable enlarged image view | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Image gallery: Gallery image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Image hotspots

Type: `mte-interactive/image-hotspots`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Image with two keyboard reachable authored hotspots.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `height` / Desktop image height (16px units) | Layout / Numeric input + bounded slider | Integer 20–60 | `32` |
| `mobileHeight` / Mobile image height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `24` |
| `hotspotLayout` / Desktop hotspot layout | Layout / Adaptive segmented choice / select | Choices: overlay, list | `"overlay"` |
| `mobileLayout` / Mobile hotspot layout | Layout / Adaptive segmented choice / select | Choices: list, overlay | `"list"` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Image hotspots: Hotspot block

Block key: `hotspot`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `label` / Hotspot label | Content / Text input | Text 1–80 characters | `"A thoughtful detail"` |
| `body` / Hotspot information | Content / Plain-text multiline input | Text 0–2000 characters | `"Describe this part of the image."` |
| `x` / Horizontal position (%) | Content / Numeric input + bounded slider | Integer 0–100 | `50` |
| `y` / Vertical position (%) | Content / Numeric input + bounded slider | Integer 0–100 | `50` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Scrolling messages

Type: `mte-interactive/scrolling-text`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Message strip with pause control.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `autoScroll` / Start scrolling | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `direction` / Scroll direction | Content / Adaptive segmented choice / select | Choices: forward, backward | `"forward"` |
| `speed` / Scroll pixels per second | Content / Numeric input + bounded slider | Integer 5–60 | `20` |
| `messageSize` / Desktop message size (px) | Content / Numeric input + bounded slider | Integer 16–96 | `40` |
| `mobileMessageSize` / Mobile message size (px) | Content / Numeric input + bounded slider | Integer 16–48 | `24` |
| `border` / Show border | Appearance / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `decoration` / Message separator | Content / Adaptive segmented choice / select | Choices: none, dot, star | `"dot"` |
| `stencil` / Outline text | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Scrolling messages: Message block

Block key: `message`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Message | Content / Text input | Text 1–500 characters | `"Make room for the everyday."` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Tabbed stories

Type: `mte-interactive/tabs`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Two authored tabs, one active panel.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `tabsStyle` / Tab appearance | Content / Adaptive segmented choice / select | Choices: underline, boxed | `"underline"` |
| `initialTab` / Initial tab (1-based) | Behavior / Numeric input + bounded slider | Integer 1–24 | `1` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Tabbed stories: Tab block

Block key: `tab`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `label` / Tab label | Content / Text input | Text 1–100 characters | `"Our story"` |
| `heading` / Tab heading | Content / Text input | Text 0–160 characters | `"Considered forms."` |
| `body` / Tab text | Content / Plain-text multiline input | Text 0–4000 characters | `"Useful shapes for the things you do every day."` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `50` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Authored testimonials

Type: `mte-interactive/testimonials`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Authored quote, attribution and pagination.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `autoRotate` / Start automatic rotation | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `interval` / Seconds per slide | Behavior / Numeric input + bounded slider | Integer 5–30 | `7` |
| `loop` / Loop slides | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `direction` / Slide direction | Content / Adaptive segmented choice / select | Choices: horizontal, vertical | `"horizontal"` |
| `height` / Desktop media height (16px units) | Layout / Numeric input + bounded slider | Integer 20–80 | `28` |
| `mobileHeight` / Mobile media height (16px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `20` |
| `hideDesktop` / Hide on desktop | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideMobile` / Hide on mobile | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `display` / Testimonial arrangement | Content / Adaptive segmented choice / select | Choices: grid, slider | `"slider"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `border` / Show card border | Appearance / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showRatings` / Show authored ratings | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `disclosure` / Source disclosure | Content / Text input | Text 1–300 characters | `"Original fictional sample quotations; these are not customer reviews."` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Authored testimonials: Testimonial block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `quote` / Quotation | Content / Plain-text multiline input | Text 1–3000 characters | `"A little care makes the everyday feel special."` |
| `name` / Attribution | Content / Text input | Text 1–120 characters | `"Fictional studio visitor"` |
| `role` / Attribution detail | Content / Text input | Text 0–120 characters | `"Demonstration copy"` |
| `rating` / Authored rating (0 hides it) | Content / Numeric input + bounded slider | Integer 0–5 | `5` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Local video

Type: `mte-interactive/video`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Local video poster, play and transcript/caption state.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `videoAssetId` / Magento video | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `description` / Video description | Content / Text input | Text 1–300 characters | `"An original studio motion study."` |
| `transcript` / Text alternative / transcript | Content / Plain-text multiline input | Text 1–4000 characters | `"A silent abstract motion study with moving shapes."` |
| `videoLayout` / Video layout | Layout / Adaptive segmented choice / select | Choices: stack, split | `"stack"` |
| `loop` / Loop video | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Video backdrop

Type: `mte-interactive/video-background`. Current placement: **template**.

Insertable local interaction subset; local registered media. Remote players and product-backed content remain gaps.

**Preview brief:** Poster and copy over a local video backdrop.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"A closer look."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–120 characters | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `""` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Content panel | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `radius` / Media corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `videoAssetId` / Magento video | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `description` / Video description | Content / Text input | Text 1–300 characters | `"An original studio motion study."` |
| `transcript` / Text alternative / transcript | Content / Plain-text multiline input | Text 1–4000 characters | `"A silent abstract motion study with moving shapes."` |
| `height` / Desktop backdrop height (16px units) | Layout / Numeric input + bounded slider | Integer 20–60 | `32` |
| `mobileHeight` / Mobile backdrop height (16px units) | Layout / Numeric input + bounded slider | Integer 16–48 | `28` |
| `autoPlay` / Start muted background playback | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `loop` / Loop background video | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `contentPosition` / Content horizontal position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `verticalAlignment` / Content vertical position | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"center"` |
| `textBox` / Show content panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `overlay` / Video shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `35` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.
