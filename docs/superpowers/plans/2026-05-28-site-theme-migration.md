# Site Theme Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved dark-only sci-fi operations theme across the Astro site while preserving readability and static behavior.

**Architecture:** Promote the `/resume` visual language into global CSS tokens and shared shell components first, then update each page surface to use those global primitives. Keep blog posts reading-first, keep resume layout-specific rules local, and validate the final theme in browser at desktop and mobile widths.

**Tech Stack:** Astro 6 static site, existing Astro layouts/components, route-local Astro styles, global CSS in `src/styles/global.css`, no new dependencies.

---

## File Structure

- Modify `src/styles/global.css`: Own dark-only color tokens, background, grid texture, layout widths, typography, links, focus states, code, tables, blockquotes, reusable panel/card utilities, and post prose helpers.
- Modify `src/components/Header.astro`: Convert the header to a command bar using global tokens and a wider shell.
- Modify `src/components/Footer.astro`: Convert the footer to a status strip.
- Modify `src/pages/index.astro`: Convert homepage to a mission panel plus latest-post signal cards.
- Modify `src/pages/blog/index.astro`: Convert blog index to signal-card post list.
- Modify `src/layouts/BlogPost.astro`: Add a dossier-style post header and prose container while keeping long-form readability.
- Modify `src/pages/about.astro`: Convert about page to a compact profile/status panel.
- Modify `src/pages/resume.astro`: Remove duplicated local theme/background/token rules and keep only resume-specific layout rules.

No new dependencies, no content rewrites, no global component framework.

---

### Task 1: Global Theme Tokens and Base Styles

**Files:**
- Modify: `src/styles/global.css`

- [ ] **Step 1: Replace the global CSS with dark-only theme foundations**

Use `apply_patch` to replace `src/styles/global.css` with the CSS below.

```css
:root {
  --font-sans: ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-mono: ui-monospace, 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace;

  --bg: #07111b;
  --bg-deep: #050a11;
  --bg-panel: rgba(12, 25, 36, 0.84);
  --bg-panel-strong: rgba(15, 33, 48, 0.94);
  --bg-subtle: rgba(94, 218, 231, 0.08);
  --fg: #eef7fb;
  --fg-muted: #a9bac5;
  --fg-subtle: #7f98a8;
  --border: rgba(94, 218, 231, 0.28);
  --border-strong: rgba(94, 218, 231, 0.58);
  --accent: #5edae7;
  --accent-strong: #8cf2ff;
  --warning: #e4ad54;
  --warning-strong: #ffd88f;
  --link: #8cf2ff;
  --link-hover: #ffd88f;
  --focus: #ffd88f;
  --code-bg: rgba(5, 10, 17, 0.86);
  --shell-width: 1080px;
  --article-width: 760px;
  --panel-shadow: 0 20px 70px rgba(0, 0, 0, 0.26);
}

* {
  box-sizing: border-box;
}

html {
  font-family: var(--font-sans);
  background: var(--bg-deep);
  color: var(--fg);
  -webkit-font-smoothing: antialiased;
}

body {
  min-height: 100vh;
  margin: 0;
  background:
    radial-gradient(circle at 76% 10%, rgba(73, 210, 224, 0.1), transparent 26rem),
    linear-gradient(135deg, var(--bg) 0%, #101923 48%, var(--bg-deep) 100%);
  color: var(--fg);
  font-size: 17px;
  line-height: 1.65;
}

body::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(94, 218, 231, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(94, 218, 231, 0.05) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.72), transparent 82%);
}

main {
  width: min(var(--shell-width), calc(100% - 2rem));
  max-width: none;
  margin: 0 auto;
  padding: 2rem 0 4rem;
}

a {
  color: var(--link);
  text-decoration: none;
}

a:hover {
  color: var(--link-hover);
  text-decoration: underline;
}

a:focus-visible,
button:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 4px;
}

h1,
h2,
h3,
h4 {
  color: var(--fg);
  line-height: 1.18;
  margin: 2rem 0 0.75rem;
}

h1 {
  font-size: clamp(2.2rem, 7vw, 4.6rem);
}

h2 {
  font-size: clamp(1.4rem, 3vw, 2rem);
}

h3 {
  font-size: 1.12rem;
}

p,
ul,
ol {
  margin: 0 0 1rem;
}

code {
  border: 1px solid rgba(94, 218, 231, 0.2);
  background: var(--code-bg);
  color: #f5d390;
  font-family: var(--font-mono);
  font-size: 0.9em;
  padding: 0.15em 0.35em;
  border-radius: 4px;
}

pre {
  border: 1px solid var(--border);
  background: var(--code-bg);
  color: var(--fg);
  font-family: var(--font-mono);
  font-size: 0.86em;
  line-height: 1.55;
  overflow-x: auto;
  padding: 1rem;
  border-radius: 0;
}

pre code {
  border: 0;
  background: transparent;
  color: inherit;
  padding: 0;
}

.astro-code,
.astro-code span {
  color: var(--shiki-dark, inherit) !important;
  background-color: var(--shiki-dark-bg, transparent) !important;
  font-style: var(--shiki-dark-font-style, inherit) !important;
  font-weight: var(--shiki-dark-font-weight, inherit) !important;
  text-decoration: var(--shiki-dark-text-decoration, inherit) !important;
}

blockquote {
  border-left: 3px solid var(--warning);
  margin: 1.25rem 0;
  padding: 0.4rem 1rem;
  color: var(--fg-muted);
  background: rgba(228, 173, 84, 0.06);
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.25rem 0;
}

th,
td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.75rem;
  text-align: left;
}

th {
  background: var(--bg-subtle);
  color: var(--fg);
}

hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 2rem 0;
}

img {
  max-width: 100%;
  height: auto;
}

.muted {
  color: var(--fg-muted);
}

.panel {
  border: 1px solid var(--border);
  background:
    linear-gradient(135deg, rgba(94, 218, 231, 0.08), transparent 16rem),
    var(--bg-panel);
  box-shadow: var(--panel-shadow);
}

.kicker {
  margin: 0 0 0.65rem;
  color: var(--warning);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.signal-card {
  display: grid;
  gap: 0.45rem;
  border: 1px solid var(--border);
  background:
    linear-gradient(135deg, rgba(94, 218, 231, 0.08), transparent 14rem),
    var(--bg-panel);
  color: inherit;
  padding: 1rem;
  text-decoration: none;
}

.signal-card:hover,
.signal-card:focus-visible {
  border-color: var(--border-strong);
  color: var(--fg);
  text-decoration: none;
  box-shadow: 0 0 0 3px rgba(94, 218, 231, 0.13);
}

.signal-card__label {
  color: var(--warning);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
}

.signal-card__title {
  color: var(--fg);
  font-weight: 700;
  line-height: 1.3;
}

.signal-card__meta {
  color: var(--fg-muted);
  font-family: var(--font-mono);
  font-size: 0.82rem;
}

.prose {
  max-width: var(--article-width);
}

.prose > :first-child {
  margin-top: 0;
}

@media (max-width: 720px) {
  body {
    font-size: 16px;
  }

  main {
    width: min(100% - 1rem, var(--shell-width));
    padding-top: 1rem;
  }
}
```

