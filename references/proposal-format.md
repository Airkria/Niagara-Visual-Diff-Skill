# Proposal data format

The viewer consumes one UTF-8 JSON object. Store only the state needed to explain the proposal; do not dump an entire Niagara asset when a concise semantic diff is sufficient.

```json
{
  "schemaVersion": 1,
  "title": "Review a Niagara emitter change",
  "engineVersion": "5.x",
  "target": {
    "system": "NS_Example",
    "emitter": "EmitterName",
    "simulationTarget": "GPUComputeSim"
  },
  "stacks": [
    { "stage": "Particle Spawn", "modules": ["Initialize Particle"] }
  ],
  "changes": [
    {
      "id": "change-001",
      "stage": "Particle Spawn",
      "action": "set-input",
      "module": "Initialize Particle",
      "input": "Lifetime",
      "before": 5,
      "after": 10,
      "reason": "Explain why this value changes.",
      "reproduce": "Where to find this control in Niagara Editor.",
      "status": "planned",
      "exampleOnly": false
    }
  ]
}
```

Supported action labels are `add-module`, `remove-module`, `reorder-module`, `set-input`, `enable-module`, `disable-module`, `add-renderer`, `remove-renderer`, and `note`. The viewer can display other labels, but the Skill must explain them explicitly.

Keep `before` and `after` faithful to the live asset. For linked values, dynamic inputs, data interfaces, or asset references, represent the binding/reference in readable JSON and state when the nested value has not been inspected. Do not replace an unknown value with a guessed default.

Change statuses are `planned`, `applied`, `verified`, and `failed`. Only the agent's post-edit inspection can move a change to `verified`.
