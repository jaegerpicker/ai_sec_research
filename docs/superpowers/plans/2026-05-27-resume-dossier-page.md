# Resume Dossier Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the approved `/resume` mission-dossier page for Shawn Campbell and add it to site navigation.

**Architecture:** Add one Astro route with self-contained data arrays, page markup, and route-local styles so the dossier can prototype the future visual theme without changing the rest of the site. Update the existing header link list to include the new route. Validate generated HTML, privacy boundaries, and desktop/mobile rendering.

**Tech Stack:** Astro 6, static routes, route-local Astro styles, existing `BaseLayout.astro`, existing global CSS tokens.

---

## File Structure

- Create `src/pages/resume.astro`: the full resume dossier page. It imports `BaseLayout`, declares local arrays for capabilities, roles, early timeline items, and signal links, renders the page, and defines route-local sci-fi operations styling.
- Modify `src/components/Header.astro`: add a `Resume` link to the existing `links` array.
- Use existing `docs/superpowers/specs/2026-05-27-resume-dossier-design.md` as the source of truth for scope and privacy boundaries.

No shared component extraction is planned for the first pass. The route is the visual prototype; global theme migration is a later issue.

---

### Task 1: Add the Resume Route Content and Layout

**Files:**
- Create: `src/pages/resume.astro`

- [ ] **Step 1: Create `src/pages/resume.astro` with data and markup**

Use `apply_patch` to add the file below. The content rewrites the LinkedIn PDF source material around AI security, secure systems, red-team methodology, and leadership. It intentionally omits street address, phone number, and personal email.

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const capabilities = [
  {
    label: 'AI Threat Research',
    detail:
      'Researches agentic attack surfaces, OWASP LLM risks, prompt-injection paths, and practical red-team lab patterns.',
  },
  {
    label: 'Secure Systems Architecture',
    detail:
      'Designs distributed systems with threat modeling, secure API boundaries, resilient data flow, and privacy-aware defaults.',
  },
  {
    label: 'Red Team Methodology',
    detail:
      'Runs application-layer assessments, proof-of-concept exploit work, secure code review, and remediation loops with engineering teams.',
  },
  {
    label: 'Mobile and IoT Security',
    detail:
      'Brings deep Swift, Kotlin, C++, React Native, and IoT experience to mobile threat models and connected-device systems.',
  },
  {
    label: 'Cloud and Data Platforms',
    detail:
      'Builds and reviews TypeScript, Python, Go, .NET, Java, AWS, GCP, serverless, GraphQL, and data-pipeline architectures.',
  },
  {
    label: 'Engineering Leadership',
    detail:
      'Leads teams, sets standards, mentors security-minded engineers, and translates risk into practical delivery decisions.',
  },
];

