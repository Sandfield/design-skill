# Sandfield Product Design Decisions & Philosophy

*Definitions:* a **view** is an independently navigable screen or modal. Panels within it are **regions**. A section marked *Guideline* is a default to adapt with judgement, not a rule. Concrete numbers and specs (density, forms, interactive states, loading/empty/error, destructive actions, type, spacing) live in `rules.md`. The accessibility floor is in `SKILL.md` and is not repeated here.

## Principles

### The NOD Test
The three tests are defined in `SKILL.md`. How to apply them:
* **No Needless Parts:** if you can't say what a user accomplishes with an element, it goes.
* **One Clear Purpose:** a composite view (e.g. a dashboard) may hold several actions, but one is dominant and each region has at most one.
* **Driven by Patterns:** users spend most of their time in *other* software, so familiarity is a feature (Jakob's Law). The product's own established patterns come first, then common platform conventions.

"Does every part earn its place, is there one obvious action, and would a user recognise this pattern?"

### Keep it simple
* Make hard choices about what to include (and what to exclude)
* One clear path forward

"What can we remove here?"

### Intuitive for first-time users
*Why:* a first-time user should succeed without training.
* Obvious next steps
* Common patterns (Jakob's Law)
* Clear labels and helpful microcopy
* Introductory tutorials
  * For genuinely complex workflows only, never as a fix for an unclear screen
* Consistent behavior
* Progressive disclosure (advanced features don't clutter basic workflows)

"Does it work for first-time users?"

### Powerful for experts
*Why:* seconds saved on daily tasks add up.
* Keyboard shortcuts for common actions
  * Follow platform conventions; never override browser or OS shortcuts
* Smart defaults and prefilling from what the system already knows or can infer: the value is already in the field and editable, like any other default
* Information used daily is reachable within two interactions of where the user starts

"Does this make the routine easier for frequent users?"

### Prevent mistakes
*Why:* prevention comes first; how we handle the mistakes that still happen defines user trust.
* Inline validation before submission
* Microcopy explains user input's requirements upfront
* Confirmation dialogs for destructive actions

"What could go wrong here, and did we stop it before it happened?"

### Help recover from errors
* Always show clear next steps
* Offer path to resolution

"How do we handle mistakes?"

### Edge cases
* Never let an edge case negatively impact the common use case

"Who pays for this edge case, the 1% or the 99%?"

### Context-aware
Always design given the appropriate context. If a user has limited time for a task, make the task easy to resolve within this limited time period. If a common scenario of the software is to be used in a chaotic environment, increase the touch area size and decrease the amount of choices to be made. If a user has a great benefit from seeing a lot of information on the screen, enable the user to do so with the correct data compactness.
* Chaotic environments often have flaky connections: retries are safe

"Where is the user, on what device, with how much attention?"

## Patterns

### Layout & Navigation
Apply a consistent layout structure across the software

### Working with entities
*Guideline.* Give each entity type a unique visual (an icon + colour combination) and use it the same way throughout the software.
* Consistency enables recognition

*Why:* users scan for the visual instead of reading labels.

### System status
Every system state has a visible UI state: loading, loaded, empty or errored. The specs are in `rules.md` §4.

"Does the user know something is happening?"

### Feedback & notifications
* Toasts are for non-blocking feedback that users merely want to know. Position them so they don't block important UI.
* Use persistent signals (badges, an alerts area) for things users must deal with.
* A toast is never the only copy of actionable information.

### Modals
* Use modals for confirmations and short focused tasks that return straight to where the user came from
* Anything longer, or anything that needs other data in view, gets a page or side panel
* Every modal closes with Escape

*Why:* a modal blocks the rest of the product, so it has to earn that.

### Permissions & unavailable actions
* **Never available** (role-gated): hide it. Dead controls are clutter.
* **Temporarily unavailable** (state-gated): show it disabled and explain why. The explanation teaches the workflow.

### Data formatting
* Format dates, quantities and codes the same way everywhere
* Dates and times show or imply their timezone; relative times get an exact timestamp on hover
* Quantities always carry explicit units; table alignment is in `rules.md` §5.3

*Why:* a weight without a unit is a defect.

### Responsive layout
* Define how each layout collapses at smaller viewports, the focus should be on the most important area
* Primary actions should remain easily accessible at every breakpoint (see `rules.md` §1.1)

### Search, filtering and sorting
* Any list beyond 15 items needs search or filtering
  * Only when the list will realistically hold that many
* Show active filters as removable chips or in a human-readable sentence
* Use inline dropdowns to switch between content (switching a single variable) (e.g. "Data for [2026 ▾]")
* Preserve the filtered state across navigation within a session
* After 1 hour, don't reapply saved filters silently: offer them instead, as 'Use previous filters? [filter details] [Apply] [Dismiss]'
  * *Why:* stale filters silently hiding data are worse than losing them

### Wayfinding
* Show breadcrumbs for any view nested more than two levels deep
* The current location should always be visually distinct in navigation

### Voice & tone
* Write error and empty-state copy to be brief and helpful
* Be specific

### Visual restraint
Emphasis only works when it's scarce. This governs *how often* a device is used, never *which* colours: the palette is untouched. These are defaults: if the product's design system specifies otherwise (e.g. uppercase buttons), follow the system.
* **Case:** sentence case for headings, buttons, labels, menu items and table headers. All caps is limited to at most one kind of short label per screen (e.g. overlines), plus abbreviations and codes (PDF, GST, ORD-10482).
* **Borders:** separate with whitespace first, and use one separation method at a time (space, a divider or a surface), not all three stacked.
* **Tinted backgrounds:** use faded or pale tints only where they carry meaning (status, selection, a highlighted row), not to decorate containers, badges or sections.
* Avoid the generic "AI look": decorative gradients, glows, glassmorphism, gradient text, emoji as icons, an icon on every heading, cards nested in cards, heavy shadows, or a marketing-style hero on a working screen.

"If I removed this emphasis, would anyone lose information?"

### Motion
* Motion can be used to explain a story: indicating movement, a loading state are good examples
* Avoid animations that delay the users reaching their target (e.g. a dropdown menu with a animated transition delays action; should appear instantly)
* Avoid content-shift animations or movement of text on hover (e.g. a button slightly moving up when hovering)
* Respect the user's reduced-motion preference

## Components

### Forms
Layout, validation and input states are in `rules.md` §2.

#### Wizards
* Opt to use wizards for more complicated multi-step processes
* Main navigation (Next, Back) must always be visible in the viewport, regardless of scroll
* The main action buttons should be close to the 'actionable area' for larger viewports
* Bottom of multi-step actions or wizards should preferably be ordered exactly like this:
  `[ Back ]    whitespace   [ Cancel ]  [ Continue / Confirm ]`

### Tables
* Support sorting, pagination and row selection consistently across all tables
  * Only where the table needs them
* Bulk actions appear only when at least one row is selected, always show how many rows are selected
* Sticky headers when a table can scroll past the viewport
