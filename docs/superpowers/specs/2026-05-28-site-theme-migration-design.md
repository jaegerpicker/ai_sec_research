# Site Theme Migration Design

## Goal

Migrate the site from the current minimal light/dark blog theme to a dark-only
sci-fi operations theme based on the approved `/resume` visual prototype. The
result should make the whole site feel cohesive while preserving readability for
long-form AI security writing.

## Source Direction

Use the `/resume` page as the visual reference:

- Dark navy and steel base
- Thin cyan panel borders
- Amber status labels and accents
- Compact mono metadata
- Subtle grid or tactical background texture
- Dense but readable operational panels

The theme should be original and inspired by hard sci-fi operational interfaces.
Do not use copyrighted names, logos, imagery, or direct reproduction of any
specific show's interface.

## Accessibility Requirements

The site is dark-only, but accessibility is a hard requirement:

- Body copy must use high-contrast off-white text on dark backgrounds.
- Muted text must remain readable and should not rely on very low-contrast gray.
- Links must be visually distinguishable from body text and have hover/focus
  states.
- Keyboard focus states must be obvious on all interactive elements.
- Long-form blog posts must keep comfortable line length and spacing.
- Code blocks, inline code, blockquotes, and tables must remain legible.
- Avoid tiny metadata that drops below readable contrast or size.
- Avoid decorative effects that obscure text or create visual noise.

## Recommended Approach

Use a moderate-density global theme migration:

- Promote shared colors, spacing, borders, and panel styles into
  `src/styles/global.css`.
- Update the shared shell components so every page gets the same command-bar
  framing.
- Keep blog posts optimized for reading rather than turning every paragraph into
  a dense UI panel.
- Keep resume-specific layout rules local, but remove duplicated theme rules once
  global tokens can carry the look.

This balances identity with readability. It avoids both extremes: a noisy full
dashboard treatment on every page, and a too-subtle color-only skin.

## Global Shell

### Background

Use a dark-only background. Remove the light theme token set and the
`prefers-color-scheme` branch for base colors.

The background should combine:

- Near-black/navy base
- Subtle radial glow, restrained enough not to read as a gradient-orb design
- Fine grid overlay that does not interfere with text

### Layout Width

Change the default page width from the narrow `720px` blog shell to a wider
site shell around `960px` to `1120px`, depending on surface:

- General pages can use the wider shell.
- Long-form article content should remain constrained to a comfortable reading
  measure inside that shell.
- Resume keeps its wider dossier layout.

### Header

Update `src/components/Header.astro` to become a command bar:

- Wider max-width aligned with the global shell
- Brand on the left in mono text
- Navigation on the right
- Thin cyan bottom border
- Amber or cyan hover/focus states
- Mobile wrapping without overlap

### Footer

Update `src/components/Footer.astro` to read as a low-key status strip:

- Thin top border
- Muted but readable text
- Optional mono treatment
- No extra feature text or decorative clutter

## Typography

Use the existing system font stack, but tune color, spacing, and hierarchy:

- Body text: high-contrast off-white
- Muted text: blue-gray with sufficient contrast
- Headings: crisp off-white
- Mono labels: amber or cyan, uppercase only where it adds metadata structure
- Letter spacing remains `0` for readability

Avoid using hero-scale type inside compact cards, lists, and post bodies.

## Shared Elements

Global CSS should define reusable low-level patterns without over-abstracting:

- Panel background and border tokens
- Link and focus states
- Code block treatment
- Inline code treatment
- Table and blockquote styling
- Utility muted class

Do not add a component system or CSS framework.

## Page Treatment

### Homepage

Convert the homepage into a mission panel plus latest-post signal list:

- Primary panel explains the site as AI security research and lab notes.
- Latest posts appear as compact signal cards with title and description.
- Keep the first screen useful, not a marketing landing page.

### Blog Index

Convert the blog index into a list of signal cards:

- Each post card includes title, date, and description.
- Cards should be scan-friendly and not overly decorative.
- The layout should collapse cleanly on mobile.

### Blog Posts

Keep blog posts reading-first:

- Add a dossier-style post header with title, date, description, and tags when
  available.
- Keep prose width comfortable.
- Style code blocks, blockquotes, and tables with the global theme.
- Avoid putting the entire article body in a card inside another card.

### About Page

Convert the about page into a compact profile/status page:

- Short profile copy
- Links to GitHub and the blog
- Visual treatment aligned with global panels

### Resume Page

Keep the resume page as the most expressive version of the theme:

- Preserve the mission-dossier layout.
- Remove duplicated local background, color, and broad token definitions where
  global CSS now owns them.
- Keep resume-only layout rules such as capability grids, role cards, and hero
  telemetry layout.

## Implementation Boundaries

The implementation should:

- Update global CSS and shared layout components.
- Update homepage, blog index, blog post layout, about page, and resume styles.
- Keep route behavior and content semantics unchanged unless styling requires
  minor markup structure.
- Preserve `import.meta.env.BASE_URL` handling for internal links.
- Keep the site static and dependency-free beyond existing Astro dependencies.

The implementation should not:

- Add JavaScript-only visual effects.
- Add new design libraries.
- Add copyrighted assets or show-specific references.
- Rewrite blog content.
- Implement the interactive lab lesson system.
- Build a presentation deck.

## Validation

Implementation should be validated with:

- `ASTRO_TELEMETRY_DISABLED=1 npm run build`
- `git diff --check`
- Browser inspection of homepage, blog index, one blog post, about, and resume
  at desktop and mobile widths
- Checks for horizontal overflow on mobile
- Checks that header navigation wraps without overlap
- Basic contrast review for body text, muted text, links, focus states, and code
  blocks

## Follow-Up Work

After this migration, the next planned work should be the blog and presentation
synthesis pass across the completed OWASP LLM modules. The interactive lab
lesson system remains deferred until lab, blog, and presentation work are
complete.
