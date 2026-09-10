# ADR 0003: Custom React for the bounded editor concept

Status: **accepted only for the local Batch 02 concept; reversible before native integration**.
Date: 2026-09-07. Owner: task `01a07b0a-53c4-7382-aea4-79c44a2ca13a`, Astra High.
Scope: [SOL-493](https://linear.app/solventech/issue/SOL-493), prototype subset of
[SOL-501](https://linear.app/solventech/issue/SOL-501). No merchant or Magento acceptance.

## Decision and rationale

Use custom React controls over the existing portable content document, with a separate UI-state
object for selection/history. Store no React/library tree in JSON. The flat four-component v1
contract needs fewer abstractions than a general visual builder. This avoids bidirectional tree
mapping and keeps a future native-renderer iframe independent of React rendering.

React 19.2.8 and React DOM 19.2.8, with scheduler 0.27.0, are the complete added package graph.
Their exact local-browser-use review, locked identities and original notices are retained in
`product/third-party/`. A fixed first-party build wrapper packages four unchanged production CJS
files; it introduces no compiler/dev-server dependency. The browser calls a loopback-only Node
validator/demo persistence service. Server contract/key/filesystem logic stays out of the bundle.
See [comparison and runnable concept](../architecture/editor-concept.md).

## Consequences and reversibility

We own controls, command history, focus management, persistence feedback and accessibility work.
This spike is deliberately flat: no pointer drag/drop, arbitrary nesting, rich-text model or
generic field-schema renderer. Adding those capabilities could make Puck a better accelerator;
that decision would need a measured candidate spike and a complete actual dependency review.
The comparison does not establish a four-way performance or usability ranking.

The illustrative iframe demonstrates a replaceable preview boundary and stable-ID selection.
It proves no native PHTML renderer, cross-origin authenticated session, Magento preview parity,
cache isolation, publish, restore or real merchant task outcome. The next decision point is a
small native home/CMS adapter proof using the authorized local compatibility targets with
appropriate state isolation. Keep the current versioned document unchanged while testing that
boundary. Hosted framework/database/provider selection remains open.

## Evidence

The [Batch 02 evidence](../roadmap/batch-02-evidence-2026-09-07.md) separates automated tests,
observed browser interactions, documentary candidate assessment and open criteria. Source remains
local without a Git branch/SHA. No code was uploaded and no hosting or paid editor was adopted.
