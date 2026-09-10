# Editorial control coverage

Observed 2026-09-10. Extracted from `component-library/packages/editorial/package.mjs` (1.0.0); source SHA-256 `fa7dcd8019f79bafc2cf2b9c98c3b6b4af21c18ecc2a4625b815a81babe249b9`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Section anchor

Type: `mte-editorial/anchor-link`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Named in-page destination and visible navigation link.

**Uniqueness:** `anchorName`. Revalidate when duplicating.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `anchorName` / Anchor name | Content / Text input | Text 0–48 characters; pattern ^[a-z][a-z0-9-]{0,47}$ | `"studio-notes"` |
| `linkLabel` / Jump link label | Source and links / Text input | Text 1–80 characters | `"Continue to studio notes"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Separator

Type: `mte-editorial/separator`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Section divider with adjustable spacing.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `separatorStyle` / Separator style | Content / Adaptive segmented choice / select | Choices: line, dots, space | `"line"` |
| `lineColor` / Separator color | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^#[a-fA-F0-9]{6}$ | `"#6b7c6b"` |
| `marginBottom` / Bottom margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Two-column banners

Type: `mte-editorial/banner-two-columns`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Two independently authored panels.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `2` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `cardStyle` / Card arrangement | Content / Adaptive segmented choice / select | Choices: bordered, plain, overlay | `"bordered"` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Two-column banners: Editorial card block

Block key: `panel`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `headingLevel` / Card heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Card heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Card heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `captionStyle` / Card caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Card text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `overlay` / Card image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `20` |
| `heading` / Card heading | Content / Text input | Text 1–160 characters | `"A quiet moment."` |
| `caption` / Card caption | Content / Text input | Text 0–120 characters | `"STUDIO JOURNAL"` |
| `body` / Card text | Content / Plain-text multiline input | Text 0–3000 characters | `"Make a little room for something useful and beautiful."` |
| `surface` / Card surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `textBox` / Show text panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Heading with images

Type: `mte-editorial/heading-with-images`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Editorial heading flanked by small images.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `cardStyle` / Card arrangement | Content / Adaptive segmented choice / select | Choices: bordered, plain, overlay | `"bordered"` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Heading with images: Image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Information cards

Type: `mte-editorial/info-cards`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Short information panels with hierarchy.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `cardStyle` / Card arrangement | Content / Adaptive segmented choice / select | Choices: bordered, plain, overlay | `"bordered"` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Information cards: Editorial card block

Block key: `card`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `headingLevel` / Card heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Card heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Card heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `captionStyle` / Card caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Card text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `overlay` / Card image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `20` |
| `heading` / Card heading | Content / Text input | Text 1–160 characters | `"A quiet moment."` |
| `caption` / Card caption | Content / Text input | Text 0–120 characters | `"STUDIO JOURNAL"` |
| `body` / Card text | Content / Plain-text multiline input | Text 0–3000 characters | `"Make a little room for something useful and beautiful."` |
| `surface` / Card surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `textBox` / Show text panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Promotion cards

Type: `mte-editorial/promotion-cards`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Promotional image panels with links.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `cardStyle` / Card arrangement | Content / Adaptive segmented choice / select | Choices: bordered, plain, overlay | `"overlay"` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Promotion cards: Editorial card block

Block key: `card`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `headingLevel` / Card heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Card heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Card heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `captionStyle` / Card caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Card text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `overlay` / Card image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `20` |
| `heading` / Card heading | Content / Text input | Text 1–160 characters | `"A quiet moment."` |
| `caption` / Card caption | Content / Text input | Text 0–120 characters | `"STUDIO JOURNAL"` |
| `body` / Card text | Content / Plain-text multiline input | Text 0–3000 characters | `"Make a little room for something useful and beautiful."` |
| `surface` / Card surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `textBox` / Show text panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Editorial columns

Type: `mte-editorial/multicolumn`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Editorial cards with responsive column density.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `cardStyle` / Card arrangement | Content / Adaptive segmented choice / select | Choices: bordered, plain, overlay | `"bordered"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Editorial columns: Editorial card block

Block key: `card`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `headingLevel` / Card heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Card heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Card heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `captionStyle` / Card caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Card text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `overlay` / Card image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `20` |
| `heading` / Card heading | Content / Text input | Text 1–160 characters | `"A quiet moment."` |
| `caption` / Card caption | Content / Text input | Text 0–120 characters | `"STUDIO JOURNAL"` |
| `body` / Card text | Content / Plain-text multiline input | Text 0–3000 characters | `"Make a little room for something useful and beautiful."` |
| `surface` / Card surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `textBox` / Show text panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Editorial rich text

