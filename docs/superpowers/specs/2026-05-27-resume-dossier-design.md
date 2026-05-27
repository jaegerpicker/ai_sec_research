# Resume Dossier Page Design

## Goal

Create a `/resume` page that presents Shawn Campbell as an AI security,
application security, and engineering leadership practitioner. The page should
read as a mission dossier for technical peers first, hiring managers and
recruiters second, and conference or blog readers third.

## Source Material

The initial content source is the exported LinkedIn profile PDF at
`~/Downloads/Profile-2.pdf`. The page must rewrite the source material rather
than copy it verbatim. It must not publish the street address, phone number, or
personal email from the PDF unless explicitly approved later.

## Audience Priority

1. Security and AI peers
2. Hiring managers and recruiters
3. Conference and blog readers

This priority means the page should emphasize technical judgment, AI threat
research, secure architecture, red-team methodology, and credible hands-on
leadership before general career narrative.

## Page Concept

The resume page is a "mission dossier" rather than a traditional resume. It is
concise, signal-heavy, and organized like an operational profile.

The first implementation should scope the visual system to `/resume` only. Once
the look is approved, the same theme can be promoted into the global site design
as a follow-up issue.

## Visual Direction

Use an original sci-fi operations aesthetic inspired by hard sci-fi interfaces:

- Dark steel/navy base colors
- Thin borders and tactical divider lines
- Amber and cyan accents for status and telemetry cues
- Compact mono labels and metadata rows
- Subtle grid, scanline, or orbital-map motifs
- Dense but readable panels

Avoid copyrighted names, logos, imagery, or direct reproduction of a specific
show's interface. The feel should be technically sharp and restrained, not
costume-like or noisy.

## Information Architecture

### Header / Mission Profile

Top section with:

- Shawn Campbell
- A concise role line focused on AI security, secure systems, and technical
  leadership
- A short mission profile paragraph
- Signal badges such as `AI Security`, `Red Team`, `Secure Systems`,
  `Engineering Leadership`, and `Distributed Systems`

### Capabilities Matrix

Grouped capabilities rewritten from the profile:

- AI threat research and agentic systems security
- Application security architecture and assessment
- Red-team methodology, threat modeling, and secure code review
- Distributed systems, cloud-native services, and data pipelines
- Mobile, IoT, Swift, Kotlin, C++, TypeScript, Go, Python, and related systems
- Engineering leadership, mentoring, standards, and cross-functional execution

### Operational Record

Main role entries:

- Brivo
- Riffle Analytics
- VividCloud
- GrowFlow Corp
- Minnow
- Vox Media
- Vets First Choice

Each entry should include a short title/date/location line and two to four
bullets rewritten around AI/security/leadership relevance. The page should favor
impact and scope over exhaustive responsibility lists.

Older roles should be compressed into an "Early Systems Work" timeline that
shows long-term depth without making the page too long.

### Selected Signals

Include publications, lab work, blog work, talks, and current AI threat research
when available in the repo. This section can link to existing blog/lab material
without claiming completed external talks or publications beyond what the source
supports.

### Contact Links

Include public professional links by default:

- LinkedIn profile
- Site/blog links

Do not include address, phone number, or personal email in the first pass.

## Content Voice

The voice should be direct, technical, and credible. It should avoid generic
resume filler and focus on:

- AI threat research
- Secure distributed systems
- Mobile and IoT security depth
- Application security and red-team practices
- Hands-on senior engineering
- Team leadership and engineering standards

## Implementation Boundaries

The first implementation should:

- Add a `/resume` route.
- Add a `Resume` navigation link.
- Keep styling local to the resume page where practical.
- Use existing Astro patterns and shared layout components.
- Avoid changing global blog typography or color tokens except where required by
  the route.
- Avoid adding a PDF download unless explicitly requested later.

The first implementation should not:

- Publish private contact information.
- Claim unverified AI/security accomplishments beyond the PDF and repo material.
- Redesign the full site.
- Add a CMS or resume content pipeline.

## Follow-Up Theme Migration

After the `/resume` page look is approved, create a follow-up issue to promote
the visual language into the rest of the site. That migration can update global
tokens, header/footer styling, blog list treatment, post pages, and homepage
layout using the resume page as the reference.

## Validation

Implementation should be validated with:

- `ASTRO_TELEMETRY_DISABLED=1 npm run build`
- `git diff --check`
- Local browser inspection of `/resume` at desktop and mobile widths
- A content review confirming no private contact fields from the LinkedIn PDF
  were published
