import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const [config, projects, blog, readme] = await Promise.all([
  readFile(new URL('../src/content.config.ts', import.meta.url), 'utf8'),
  readFile(new URL('../src/pages/projects/index.astro', import.meta.url), 'utf8'),
  readFile(new URL('../src/pages/blog/index.astro', import.meta.url), 'utf8'),
  readFile(new URL('../README.md', import.meta.url), 'utf8'),
]);

for (const format of [
  'system-deep-dive',
  'flight-log',
  'postmortem',
  'cross-system-test',
]) {
  assert.match(config, new RegExp(format));
}

assert.match(config, /optional\(\)/);
assert.match(projects, /Native Mobile/);
assert.match(projects, /React and React Native/);
assert.match(projects, /Frontend and Product Systems/);
assert.match(projects, /Game Lab/);
assert.match(projects, /Under construction/);
assert.match(blog, /Flight Log/);
assert.match(blog, /System Deep Dives/);
assert.match(readme, /50% AI security and application security/);

console.log('projects and editorial tests passed');
