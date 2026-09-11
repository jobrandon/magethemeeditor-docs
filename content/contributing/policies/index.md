# Agent policies and templates

AGENTS files contain only essential rules and task routing. Read the policy needed for the
current change, then only the linked references or templates that help complete it. Do not
load this whole directory at startup. Policies preserve existing scope; they do not authorize
new work, dependencies, delegation or publication.

| Work | Read when relevant |
| --- | --- |
| TypeScript, React or source organization | [Source code](source-code.md) |
| Editor styles, tokens or component CSS | [Tailwind styling](styling.md) |
| Task ownership, model selection or preview integration | [Coordination](coordination.md) |
| Local Magento or native contracts | [Magento](magento.md) |
| Dependencies, Git delivery or Linear updates | [Delivery](delivery.md) |
| Documentation or MkDocs | [Documentation](documentation.md) |
| Separate editor design specimens | [UIUX workspace](uiux.md) |
| Choosing development skills | [Task-to-skill routing](../project-skills.md#task-routing) |

Templates are optional starting points, not mandatory scaffolding:

- [React component and spacing](templates/component.md)
- [Task brief](templates/task-brief.md), only for already-authorized delegation
- [Change or verification receipt](templates/change-receipt.md)

Keep each rule in one owning policy. Nested AGENTS files add only local differences.
Store changing task status in the [execution plan](../../roadmap/execution-plan.md), design
decisions in the [decision register](../../decisions/index.md), and dated evidence beside the
relevant workstream. Do not append task transcripts, test counts or SDK hashes to AGENTS.

This organization was introduced on 11 September 2026. It records existing conventions;
it does not establish that legacy source or CSS has already been migrated.
