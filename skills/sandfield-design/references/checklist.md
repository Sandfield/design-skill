# Sandfield Review Checklist

Read this before building, run it before calling a prototype done, and use it to review an existing design. Each item is **pass / fail / n/a**. A partially met item is a fail. An item is **n/a** when the brief doesn't imply the need.

Each item points to where its detail lives (`P` = `philosophy.md`, `R` = `rules.md`, `E` = `examples.md`). If you're unsure whether an item passes, open that section.

**Floor:** item 22 (accessibility) can never be an exception.

**Gate:** all three NOD items must pass. A design that fails NOD isn't ready, however well it does on the rest.

## Gate: NOD (SKILL.md, P: The NOD Test)
- [ ] **No Needless Parts:** every element serves a goal
- [ ] **One Clear Purpose:** exactly one dominant primary action per view
- [ ] **Driven by Patterns:** established patterns only, nothing invented without alignment

## Structure
1. [ ] Reading order is orientation → status → primary action → detail (R §1.1)
2. [ ] Primary action is easy to reach at every breakpoint: in view on short views, at the end or sticky on long forms (R §1.1)
3. [ ] Density matches the user and context, and the choice is stated (R §1.2)
4. [ ] Current location is visually distinct; breadcrumbs if >2 levels deep (P: Wayfinding)
5. [ ] At narrow viewports, the most important area keeps the space (P: Responsive layout)

## States
6. [ ] Every region that loads, can be empty or can fail has those states (R §4.1)
7. [ ] Every interactive element has its states (hover, focus, active, disabled, loading, selected) with no layout shift (R §3)
8. [ ] Every input has default, focus, filled, validation (success/warning/error) and disabled states (R §2.3)
9. [ ] Disabled controls explain why; role-gated controls are hidden (P: Permissions)

## Copy
10. [ ] Buttons use specific verbs; the final step names the commitment (E: Buttons)
11. [ ] Empty states say why they're empty plus the next step; error states say what happened, why, and the next step (R §4.1, E: Empty states, Errors)
12. [ ] One term per concept throughout
13. [ ] Realistic data with explicit units, a consistent date format and timezone; no lorem ipsum (P: Data formatting)

## Safety & recovery
14. [ ] Destructive actions have a confirmation stating exactly what is lost, with a prominent `Cancel` (R §4.2, E: Destructive action)
15. [ ] Inline validation; entered values are never cleared on error (R §2.2)

## Patterns
16. [ ] Forms: top labels (inline allowed in filter bars/toolbars), single column (unless fields are paired), required fields marked, fieldsets at 7+ fields (R §2.1)
17. [ ] Wizards: Back/Next always visible; bottom bar `[Back] … [Cancel] [Continue]` (P: Wizards, E: Wizard footer)
18. [ ] Tables: sorting, pagination and selection (where needed) consistent; bulk actions show a count; sticky headers; right-aligned numbers (P: Tables, E: Tables)
19. [ ] Lists that will realistically exceed 15 items have search; active filters shown as chips or a sentence (P: Search, filtering and sorting)
20. [ ] Toasts are non-blocking, in a fixed corner, and never the only copy of actionable info (P: Feedback & notifications)
21. [ ] Modals only for short focused tasks; Escape closes them (P: Modals)

## Accessibility & motion
22. [ ] WCAG AA contrast, visible focus, 44×44px targets, never colour alone, fully keyboard-reachable (SKILL.md: Precedence)
23. [ ] Motion only explains; nothing delays the target; reduced motion respected (P: Motion)
24. [ ] Visual restraint (unless the product system says otherwise): sentence case, all caps on at most one kind of short label; one separation method at a time; tints only where they carry meaning; no generic "AI look" (P: Visual restraint)

Report in the format in SKILL.md step 5, using these item numbers.
