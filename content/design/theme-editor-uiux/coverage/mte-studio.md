# Studio control coverage

Observed 2026-09-10. Extracted from `component-library/packages/studio/package.mjs` (1.0.0); source SHA-256 `2b0f7f76c493fa64d7fc2f82b21d51cec11103cf76b0b90dbd93c41f0fc47518`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Banner / hero

Type: `mte-studio/banner`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Two-column hero with image, eyebrow and CTA.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Make room for everyday discoveries."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `width` / Content width | Layout / Adaptive segmented choice / select | Choices: standard, wide | `"standard"` |
| `spacing` / Section spacing | Layout / Adaptive segmented choice / select | Choices: compact, comfortable, spacious | `"comfortable"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `eyebrow` / Eyebrow | Content / Text input | Text 0–100 characters | `"A fresh perspective"` |
| `body` / Description | Content / Plain-text multiline input | Text 0–2000 characters | `"Explore the ideas, people and details behind our work."` |
| `imageAssetId` / Image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `height` / Banner height | Layout / Adaptive segmented choice / select | Choices: natural, tall | `"natural"` |

## Rich text

Type: `mte-studio/rich-text`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Readable ordered text with heading, body, list and quote.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Thoughtfully made, simply shared."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Content width | Layout / Adaptive segmented choice / select | Choices: standard, wide | `"standard"` |
| `spacing` / Section spacing | Layout / Adaptive segmented choice / select | Choices: compact, comfortable, spacious | `"comfortable"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Rich text: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Paragraph | Content / Plain-text multiline input | Text 1–4000 characters | `"Tell your story in your own words."` |
| `emphasis` / Emphasis | Content / Adaptive segmented choice / select | Choices: normal, strong, em | `"normal"` |

### Rich text: Subheading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Subheading | Content / Text input | Text 1–160 characters | `"The details matter."` |

### Rich text: List block

Block key: `list`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `items` / List items (one per line) | Content / Ordered text list | 1–12 text items; item max 500;  | `["Considered materials","Practical design"]` |

### Rich text: Quote block

Block key: `quote`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `text` / Quote | Content / Plain-text multiline input | Text 1–2000 characters | `"Useful things deserve a little care."` |
| `credit` / Attribution | Content / Text input | Text 0–160 characters | `"Our studio"` |

## Image with text

Type: `mte-studio/image-text`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Image and copy side by side.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Behind the everyday."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Content width | Layout / Adaptive segmented choice / select | Choices: standard, wide | `"standard"` |
| `spacing` / Section spacing | Layout / Adaptive segmented choice / select | Choices: compact, comfortable, spacious | `"comfortable"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `body` / Description | Content / Plain-text multiline input | Text 0–4000 characters | `"Share the process, a place or the people who make it possible."` |
| `imageAssetId` / Image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `imageSide` / Image position | Media / Adaptive segmented choice / select | Choices: start, end | `"start"` |
| `imageFit` / Image fit | Media / Adaptive segmented choice / select | Choices: cover, contain | `"cover"` |

## Multi-column cards

Type: `mte-studio/cards`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Three consistent image-and-copy columns.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Ideas worth exploring."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Content width | Layout / Adaptive segmented choice / select | Choices: standard, wide | `"standard"` |
| `spacing` / Section spacing | Layout / Adaptive segmented choice / select | Choices: compact, comfortable, spacious | `"comfortable"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Multi-column cards: Card block

Block key: `card`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Card heading | Content / Text input | Text 1–160 characters | `"A new perspective"` |
| `body` / Card description | Content / Plain-text multiline input | Text 0–2000 characters | `"A short introduction to something useful."` |
| `imageAssetId` / Image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkLabel` / Link label | Source and links / Text input | Text 0–80 characters | `""` |
| `pageId` / Magento CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |

## Collapsible FAQ

Type: `mte-studio/faq`. Current placement: **template**.

Insertable authored template content with registered media/CMS references; registration is not full reference parity or release proof.

**Preview brief:** Two questions, one expanded.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Good questions, clear answers."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `width` / Content width | Layout / Adaptive segmented choice / select | Choices: standard, wide | `"standard"` |
| `spacing` / Section spacing | Layout / Adaptive segmented choice / select | Choices: compact, comfortable, spacious | `"comfortable"` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center, end | `"start"` |

**Nested blocks:** 0–24 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Collapsible FAQ: Question block

Block key: `question`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `question` / Question | Content / Text input | Text 1–240 characters | `"Where can I learn more?"` |
| `answer` / Answer | Content / Plain-text multiline input | Text 1–4000 characters | `"Visit the information pages maintained by this store."` |
| `open` / Initially expanded | Content / Adaptive Enabled/Disabled choice / select | true / false | `false` |
