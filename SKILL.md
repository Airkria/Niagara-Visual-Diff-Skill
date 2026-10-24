---
name: niagara-visual-diff
description: Turn Unreal Engine Niagara system edits into a visual, reviewable change proposal, support discussion of individual changes, and verify the applied result. Use when a user needs to understand or review Niagara stack edits made through an agent or MCP.
---

# Niagara Visual Diff

Make Niagara edits understandable before and after they reach Unreal Editor. Treat the visual proposal as a translation and review layer over the actual Niagara system, not as a replacement simulator.

## Workflow

1. Identify the exact Niagara System and emitter. Read the current emitter topology, ordered script stacks, renderer list, and relevant input values from the connected Unreal/Niagara tools. Record the engine version when available. Never infer current values from an old screenshot or example.
2. Before changing the asset, prepare a semantic proposal. Each change needs a stable ID, target emitter and stack stage, operation, affected module/input, before and after values when applicable, a short reason, and a practical replication hint. Distinguish `planned`, `applied`, `verified`, and `failed` states. Mark illustrative examples as `exampleOnly`; never present them as recommendations.
3. Render the proposal using `scripts/render_proposal.py` and `assets/proposal-template.html`. Put generated files in a task-specific output folder, not beside the Skill package. Show the resulting HTML to the user when the environment supports opening local files. The page is data-driven; it does not mutate a Niagara asset.
4. Invite feedback on a specific change ID. If the user edits a card comment in the page, ask them to paste its copied feedback into the conversation; use that feedback to revise the proposal and render it again. Keep discussion attached to the affected change.
5. Apply changes only when the user's request authorizes the actual Niagara edit. A request to inspect, explain, or prepare a proposal alone does not authorize mutation. Apply only the accepted operations through the available Niagara tools.
6. Re-read the affected emitter stacks and values after editing. Mark each operation `verified` only when the live Niagara state matches the proposal; otherwise report the observed mismatch and leave it `failed` or unresolved. Report compile or stack issues separately from structural matching.

## Proposal format

Read [references/proposal-format.md](references/proposal-format.md) when creating or editing proposal data. Use [examples/terrain-brush-proposal.json](examples/terrain-brush-proposal.json) only as a format example based on the terrain-brush emitter; its sample change is explicitly illustrative and must not be applied.

## Limits

- Do not claim that a visual proposal proves Niagara compilation, runtime behavior, or cross-version compatibility.
- Preserve exact Niagara module/script names and parameter values from live inspection. Explain display-name versus internal-name differences when they matter.
- Do not silently omit unsupported inputs, dynamic-input chains, data interfaces, renderer settings, or dependencies. Mark them as not inspected or unsupported and explain what additional inspection is needed.
- Keep the user's existing emitter and project files unchanged while preparing a proposal. Editing is a separate, user-directed step.
