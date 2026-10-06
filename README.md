# Sandfield Design Skill

By the design team at [Sandfield](https://www.sandfield.co.nz), New Zealand.

Our product design philosophy, packaged as an [Agent Skill](https://agentskills.io) for AI prototyping. When someone asks an AI tool to prototype or review a UI, the skill loads automatically. It anchors the output to how Sandfield designs: the NOD test, principles, complete states, and a self-review checklist.

It governs **decisions, not visuals**. Brand comes from a per-project theme.

## Install

| Where you work | How |
|---|---|
| Claude Code, Codex, Cursor, Copilot, other agents | `npx skills add sandfield/design-skill` |
| Claude Code (plugin) | `/plugin marketplace add sandfield/design-skill`, then `/plugin install sandfield-design@sandfield` |
| Claude.ai / Claude Desktop | An org admin uploads the skill once for the whole organisation (build the zip with `./scripts/build.sh`) |
| Other tools (e.g. AI Studio) | No supported route yet. A simplified version for custom instructions needs testing |

### For IT: roll out automatically (Claude Code)
Add to managed settings (Claude admin console, or `managed-settings.json` via MDM):

```json
{
  "extraKnownMarketplaces": {
    "sandfield": { "source": { "source": "github", "repo": "sandfield/design-skill" } }
  },
  "enabledPlugins": { "sandfield-design@sandfield": true }
}
```

## Use

Just ask for a prototype. The skill triggers on UI work:

> "Prototype an order list for warehouse staff who check 200+ orders a shift."

The AI states its assumptions (user, context, density), builds every state, self-reviews against the checklist, and ends by listing anything still failing and any rule broken on purpose:

```
Sandfield review
Still failing: filtered-empty state on the Orders table
Deliberate exceptions: two-column form (paired start/end dates)
```

To review an existing design: *"Review this screen against Sandfield standards."*

To strip the generic AI look from an existing prototype, keeping structure and content: *"Clean up the AI slop"* or *"Sandfield reset"*.

To apply Sandfield rules over a product's own design system (explicit only): *"Ignore our design system and redo this with Sandfield rules."*

For a client brand, supply their guidelines. See [`themes/README.md`](skills/sandfield-design/themes/README.md).

## What's inside

```
skills/sandfield-design/
├── SKILL.md                 working method, modes, NOD test
├── references/
│   ├── philosophy.md        principles + patterns + reasoning (how we decide)
│   ├── rules.md             the numbers: density, forms, states, type, spacing
│   ├── checklist.md         24-item self-review with a NOD gate
│   └── examples.md          good vs. not-yet: empty states, errors, buttons, wizards
└── themes/README.md         how to plug in a client brand (client themes stay private)
evals/prompts.md             benchmark prompts to test the skill with/without
scripts/build.sh             builds dist/ (zip for Claude.ai, single .md for other tools, reader.html)
```

## Contributing

Content is owned by the Sandfield Design Team. Propose changes via PR. Every rule change needs its reasoning (the *why*), and the evals should be re-run. Bump the version in `.claude-plugin/plugin.json` + `marketplace.json` and add an entry to `CHANGELOG.md`.

```bash
./scripts/build.sh     # → dist/sandfield-design.zip, dist/sandfield-design.md, dist/reader.html
```
