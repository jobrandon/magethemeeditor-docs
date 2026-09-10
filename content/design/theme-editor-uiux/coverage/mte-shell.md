# Shell control coverage

Observed 2026-09-10. Extracted from `component-library/packages/shell/package.mjs` (1.0.0); source SHA-256 `c88afc92ad9632677d799eb97eb3152dc609a59fd75fb81fc7a0362dc5d5decc`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Demo header

Type: `mte-shell/header`. Current placement: **shell**.

Registered shell presentation; not a template insertion. Current full editor uses a separate fixed shared shell model. Drag composition into shared shell is proposed.

**Preview brief:** Wordmark and registered demo links.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Welcome to the studio"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Objects with intention."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |
| `wordmark` / Wordmark | Content / Text input | Text 1–80 characters | `"silt & form"` |
| `showSearch` / Show native search link | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showAccount` / Show native account link | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `showCart` / Show read-only cart disclosure | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `pageFont` / Page typography | Appearance / Adaptive segmented choice / select | Choices: sans, serif | `"sans"` |
| `pagePalette` / Page palette | Content / Adaptive segmented choice / select | Choices: chalk, clay, forest | `"chalk"` |
| `pageWidth` / Page width | Layout / Adaptive segmented choice / select | Choices: reading, wide | `"wide"` |
| `linkStyle` / Link style | Source and links / Adaptive segmented choice / select | Choices: underlined, outlined | `"underlined"` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Demo header: Demo page link block

Block key: `link`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Registered CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^page-silt-[a-z-]+$ | `"page-silt-home"` |
| `linkLabel` / Link label | Source and links / Text input | Text 1–80 characters | `"Studio home"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Demo footer

Type: `mte-shell/footer`. Current placement: **shell**.

Registered shell presentation; not a template insertion. Current full editor uses a separate fixed shared shell model. Drag composition into shared shell is proposed.

**Preview brief:** Footer note and grouped registered links.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Keep in touch with the studio"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Original fictional studio. Useful forms. Everyday stories."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |
| `backToTop` / Back to this demo header | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Demo footer: Demo page link block

Block key: `link`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Registered CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^page-silt-[a-z-]+$ | `"page-silt-home"` |
| `linkLabel` / Link label | Source and links / Text input | Text 1–80 characters | `"Studio home"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Announcement

Type: `mte-shell/announcement-bar`. Current placement: **shell**.

Registered shell presentation; not a template insertion. Current full editor uses a separate fixed shared shell model. Drag composition into shared shell is proposed.

**Preview brief:** Short announcement strip and CTA.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"A little room for everyday rituals"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Explore the original Silt & Form studio stories."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"ink"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |
| `alignment` / Text alignment | Layout / Adaptive segmented choice / select | Choices: start, center | `"center"` |
| `dismissible` / Allow dismissal for this page visit | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Announcement: Demo page link block

Block key: `link`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Registered CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^page-silt-[a-z-]+$ | `"page-silt-home"` |
| `linkLabel` / Link label | Source and links / Text input | Text 1–80 characters | `"Studio home"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Quick information

Type: `mte-shell/quick-info-bar`. Current placement: **shell**.

Registered shell presentation; not a template insertion. Current full editor uses a separate fixed shared shell model. Drag composition into shared shell is proposed.

**Preview brief:** Two concise service messages.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Good to know"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"A few notes about the studio."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |
| `columns` / Desktop columns | Layout / Numeric input + bounded slider | Integer 1–4 | `3` |
| `border` / Show border | Appearance / Adaptive Enabled/Disabled choice / select | true / false | `true` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Quick information: Information item block

Block key: `info`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Title | Content / Text input | Text 1–100 characters | `"Thoughtfully made"` |
| `text` / Description | Content / Text input | Text 1–500 characters | `"Small details make useful objects feel at home."` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Missing-page presentation

Type: `mte-shell/main-404`. Current placement: **shell**.

Registered shell presentation; does not prove global 404 routing. Not a template insertion.

**Preview brief:** Missing-page content without promising routing interception.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"That story is not here."` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Find your way back to the studio or choose another demo page."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Nested blocks:** 0–8 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Missing-page presentation: Demo page link block

Block key: `link`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `pageId` / Registered CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^page-silt-[a-z-]+$ | `"page-silt-home"` |
| `linkLabel` / Link label | Source and links / Text input | Text 1–80 characters | `"Studio home"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Your account

Type: `mte-shell/main-account`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Account route handoff with heading and CTA.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Your account"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Continue to the store to view your account securely."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Sign in

Type: `mte-shell/main-login`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Sign-in route handoff without login fields.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Sign in"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Use the store’s native sign-in page to access your account."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Create an account

Type: `mte-shell/main-register`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Registration route handoff without credential entry.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Create an account"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Registration continues on the store’s native account page."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Password help

Type: `mte-shell/main-reset-password`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Password-help route handoff without token handling.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Password help"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Request password help through the store’s native recovery page."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Your addresses

Type: `mte-shell/main-addresses`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Address-management route handoff, no addresses.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Your addresses"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"View and manage your addresses securely in your store account."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Your orders

Type: `mte-shell/main-order`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Orders route handoff, no customer order data.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Your orders"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"View your order history through your authenticated store account."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Your shopping bag

Type: `mte-shell/main-cart-items`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Shopping bag route handoff, no live totals.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Your shopping bag"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Your current browser’s Magento cart appears here when its data is available."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Continue with your bag

Type: `mte-shell/main-cart-footer`. Current placement: **shell**.

Registered shell/native-route handoff; not an embedded authenticated or cart editor. Not a template insertion.

**Preview brief:** Continue-to-bag route handoff.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 1–160 characters | `"Continue with your bag"` |
| `text` / Supporting text | Content / Plain-text multiline input | Text 1–1600 characters | `"Review quantities, totals and options on the store’s native cart page."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `spacing` / Vertical padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `6` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.
