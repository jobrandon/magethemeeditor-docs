# React component template

Read only when creating a component or checking spacing. This is an illustrative starting
point, not an adopted product component or mandatory scaffold. Follow the
[source policy](../source-code.md) and [Tailwind styling policy](../styling.md).

```text
product/editor/features/preview/components/PreviewToolbar/
  PreviewToolbar.tsx
  usePreviewToolbar.tsx   # only if behavior needs its own hook
  types.ts               # only if types have another consumer
  index.ts               # optional narrow public entry
```

Keep small private types in the component file. Shared UI belongs under
`product/editor/components/`. Add a plain `.module.css` only for a justified custom-CSS
exception with verified build support. Do not create empty tests/stories/hooks directories.

```tsx
type PreviewToolbarProps = {
  canUndo: boolean;
  onUndo: () => void;
};

export function PreviewToolbar({ canUndo, onUndo }: PreviewToolbarProps) {
  return (
    <div className="flex items-center gap-2">
      <button
        type="button"
        disabled={!canUndo}
        onClick={onUndo}
        className="rounded-md border px-3 py-2 text-sm focus-visible:outline-2 disabled:opacity-50"
      >
        Undo
      </button>
    </div>
  );
}
```

Use the existing design system's tokens/variants for production styles and accessible
contrast. Keep component APIs narrow; do not add a styling dependency for this example.

```ts
function normalizeLabel(value: string | undefined): string {
  if (value === undefined) {
    return '';
  }

  const trimmedLabel = value.trim();

  return trimmedLabel;
}
```

The guard, preparation and return are visually separated. Apply the same grouping between
imports, declarations and individual React hooks; keep related object properties together.
