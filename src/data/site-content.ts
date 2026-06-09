export const systems = [
  {
    id: 'mobile',
    opsLabel: 'Native Mobile',
    directLabel: 'Mobile Engineering',
    detail: 'Swift, Kotlin, connected devices, and resilient field workflows.',
    status: 'Flight proven',
    href: '#selected-work',
  },
  {
    id: 'react',
    opsLabel: 'Product Systems',
    directLabel: 'React and React Native',
    detail: 'Cross-platform products, frontend architecture, and design systems.',
    status: 'Flight proven',
    href: '#selected-work',
  },
  {
    id: 'games',
    opsLabel: 'Game Lab',
    directLabel: 'Game Development',
    detail: 'Godot and Unreal experiments, mechanics, tools, and postmortems.',
    status: 'Under construction',
    href: '#game-lab',
  },
  {
    id: 'rigor',
    opsLabel: 'Systems Rigor',
    directLabel: 'Security and Architecture',
    detail: 'Threat-aware engineering, distributed systems, and technical leadership.',
    status: 'Embedded discipline',
    href: '#systems-rigor',
  },
] as const;

export const missions = [
  {
    label: '01 / Mobile',
    directLabel: 'Mobile Engineering',
    title: 'Native systems for the real world',
    summary:
      'Long-running work across iOS, Android, connected devices, offline behavior, and operationally demanding products.',
    status: 'Flight proven',
    href: '/resume',
    tone: 'cyan',
  },
  {
    label: '02 / Product',
    directLabel: 'React and React Native',
    title: 'Cross-platform product systems',
    summary:
      'Frontend architecture, GraphQL, design systems, performance, and team-scale delivery without flattening platform strengths.',
    status: 'Flight proven',
    href: '/resume',
    tone: 'amber',
  },
  {
    label: '03 / Frontier',
    directLabel: 'Game Development',
    title: 'Playable experiments and honest field notes',
    summary:
      'A visible learning trajectory through Godot and Unreal, focused on mechanics, game state, tools, and AI-assisted iteration.',
    status: 'Under construction',
    href: '/blog',
    tone: 'green',
  },
] as const;
