# ai-sec-research

Personal blog and research notes on AI security, red teaming, and agentic
systems. Built with [Astro](https://astro.build) and deployed to GitHub Pages.

Live site: <https://sandkcampbell.com/>

## Local development

```bash
npm install
npm run dev       # http://localhost:4321/
npm run build
npm run preview
```

Drafts (`draft: true` in frontmatter) are visible in dev, hidden in production.

## Writing a post

Drop a `.md` or `.mdx` file in `src/content/blog/`:

```yaml
---
title: "..."
description: "..."
pubDate: 2026-05-13
draft: true            # optional; defaults to false
tags: ["..."]          # optional
---
```

## Presentation package

The accepted OWASP LLM Top 10 lab talk lives in
`talks/summit-owasp-llm-top-10/`.

- Repo-native slide source: `talks/summit-owasp-llm-top-10/slides.md`
- Speaker notes: `talks/summit-owasp-llm-top-10/speaker-notes.md`
- Demo runbook: `talks/summit-owasp-llm-top-10/demo-runbook.md`
- Public web version after deploy:
  <https://sandkcampbell.com/talks/summit-owasp-llm-top-10/>

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys on every
push to `main`. To enable:

1. Repo → Settings → Pages → Source: **GitHub Actions**.
2. First push to `main` runs the workflow.

## Comments (Giscus)

Giscus is configured in `src/components/Giscus.astro`.

To maintain it:

1. Keep GitHub Discussions enabled on the repo.
2. Keep the giscus app installed: <https://github.com/apps/giscus>.
3. Update `data-repo`, `data-repo-id`, or `data-category-id` only if the
   repository or discussion category changes.
4. Keep `data-theme="dark"` so comments match the dark-only site theme.

## Planning docs (not published)

- `lab_build_plan.md` — AI red-team lab build plan
- `career_roadmap.md` — personal study/transition plan
- `blog_post_drafts.md` — post outlines (the draft posts in `src/content/blog/`
  are stubs derived from these)

These stay at the repo root and are not built into the site.
