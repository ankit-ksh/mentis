---
layout: page
title: Our Team
---

<script setup lang="ts">
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers
} from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/ankit-ksh.png',
    name: 'Ankit Kumar',
    title: 'Lead',
    links: [
      { icon: 'github', link: 'https://github.com/ankit-ksh' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/ankit-kumar-b5425617b/' }
    ]
  }
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>
      Our Team
    </template>
  </VPTeamPageTitle>

  <VPTeamMembers
    :members="members"
  />
</VPTeamPage>
