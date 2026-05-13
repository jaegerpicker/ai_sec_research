# ai-sec-research

Personal blog and research notes on AI security, red teaming, and agentic
systems. Built with [Astro](https://astro.build) and deployed to GitHub Pages.

Live site: <https://jaegerpicker.github.io/ai_sec_research/>

## Local development

```bash
npm install
npm run dev       # http://localhost:4321/ai_sec_research/
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

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys on every
push to `main`. To enable:

1. Repo → Settings → Pages → Source: **GitHub Actions**.
2. First push to `main` runs the workflow.

## Comments (Giscus)

Stubbed in `src/components/Giscus.astro`. To enable:

1. Enable Discussions on the repo.
2. Install <https://github.com/apps/giscus>.
3. Visit <https://giscus.app>, configure for this repo, copy the `data-repo-id`
   and `data-category-id`.
4. Edit `src/components/Giscus.astro`, paste the IDs, flip `disabled = false`.

## Planning docs (not published)

- `lab_build_plan.md` — AI red-team lab build plan
- `career_roadmap.md` — personal study/transition plan
- `blog_post_drafts.md` — post outlines (the draft posts in `src/content/blog/`
  are stubs derived from these)

These stay at the repo root and are not built into the site.
