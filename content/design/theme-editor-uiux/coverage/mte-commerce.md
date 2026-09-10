# Commerce control coverage

Observed 2026-09-10. Extracted from `component-library/packages/commerce/package.mjs` (1.0.0); source SHA-256 `73b5a3b16bc4b906e00e6ff6453055a5b9df661cc157b58a604effda618442a5`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Category cards

Type: `mte-commerce/collection-list`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Named category cards.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Category cards"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Category cards: Category block

Block key: `collection`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `label` / Optional category label | Content / Text input | Text 0–120 characters | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## All store categories

Type: `mte-commerce/main-list-collections`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Store categories with empty state companion.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"All store categories"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### All store categories: Category block

Block key: `collection`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `label` / Optional category label | Content / Text input | Text 0–120 characters | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Category disclosures

Type: `mte-commerce/collection-tabs`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Category disclosure groups, accurately shown as disclosures.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Category disclosures"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Category disclosures: Category block

Block key: `collection`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `label` / Optional category label | Content / Text input | Text 0–120 characters | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Featured category groups

Type: `mte-commerce/featured-collections`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Several authored category groups.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Featured category groups"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Featured category groups: Category block

Block key: `collection`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `label` / Optional category label | Content / Text input | Text 0–120 characters | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Featured category products

Type: `mte-commerce/featured-collection`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Products from one selected category.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Featured category products"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `sort` / Product order | Results / Adaptive segmented choice / select | Choices: position, name, newest | `"position"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Category product grid

Type: `mte-commerce/main-collection-product-grid`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Category-bound product results with source context.

**Route context:** {"categoryId":"category"}. Display a route-bound source chip; do not silently replace it with a handpicked source.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Category product grid"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `sort` / Product order | Results / Adaptive segmented choice / select | Choices: position, name, newest | `"position"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Subcategories

Type: `mte-commerce/subcollections`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Child category cards for one parent.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Explore subcategories"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Category introduction

Type: `mte-commerce/main-collection-banner`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Category introduction and native description.

**Route context:** {"categoryId":"category"}. Display a route-bound source chip; do not silently replace it with a handpicked source.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"About this category"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Image and categories

Type: `mte-commerce/image-banner-with-collections`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Authored image plus category cards.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Discover the catalog"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `imageAssetId` / Editorial banner image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:asset-ceramics)?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Image and categories: Category block

Block key: `collection`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `label` / Optional category label | Content / Text input | Text 0–120 characters | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Image and category products

Type: `mte-commerce/image-banner-with-featured-collection`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Authored image plus category products.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"A closer look"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `imageAssetId` / Editorial banner image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:asset-ceramics)?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `categoryId` / Magento category | Source and links / Searchable reference picker (categories) | Text 0–32 characters; pattern ^(?:category-[1-9][0-9]{0,9})?$ | `""` |
| `sort` / Product order | Results / Adaptive segmented choice / select | Choices: position, name, newest | `"position"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Featured product

Type: `mte-commerce/featured-product`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** One fictional simple product with source identity.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Featured product"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Product overview

Type: `mte-commerce/main-product`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Route-bound product overview; unavailable product state.

**Route context:** {"productId":"product"}. Display a route-bound source chip; do not silently replace it with a handpicked source.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Product overview"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Related products

Type: `mte-commerce/related-products`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Products related to a selected product.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Related products"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Pickup information

Type: `mte-commerce/pickup-availability`. Current placement: **template**.

Insertable presentation; provider unbound. Preserve unavailable state.

**Preview brief:** Pickup provider unavailable message; no invented inventory.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Pickup information"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Persistent product action

Type: `mte-commerce/sticky-add-to-cart`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Persistent product action presentation using sample state.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Persistent product action"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Search this store

Type: `mte-commerce/main-search`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Query input and sample results/empty state.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Search this store"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `query` / Initial search phrase | Source and links / Text input | Text 0–100 characters | `""` |
| `buttonLabel` / Search button label | Form and consent / Text input | Text 0–80 characters | `"Search"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Search suggestions

Type: `mte-commerce/predictive-search`. Current placement: **template**.

Insertable; store-scoped catalog/provider dependency. Local simple-product subset; advanced product and full reference parity unproven.

**Preview brief:** Search suggestion presentation; provider limits stated.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Search suggestions"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `query` / Initial search phrase | Source and links / Text input | Text 0–100 characters | `""` |
| `buttonLabel` / Search button label | Form and consent / Text input | Text 0–80 characters | `"Search"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Find products by SKU

Type: `mte-commerce/quick-order-list`. Current placement: **template**.

Insertable; read-only SKU discovery, not bulk ordering.

**Preview brief:** Read-only SKU finder; no bulk-order success.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Find your next item"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `mobileColumns` / Mobile columns | Layout / Numeric input + bounded slider | Integer 1–2 | `1` |
| `limit` / Maximum results | Results / Numeric input + bounded slider | Integer 1–24 | `6` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |
| `showImage` / Show Magento image | Media / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showDescription` / Show Magento description | Results / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `sku` / Initial SKU | Source and links / Text input | Text 0–64 characters | `""` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Find products by SKU: Product reference block

Block key: `item`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `productId` / Magento product | Source and links / Searchable reference picker (products) | Text 0–32 characters; pattern ^(?:product-[1-9][0-9]{0,9})?$ | `""` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Recently viewed

Type: `mte-commerce/recently-viewed-products`. Current placement: **template**.

Insertable presentation; provider unbound. Preserve unavailable state.

**Preview brief:** Private-history provider unavailable state.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Recently viewed in this browser"` |
| `intro` / Introduction | Content / Plain-text multiline input | Text 0–2000 characters | `""` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `8` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.