const roles = [
  {
    org: 'Brivo',
    title: 'Lead Software Engineer',
    period: 'Dec 2023 - Present',
    location: 'Remote',
    bullets: [
      'Leads design and delivery for distributed, security-first platforms in smart access and IoT environments.',
      'Champions threat modeling, secure code review, CI/CD hardening, and engineering practices that reduce product risk.',
      'Connects engineering, product, and security groups around pragmatic architecture decisions.',
    ],
  },
  {
    org: 'Riffle Analytics',
    title: 'Lead AI and Mobile Engineer',
    period: 'Feb 2019 - Dec 2023',
    location: 'Portland, Maine Metropolitan Area',
    bullets: [
      'Built privacy-aware native mobile applications across Swift, Kotlin, and C++.',
      'Designed Python and Node.js data pipelines that supported machine-learning workflows while protecting user data.',
      'Created internal tooling to evaluate and improve mobile application security posture.',
    ],
  },
  {
    org: 'VividCloud',
    title: 'Principal Software Engineer 2',
    period: 'Aug 2020 - Nov 2023',
    location: 'Brunswick, Maine',
    bullets: [
      'Led multidisciplinary teams across Python, .NET, Java, and Swift projects with secure scalable architecture as the centerline.',
      'Conducted internal red-team assessments and security reviews for client systems.',
      'Partnered with DevSecOps on secure cloud infrastructure patterns and distributed-systems design.',
    ],
  },
  {
    org: 'GrowFlow Corp',
    title: 'Mobile Engineering Lead and Manager',
    period: 'May 2019 - Aug 2020',
    location: 'Remote',
    bullets: [
      'Managed and grew a cross-platform mobile team working in React Native and TypeScript.',
      'Designed GraphQL and backend service boundaries with role-based access, integrity, and resilience in mind.',
      'Introduced secure development lifecycle practices and peer security review habits.',
    ],
  },
  {
    org: 'Minnow',
    title: 'Director of Engineering, Mobile',
    period: 'Jan 2018 - Dec 2019',
    location: 'Portland, Maine Area',
    bullets: [
      'Owned mobile architecture across Swift and Kotlin while coordinating with IoT, Go, Elixir, and Python backend teams.',
      'Raised standards for mobile, hardware integration, testing, and embedded security practices.',
      'Managed contractor teams and established engineering expectations around quality and threat mitigation.',
    ],
  },
  {
    org: 'Vox Media',
    title: 'Application Security Engineer',
    period: 'Jun 2017 - Aug 2018',
    location: 'Portland, Maine Area',
    bullets: [
      'Led internal red-team operations including application-layer penetration testing, vulnerability research, and exploit prototypes.',
      'Partnered with development teams on blue-team practices including threat modeling, secure review, and infrastructure hardening.',
      'Built SecDevOps pipelines, automated security gates, and Python-based NLP/data workflows on GCP Cloud Dataflow.',
    ],
  },
  {
    org: 'Vets First Choice',
    title: 'Director of Engineering - Mobile and Web Front End',
    period: 'Mar 2014 - Jun 2017',
    location: 'Portland, Maine Area',
    bullets: [
      'Built and led engineering teams across native mobile, frontend, GraphQL, data pipelines, and AWS platform work.',
      'Stayed hands-on across Swift, Kotlin, TypeScript, React, Node.js, and Python while managing up to three teams.',
      'Scaled engineering standards across mobile, web, cloud, and data delivery.',
    ],
  },
];

const earlySystems = [
  'Partner and mobile director building Objective-C social software at Bark Software.',
  'Senior engineering work across Python microservices, Go APIs, Node.js DevOps, JavaScript, Android, and Objective-C.',
  'Software architecture and business systems across C#, SQL Server, Oracle, ASP.NET MVC, Ruby on Rails, Django, PHP, classic ASP, VB6, Perl, and MySQL.',
];

const signals = [
  {
    label: 'AI Red-Team Lab',
    href: '/blog/breaking-agents-llm01-prompt-injection',
    detail: 'Hands-on lab work around OWASP LLM Top 10 failure modes and agent attack surfaces.',
  },
  {
    label: 'Production Agent Attack Surface',
    href: '/blog/production-agent-attack-surface',
    detail: 'Research notes on the risks that show up when agentic systems move into production paths.',
  },
  {
    label: 'Shai-Hulud AI Tooling Notes',
    href: '/blog/shai-hulud-ai-tooling',
    detail: 'Supply-chain and AI-tooling analysis from the broader security research stream.',
  },
  {
    label: 'Publications',
    href: 'https://www.linkedin.com/in/shawnmcampbell/',
    detail: 'Testing and Packaging JavaScript: JS\'s Final Frontier; Servers: We Don\'t Need Any Stinkin\' Servers.',
  },
];
---

<BaseLayout
  title="Resume — Shawn Campbell"
  description="Mission dossier for Shawn Campbell: AI security, secure systems architecture, red-team methodology, and engineering leadership."