Type: `mte-editorial/rich-text`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Readable ordered text with heading, body, list and quote.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Editorial rich text: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Heading | Content / Text input | Text 1–160 characters | `"A considered detail."` |
| `level` / Heading level | Content / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `size` / Heading size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `style` / Heading style | Content / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Editorial rich text: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Caption | Content / Text input | Text 1–120 characters | `"STUDIO NOTES"` |
| `style` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `size` / Caption size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Editorial rich text: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Text | Content / Plain-text multiline input | Text 1–4000 characters | `"Every useful object has a story. Give yours room to unfold."` |
| `emphasis` / Emphasis | Content / Adaptive segmented choice / select | Choices: normal, strong, em | `"normal"` |

### Editorial rich text: List block

Block key: `list`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `items` / Items (one per line) | Content / Ordered text list | 1–12 text items; item max 500;  | `["A useful purpose.","A thoughtful detail."]` |

### Editorial rich text: Quote block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Quotation | Content / Plain-text multiline input | Text 1–2000 characters | `"A little attention changes the everyday."` |
| `credit` / Attribution | Content / Text input | Text 0–160 characters | `"Silt & Form"` |

### Editorial rich text: Image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

### Editorial rich text: Button block

Block key: `button`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Editorial image banner

Type: `mte-editorial/image-banner`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Image banner with stacked content blocks.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `mobileImageAssetId` / Mobile Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `boxSurface` / Text panel surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `height` / Banner height | Layout / Adaptive segmented choice / select | Choices: natural, tall | `"tall"` |
| `imagePosition` / Image placement | Layout / Adaptive segmented choice / select | Choices: start, end, background | `"background"` |
| `verticalAlignment` / Vertical alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"center"` |
| `textBox` / Show text panel | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `overlay` / Image shade (%) | Content / Numeric input + bounded slider | Integer 0–80 | `30` |
| `radius` / Image corner radius (px) | Appearance / Numeric input + bounded slider | Integer 0–32 | `8` |
| `textBelowMobile` / Text below image on mobile | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Editorial image banner: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Heading | Content / Text input | Text 1–160 characters | `"A considered detail."` |
| `level` / Heading level | Content / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `size` / Heading size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `style` / Heading style | Content / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Editorial image banner: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Caption | Content / Text input | Text 1–120 characters | `"STUDIO NOTES"` |
| `style` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `size` / Caption size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Editorial image banner: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Text | Content / Plain-text multiline input | Text 1–4000 characters | `"Every useful object has a story. Give yours room to unfold."` |
| `emphasis` / Emphasis | Content / Adaptive segmented choice / select | Choices: normal, strong, em | `"normal"` |

### Editorial image banner: List block

Block key: `list`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `items` / Items (one per line) | Content / Ordered text list | 1–12 text items; item max 500;  | `["A useful purpose.","A thoughtful detail."]` |

### Editorial image banner: Quote block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Quotation | Content / Plain-text multiline input | Text 1–2000 characters | `"A little attention changes the everyday."` |
| `credit` / Attribution | Content / Text input | Text 0–160 characters | `"Silt & Form"` |

### Editorial image banner: Image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

### Editorial image banner: Button block

Block key: `button`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Editorial image and text

Type: `mte-editorial/image-with-text`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Image column with ordered story blocks.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `imagePosition` / Image placement | Layout / Adaptive segmented choice / select | Choices: start, end | `"start"` |
| `imageShare` / Image column width (%) | Layout / Numeric input + bounded slider | Integer 25–70 | `50` |
| `verticalAlignment` / Vertical alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"center"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Editorial image and text: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Heading | Content / Text input | Text 1–160 characters | `"A considered detail."` |
| `level` / Heading level | Content / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `size` / Heading size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `style` / Heading style | Content / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Editorial image and text: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Caption | Content / Text input | Text 1–120 characters | `"STUDIO NOTES"` |
| `style` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `size` / Caption size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Editorial image and text: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Text | Content / Plain-text multiline input | Text 1–4000 characters | `"Every useful object has a story. Give yours room to unfold."` |
| `emphasis` / Emphasis | Content / Adaptive segmented choice / select | Choices: normal, strong, em | `"normal"` |

### Editorial image and text: List block

Block key: `list`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `items` / Items (one per line) | Content / Ordered text list | 1–12 text items; item max 500;  | `["A useful purpose.","A thoughtful detail."]` |

### Editorial image and text: Quote block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Quotation | Content / Plain-text multiline input | Text 1–2000 characters | `"A little attention changes the everyday."` |
| `credit` / Attribution | Content / Text input | Text 0–160 characters | `"Silt & Form"` |

### Editorial image and text: Image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

### Editorial image and text: Button block

Block key: `button`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Two-image story

Type: `mte-editorial/two-images-text`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Two distinct images and story text.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `imagePosition` / Images placement | Layout / Adaptive segmented choice / select | Choices: start, end | `"start"` |
| `mobileLayout` / Mobile images | Layout / Adaptive segmented choice / select | Choices: stack, pair | `"pair"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Two-image story: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Heading | Content / Text input | Text 1–160 characters | `"A considered detail."` |
| `level` / Heading level | Content / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `size` / Heading size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `style` / Heading style | Content / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Two-image story: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Caption | Content / Text input | Text 1–120 characters | `"STUDIO NOTES"` |
| `style` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `size` / Caption size | Content / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Two-image story: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Text | Content / Plain-text multiline input | Text 1–4000 characters | `"Every useful object has a story. Give yours room to unfold."` |
| `emphasis` / Emphasis | Content / Adaptive segmented choice / select | Choices: normal, strong, em | `"normal"` |

