# Small Screens / Big Worlds Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the personal site around the Small Screens / Big Worlds publication identity with an immersive Ops presentation and a persistent, query-addressable Direct presentation.

**Architecture:** Keep one Astro document and one URL for each piece of content. A small inline head script resolves `view` from the query string and local storage, writes `data-view` to the root element before paint, and exposes a header control that switches presentation without duplicating content. Shared components provide the orbital hero, mission navigation, project summaries, editorial taxonomy, and dual-label terminology.

**Tech Stack:** Astro 6, TypeScript in Astro frontmatter and browser scripts, semantic HTML, modern CSS, Node test runner for view-resolution helpers, Astro production build, browser-based responsive and accessibility QA.

---

## File Structure

- `src/lib/view-mode.ts`: pure view parsing and resolution helpers.
- `scripts/test-view-mode.mjs`: Node assertions for query and preference rules.
- `src/components/ViewModeToggle.astro`: accessible Ops/Direct switch.
- `src/components/Header.astro`: publication brand and dual-mode navigation.
- `src/components/OrbitMap.astro`: decorative and navigational homepage system map.
- `src/components/MissionCard.astro`: reusable project and article summary.
- `src/data/site-content.ts`: initial project, capability, and editorial taxonomy.
- `src/layouts/BaseLayout.astro`: pre-paint mode initialization and updated metadata.
- `src/styles/global.css`: tokens, shared typography, mode selectors, and accessibility.
- `src/pages/index.astro`: redesigned publication homepage.
- `src/pages/projects/index.astro`: Shipyard / Projects index.
- `src/pages/blog/index.astro`: Flight Log / Blog archive and formats.
- `src/pages/resume.astro`: mobile-led dual-presentation resume.
- `src/pages/about.astro`: revised publication and career narrative.
- `src/content.config.ts`: optional article-format schema additions.
- `README.md`: updated publication, view-mode, and writing documentation.

### Task 1: Persistent View Infrastructure

**Files:**
- Create: `src/lib/view-mode.ts`
- Create: `scripts/test-view-mode.mjs`
- Create: `src/components/ViewModeToggle.astro`
- Modify: `src/layouts/BaseLayout.astro`
- Modify: `src/components/Header.astro`
- Modify: `src/styles/global.css`
- Modify: `package.json`

- [ ] **Step 1: Add failing view-resolution assertions**

Create assertions covering valid query values, invalid query values, stored
preferences, and the Ops default:

```js
import assert from 'node:assert/strict';
import {
  parseViewMode,
  resolveViewMode,
} from '../dist-test/view-mode.js';

assert.equal(parseViewMode('direct'), 'direct');
assert.equal(parseViewMode('ops'), 'ops');
assert.equal(parseViewMode('other'), null);
assert.equal(resolveViewMode('direct', 'ops'), 'direct');
assert.equal(resolveViewMode(null, 'direct'), 'direct');
assert.equal(resolveViewMode(null, null), 'ops');
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `npm run test:view`

Expected: failure because `src/lib/view-mode.ts` and the script do not exist.

- [ ] **Step 3: Implement pure mode helpers**

Implement:

```ts
export type ViewMode = 'ops' | 'direct';

export function parseViewMode(value: string | null): ViewMode | null {
  return value === 'ops' || value === 'direct' ? value : null;
}

export function resolveViewMode(
  queryMode: string | null,
  storedMode: string | null,
): ViewMode {
  return parseViewMode(queryMode) ?? parseViewMode(storedMode) ?? 'ops';
}
```

Compile the helper into a temporary test directory in `test:view`, run the Node
assertions, and remove the temporary output after the test.

- [ ] **Step 4: Add pre-paint mode resolution**

Add an inline script in `BaseLayout.astro` that:

1. reads `new URLSearchParams(location.search).get('view')`;
2. accepts only `ops` or `direct`;
3. falls back to `localStorage.getItem('site-view')`;
4. defaults to `ops`;
5. writes `document.documentElement.dataset.view`;
6. persists a valid query selection;
7. catches storage failures without blocking rendering.

Keep canonical metadata based on `Astro.url.pathname` so query parameters do not
create duplicate canonical pages.

- [ ] **Step 5: Add the accessible switch**

Render two real buttons in `ViewModeToggle.astro` within a group labelled
`Site presentation`. The client script must update `data-view`,
`aria-pressed`, local storage, and the current URL's `view` parameter using
`history.replaceState`.

- [ ] **Step 6: Add minimal dual-mode tokens**

Define shared functional colors and `[data-view='direct']` overrides. Ensure the
page remains legible before scripts execute and under `prefers-reduced-motion`.

- [ ] **Step 7: Verify infrastructure**

Run:

```bash
npm run test:view
npm run build
```

Expected: all assertions pass and Astro completes without errors.

- [ ] **Step 8: Commit**

```bash
git add package.json scripts/test-view-mode.mjs src/lib/view-mode.ts \
  src/components/ViewModeToggle.astro src/components/Header.astro \
  src/layouts/BaseLayout.astro src/styles/global.css
