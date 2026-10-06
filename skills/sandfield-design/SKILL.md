---
name: sandfield-design
description: Product design philosophy and UX rules for prototyping software, by the Sandfield design team. Use whenever you prototype, build, mock up or review a UI, including screens, dashboards, forms, tables, wizards, flows or components, or when someone asks you to check a design against Sandfield standards, or to strip the generic "AI look" (clutter, excess borders, caps, tints) from an existing UI or prototype. It governs decisions and interaction quality, not brand visuals.
license: MIT
---

# Design philosophy & UX rules

*Made by the design team at [Sandfield](https://www.sandfield.co.nz), New Zealand.*

The people using this skill are often business analysts and product managers, not designers. Your job is to turn their brief into a prototype that **holds up under design and dev review on the first pass**.

Without guidance, generated UIs reflect the average of everything you have seen: missing states, competing actions, invented patterns. This skill replaces that average with our standard.

## What this skill governs

- **Governs:** structure, hierarchy, interaction, states, copy and patterns. These are *how we decide*.
- **Does not govern:** brand colours, logos or typefaces (those come from a theme, see `themes/README.md`), or technology choices. Use whatever the user's tool produces.

## Precedence

1. **Accessibility is a floor, not a preference.** WCAG AA contrast, visible focus, 44×44px touch targets, full keyboard access, and never colour as the only signal. Nothing overrides it, including the NOD test, simplicity, a brand or a stated exception.
2. **The product's existing design system and established patterns come next.** If the product or client already has components, conventions or a design system, follow them. Apply Sandfield rules only where the existing system is silent. Where they conflict, follow the existing system and list the conflict in your review.
3. **Then this skill's principles** (below).

**Override:** only when the user explicitly says to ignore or replace the existing design system ("ignore our design system", "redesign this with Sandfield rules instead"), swap 2 and 3 for that request. The accessibility floor and the client's brand still hold. List what you overrode in your review, so nobody mistakes the result for something that fits the current product. "Redesign", "modernise" or "make it better" on their own are **not** an override. If a request is ambiguous and the product has a design system, ask one question: "Keep your existing design system, or override it with Sandfield rules?"

## Modes

Pick exactly one mode per request. When unsure between two, use the one that changes less.

| Mode | Triggered when | Not triggered by | Does |
|---|---|---|---|
| **Build** (default) | Asked to create, prototype or extend a UI | Nothing else matches | The working method below |
| **Review** | "Review", "check", "critique", "audit", "what's wrong with…" | Any request to change something | Report only; change nothing (see *Reviewing an existing design*) |
| **Reset** | The user explicitly asks to strip the look: "clean up / declutter / tidy up the AI slop", "make it look less AI", "Sandfield reset", "remove the clutter" on an existing UI | Building something new (restraint already applies). "Improve", "polish" or "make it better" (that's Build on the existing UI). A review request. Screens that follow the product's own design system | A visual-only cleanup (see *Reset mode*) |

After a Review that finds three or more Visual-restraint failures, or when someone shares a prototype made in another tool and asks to improve it, you may *offer* Reset in one line. Never run it unasked.

## Working method

Follow these steps in order. Don't skip steps 1 and 5.

### 1. Frame the context before building
Infer the following from the brief. If one of them is missing **and would change the design**, ask one short question that covers all of them. Otherwise state your assumptions in one line and proceed.

- **Who** the user is: first-time, occasional, or daily expert
- **Where** they work: desk, warehouse floor, vehicle cab, customer-facing, mobile
- **Main job** of this view: the one thing it must make easy
- **Density:** compact, cozy or default (see `references/rules.md` §1.2)

Then read `references/checklist.md`. It's the bar your output is reviewed against, and each item points to the section that holds its detail.

### 2. Structure each view
- Establish the reading order: orientation → status → primary action → supporting detail.
- Apply the NOD test (below).

### 3. Build the states that can happen
Every region that loads data, can be empty or can fail gets those states: **loading, loaded, empty, errored**. A static region (a heading, a fixed form) doesn't need them. Every interactive element gets its interactive states (`references/rules.md` §3).

**Tweaks (only when asked).** If the user wants to compare options for a design decision (a layout, a density, where an action sits), add one small control panel that switches between them. Style it so nobody mistakes it for the product, and leave it out of your review.

**Build what the brief needs, not what the checklist lists.** Pattern rules (search, filters, bulk actions, pagination, shortcuts, wizards) apply only when the brief implies the need. Don't add a feature just to satisfy a rule. If you think one is missing, list it under "Recommended additions" in your review.

### 4. Write the copy
Use specific verbs on buttons, and name the commitment on the final step (`Confirm purchase`, not `Continue`). Empty and error copy says what happened, why, and what to do next. Use one term per concept throughout. Use realistic, domain-appropriate data with real-looking names, codes, dates and units, never lorem ipsum. Include one long value and one empty field so edge cases show up. **Always invent the data.** Never copy real people, customers or client records from attached files or screenshots, even when asked to "use the real data". Mirror their shape, not their content.

### 5. Self-review before you say "done"
Go through `references/checklist.md` item by item and fix any failures you can. When you can't tell whether an item passes, open the section it points to and check against that. Don't judge from memory. At the end of your reply, report only what still fails and what you broke on purpose. Don't give a score:

```
Sandfield review
Still failing: #6 filtered-empty state on the Orders table (not enough detail in the brief)
Deliberate exceptions: #16 two-column form, because the fields are paired start/end dates
Conflicts with product system: product uses inline labels; kept them
Recommended additions: #19 search (list may grow past 15 items)
```

Leave out any line that has nothing in it. If nothing is left, write "Sandfield review: no open issues."

**Exceptions:** you may break a pattern or rule only when you name it and give a reason tied to *this* brief's user or context ("breaking X because Y"). "It looks cleaner" or "it's simpler" is not a reason. Never break the accessibility floor or the NOD test, and never break a rule silently. Items marked *Guideline* are defaults: adapt them to the brief without logging an exception.

## The NOD test

### No Needless Parts
Every element must serve a goal.
* Remove decorative chrome, redundant borders and placeholder text

### One Clear Purpose
Exactly one dominant primary action per view.
* If two actions compete, restructure

### Driven by Patterns
Follow established standards.
* Do not invent custom UI patterns without explicit alignment

## Reference files

Read the checklist every time. Read the others when the task touches their topic, or when a checklist item points you there:

| File | Read when |
|---|---|
| `references/philosophy.md` | Deciding *how* something should work: principles, patterns, components and the reasoning behind them |
| `references/rules.md` | You need the numbers: density modes, form layout, interactive states, type, spacing |
| `references/checklist.md` | Always: before building (step 1), at step 5, and when reviewing an existing design |
| `references/examples.md` | Writing empty/error states, button labels, wizards, or tables |
| `themes/README.md` | The user names a client or brand, or supplies brand guidelines |

## Reset mode

A visual-only cleanup of an existing UI, against *Visual restraint* in `references/philosophy.md`.

- **Keep:** structure, layout, content, copy, flows, data, states and brand colours. Nothing gets added.
- **Remove or reduce:** excess all caps, stacked borders, decorative tints, shadows, gradients, glows, emoji icons, icons on every heading, and nested cards.
- **Respect the product's system.** If the product's design system specifies something (e.g. uppercase buttons), it isn't slop, so leave it.
- **Report** a short list of what you removed, then offer a full Review if structural issues are visible. Don't fix those unasked.

## Reviewing an existing design

When asked to review rather than build, don't rebuild. Run `references/checklist.md`. Report accessibility-floor failures first, then NOD failures, then the other failures ranked by user impact. Each failure gets the rule it breaks and a concrete fix.
