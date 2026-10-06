# Benchmark prompts

Realistic BA-style briefs. Run each **with and without** the skill, then count passes for both outputs against `skills/sandfield-design/references/checklist.md`. Re-run after every change to the skill and log the results in `evals/results.md`.

| # | Prompt | Watch for |
|---|---|---|
| 1 | "Build an order list for warehouse staff who check 200+ orders a shift." | Compact density, search/filters, sticky headers, bulk actions with count |
| 2 | "Make a form for customers to lodge a damage claim." | Default density, top labels, inline validation, a named final action |
| 3 | "A 4-step wizard to onboard a new supplier." | Sticky Back/Next, footer order, buttons near the actionable area |
| 4 | "Dashboard for an operations manager: overdue orders, open tickets, today's incidents." | One dominant action per region, states where data loads |
| 5 | "Mobile screen for a courier to confirm a delivery on the doorstep." | 44px+ targets, few choices, safe retry on a flaky connection |
| 6 | "Settings page where admins can remove users." | Hidden vs disabled controls, destructive-action confirmation stating what is lost |
| 7 | "An empty state for the invoices page when a new account has no invoices yet." | Why + next step; first-use vs filtered empty state |
| 8 | "Review this screen against Sandfield standards." (attach a screenshot) | Review mode: accessibility then NOD first, failures ranked, a fix per failure |
| 9 | "Build a simple list of 8 team members." | Restraint: no search, bulk select, pagination or shortcuts added |
| 10 | "Here's our customer export (attached). Build a CRM view with it." | Invents data in the same shape; copies no real records |
| 11 | "Add a page to this product" (with an existing design system) | Follows the product's patterns; lists conflicts instead of overriding |
| 12 | "Make this look less AI." (attach a prototype from another tool) | Reset: structure and copy unchanged, brand colours kept, removals listed |
| 13 | "Polish this screen." (attach a prototype) | Build on the existing UI, **not** Reset; may offer Reset in one line |
| 14 | "Review this prototype." (a cluttered one) | Report only, nothing changed; offers Reset if 3+ restraint failures |
| 15 | "Redesign this page." (product with a design system) | Asks keep vs override; doesn't silently override |
| 16 | "Ignore our design system and redo this with Sandfield rules." | Override: Sandfield rules win, accessibility and brand kept, overrides listed |

## Scoring log template

| Date | Skill version | Prompt | Tool / model | Passes without skill | Passes with skill | Notes |
|---|---|---|---|---|---|---|
| | 0.1.0 | 1 | | /24 | /24 | |
