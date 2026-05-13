import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Deploy target: https://jaegerpicker.github.io/ai_sec_research
// If you later move to a custom domain, set `site` to that domain and remove `base`.
export default defineConfig({
  site: 'https://jaegerpicker.github.io',
  base: '/ai_sec_research',
  trailingSlash: 'ignore',
  integrations: [mdx(), sitemap()],
  markdown: {
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      wrap: true,
    },
  },
});
