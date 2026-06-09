export type ViewMode = 'ops' | 'direct';

export function parseViewMode(value: string | null): ViewMode | null {
  return value === 'ops' || value === 'direct' ? value : null;
}

export function resolveViewMode(
  queryMode: string | null,
  storedMode: string | null,
): ViewMode {
  return parseViewMode(queryMode) ?? parseViewMode(storedMode) ?? 'ops';
}
