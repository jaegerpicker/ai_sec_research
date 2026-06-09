import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const [layout, header, toggle, orbit, globalCss, resume, giscus] =
  await Promise.all([
    readFile(new URL('../src/layouts/BaseLayout.astro', import.meta.url), 'utf8'),
    readFile(new URL('../src/components/Header.astro', import.meta.url), 'utf8'),
    readFile(new URL('../src/components/ViewModeToggle.astro', import.meta.url), 'utf8'),
    readFile(new URL('../src/components/OrbitMap.astro', import.meta.url), 'utf8'),
    readFile(new URL('../src/styles/global.css', import.meta.url), 'utf8'),
    readFile(new URL('../src/pages/resume.astro', import.meta.url), 'utf8'),
    readFile(new URL('../src/components/Giscus.astro', import.meta.url), 'utf8'),
  ]);

assert.match(layout, /<main>/);
assert.match(layout, /Astro\.url\.pathname/);
assert.match(header, /<nav>/);
assert.match(toggle, /role="group"/);
assert.match(toggle, /aria-label="Site presentation"/);
assert.match(toggle, /aria-pressed/);
assert.match(toggle, /site-view-change/);
assert.match(orbit, /aria-label="Engineering focus areas"/);
assert.match(orbit, /aria-hidden="true"/);
assert.match(globalCss, /:focus-visible/);
assert.match(globalCss, /prefers-reduced-motion: reduce/);
assert.match(resume, /@media print/);
assert.match(giscus, /small_screens_big_worlds/);
assert.match(giscus, /site-view-change/);

console.log('accessibility contract tests passed');
