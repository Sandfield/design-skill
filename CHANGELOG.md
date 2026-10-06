# Changelog

## 0.1.0 (draft)
- First packaging of the design philosophy as an Agent Skill.
- Philosophy based on `design.md` (the original wording), with selected additions from `design-improved.md` (reasoning lines, view/region, review questions, modals, hide vs disable, data formatting, feedback signals, two-interaction reach, flaky connections, reduced motion, tutorials stance). No priority ranking.
- Merged back from the August `design.md`: Success/Warning/Error input states; wizard footer order softened to "preferably"; action buttons close to the actionable area; AI-assisted prefilling; inline single-variable dropdowns; filter details in "Use previous filters?"; motion examples; "explain exactly what will be lost" on destructive confirms.
- Rules based on the AI Prototyping Context doc; reconciled with the philosophy (input states, undo-first destructive actions). Spacing: §6.2 Proximity and §6.3 Alignment added.
- Scope: UX/UI only. No technology or stack guidance, and no default visual theme (only anti-generic-AI guardrails when no brand is supplied).
- Added: working method, self-review checklist with NOD gate (reports fails + exceptions only, no score), examples, theme contract, benchmark prompts.
- Hardening: accessibility is a non-negotiable floor (unranked); an existing product design system takes precedence over Sandfield rules; pattern rules apply only when the brief implies them ("Recommended additions" instead of adding features); states only where they can happen; exceptions need a brief-specific reason and never apply to accessibility or NOD; data always invented; themes never alter a client brand.
- Resolved conflicts: Escape vs losing entered data, top labels vs filter bars, 16px body vs compact tables, primary action reachability on long forms.
- Examples and eval prompts use mixed, client-neutral domains; added restraint, data-privacy and precedence evals.
- Added Visual restraint (all caps, borders, tints, generic AI look). Governs frequency of use, not palette. Checklist item 24.
- Added modes (Build / Review / Reset) with explicit trigger and non-trigger phrases, and an explicit-only design-system override. Evals 12–16 test triggering.
- Removed from the rewrite: undo over confirm, constrain input, never-lose-data, regions failing independently / background operations. Checklist now 24 items.
- Added tweaks: when asked, one clearly-not-product control panel for comparing options for a design decision.
- Removed duplication: each rule now has one home (NOD and accessibility in SKILL.md, specs in rules.md, reasoning in philosophy.md). The checklist is read before building, and every item points to the section that holds its detail.
- Added *Guideline* marking for defaults applied with judgement; "Working with entities" is a guideline.