git commit -m "Add persistent Ops and Direct site views"
```

### Task 2: Publication Shell and Homepage

**Files:**
- Create: `src/components/OrbitMap.astro`
- Create: `src/components/MissionCard.astro`
- Create: `src/data/site-content.ts`
- Modify: `src/components/Header.astro`
- Modify: `src/components/Footer.astro`
- Modify: `src/pages/index.astro`
- Modify: `src/styles/global.css`

- [ ] **Step 1: Add shared content data**

Define typed records for the four homepage systems:

```ts
export const systems = [
  { id: 'mobile', opsLabel: 'Native Mobile', directLabel: 'Mobile Engineering', status: 'Flight proven' },
  { id: 'react', opsLabel: 'Product Systems', directLabel: 'React and React Native', status: 'Flight proven' },
  { id: 'games', opsLabel: 'Game Lab', directLabel: 'Game Development', status: 'Under construction' },
  { id: 'rigor', opsLabel: 'Systems Rigor', directLabel: 'Security and Architecture', status: 'Embedded discipline' },
] as const;
```

- [ ] **Step 2: Build the semantic orbital map**

Use an ordinary list of links as the source markup. Apply orbital positioning
only in Ops mode and at wide breakpoints. In Direct mode and narrow layouts,
render it as a conventional capability list.

- [ ] **Step 3: Build reusable mission summaries**

`MissionCard.astro` accepts literal and themed labels, title, summary, status,
and URL. It must not depend on the current mode in JavaScript; CSS selects the
appropriate visible label.

- [ ] **Step 4: Rebuild the homepage**

Use the approved copy:

```text
Small Screens / Big Worlds
Software for small screens and big worlds.
```

Lead with native mobile and React products. Present game development as a new
trajectory and AI as part of the toolkit. Include the current experiment,
selected missions, and latest posts.

- [ ] **Step 5: Verify first-viewport and responsive behavior**

Run the dev server and inspect:

- 1440 x 1000 Ops
- 1440 x 1000 Direct
- 390 x 844 Ops
- 390 x 844 Direct

Expected: publication name, headline, action, and next-section hint remain
visible; no overlap or horizontal overflow occurs.

- [ ] **Step 6: Commit**

```bash
git add src/components/OrbitMap.astro src/components/MissionCard.astro \
  src/data/site-content.ts src/components/Header.astro \
  src/components/Footer.astro src/pages/index.astro src/styles/global.css
git commit -m "Rebrand homepage as Small Screens Big Worlds"
```

### Task 3: Projects and Editorial Taxonomy

**Files:**
- Create: `src/pages/projects/index.astro`
- Modify: `src/pages/blog/index.astro`
- Modify: `src/content.config.ts`
- Modify: `src/styles/global.css`
- Modify: `README.md`

- [ ] **Step 1: Add article format metadata**

Extend the blog schema with an optional enum:

```ts
format: z.enum([
  'system-deep-dive',
  'flight-log',
  'postmortem',
  'cross-system-test',
]).optional()
```

Existing posts must continue building without modification.

- [ ] **Step 2: Build the projects index**

Create sections for Native Mobile, React and React Native, Frontend and Product
Systems, and Game Lab. Use honest status language and avoid invented client
outcomes or project metrics.

- [ ] **Step 3: Reframe the blog archive**

Keep existing posts. Add format descriptions and filters that degrade to normal
links or a complete list without JavaScript. Use `Flight Log / Blog` in Ops and
`Writing` in Direct.

- [ ] **Step 4: Update author documentation**

Document the four formats, editorial percentages, initial article sequence, and
frontmatter field in `README.md`.

- [ ] **Step 5: Verify**

Run:

```bash
npm run build
```

Expected: all old blog URLs build and the new projects route appears in output.

- [ ] **Step 6: Commit**

```bash
git add src/pages/projects/index.astro src/pages/blog/index.astro \
  src/content.config.ts src/styles/global.css README.md
git commit -m "Add project shipyard and editorial taxonomy"
```

### Task 4: Resume and About Repositioning

**Files:**
- Modify: `src/pages/resume.astro`
- Modify: `src/pages/about.astro`
- Modify: `src/styles/global.css`

- [ ] **Step 1: Reorder resume positioning**

Lead with mobile engineering, connected products, React/React Native, technical
leadership, and frontend architecture. Keep factual employment history and
security achievements. Describe games only as a current learning focus.

- [ ] **Step 2: Implement dual resume presentation**

Ops mode uses Crew File terminology and telemetry framing. Direct mode exposes a
compact professional heading, capability summary, chronological experience, and
selected writing without decorative map elements.

- [ ] **Step 3: Rewrite About**

Explain Small Screens / Big Worlds, the move toward game development, practical
AI use, leadership experience, and security as an embedded discipline.

- [ ] **Step 4: Verify print and narrow layouts**

Check Direct resume at desktop, mobile, and print preview. Expected: readable
chronology, no clipped content, and no decorative backgrounds consuming ink.

- [ ] **Step 5: Commit**

```bash
git add src/pages/resume.astro src/pages/about.astro src/styles/global.css
git commit -m "Reposition resume and about around mobile product work"
```

### Task 5: Accessibility, Motion, and Final Visual QA

**Files:**
- Modify: `src/styles/global.css`
- Modify: affected components from Tasks 1-4
- Create: `docs/qa/small-screens-big-worlds-qa.md`

- [ ] **Step 1: Run automated production checks**

Run:

```bash
npm run test:view
npm run build
```

Expected: both commands pass.

- [ ] **Step 2: Keyboard-test both modes**

Verify header navigation, view switch, orbital links, project links, blog links,
and footer links in source order with visible focus.

- [ ] **Step 3: Test reduced motion**

Emulate `prefers-reduced-motion: reduce`. Expected: orbital and status motion
stops without hiding content or state.

- [ ] **Step 4: Test query-addressable Direct mode**

Open:

```text
/?view=direct
/resume?view=direct
/blog?view=direct
/projects?view=direct
```

Expected: each paints Direct mode immediately, persists the preference, and has
a canonical URL without the query string.

- [ ] **Step 5: Record visual fidelity ledger**

Document concept evidence, browser evidence, mismatches, fixes, desktop/mobile
viewports, contrast checks, and intentional deviations in
`docs/qa/small-screens-big-worlds-qa.md`.

- [ ] **Step 6: Commit**

```bash
git add src docs/qa/small-screens-big-worlds-qa.md
git commit -m "Complete redesign accessibility and visual QA"
```