- [ ] **Step 2: Build after the global CSS replacement**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: build exits 0.

- [ ] **Step 3: Commit Task 1**

Run:

```bash
git add src/styles/global.css
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Add global sci-fi ops theme tokens"
```

Expected: signed commit containing only `src/styles/global.css`.

---

### Task 2: Shared Header and Footer Shell

**Files:**
- Modify: `src/components/Header.astro`
- Modify: `src/components/Footer.astro`

- [ ] **Step 1: Replace `Header.astro` style block**

Keep the existing frontmatter and markup. Replace only the `<style>` block in
`src/components/Header.astro` with:

```astro
<style>
  header {
    border-bottom: 1px solid var(--border);
    background: rgba(5, 10, 17, 0.72);
    backdrop-filter: blur(14px);
  }

  nav {
    width: min(var(--shell-width), calc(100% - 2rem));
    margin: 0 auto;
    padding: 0.9rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }

  .brand {
    color: var(--fg);
    font-family: var(--font-mono);
    font-weight: 700;
  }

  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: 0.35rem 0.9rem;
  }

  a {
    color: var(--link);
  }

  a:hover,
  a:focus-visible {
    color: var(--warning-strong);
  }

  @media (max-width: 620px) {
    nav {
      width: min(100% - 1rem, var(--shell-width));
      align-items: flex-start;
      flex-direction: column;
    }

    ul {
      justify-content: flex-start;
    }
  }
</style>
```

- [ ] **Step 2: Replace `Footer.astro` style block**

Keep existing frontmatter and markup. Replace only the `<style>` block in
`src/components/Footer.astro` with:

