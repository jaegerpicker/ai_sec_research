export const systems = [
  {
    id: 'mobile',
    opsLabel: 'Secure Mobile',
    directLabel: 'Mobile Application Security',
    detail: 'Swift, Kotlin, connected devices, storage, permissions, and field trust boundaries.',
    status: 'Operational',
    href: '#selected-work',
  },
  {
    id: 'react',
    opsLabel: 'Product Attack Surface',
    directLabel: 'Product and Frontend Security',
    detail: 'React, React Native, GraphQL, APIs, auth flows, and reviewable delivery systems.',
    status: 'Active focus',
    href: '#selected-work',
  },
  {
    id: 'games',
    opsLabel: 'AI Security Lab',
    directLabel: 'AI Security Research',
    detail: 'Executable OWASP LLM labs, prompt injection, agent tooling, and defense experiments.',
    status: 'Under construction',
    href: '#security-lab',
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
    label: '01 / AI Security',
    directLabel: 'AI Security Research',
    title: 'Executable security research for agentic systems',
    summary:
      'OWASP LLM Top 10 labs, vulnerable agents, attack harnesses, and writeups that make AI risks observable instead of abstract.',
    status: 'Active focus',
    href: '/blog',
    tone: 'cyan',
  },
  {
    label: '02 / AppSec',
    directLabel: 'Application Security',
    title: 'Security reviews that stay close to delivery',
    summary:
      'Threat modeling, secure code review, trust boundaries, CI/CD hardening, and practical fixes across product teams.',
    status: 'Flight proven',
    href: '/resume',
    tone: 'amber',
  },
  {
    label: '03 / Secure Product',
    directLabel: 'Secure Product Engineering',
    title: 'Mobile and product systems with security built in',
    summary:
      'Native mobile, React, React Native, GraphQL, and connected-device work grounded in permissions, data flow, and failure modes.',
    status: 'Flight proven',
    href: '/projects',
    tone: 'green',
  },
] as const;
