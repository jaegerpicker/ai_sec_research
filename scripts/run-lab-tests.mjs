import { existsSync } from 'node:fs';
import { platform } from 'node:os';
import { spawnSync } from 'node:child_process';

const pythonPath = platform() === 'win32'
  ? '.venv\\Scripts\\python.exe'
  : '.venv/bin/python';

if (!existsSync(pythonPath)) {
  console.error(`Missing ${pythonPath}. Create the lab virtualenv first:`);
  console.error('  python3 -m venv .venv');
  console.error('  .venv/bin/python -m pip install -r lab/requirements.txt');
  process.exit(1);
}

const result = spawnSync(
  pythonPath,
  process.argv.length > 2
    ? ['-m', 'unittest', ...process.argv.slice(2)]
    : ['-m', 'unittest', 'discover', '-s', 'tests'],
  { stdio: 'inherit' },
);

process.exit(result.status ?? 1);
