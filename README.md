# Niagara Visual Diff Skill

**A visual review layer for Niagara edits made with an AI agent or MCP.** It turns planned stack changes into a local, shareable page so artists can see what will change, discuss a specific module, and compare the result with the live emitter.

This is a Codex Skill package with a lightweight HTML proposal viewer. It does not replace Niagara Editor or simulate particles in the browser. Unreal remains the source of truth for module availability, compilation, and runtime behavior.

## What it does

- Reads the current Niagara emitter stack and relevant values through the connected Unreal/Niagara tools.
- Shows additions, removals, reorderings, and parameter changes as a proposal before applying them.
- Lets a user attach a question or note to a specific change and copy that feedback back into the conversation.
- Re-reads the live system after an authorized edit and marks changes as verified only when they match.

## Install

Clone or download this repository and place its root folder in your Codex skills directory as `niagara-visual-diff`. The Skill uses the Unreal/Niagara MCP tools available in the current session; it does not bundle or install an Unreal plugin.

To render proposal data manually with Python 3:

```powershell
python scripts/render_proposal.py examples/terrain-brush-proposal.json --output ./niagara-proposal.html
```

Open the generated HTML file in a browser. No web server, package manager, or external network request is required.

## Example case

The included example captures the observed shape of `NS_TerrainBrush` in MyResource: GPU simulation, Emitter Update with Emitter State and Spawn Particles in Grid, Particle Spawn with Initialize Particle and Grid Location, and a Sprite Renderer. Its X/Y grid-count proposal is marked `exampleOnly`; it demonstrates the review UI and is not an approved performance recommendation.

## Status meanings

`planned` means proposed only. `applied` means an edit call completed but the result has not yet been checked. `verified` means the current emitter was re-read and matches. `failed` means application or verification did not complete. The page itself never changes an Unreal asset.

## Repository

Repository name: **Niagara Visual Diff Skill** (`Niagara-Visual-Diff-Skill`). A public repository makes the files visible; usage and redistribution rights depend on a license, which is intentionally not declared in this initial package.
