# Change receipt template

Use for meaningful implementation or verification evidence, not every small edit. Keep raw
logs under ignored `.local/` and durable summaries beside their workstream. Follow
[documentation](../documentation.md) and [delivery](../delivery.md) policies.

```text
Date and scope: What was changed or inspected; what this evidence establishes.
Result: Concrete resulting behavior or artifact.
Source: Checkout, branch/SHA and changed paths; identify uncommitted source where applicable.
Environment: Actual runtime/configuration and local target.
Verification: Commands or browser actions, observed outcomes and evidence locations.
Preservation: Data/source checks and reversal steps where relevant.
Limits: Unverified acceptance criteria or remaining issues; distinguish reviewed owner evidence.
Next owner/action: Only if further work is required and already assigned.
```

For instructions-only edits, a scoped diff/link review is usually sufficient; run the docs
build when site content changes. Do not invent runtime evidence or repeat passing suites
merely to populate a template.
