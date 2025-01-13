import { defineConfig } from 'vitepress'
import sidebars from '../public/database/sidebars.json'

export default defineConfig({
  title: "Mentis",
  description: "Distraction Free Course Explorer",
  cleanUrls: true,
  srcDir: 'courses/',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Courses', items: [
          { text: 'BS in Data Science and Applications, IIT Madras', link: '/iitm-bs-ds/' },
          { text: 'BS in Electronic Systems, IIT Madras', link: '/iitm-bs-es/' },
          { text: 'YouTube Courses', link: '/youtube' },
          { text: 'NPTEL', link: '/nptel' },
          { text: 'MIT OpenCourseWare', link: '/mit-ocw' },
        ]
      },
      { text: 'Misc', items: [
          { text: 'Roadmap', link: '/docs/roadmap.md'},
          { text: 'Contribution guide', link: '/docs/contribution-guide.md' },
          { text: 'Team', link: '/docs/team.md' }
        ]
      },
    ],
    search: {
      provider: 'local'
    },

    sidebar: sidebars,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ankit-ksh/mentis' }
    ]
  }
})