### Two-image story: List block

Block key: `list`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `items` / Items (one per line) | Content / Ordered text list | 1–12 text items; item max 500;  | `["A useful purpose.","A thoughtful detail."]` |

### Two-image story: Quote block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Quotation | Content / Plain-text multiline input | Text 1–2000 characters | `"A little attention changes the everyday."` |
| `credit` / Attribution | Content / Text input | Text 0–160 characters | `"Silt & Form"` |

### Two-image story: Image block

Block key: `image`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `linkImage` / Link image to its CMS page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |
| `imageRatio` / Image ratio | Media / Adaptive segmented choice / select | Choices: landscape, square, portrait | `"landscape"` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `mobileImageWidth` / Mobile image width (%) | Layout / Numeric input + bounded slider | Integer 20–100 | `100` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImageMobile` / Hide image on mobile | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

### Two-image story: Button block

Block key: `button`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Editorial disclosures

Type: `mte-editorial/collapsible-content`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Question-and-answer disclosure rows.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `openMode` / Initial disclosure state | Behavior / Adaptive segmented choice / select | Choices: individual, first, all | `"individual"` |
| `layout` / Disclosure layout | Layout / Adaptive segmented choice / select | Choices: stack, split | `"stack"` |
| `rowSurface` / Row surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Editorial disclosures: Question block

Block key: `question`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `question` / Question | Content / Text input | Text 1–240 characters | `"What makes an everyday object special?"` |
| `answer` / Answer | Content / Plain-text multiline input | Text 0–4000 characters | `"A useful form and a little attention to the details."` |
| `open` / Initially expanded | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `marker` / Question marker | Appearance / Adaptive segmented choice / select | Choices: none, plus, number | `"plus"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Primary CMS composition

Type: `mte-editorial/main-page`. Current placement: **template**.

Insertable bounded plain CMS composition; arbitrary directives, widgets and inherited HTML remain gaps.

**Preview brief:** Selected CMS title and bounded plain editorial content.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `showPageTitle` / Show Magento page title | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Reusable CMS composition

Type: `mte-editorial/page`. Current placement: **template**.

Insertable bounded plain CMS composition; arbitrary directives, widgets and inherited HTML remain gaps.

**Preview brief:** Reusable bounded CMS excerpt with source label.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `backgroundColor` / Custom background (hex, both colors required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `foregroundColor` / Custom text (hex, readable contrast required) | Appearance / Swatch + validated hex input | Text 0–7 characters; pattern ^(?:#[a-fA-F0-9]{6})?$ | `""` |
| `captionStyle` / Caption style | Content / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `heading` / Section heading | Content / Text input | Text 0–160 characters | `"Stories for everyday living."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `mobileHeadingSize` / Mobile heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading style | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Section caption | Content / Text input | Text 0–120 characters | `""` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Section width | Layout / Adaptive segmented choice / select | Choices: standard, wide, full | `"standard"` |
| `alignment` / Desktop text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `mobileAlignment` / Mobile text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `contentWidth` / Reading width (rem) | Layout / Numeric input + bounded slider | Integer 20–80 | `48` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Link appearance | Source and links / Adaptive segmented choice / select | Choices: outline, solid, text | `"outline"` |
| `showPageTitle` / Show Magento page title | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.