```astro
<style>
  footer {
    border-top: 1px solid var(--border);
    background: rgba(5, 10, 17, 0.62);
    color: var(--fg-muted);
    font-family: var(--font-mono);
    font-size: 0.82rem;
    padding: 1.25rem 1rem;
    text-align: center;
  }

  footer p {
    margin: 0;
  }

  footer a {
    color: var(--link);
  }

  footer a:hover,
  footer a:focus-visible {
    color: var(--warning-strong);
  }
</style>
```

- [ ] **Step 3: Build and inspect generated navigation**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
rg -n 'href="/resume".*>Resume' dist/index.html dist/blog/index.html dist/resume/index.html
```

Expected: build exits 0 and `rg` finds Resume nav links in all three files.

- [ ] **Step 4: Commit Task 2**

Run:

```bash
git add src/components/Header.astro src/components/Footer.astro
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Update shared command shell"
```

Expected: signed commit containing only header and footer changes.

---

### Task 3: Homepage and Blog Index Page Treatments

**Files:**
- Modify: `src/pages/index.astro`
- Modify: `src/pages/blog/index.astro`

- [ ] **Step 1: Replace homepage markup and styles**

In `src/pages/index.astro`, keep the frontmatter. Replace the content inside
`<BaseLayout title="ai-sec-research">` and the route-local `<style>` block with:

```astro
<BaseLayout title="ai-sec-research">
  <section class="home-hero panel">
    <p class="kicker">AI Security Research / Field Notes</p>
    <h1>ai-sec-research</h1>
    <p class="mission-copy">
      Notes on AI security, red teaming, and the attack surface of agentic systems.
      Maintained by Shawn Campbell. Written to think clearly about what breaks,
      what defends, and what evidence survives contact with real systems.
    </p>
    <p class="hero-link">
      <a href={`${base}/blog`}>Read the blog</a>
    </p>
  </section>

  {posts.length > 0 && (
    <section class="latest-section" aria-labelledby="latest-heading">
      <p class="kicker">Latest Signals</p>
      <h2 id="latest-heading">Recent Notes</h2>
      <div class="post-grid">
        {posts.map((post) => (
          <a class="signal-card" href={`${base}/blog/${post.id}`}>
            <span class="signal-card__label">Post</span>
            <span class="signal-card__title">{post.data.title}</span>
            <p class="muted">{post.data.description}</p>
          </a>
        ))}
      </div>
    </section>
  )}
</BaseLayout>