>
  <article class="resume-dossier">
    <section class="hero-panel" aria-labelledby="resume-title">
      <div class="kicker">Mission Dossier / AI Security</div>
      <h1 id="resume-title">Shawn Campbell</h1>
      <p class="role-line">AI security researcher, secure systems architect, and hands-on engineering leader.</p>
      <p class="mission-profile">
        I build and break distributed systems with a security-first bias: agentic AI labs, red-team
        exercises, application security programs, mobile and IoT platforms, and engineering teams
        that can turn risk into working software.
      </p>
      <ul class="signal-list" aria-label="Primary focus areas">
        <li>AI Security</li>
        <li>Red Team</li>
        <li>Secure Systems</li>
        <li>Engineering Leadership</li>
        <li>Distributed Platforms</li>
      </ul>
    </section>

    <section class="dossier-section" aria-labelledby="capabilities-title">
      <div class="section-heading">
        <p>Capabilities Matrix</p>
        <h2 id="capabilities-title">Operating Domains</h2>
      </div>
      <div class="capability-grid">
        {capabilities.map((capability) => (
          <div class="capability-card">
            <h3>{capability.label}</h3>
            <p>{capability.detail}</p>
          </div>
        ))}
      </div>
    </section>

    <section class="dossier-section" aria-labelledby="record-title">
      <div class="section-heading">
        <p>Operational Record</p>
        <h2 id="record-title">Selected Assignments</h2>
      </div>
      <div class="timeline">
        {roles.map((role) => (
          <section class="role-card" aria-labelledby={`${role.org.toLowerCase().replaceAll(' ', '-')}-title`}>
            <div class="role-meta">
              <span>{role.period}</span>
              <span>{role.location}</span>
            </div>
            <h3 id={`${role.org.toLowerCase().replaceAll(' ', '-')}-title`}>{role.org}</h3>
            <p class="role-title">{role.title}</p>
            <ul>
              {role.bullets.map((bullet) => <li>{bullet}</li>)}
            </ul>
          </section>
        ))}
      </div>
    </section>

    <section class="dossier-section early-section" aria-labelledby="early-title">
      <div class="section-heading">
        <p>Long-Range Track</p>
        <h2 id="early-title">Early Systems Work</h2>
      </div>
      <ol class="early-list">
        {earlySystems.map((item) => <li>{item}</li>)}
      </ol>
    </section>

    <section class="dossier-section" aria-labelledby="signals-title">
      <div class="section-heading">
        <p>Selected Signals</p>
        <h2 id="signals-title">Research, Labs, and Notes</h2>
      </div>
      <div class="signals-grid">
        {signals.map((signal) => (
          <a class="signal-card" href={signal.href}>
            <span>{signal.label}</span>
            <p>{signal.detail}</p>
          </a>
        ))}
      </div>
    </section>

    <section class="contact-panel" aria-labelledby="contact-title">
      <div>
        <p class="kicker">Open Channel</p>
        <h2 id="contact-title">Professional Links</h2>
      </div>
      <div class="contact-links">
        <a href="https://www.linkedin.com/in/shawnmcampbell/">LinkedIn</a>
        <a href="https://github.com/jaegerpicker">GitHub</a>
        <a href="/blog">Blog</a>
      </div>
    </section>
  </article>
