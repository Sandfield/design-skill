# Sandfield Rules: the numbers

The structural, interaction and UX rules that apply regardless of product or brand. The reasoning behind them lives in `philosophy.md`. Colours are set per product via a theme.

---

## Rule Set 1: Layout & Structure

### 1.1 Information hierarchy
Every screen establishes this reading order:

1. **Orientation:** where am I, what module, what record?
2. **Status or summary:** what is the current state?
3. **Primary action:** what should I do next?
4. **Supporting detail:** context, history, metadata (below the fold or in a secondary panel)

Content that serves orientation comes before content that requires action. Never bury the primary call to action. On short views it's in view without scrolling. On long forms, put it at the natural end or in a sticky footer.

### 1.2 Data density
Infer density from the user type and context in the brief. Don't expose density as a user-facing control.

| Mode | When to apply |
|---|---|
| Compact | Daily power users: financial data, operational tables, row-scanning workflows |
| Cozy | Back-office users at moderate frequency: balances visibility with less fatigue over long sessions |
| Default | Customer-facing, occasional or public users, mobile-first, onboarding |

Rule of thumb: if the user scans many rows as their primary job, use compact. If they arrive infrequently or need orientation, use default. When in doubt, use default. In chaotic environments, touch targets stay ≥44px regardless of density.

---

## Rule Set 2: Forms

### 2.1 Form layout
- **Labels:** in forms, top-aligned above the input, never right-aligned. Compact contexts (filter bars, toolbars, inline table editing) may use inline labels, but a field's purpose is always visible, never only in placeholder text.
- **Layout:** single column by default. Use multiple columns only when fields are logically paired (First/Last name, Start/End date).
- **Required fields:** mark *required*, not optional. It's the less common state.
- **Submission:** one primary submit action per form. Destructive or cancel actions are secondary and visually distinct.
- **Grouping:** use fieldsets when a form has 7+ fields that can be logically categorised.

### 2.2 Validation
- Validate at field level (on blur), not only on submit.
- Show errors in context, next to the field that caused them, not in a remote banner. For long forms, add a summary at the top that links to each field.
- Never clear a field value when showing an error. The user needs to see what they typed.
- Confirm success. Don't assume the user noticed.

### 2.3 Input states
Every input has all five designed:

| State | Notes |
|---|---|
| Default | Idle, no interaction |
| Focus | Actively selected, by keyboard or mouse; visible focus ring |
| Filled | Has a value |
| Validation | **Success**, **Warning** or **Error**, each with a message. Never colour alone; pair it with an icon and text |
| Disabled | Not interactable and visually suppressed. Explain why when state-gated |

---

## Rule Set 3: Interactive states

Every interactive element has all applicable states defined before the screen is complete:

| State | Purpose |
|---|---|
| Default | The baseline: no interaction has occurred |
| Hover | Signals interactivity; distinct from default, with no layout shift |
| Focus | Keyboard navigation indicator; meets contrast requirements |
| Active / Pressed | Confirms the interaction is registering |
| Loading | System is working; element temporarily non-interactive, and its size doesn't change |
| Disabled | Not available; communicates why when possible |
| Selected / Checked | Persists after interaction; distinct from active |

If a state is not designed, a developer will invent it, and that invention will be inconsistent.

---

## Rule Set 4: Feedback & system status

### 4.1 Always communicate state
Every system state has a corresponding UI state:

- **Loading:** skeleton screens for content areas; a spinner only for isolated elements (e.g. a button mid-submit). Never a blank screen. Show it after 300ms. Under that, a spinner distracts more than the wait.
- **Empty:** explain why it's empty and what to do next. "No results" is not enough. "No projects yet. Create a project to get started." is. Distinguish a *first-use* empty state (nothing exists yet) from a *filtered* empty state (offer to clear filters).
- **Error:** be specific. "Something went wrong" is a UX failure. State what happened, why, and the next step.
- **Success:** confirm the outcome. Use a toast for non-blocking confirmations, or inline feedback when the result is visible on the current screen.

### 4.2 Destructive actions
Any action that deletes, overwrites, or cannot be undone requires:

1. A confirmation step before execution
2. Clear labelling of exactly what will be affected ("Delete 3 projects and their 12 files?")
3. A way out: `Cancel` is always present, prominent, and the default focus
4. A confirm button that names the action (`Delete 3 projects`, not `OK`)

---

## Rule Set 5: Typography & readability

### 5.1 Hierarchy
No more than three typographic levels per screen:

- **Heading:** screen or section title; one per logical section
- **Body:** default reading text; 16px minimum, 1.5 line-height. Compact data tables may go smaller, as long as they still meet WCAG AA legibility
- **Supporting:** metadata, labels, captions; visually subdued but still AA-legible

Don't use font size alone to create hierarchy. Weight, colour and spacing carry equal responsibility.

### 5.2 Line length
Keep body text at 60–80 characters per line. Use max-width constraints so text doesn't span full-width containers at wide viewports.

### 5.3 Alignment
- Body text: left-aligned
- Numbers in tables: right-aligned, with consistent decimals and units
- Centred text: headings and short UI labels only, never body paragraphs

---

## Rule Set 6: Spacing & visual rhythm

### 6.1 Spacing scale
Use a consistent spacing scale based on a base unit (typically 4px or 8px). No arbitrary values. Every margin, padding and gap is a multiple of the base unit.

### 6.2 Proximity
- Related items sit closer together than unrelated ones. Spacing *inside* a group is smaller than spacing *between* groups.
- A label sits closer to its own input than to the previous field.
- Use whitespace for grouping before adding borders or dividers (No Needless Parts).

### 6.3 Alignment grid
- Align content to a shared left edge. Avoid more than two alignment lines per region.
- Primary actions align to a consistent edge within the product (e.g. always right-aligned in a form footer).
