# Author example control coverage

Observed 2026-09-10. Extracted from `component-library/packages/author-example/package.mjs` (1.0.0); source SHA-256 `f7d875a4e90eecb03295ee33dde96cd17cadf0ee6612fa5e95e92471b6b95203`. This appendix preserves every declared section/block field and default. Inspector group/control choices are proposals; schemas and bounds are current source.

[Coverage overview](index.md) · [Inspector rules](../interactions.md#contextual-inspector)

## Studio notice

Type: `author-example/notice`. Current placement: **not registered**.

Registered author example; not eligible in full-theme registration. Preview in catalog; insertion disabled for this theme.

**Preview brief:** Small author-example notice and tone choice.

| Field / merchant label | Inspector group / control | Existing bounds | Default |
| --- | --- | --- | --- |
| `heading` / Notice heading | Content / Text input | Text 1–160 characters | `"A note from the studio"` |
| `body` / Notice message | Content / Plain-text multiline input | Text 1–1000 characters | `"Our next collection is taking shape. Visit again for a closer look."` |
| `tone` / Notice appearance | Content / Adaptive segmented choice / select | Choices: quiet, highlight | `"quiet"` |