</BaseLayout>
```

- [ ] **Step 2: Add route-local styles to the same file**

Append this `<style>` block below the `</BaseLayout>` closing tag in `src/pages/resume.astro`.

```astro
<style>
  :global(body) {
    background:
      radial-gradient(circle at top left, rgba(54, 190, 201, 0.16), transparent 34rem),
      radial-gradient(circle at 85% 12%, rgba(237, 177, 80, 0.12), transparent 28rem),
      #070b12;
    color: #dbe7ef;
  }

  :global(main) {
    max-width: 1120px;
    padding: 2rem 1.25rem 4rem;
  }

  .resume-dossier {
    position: relative;
    display: grid;
    gap: 1.4rem;
  }

  .resume-dossier::before {
    content: '';
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
      linear-gradient(rgba(123, 210, 219, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(123, 210, 219, 0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.7), transparent 80%);
  }

  .hero-panel,
  .dossier-section,
  .contact-panel {
    position: relative;
    border: 1px solid rgba(127, 221, 232, 0.28);
    background:
      linear-gradient(135deg, rgba(14, 24, 36, 0.96), rgba(7, 11, 18, 0.9)),
      linear-gradient(90deg, rgba(237, 177, 80, 0.08), transparent);
    box-shadow: 0 18px 42px rgba(0, 0, 0, 0.32);
  }

  .hero-panel::after,
  .dossier-section::after,
  .contact-panel::after {
    content: '';
    position: absolute;
    top: -1px;
    right: -1px;
    width: 5rem;
    height: 1px;
    background: #edb150;
  }

  .hero-panel {
    min-height: 30rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: clamp(1.5rem, 4vw, 3.5rem);
    overflow: hidden;
  }

  .hero-panel::before {
    content: '';
    position: absolute;
    right: clamp(1rem, 8vw, 6rem);
    top: 2rem;
    width: min(32vw, 18rem);
    aspect-ratio: 1;
    border: 1px solid rgba(127, 221, 232, 0.35);
    border-radius: 50%;
    background:
      linear-gradient(90deg, transparent 49%, rgba(127, 221, 232, 0.2) 50%, transparent 51%),
      linear-gradient(transparent 49%, rgba(127, 221, 232, 0.2) 50%, transparent 51%);
    opacity: 0.55;
  }

  .kicker,
  .section-heading p,
  .role-meta,
  .signal-list,
  .contact-links {
    font-family: var(--font-mono);
  }

  .kicker,
  .section-heading p {
    color: #edb150;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    margin: 0 0 0.75rem;
    text-transform: uppercase;
  }

  .hero-panel h1 {
    max-width: 12ch;
    margin: 0;
    color: #f4f8fb;
    font-size: clamp(3rem, 9vw, 6.8rem);
    line-height: 0.9;
  }

  .role-line {
    max-width: 42rem;
    margin: 1.25rem 0 0;
    color: #7fdee8;
    font-size: clamp(1.15rem, 3vw, 1.65rem);
    line-height: 1.35;
  }

  .mission-profile {
    max-width: 52rem;
    margin: 1rem 0 0;
    color: #b8c8d2;
  }

  .signal-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    list-style: none;
    margin: 1.5rem 0 0;
    padding: 0;
  }

  .signal-list li {
    border: 1px solid rgba(237, 177, 80, 0.46);
    padding: 0.35rem 0.6rem;
    color: #ffd188;
    font-size: 0.74rem;
    text-transform: uppercase;
  }

  .dossier-section,
  .contact-panel {
    padding: clamp(1.1rem, 3vw, 2rem);
  }

  .section-heading {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid rgba(127, 221, 232, 0.18);
    padding-bottom: 0.8rem;
  }

  .section-heading h2,
  .contact-panel h2 {
    margin: 0;
    color: #f4f8fb;
    font-size: clamp(1.3rem, 3vw, 2rem);
  }

  .capability-grid,
  .signals-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.9rem;
  }

  .capability-card,
  .role-card,
  .signal-card {
    border: 1px solid rgba(127, 221, 232, 0.18);
    background: rgba(5, 10, 17, 0.54);
  }

  .capability-card,
  .signal-card {
    padding: 1rem;
  }

  .capability-card h3,
  .role-card h3 {
    margin: 0 0 0.45rem;
    color: #f4f8fb;
  }

  .capability-card p,
  .signal-card p {
    margin: 0;
    color: #b8c8d2;
    font-size: 0.95rem;
  }

  .timeline {
    display: grid;
    gap: 0.9rem;
  }

  .role-card {
    padding: 1rem;
  }

  .role-meta {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.5rem;
    color: #7fdee8;
    font-size: 0.76rem;
    text-transform: uppercase;
  }

  .role-title {
    margin: 0 0 0.75rem;
    color: #edb150;
  }

  .role-card ul,
  .early-list {
    margin-bottom: 0;
    color: #cbd8df;
  }

  .early-list {
    display: grid;
    gap: 0.65rem;
    padding-left: 1.2rem;
  }

  .signal-card {
    color: #dbe7ef;
  }

  .signal-card:hover {
    border-color: rgba(237, 177, 80, 0.7);
    color: #f4f8fb;
    text-decoration: none;
  }

  .signal-card span {
    display: block;
    margin-bottom: 0.45rem;
    color: #7fdee8;
    font-family: var(--font-mono);
    font-size: 0.8rem;
    text-transform: uppercase;
  }

  .contact-panel {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }

  .contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .contact-links a {
    border: 1px solid rgba(127, 221, 232, 0.35);
    padding: 0.45rem 0.7rem;
    color: #7fdee8;
    text-transform: uppercase;
  }

  .contact-links a:hover {
    border-color: rgba(237, 177, 80, 0.7);
    color: #ffd188;
    text-decoration: none;
  }

  @media (max-width: 840px) {
    .capability-grid,
    .signals-grid {
      grid-template-columns: 1fr;
    }

    .hero-panel {
      min-height: auto;
    }

    .hero-panel::before {
      opacity: 0.2;
    }

    .section-heading,
    .contact-panel {
      align-items: flex-start;
      flex-direction: column;
    }
  }
