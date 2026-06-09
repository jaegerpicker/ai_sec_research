# Small Screens / Big Worlds QA

Date: June 9, 2026

## Scope

Final QA for the redesign tracked by issue #86:

- Ops and Direct presentation modes
- Home, Projects, Blog, Resume, About, and article routes
- desktop and mobile layouts
- keyboard and semantic accessibility
- contrast
- reduced motion
- query-addressable Direct links
- canonical URLs
- Direct resume printing
- Giscus presentation synchronization

## Automated Checks

Commands:

```bash
npm run test:a11y
npm run test:profile
npm run test:editorial
npm run test:shell
npm run test:view
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

All checks pass. The production build generates ten pages, including
`/projects`, all existing blog URLs, `/resume`, and `/about`.

## Route Matrix

The following links were loaded with `?view=direct`:

- `/`
- `/projects`
- `/blog`
- `/resume`
- `/about`
- `/blog/welcome`

For every route:

- `data-view` resolved to `direct`;
- the Direct toggle reported `aria-pressed="true"`;
- exactly one `main` landmark and one `h1` were present;
- document width did not exceed viewport width;
- the canonical URL excluded `?view=direct`.

The article route initialized Giscus with its light theme. Switching to Ops
updated the site mode, URL, selected toggle state, and sent the Giscus theme
configuration to its iframe.

## Keyboard and Spatial Navigation

The Ops homepage exposed 20 visible native interactive controls, including four
ordinary links beneath the orbital presentation and two real mode buttons.
Every visible control:

- had a non-negative tab index;
- accepted focus;
- had non-zero dimensions;
- remained available without relying on pointer coordinates.

Global `:focus-visible` styling supplies a two-pixel contrasting outline.
The orbit graphic is `aria-hidden`; the semantic link list carries navigation.

## Contrast

Measured representative foreground/background contrast:

| Surface | Ops | Direct |
| --- | ---: | ---: |
| Body text | 17.50:1 | 14.98:1 |
| Muted body copy | 9.52:1 | 5.85:1 |
| Kicker text | 9.42:1 | 4.50:1 |
| Primary action | 9.42:1 | 4.95:1 |

All tested combinations meet WCAG AA. Direct kicker text is exactly at the
4.50:1 normal-text threshold; future palette changes must not reduce it.

## Reduced Motion

Chromium was launched with `prefers-reduced-motion: reduce`.

- the media query matched;
- transition and animation durations resolved to `0.01ms`;
- orbital links and all page content remained visible.

## Responsive Review

Reviewed at:

- 1440 x 1000 Ops
- 1440 x 1000 Direct
- 390 x 844 Ops
- 390 x 844 Direct

Pages inspected: Home, Projects, Blog, Resume, and About.

No clipped headings, incoherent overlap, or horizontal overflow remained.
On narrow screens, the orbital layout becomes a conventional vertical link
list. Direct resume content collapses to one column.

## Print Review

Chrome's print engine rendered `/resume?view=direct` to a six-page US Letter
PDF.

- site header and footer were removed;
- decorative orbital elements and dark backgrounds were removed;
- text rendered black on white;
- the first page contained the complete professional profile and summary;
- capability and role cards avoided internal page breaks.

## Fidelity Ledger

| Comparison point | Accepted concept | Final implementation | Result |
| --- | --- | --- | --- |
| Brand | Small Screens / Big Worlds by Shawn Campbell | Same publication and explicit author identity | Match |
| Headline | Software for small screens and big worlds | Exact retained headline | Match |
| Layout | Large left headline with orbital system map | Same two-column Ops composition | Match |
| Palette | dark shipboard surface, cyan, amber, coral, green | same functional palette; restrained Direct light palette | Match |
| Navigation | Shipyard, Flight Log, Crew File, About, mode switch | Shipyard, Blog, Resume, About, mode switch | Intentional usability adjustment |
| Mission system | mobile proven, games under construction, AI experimental | mobile/product proven, games under construction, security embedded | Updated to approved content hierarchy |
| First viewport | hero plus visible next-section edge | mission board visible at desktop fold | Match |
| Direct mode | conventional, recruiter-scannable presentation | same URLs and semantic content with compact layout | Match |
| Mobile | stable vertical collapse | orbit replaced by ordinary links; no overflow | Match |

## Defects Found and Fixed

1. Direct mobile resume inherited the desktop two-column override after the
   mobile breakpoint. A later Direct breakpoint now restores one column.
2. Giscus was permanently configured for dark mode. It now initializes from
   the active presentation and responds to `site-view-change`.

## Intentional Deviations

- The production header uses literal `Blog` and `Resume` labels rather than
  `Flight Log` and `Crew File`. The themed terminology remains inside page
  headings, while the global navigation stays immediately recognizable.
- The homepage map uses Security and Architecture as an embedded discipline
  instead of a separate AI-workflows node, reflecting the final approved
  content strategy.
- Direct mode uses a light presentation. It remains the same semantic document,
  not a separately maintained site.

## Result

The implementation is faithful to the approved hybrid concept and meets the
issue #88 acceptance criteria. No material visual, accessibility, responsive,
or mode-selection defects remain.