<style>
  .home-hero {
    padding: clamp(1.25rem, 4vw, 2.5rem);
  }

  .home-hero h1 {
    margin: 0;
  }

  .mission-copy {
    max-width: 48rem;
    color: var(--fg-muted);
    font-size: clamp(1.05rem, 2vw, 1.25rem);
  }

  .hero-link {
    margin-bottom: 0;
  }

  .latest-section {
    margin-top: 1.25rem;
  }

  .post-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.9rem;
  }

  @media (max-width: 760px) {
    .post-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
```

- [ ] **Step 2: Replace blog index markup and styles**

In `src/pages/blog/index.astro`, keep the frontmatter. Replace the
`<BaseLayout ...>` block and style block with:

```astro
<BaseLayout title="Blog — ai-sec-research" description="All posts">
  <section class="blog-index panel">
    <p class="kicker">Signal Archive</p>
    <h1>Blog</h1>
    <p class="muted">
      Field notes, lab writeups, and practical analysis from AI security work.
    </p>
  </section>

  {posts.length === 0 ? (
    <p class="muted">No posts yet.</p>
  ) : (
    <div class="post-list">
      {posts.map((post) => (
        <a class="signal-card" href={`${base}/blog/${post.id}`}>
          <span class="signal-card__label">
            {post.data.draft ? 'Draft' : 'Post'}
          </span>
          <span class="signal-card__title">{post.data.title}</span>
          <time class="signal-card__meta" datetime={post.data.pubDate.toISOString()}>
            {dateFmt.format(post.data.pubDate)}
          </time>
          <p class="muted">{post.data.description}</p>
        </a>
      ))}
    </div>
  )}
</BaseLayout>

<style>
  .blog-index {
    margin-bottom: 1rem;
    padding: clamp(1.25rem, 3vw, 2rem);
  }

  .blog-index h1 {
    margin: 0 0 0.75rem;
  }

  .blog-index p {
    max-width: 42rem;
    margin-bottom: 0;
  }

  .post-list {
    display: grid;
    gap: 0.9rem;
  }
</style>
```

- [ ] **Step 3: Build**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: build exits 0.

- [ ] **Step 4: Commit Task 3**

Run:

```bash
git add src/pages/index.astro src/pages/blog/index.astro
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Apply theme to home and blog index"
```

Expected: signed commit containing homepage and blog index changes.

---

### Task 4: Blog Post and About Page Treatments

**Files:**
- Modify: `src/layouts/BlogPost.astro`
- Modify: `src/pages/about.astro`

- [ ] **Step 1: Replace `BlogPost.astro` layout markup and styles**

Keep the frontmatter. Replace the `<BaseLayout ...>` block and style block with:

```astro
<BaseLayout title={title} description={description}>
  <article class="post-shell">
    <header class="post-header panel">
      {draft && <p class="draft-banner">Draft - not yet published</p>}
      <p class="kicker">Field Note</p>
      <h1>{title}</h1>
      <p class="description">{description}</p>
      <p class="meta">
        <time datetime={pubDate.toISOString()}>{dateFmt.format(pubDate)}</time>
        {updatedDate && (
          <> / updated <time datetime={updatedDate.toISOString()}>{dateFmt.format(updatedDate)}</time></>
        )}
      </p>
      {tags.length > 0 && (
        <ul class="tag-list" aria-label="Post tags">
          {tags.map((t) => <li>{t}</li>)}
        </ul>
      )}
    </header>

    <div class="prose post-body">
      <slot />
    </div>
  </article>
  <Giscus />
</BaseLayout>

<style>
  .post-shell {
    display: grid;
    justify-items: center;
    gap: 1.25rem;
  }

  .post-header {
    width: min(100%, var(--article-width));
    padding: clamp(1.25rem, 3vw, 2rem);
  }

  .post-header h1 {
    margin: 0.35rem 0 0.75rem;
    font-size: clamp(2rem, 5vw, 3.4rem);
  }

  .description {
    color: var(--fg-muted);
    font-size: 1.08rem;
  }

  .meta {
    color: var(--fg-muted);
    font-family: var(--font-mono);
    font-size: 0.86rem;
  }

  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    list-style: none;
    margin: 1rem 0 0;
    padding: 0;
  }

  .tag-list li,
  .draft-banner {
    border: 1px solid rgba(228, 173, 84, 0.42);
    background: rgba(228, 173, 84, 0.08);
    color: var(--warning-strong);
    font-family: var(--font-mono);
    font-size: 0.74rem;
    font-weight: 700;
    padding: 0.25rem 0.5rem;
    text-transform: uppercase;
  }

  .draft-banner {
    display: inline-block;
    margin: 0 0 0.75rem;
  }

  .post-body {
    width: min(100%, var(--article-width));
  }
</style>
```

- [ ] **Step 2: Replace about page markup**

Replace all content in `src/pages/about.astro` with:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const base = import.meta.env.BASE_URL.replace(/\/$/, '');
---

<BaseLayout title="About — ai-sec-research" description="About Shawn Campbell and this site.">
  <section class="about-panel panel">
    <p class="kicker">Profile</p>
    <h1>About</h1>
    <p>
      I'm Shawn Campbell, a security/software engineer working on AI red teaming
      and the security of agentic systems. This site is where I publish writeups
      from my personal AI red-team lab and notes on supply-chain and
      agent-attack-surface work.
    </p>
    <nav class="about-links" aria-label="Profile links">
      <a href="https://github.com/jaegerpicker">GitHub</a>
      <a href={`${base}/blog`}>Blog</a>
      <a href={`${base}/resume`}>Resume</a>
    </nav>
  </section>
</BaseLayout>

<style>
  .about-panel {
    padding: clamp(1.25rem, 3vw, 2rem);
  }

  .about-panel h1 {
    margin: 0 0 0.75rem;
  }

  .about-panel p {
    max-width: 44rem;
    color: var(--fg-muted);
  }

  .about-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
  }

  .about-links a {
    border: 1px solid var(--border);
    color: var(--link);
    font-family: var(--font-mono);
    padding: 0.5rem 0.75rem;
    text-transform: uppercase;
  }

  .about-links a:hover,
  .about-links a:focus-visible {
    border-color: var(--border-strong);
    color: var(--warning-strong);
    text-decoration: none;
  }
</style>
```

- [ ] **Step 3: Build**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: build exits 0.

- [ ] **Step 4: Commit Task 4**

Run:

```bash
git add src/layouts/BlogPost.astro src/pages/about.astro
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Apply theme to posts and about page"
```

Expected: signed commit containing blog post layout and about page changes.

---

### Task 5: Resume Theme Cleanup

**Files:**
- Modify: `src/pages/resume.astro`

- [ ] **Step 1: Remove duplicated global theme rules from resume styles**