</style>
```

- [ ] **Step 3: Run the build and inspect the route generation**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: command exits 0 and includes a generated route line like:

```text
├─ /resume/index.html
```

- [ ] **Step 4: Search for private PDF contact details in source and build output**

Run:

```bash
rg -n "<private-street-address>|<private-phone>|<private-email>" src/pages/resume.astro dist/resume/index.html
```

Expected: replace the placeholder values locally before running. The command
must exit 1 with no matches. Do not commit the private values.

- [ ] **Step 5: Commit Task 1**

Run:

```bash
git add src/pages/resume.astro
git -c gpg.format=ssh -c user.signingkey=~/.ssh/id_rsa commit -S -m "Add resume dossier page"
```

Expected: signed commit created with `src/pages/resume.astro`.

---

### Task 2: Add Resume to the Header Navigation

**Files:**
- Modify: `src/components/Header.astro`

- [ ] **Step 1: Update the links array**

Change the `links` array in `src/components/Header.astro` to include the resume route between Blog and About:

```astro
const links = [
  { href: `${base}/`, label: 'Home' },
  { href: `${base}/blog`, label: 'Blog' },
  { href: `${base}/resume`, label: 'Resume' },
  { href: `${base}/about`, label: 'About' },
];
```

- [ ] **Step 2: Run the build**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Expected: command exits 0.

- [ ] **Step 3: Confirm generated navigation includes Resume**

Run:

```bash
rg -n 'href="/resume".*>Resume' dist/index.html dist/blog/index.html dist/resume/index.html
```

Expected: matches in all three generated files.

- [ ] **Step 4: Commit Task 2**

Run:

```bash
git add src/components/Header.astro
git -c gpg.format=ssh -c user.signingkey=~/.ssh/id_rsa commit -S -m "Add resume navigation link"
```

Expected: signed commit created with `src/components/Header.astro`.

---

### Task 3: Browser Validation and Final Checks

**Files:**
- No source edits expected.

- [ ] **Step 1: Start the local Astro dev server**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run dev -- --host 127.0.0.1
```

Expected: dev server reports a local URL on port 4321 or another available port.

- [ ] **Step 2: Open `/resume` in the browser at desktop width**

Open the local URL for `/resume`, for example:

```text
http://127.0.0.1:4321/resume
```

Expected visual result:

- The page has a dark sci-fi operations aesthetic.
- Hero text is readable and not clipped.
- Capability cards form a 3-column grid on desktop.
- Operational record cards are readable.
- Header navigation includes Resume.

- [ ] **Step 3: Inspect `/resume` at mobile width**

Use a mobile-sized viewport around 390px wide.

Expected visual result:

- No horizontal overflow.
- Hero text wraps cleanly.
- Capability and signal cards stack into one column.
- Contact links wrap without overlap.

- [ ] **Step 4: Run final source and generated-output checks**

Run:

```bash
git diff --check
ASTRO_TELEMETRY_DISABLED=1 npm run build
rg -n "<private-street-address>|<private-phone>|<private-email>" docs src dist
```

Expected:

- `git diff --check` exits 0.
- Build exits 0.
- Replace the placeholder values locally before running. The private contact
  search exits 1 with no matches. Do not commit the private values.

- [ ] **Step 5: Push and open the implementation PR**

Run:

```bash
git push -u origin issue-62-resume-dossier-page
gh pr create --title '[#62] Implement resume dossier page' --body 'Closes #62

## Summary
- Add the /resume mission-dossier page.
- Add Resume to the site navigation.
- Keep the sci-fi operations styling scoped to the resume route as the future theme prototype.

## Validation
- ASTRO_TELEMETRY_DISABLED=1 npm run build
- git diff --check
- Browser inspection of /resume at desktop and mobile widths
- Private contact scan for street address, phone number, and personal email

## Known limitations
- Full-site theme migration is intentionally deferred to a follow-up issue.'
```

Expected: branch pushed and PR URL returned.

---

## Self-Review

- Spec coverage: Tasks add `/resume`, add navigation, keep styling local, omit private contact fields, include mission profile, capabilities matrix, operational record, early systems work, selected signals, contact links, and validation.
- Placeholder scan: The plan uses privacy-safe placeholders for private contact
  validation commands and contains no private contact values.
- Type consistency: All arrays used in markup are defined in `src/pages/resume.astro`, and all referenced fields match their object definitions.
