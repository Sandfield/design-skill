# Sandfield Design Skill: overview

*Version 0.1.0 · Sandfield Design Team · Max van IJsselmuiden*

An Agent Skill that teaches AI tools how Sandfield designs software. When someone asks an AI to prototype or review a UI, the skill loads on its own and holds the output to our standards. It governs **decisions, not visuals**.

The suggested way of distribution across Sandfield is explained in this document. We're suggesting publishing the skill to one GitHub repository, which is connected to the npx skill repository and our Claude organisation-wide managed settings, making it incredibly easy for anyone to install.

Distributing the skill publicly avoids the burden of authentication, making it easy for coworkers to apply the skill from any tool they use, in any environment. Because a skill is a set of Markdown files, there is little to no maintenance required for this open-source approach.

## Why publish it to the open skills registry

- **One install.** `npx skills add sandfield/design-skill` installs it into Claude Code, Codex, Cursor, Copilot and other agents.
- **One source of truth.** The skill lives in one GitHub repo. No copies drift apart.
- **Safe to be public.** It contains no client work: it's brand-agnostic.
- **Visible expertise.** A public, installable design standard shows how Sandfield works, for clients, partners and future hires.

## Modes

| Mode | When | What it does |
|---|---|---|
| **Build** (default) | Asked to create, prototype or extend a UI | Frames the context (who, where, main job, density), structures the view, builds every state that can happen, writes real copy with invented data, then self-reviews against a 24-item checklist |
| **Review** | "Review", "check", "audit" a design | Reports only and changes nothing. Accessibility failures first, then NOD, then the rest ranked by user impact, each with a fix |
| **Reset** | Explicitly asked to strip the "AI look" | A visual-only cleanup: removes excess caps, borders, tints, gradients and similar, and keeps structure, copy and brand |

Two behaviours run in every mode:

- **Precedence:** accessibility is a floor; the product's own design system comes before Sandfield rules unless the user explicitly says otherwise.

Every build ends with a short review: what still fails, which rules were broken on purpose and why, and what the skill suggests to add to the prototype.

## What it's built on

- **Sandfield's design philosophy:** the design team's principles and patterns document, including the **NOD test** (No needless parts, One clear purpose, Driven by patterns).
- **The AI prototyping context rules:** the concrete numbers for density, forms, interactive states, typography and spacing.
- **Established standards:** WCAG AA accessibility and familiar platform patterns (Jakob's Law).
- **The Agent Skills open standard** ([agentskills.io](https://agentskills.io)): a short main file, with detailed references loaded only when needed, to keep it efficient.

## Distribution across Sandfield

| Who | How |
|---|---|
| Developers (Claude Code, Cursor, Copilot) | `npx skills add sandfield/design-skill` |
| Everyone on Claude Code, automatically | IT enables the plugin in managed settings (Claude admin console or MDM) |
| Claude.ai / Claude Desktop users (BAs, PMs) | An org admin uploads the skill once for the whole organisation |
| Other tools (AI Studio) | Unfortunately no easy way to distribute the skill; a simplified variant in user instructions could work, needs testing. |

**Ownership:** the Sandfield Design Team owns the content. Changes go through pull requests, each with its reasoning.

## Next steps

1. Publish the repo to GitHub as `sandfield/design-skill`.
2. Roll it out to Claude Code through managed settings, and to Claude.ai through an org admin.