In `src/pages/resume.astro`, remove the route-local `:global(body)`,
`:global(body main)`, local CSS custom property definitions inside
`.resume-dossier`, and `.resume-dossier::before`. Keep the resume-specific
layout rules.

After editing, the start of the style block should look like:

```astro
<style>
  .resume-dossier {
    position: relative;
    display: grid;
    gap: 1.2rem;
    padding: 2rem 0 3rem;
  }
```

- [ ] **Step 2: Update resume panel styles to use global tokens**

Ensure the shared resume panel rule uses global tokens:

```css
  .hero-panel,
  .dossier-section,
  .contact-panel,
  .capability-card,
  .role-card,
  .signal-card {
    position: relative;
    border: 1px solid var(--border);
    background:
      linear-gradient(135deg, rgba(94, 218, 231, 0.08), transparent 16rem),
      var(--bg-panel);
    box-shadow: var(--panel-shadow);
  }
```

Ensure existing references to `var(--amber)`, `var(--cyan)`, `var(--muted)`,
`var(--line)`, and `var(--line-strong)` are replaced with global equivalents:

```text
--amber -> --warning
--cyan -> --accent
--muted -> --fg-muted
--line -> --border
--line-strong -> --border-strong
```

- [ ] **Step 3: Build**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: build exits 0 and `/resume/index.html` is generated.

- [ ] **Step 4: Commit Task 5**

Run:

```bash
git add src/pages/resume.astro
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Align resume page with global theme"
```

Expected: signed commit containing only `src/pages/resume.astro`.

---

### Task 6: Browser and Final Validation

**Files:**
- No source edits expected unless validation finds a defect.

- [ ] **Step 1: Run final build and static checks**

Run:

```bash
git diff --check
ASTRO_TELEMETRY_DISABLED=1 npm run build
rg -n 'prefers-color-scheme|#ffffff|#0969da|#fff4ce' src/styles/global.css src/components src/pages src/layouts
```

Expected:

- `git diff --check` exits 0.
- Build exits 0.
- `rg` exits 1 with no matches for removed light-theme artifacts.

- [ ] **Step 2: Start local dev server**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run dev -- --host 127.0.0.1
```

Expected: dev server reports a local URL, normally `http://127.0.0.1:4321/`.

- [ ] **Step 3: Browser inspect required routes**

Open and inspect these routes at desktop and mobile widths:

```text
http://127.0.0.1:4321/
http://127.0.0.1:4321/blog
http://127.0.0.1:4321/blog/welcome
http://127.0.0.1:4321/about
http://127.0.0.1:4321/resume
```

Expected:

- No horizontal overflow at mobile width around 390px.
- Header navigation wraps without overlap.
- Body text, muted text, links, and code blocks are readable.
- Homepage uses mission panel and signal cards.
- Blog index uses signal cards.
- Blog post has a dossier-style header and readable prose width.
- About page uses profile/status panel.
- Resume keeps its dossier layout.

- [ ] **Step 4: Basic contrast spot-check**

Using browser computed styles or visual inspection, verify:

```text
body text: high-contrast off-white on dark
muted text: readable blue-gray on dark panels
links: cyan and visually distinct
hover/focus: amber/cyan visible
code blocks: readable foreground/background
```

Expected: no low-contrast text that materially affects reading.

- [ ] **Step 5: Push and open PR**

Run:

```bash
git push -u origin issue-68-site-theme-implementation
gh pr create --title '[#68] Implement site-wide sci-fi ops theme' --body 'Closes #68

## Summary
- Promote the resume visual language into global dark-only site tokens and shared shell styling.
- Update homepage, blog index, blog post layout, about page, and resume page to use the sci-fi operations theme.
- Preserve static behavior and keep blog posts reading-first.

## Validation
- ASTRO_TELEMETRY_DISABLED=1 npm run build
- git diff --check
- Removed light-theme artifact scan
- Browser inspection of homepage, blog index, blog post, about, and resume at desktop and mobile widths
- Basic contrast spot-check for body text, muted text, links, focus states, and code blocks

## Known limitations
- This does not implement blog/presentation synthesis or the interactive lab lesson system.'
```

Expected: branch pushed and PR URL returned.

---

## Self-Review

- Spec coverage: Tasks cover global dark-only tokens, header/footer shell, homepage, blog index, blog posts, about page, resume cleanup, browser validation, mobile overflow checks, and contrast spot-checks.
- Scope check: The plan does not add dependencies, JavaScript effects, content rewrites, presentation work, or lesson-system implementation.
- Type consistency: All CSS class names introduced in markup are defined in the same route/layout or global CSS.
