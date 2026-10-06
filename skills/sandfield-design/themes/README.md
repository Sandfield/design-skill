# Themes

The Sandfield skill is **brand-agnostic**. It decides structure and behaviour. A theme decides how it looks for a given product or client.

**Client themes never live in this public repository.** Keep them in the client's project folder or in the private `sandfield-themes` repo.

## Using a theme

When the user supplies brand guidelines (a file, a URL summary or pasted text), map them onto these roles:

- **Primary:** primary actions, active navigation and the focus ring, plus the text colour used on it
- **Neutrals:** background, surface, border, text, muted text
- **Semantic:** success, warning, danger, info. These must stay distinguishable from the brand colour
- **Type:** heading and body typefaces
- **Shape:** corner radius

Rules when applying a theme:
- **Never alter the client's brand.** Don't darken, lighten or substitute their colours or fonts.
- The theme never overrides the accessibility floor. If a brand colour fails WCAG AA as text, use it only where it passes (e.g. fills behind text that does pass, large headings, accents), and flag it in your review.
- If a brand colour could be confused with a semantic colour (e.g. an orange brand vs. warning), don't change either one. Pair the semantic state with an icon and text so it never relies on colour, and flag it in your review.
- One primary colour for primary actions only. Don't spread the brand colour over every heading.

## No theme supplied

No visual direction is prescribed. The *Visual restraint* rules in `references/philosophy.md` still apply, with or without a theme.

## Theme file template

Copy this into a client project as `theme.md`:

```markdown
# <Client> theme
- Primary: #…  (use for: …)
- Text on primary: #…
- Neutrals: bg #…, surface #…, border #…, text #…, muted #…
- Semantic: success #…, warning #…, danger #…, info #…
- Fonts: heading …, body … (fallback: system-ui)
- Radius: …px
- Voice: … (e.g. direct, plain language, safety-conscious)
- Logo: <path or "text wordmark only in prototypes">
```
