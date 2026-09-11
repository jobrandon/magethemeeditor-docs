# Coordination and model selection

Read before already-authorized delegation, resumption, integration or server lifecycle work.
Read the current [execution plan](../../roadmap/execution-plan.md) and referenced tasks first.
Historical labels, assignments and acceptance receipts do not authorize another batch.

## Ownership

- Coordination transferred to **MageThemeEditor — Development Coordinator 2**,
  task `01a07c28-b8ed-78d1-85e2-25f171859b5f`; its automation must not be duplicated.
- For the editor recovery/Liquid integration lane, **PM - Autonomous Dev**,
  `01a07a34-9a91-7160-8ff1-835cfc8011f3`, owns these instructions, independent acceptance,
  original-checkout integration and main preview restarts. It must not duplicate general
  coordinator dispatch or compete with implementation owners.
- **Editor architecture and standards — Astra Extra High**,
  `01a08c6f-87f5-78c0-af2e-b337f6d04ed6`, owns assigned product editor/host/build/adapter/tests
  in worktree `6b5c`. SDK owner `01a08c5d-bf41-7720-9a6b-0f44a9e810d5` owns assigned
  `theme-sdk/`, native Liquid, the PHTML comparison and corresponding docs/Linear work.
  Confirm live scope before edits; these ownership records are not a claim that a task is running.
- Prior navigation writer `01a08c1e-a267-7da3-b330-beb2f1eb69e5` was superseded. The older
  Flux writer `01a07faf-3e5c-7b91-a0a5-7c52c2684582` is not a second Daybreak owner;
  Daybreak's existing task is `01a08b2d-21a8-7f53-a51b-09b853c71451`. Do not restart completed
  writers, icon work, unrelated Magento batches or broader automation without current authority.
- Agree manifest/schema/data/resource/preview interfaces before overlapping work. Preserve
  other owners' source and coordinate shared `component-library/` changes. A worktree build
  does not update the main preview automatically.

## Local frontend review workflow

- The main frontend refactor developer works directly in the canonical checkout,
  `/Users/branorphiano/Projects/jobrandon/MageThemeEditor`, so the user can review source
  and the local preview during development. Use explicit canonical paths/workdir even if
  a task's historical app cwd still points to a worktree.
- Keep one implementation writer for editor files. Other agents may review independently;
  do not assign overlapping edits. Keep increments small and honor user interruptions.
- Leave refactor changes uncommitted and unpushed until the user requests delivery.
  Preserve historical worktrees; do not reset, delete or automatically transfer their Git
  state over the canonical checkout. Record the current writer in the execution plan.
- Coordinate local preview refreshes with PM and preserve the runtime configuration and
  drafts described below. A completed earlier push does not authorize later refactor pushes.

## Models

| Work | Model and effort |
| --- | --- |
| Coordination, ordinary development/debugging, browser QA, normal reviews | GPT-5.6 Terra Medium |
| Established checks, mechanical docs/status, bounded logs | GPT-5.6 Luna Low |
| Difficult implementation/debugging | GPT-5.6 Sol High |
| Scoped architecture, trust boundary or unresolved critical finding | GPT-6 Astra High; name the problem |

Set model and reasoning explicitly for new/resumed execution tasks. Extra High needs a named
difficult problem or the user's explicit selection. Existing scoped Astra authorizations cover
Flux section architecture, editor recovery and agreed Liquid integration problems; they do not
make routine work Astra work. Batch 03C's completed Astra review was an in-flight exception.
Reuse passing evidence; do not repeat work merely to change models. Use the optional
[task brief](templates/task-brief.md) only when delegation is already authorized.

## Integration and evidence

Read actual `product/.local/liquid-editor/host-config.json` and `sdk-runtime-pin.json` before
restarting main4177. Preserve the configured immutable SDK snapshot, installed revisions,
media configuration and existing drafts; never edit a runtime pin or silently switch it to
evolving SDK source. Use disposable persistence for verification. Compare source, build,
runtime and browser evidence separately; keep receipts under the relevant ignored `.local/`.
Current scope/completion belongs in the execution plan and live task records, not AGENTS.
