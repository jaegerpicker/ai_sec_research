# Small Screens / Big Worlds Design

## Purpose

Reposition the site from an AI-security publication to a personal technical
publication led by mobile and product engineering. React and React Native remain
major supporting disciplines. Game development is presented as an active,
serious learning trajectory in Godot and Unreal Engine. AI is treated as a
practical development tool, while security remains visible as an engineering
quality rather than a separate site identity.

The summit presentation work is paused and does not appear in the redesigned
homepage narrative.

## Brand

The primary publication identity is **Small Screens / Big Worlds**.

Shawn Campbell remains explicit in the header, metadata, resume, and author
information. The site is not presented as a fictional company or anonymous
studio.

The retained homepage headline is:

> Software for small screens and big worlds.

Supporting copy describes native mobile systems, React products, game
development, AI-assisted workflows, and engineering leadership without
overstating current game-development experience.

## Audience Priority

1. Engineers and technical peers
2. Hiring managers and recruiters
3. Conference and blog readers

Mobile and product engineering lead the first viewport. Game development is
clearly identified as a growing body of work. Security appears as systems rigor
inside case studies, articles, and resume content.

## Visual Direction

The default presentation is an immersive, playful, hard-science-fiction
operations interface:

- dark shipboard surfaces;
- cyan, amber, coral, and green functional accents;
- orbital navigation and mission-board compositions;
- condensed display typography paired with readable sans-serif body text;
- monospaced interface labels;
- sharp or lightly rounded industrial geometry;
- playful status language, easter eggs, and system feedback;
- real project screenshots and playable artifacts as the main visual evidence.

The design is inspired by utilitarian spacecraft interfaces without copying
franchise logos, characters, names, or exact screen designs.

Decorative telemetry must not replace meaningful project content. Scanlines,
noise, and animation cannot run over body text.

## View Modes

The site has two presentations of the same semantic content.

### Ops

`Ops` is the default presentation. It uses immersive layouts and playful
shipboard terminology:

- Shipyard / Projects
- Flight Log / Blog
- Crew File / Resume
- Mission Map / Home

Every themed label includes a literal companion in accessible text or nearby
copy.

### Direct

`Direct` presents conventional navigation, compact typography, scannable
project summaries, standard resume language, and reduced decorative UI. It is
intended for recruiters, hiring managers, and readers who want immediate access
to evidence.

Direct mode is not a separate site. Both modes use identical URLs, source
content, document semantics, metadata, and functionality.

### Selection Contract

View resolution order:

1. `?view=direct` or `?view=ops`
2. a saved local preference
3. `Ops`

A valid query parameter updates the saved preference. The header switch updates
the saved preference and current document without changing the content URL.
Invalid query values are ignored.

Examples:

- `https://sandkcampbell.com/?view=direct`
- `https://sandkcampbell.com/resume?view=direct`
- `https://sandkcampbell.com/blog/example?view=direct`

Canonical URLs omit the query parameter. An inline head script resolves the mode
before first paint to avoid a flash of the wrong presentation. The page remains
usable when JavaScript or local storage is unavailable.

## Information Architecture

### Home

- publication identity and retained headline;
- mobile/product positioning;
- orbital map of native mobile, React products, game development, and systems
  rigor;
- selected project missions;
- current game-development experiment;
- latest writing;
- direct-mode shortcut.

### Projects

The Shipyard / Projects page groups work into:

- Native Mobile
- React and React Native
- Frontend and Product Systems
- Game Lab

Each case study should show role, constraints, decisions, implementation,
outcome, screenshots or playable evidence, and lessons learned. Game projects
must clearly distinguish completed experience from active learning.

### Blog

The Flight Log / Blog supports four formats:

- System Deep Dives
- Flight Logs
- Postmortems
- Cross-System Tests

Editorial emphasis:

- 50% mobile and product engineering;
- 20% AI-assisted development;
- 20% game-development field logs;
- 10% security and systems rigor.

Existing security articles remain in the main archive and are categorized as
systems-under-stress material.

### Resume

The Crew File / Resume prioritizes:

- mobile and connected-product engineering;
- React and React Native leadership;
- frontend architecture;
- technical leadership and team building;
- security as an embedded engineering discipline;
- game development as a current learning focus, not established expertise.

Direct mode must read as a conventional professional resume suitable for a job
application link.

### About

The About page explains the publication, Shawn's engineering background, the
current game-development trajectory, and the role of AI in the development
workflow.

## Initial Editorial Backlog

Recommended first publication sequence:

1. Building the Same Feature in SwiftUI, Jetpack Compose, and React Native
2. What AI Coding Agents Get Wrong About Mobile Apps
3. Learning Godot as a Mobile Systems Engineer
4. Offline-First Sync Without Lying to the User

Additional topics:

- Cross-Platform Without Lowest-Common-Denominator Design
- The Mobile App Lifecycle Is Part of Your Architecture
- Building My First Complete Gameplay Loop in Godot
- The Same Mechanic in Godot and Unreal
- What Product Engineers Have to Unlearn When Building Games
- Using AI for Game Prototypes Without Surrendering Art Direction
- Can an AI Agent Build a Feature That Survives Real Device Testing?
- Security Is Product Quality: Permissions, Storage, and Trust

## Accessibility

- Meet WCAG AA contrast requirements in both modes.
- Respect `prefers-reduced-motion`.
- Maintain a clear visible focus state.
- Make orbital navigation keyboard accessible.
- Provide conventional link alternatives to all spatial navigation.
- Never use color as the only state indicator.
- Keep body copy free from scanlines and moving visual effects.
- Preserve semantic heading order and landmarks in both modes.
- Ensure the view switch has an accessible name and selected-state semantics.
- Keep content available if JavaScript, storage, or animation is unavailable.

## Responsive Behavior

The first viewport must preserve the publication name, headline, primary action,
and a hint of the next section on desktop and mobile. Orbital content collapses
into a stable vertical mission list on narrow screens. Navigation remains
conventional enough to operate without understanding the theme.

## Success Criteria

- A recruiter can open any page with `?view=direct` and immediately understand
  Shawn's experience and current focus.
- A technical reader sees mobile authority before game-development ambition.
- Ops mode is memorable, playful, and substantially more immersive than the
  current site.
- Existing security posts and research remain reachable and credible.
- Both modes pass keyboard, responsive, reduced-motion, and contrast checks.
- The production build contains no duplicate mode-specific content pages.

