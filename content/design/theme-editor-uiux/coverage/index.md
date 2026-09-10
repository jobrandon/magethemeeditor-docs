# Current element coverage

Observed 2026-09-10 from the current trusted registry. **66 definitions: 52 full-theme template types, 13 shell types, 1 author example outside full-theme registration.** The 76-section reference census is a broader unfinished target, not this registry.

The appendices account for **1144 section-field occurrences, 66 block-kind declarations and 384 block-field occurrences**. Repeated common fields count once per definition that owns them; these totals are not unique control types. Every type has a preview brief, placement/capability caveat and all its meaningful fields/blocks.

| Package | Definitions | Detailed controls |
| --- | --- | --- |
| Studio | 5 | [All fields and blocks](mte-studio.md) |
| Editorial | 14 | [All fields and blocks](mte-editorial.md) |
| Interactive | 10 | [All fields and blocks](mte-interactive.md) |
| Commerce | 19 | [All fields and blocks](mte-commerce.md) |
| Shell | 13 | [All fields and blocks](mte-shell.md) |
| Forms | 4 | [All fields and blocks](mte-forms.md) |
| Author example | 1 | [All fields and blocks](author-example.md) |

## Placement and discovery

The default Add section view lists the 52 eligible template types. An All components view includes the remaining 14 with explanatory placement labels, not draggable affordances. Shell cards open the relevant shared/native presentation context; the author example explains that the current theme does not register it. Header/Footer groups use the existing shared model, not an assumed array of shell components. This distinction keeps every existing element discoverable without inventing insertion support.

Studio and Editorial equivalents remain distinct, searchable variants with package labels. Never migrate a saved Studio type silently to an Editorial type. Internal type IDs appear in developer details only. Media-dependent previews use curated fictional assets; provider-dependent previews show their unavailable/empty states alongside bounded sample content.

## Control mapping rules

All appendices map fields to Content, Media, Source and links, Layout, Appearance, Behavior, Results or Form and consent. These groups are collapsed progressively. No field is discarded. Reference pickers preserve opaque IDs, unavailable values and accessible labels. Numeric controls retain exact schema units and bounds; the displayed 4px/8px unit conversion must round-trip exactly. String arrays remain ordered items; plain text remains plain text. All schema constraints, custom validators, reference validation, unique anchors and block limits remain authoritative.

See [interaction specifications](../interactions.md) for validation, ordering, conditional controls and accessible navigation.

## Sources and evidence limits

Read directly: `component-library/packages.mjs`, all seven package definitions, `component-library/src/registry.mjs`, `component-library/themes/silt-form/full/registration.mjs`, `product/editor/library-controls.mjs`, and the family coverage records under `component-library/reference/`. No native bridge or renderer was executed to produce this census. Package source hashes are in each appendix and the review JSON. Family records describe historical evidence and open gaps; this design pass does not revalidate Magento runtime behavior.
