import assert from 'node:assert/strict';

import {
  parseViewMode,
  resolveViewMode,
} from '../src/lib/view-mode.ts';

assert.equal(parseViewMode('direct'), 'direct');
assert.equal(parseViewMode('ops'), 'ops');
assert.equal(parseViewMode('DIRECT'), null);
assert.equal(parseViewMode('other'), null);
assert.equal(parseViewMode(null), null);

assert.equal(resolveViewMode('direct', 'ops'), 'direct');
assert.equal(resolveViewMode('ops', 'direct'), 'ops');
assert.equal(resolveViewMode('invalid', 'direct'), 'direct');
assert.equal(resolveViewMode(null, 'direct'), 'direct');
assert.equal(resolveViewMode(null, 'invalid'), 'ops');
assert.equal(resolveViewMode(null, null), 'ops');

console.log('view-mode tests passed');
