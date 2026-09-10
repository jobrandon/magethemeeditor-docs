# Forms control coverage

Observed 2026-09-10. Extracted from `component-library/packages/forms/package.mjs` (1.0.0); source SHA-256 `54996e5db41401f1a12b97ad1ac36277d580d9e6eb8530c091c61949b6a49bbd`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Contact preview

Type: `mte-forms/contact-form`. Current placement: **template**.

Insertable template; validation-only, no contact delivery, subscription, campaign or capture provider.

**Preview brief:** Fictional contact fields, validation-only feedback.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Let’s start a conversation."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STAY A LITTLE LONGER"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"Try the fields using fictional sample values. This local demonstration cannot send a message."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Form surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `layout` / Layout | Layout / Adaptive segmented choice / select | Choices: stack, image-start, image-end | `"image-start"` |
| `fullWidth` / Full width | Layout / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageHeight` / Image height (8px units) | Layout / Numeric input + bounded slider | Integer 16–64 | `40` |
| `mobileImageHeight` / Mobile image height (8px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `28` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 25–65 | `45` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `consent` / Consent preference | Form and consent / Adaptive segmented choice / select | Choices: required, optional, hidden | `"required"` |
| `consentLabel` / Consent label | Form and consent / Text input | Text 1–500 characters | `"I agree to test this local preview. This does not subscribe me."` |
| `consentPosition` / Consent position | Form and consent / Adaptive segmented choice / select | Choices: before-button, after-button | `"before-button"` |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |
| `successText` / Additional validation message | Form and consent / Text input | Text 0–500 characters | `"Your sample is ready for review."` |
| `demoState` / Demo pathway | Form and consent / Adaptive segmented choice / select | Choices: validate, unavailable, error | `"validate"` |
| `emailLabel` / Email field label | Form and consent / Text input | Text 1–80 characters | `"Email address"` |
| `pageId` / Information CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Information link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open information in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Information link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `linkImage` / Link image to information page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hidePhone` / Hide telephone field | Form and consent / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `allRequired` / Require all visible fields | Form and consent / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `nameLabel` / Name field label | Form and consent / Text input | Text 1–80 characters | `"Name"` |
| `phoneLabel` / Telephone field label | Form and consent / Text input | Text 1–80 characters | `"Telephone"` |
| `messageLabel` / Message field label | Form and consent / Text input | Text 1–80 characters | `"Message"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Email signup banner

Type: `mte-forms/email-signup-banner`. Current placement: **template**.

Insertable template; validation-only, no contact delivery, subscription, campaign or capture provider.

**Preview brief:** Image banner and non-delivering email validation block.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"A note from the studio."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STAY A LITTLE LONGER"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"Occasional stories about thoughtful forms and everyday rituals."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Form surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `layout` / Layout | Layout / Adaptive segmented choice / select | Choices: stack, image-start, image-end | `"image-start"` |
| `fullWidth` / Full width | Layout / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageHeight` / Image height (8px units) | Layout / Numeric input + bounded slider | Integer 16–64 | `40` |
| `mobileImageHeight` / Mobile image height (8px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `28` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 25–65 | `45` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `consent` / Consent preference | Form and consent / Adaptive segmented choice / select | Choices: required, optional, hidden | `"required"` |
| `consentLabel` / Consent label | Form and consent / Text input | Text 1–500 characters | `"I agree to test this local preview. This does not subscribe me."` |
| `consentPosition` / Consent position | Form and consent / Adaptive segmented choice / select | Choices: before-button, after-button | `"before-button"` |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |
| `successText` / Additional validation message | Form and consent / Text input | Text 0–500 characters | `"Your sample is ready for review."` |
| `demoState` / Demo pathway | Form and consent / Adaptive segmented choice / select | Choices: validate, unavailable, error | `"validate"` |
| `emailLabel` / Email field label | Form and consent / Text input | Text 1–80 characters | `"Email address"` |
| `pageId` / Information CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Information link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open information in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Information link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `linkImage` / Link image to information page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Email signup banner: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STUDIO LETTERS"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Email signup banner: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Keep in touch."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Email signup banner: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"A fictional studio newsletter. Local validation only."` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |

### Email signup banner: Email validation form block

Block key: `email-form`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Newsletter preview

Type: `mte-forms/newsletter`. Current placement: **template**.

Insertable template; validation-only, no contact delivery, subscription, campaign or capture provider.

**Preview brief:** Compact non-delivering newsletter validation layout.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"A note from the studio."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STAY A LITTLE LONGER"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"Occasional stories about thoughtful forms and everyday rituals."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Form surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `layout` / Layout | Layout / Adaptive segmented choice / select | Choices: stack, image-start, image-end | `"stack"` |
| `fullWidth` / Full width | Layout / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageHeight` / Image height (8px units) | Layout / Numeric input + bounded slider | Integer 16–64 | `40` |
| `mobileImageHeight` / Mobile image height (8px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `28` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 25–65 | `45` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `consent` / Consent preference | Form and consent / Adaptive segmented choice / select | Choices: required, optional, hidden | `"required"` |
| `consentLabel` / Consent label | Form and consent / Text input | Text 1–500 characters | `"I agree to test this local preview. This does not subscribe me."` |
| `consentPosition` / Consent position | Form and consent / Adaptive segmented choice / select | Choices: before-button, after-button | `"before-button"` |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |
| `successText` / Additional validation message | Form and consent / Text input | Text 0–500 characters | `"Your sample is ready for review."` |
| `demoState` / Demo pathway | Form and consent / Adaptive segmented choice / select | Choices: validate, unavailable, error | `"validate"` |
| `emailLabel` / Email field label | Form and consent / Text input | Text 1–80 characters | `"Email address"` |
| `pageId` / Information CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Information link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open information in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Information link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `linkImage` / Link image to information page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |

**Nested blocks:** 0–12 total. Only the following kinds are valid children. This is one block level, not unrestricted containers.

### Newsletter preview: Caption block

Block key: `caption`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STUDIO LETTERS"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"uppercase"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"small"` |

### Newsletter preview: Heading block

Block key: `heading`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"Keep in touch."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h3"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |

### Newsletter preview: Paragraph block

Block key: `paragraph`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"A fictional studio newsletter. Local validation only."` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |

### Newsletter preview: Email validation form block

Block key: `email-form`.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.

## Promotion popup

Type: `mte-forms/popup`. Current placement: **template**.

Insertable template; validation-only, no contact delivery, subscription, campaign or capture provider.

**Preview brief:** Manually opened promotion dialog with close and frequency hints.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Heading | Content / Text input | Text 0–160 characters | `"A little studio inspiration."` |
| `headingLevel` / Heading level | Appearance / Adaptive segmented choice / select | Choices: h2, h3, h4 | `"h2"` |
| `headingSize` / Heading size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `headingStyle` / Heading font | Appearance / Adaptive segmented choice / select | Choices: serif, sans | `"serif"` |
| `caption` / Caption | Content / Text input | Text 0–160 characters | `"STAY A LITTLE LONGER"` |
| `textStyle` / Text style | Appearance / Adaptive segmented choice / select | Choices: plain, uppercase | `"plain"` |
| `textSize` / Text size | Appearance / Adaptive segmented choice / select | Choices: small, medium, large | `"medium"` |
| `body` / Introduction | Content / Plain-text multiline input | Text 0–4000 characters | `"Occasional stories about thoughtful forms and everyday rituals."` |
| `surface` / Surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"paper"` |
| `panelSurface` / Form surface | Appearance / Adaptive segmented choice / select | Choices: paper, tint, ink | `"tint"` |
| `layout` / Layout | Layout / Adaptive segmented choice / select | Choices: stack, image-start, image-end | `"stack"` |
| `fullWidth` / Full width | Layout / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageAssetId` / Magento image | Media / Searchable reference picker (assets) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `alt` / Image description | Media / Text input | Text 0–300 characters | `""` |
| `decorative` / Decorative image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideImage` / Hide image | Media / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `imageHeight` / Image height (8px units) | Layout / Numeric input + bounded slider | Integer 16–64 | `40` |
| `mobileImageHeight` / Mobile image height (8px units) | Layout / Numeric input + bounded slider | Integer 12–48 | `28` |
| `imageWidth` / Image width (%) | Layout / Numeric input + bounded slider | Integer 25–65 | `45` |
| `paddingTop` / Top padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `paddingBottom` / Bottom padding (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `12` |
| `marginTop` / Top margin (4px units) | Layout / Numeric input + bounded slider | Integer 0–24 | `0` |
| `spacingMode` / Padding source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `marginMode` / Margin source | Layout / Adaptive segmented choice / select | Choices: custom, theme | `"custom"` |
| `consent` / Consent preference | Form and consent / Adaptive segmented choice / select | Choices: required, optional, hidden | `"required"` |
| `consentLabel` / Consent label | Form and consent / Text input | Text 1–500 characters | `"I agree to test this local preview. This does not subscribe me."` |
| `consentPosition` / Consent position | Form and consent / Adaptive segmented choice / select | Choices: before-button, after-button | `"before-button"` |
| `buttonLabel` / Validation button label | Form and consent / Text input | Text 1–80 characters | `"Validate demo"` |
| `successText` / Additional validation message | Form and consent / Text input | Text 0–500 characters | `"Your sample is ready for review."` |
| `demoState` / Demo pathway | Form and consent / Adaptive segmented choice / select | Choices: validate, unavailable, error | `"validate"` |
| `emailLabel` / Email field label | Form and consent / Text input | Text 1–80 characters | `"Email address"` |
| `pageId` / Information CMS page | Source and links / Searchable reference picker (pages) | Text 0–64 characters; pattern ^(?:[a-z][a-z0-9_-]{0,63})?$ | `""` |
| `linkLabel` / Information link label | Source and links / Text input | Text 0–80 characters | `""` |
| `newTab` / Open information in new tab | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `linkStyle` / Information link style | Source and links / Adaptive segmented choice / select | Choices: solid, outline, text | `"outline"` |
| `linkImage` / Link image to information page | Source and links / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `enabled` / Enable popup | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `trigger` / Open behavior | Behavior / Adaptive segmented choice / select | Choices: manual, delay | `"manual"` |
| `delay` / Delay in seconds | Behavior / Numeric input + bounded slider | Integer 0–60 | `5` |
| `frequency` / Automatic display frequency | Behavior / Adaptive segmented choice / select | Choices: visit, session, days | `"session"` |
| `frequencyDays` / Days between automatic displays | Behavior / Numeric input + bounded slider | Integer 1–30 | `7` |
| `hideDesktop` / Hide on desktop | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `hideMobile` / Hide on mobile | Behavior / Adaptive Enabled/Disabled choice / select | true / false | `false` |
| `showSignup` / Show email validation form | Content / Adaptive Enabled/Disabled choice / select | true / false | `true` |
| `triggerLabel` / Open button label | Form and consent / Text input | Text 1–80 characters | `"Open studio invitation"` |
| `closeLabel` / Close button label | Form and consent / Text input | Text 1–80 characters | `"Close invitation"` |

**Package validation:** preserve the existing validator in addition to field constraints; its exact source is captured in the local `data/component-inventory.json`. Do not treat successful field typing as complete validation.
