# Research provenance

Imported: 7 September 2026. Research date: 7 September 2026.

The [research baseline](theme-editor-research-2026-09-07.md) is a byte-for-byte copy of the completed
shared research. The original remains at:

```text
/Users/branorphiano/Projects/jobrandon/docs/content/solven-tech/mage-theme-editor/architecture/theme-editor-research-2026-09-07.md
```

The independently owned copy is:

```text
/Users/branorphiano/Projects/jobrandon/MageThemeEditor/docs/content/architecture/theme-editor-research-2026-09-07.md
```

SHA-256 of both files at import:

```text
541f2c46a99715ea01939e71a4c017e9fd74d4bd271bacdc48dc12de7a41f6b5
```

Size: 32,592 bytes. The shared file was read and copied; its contents and shared Git
state were not changed by this setup. The workspace `.docs` symlink is routed to the local
`docs/content` only after source and site verification.

## What this copy establishes

The original citations and evidence qualifications are preserved, including the distinction
between public documentation, issue reports, community anecdotes, and independently measured
results. The research reported no merchant interviews or runtime implementation proof. Its
statement that the project directory was empty describes the original inspection, before this
documentation setup.

This import does not revalidate every external source, vendor capability, license, or dependency
recommendation. Recheck unstable claims when making a new product decision. The
[Linear research document](https://linear.app/solventech/document/magethemeeditor-research-and-architecture-baseline-953f16866313)
is a related planning resource, not the checksum source for this local copy.

## Later direction and corrections

The user subsequently confirmed [hybrid adoption](../requirements/hybrid-adoption.md): preserve the
active theme and explicitly opt in selected pages or registered regions. Those local requirements
extend the dated recommendation without rewriting it. Their complete routing/isolation criteria
were not yet recorded in Linear at the [live audit](../roadmap/linear-baseline-2026-09-07.md).

Keep this file immutable as the baseline. Add later findings in a new dated document or decision,
link back to the baseline, and describe the correction. New MageThemeEditor documentation belongs
in this local project; the shared original is historical provenance.

## Recheck the import

From the documentation repository, compare with the preserved original when it is available:

```bash
shasum -a 256 content/architecture/theme-editor-research-2026-09-07.md
cmp content/architecture/theme-editor-research-2026-09-07.md \
  /Users/branorphiano/Projects/jobrandon/docs/content/solven-tech/mage-theme-editor/architecture/theme-editor-research-2026-09-07.md
```

The ordinary build does not depend on the sibling repository being present.
