<script setup>
// import { useData, useRoute } from 'vitepress'

// const { frontmatter } = useData()
// const route = useRoute()

// // Reactive variables to handle route changes
// const urls = ref({})

// // Watch for route changes and update the URLs
// watch(() => route.path, () => {
//   urls.value = frontmatter.value.urls || {}
// })

// // Initialize on component mount
// onMounted(() => {
//   urls.value = frontmatter.value.urls || {}
// })
</script>

<template>
  <!-- <div v-if="Object.keys(urls).length" class="switcher-container">
    <button
      v-for="(url, key) in urls"
      :key="key"
      :class="['switcher-button']"
      @click="navigateTo(url)"
    >
      {{ key }}
    </button>
  </div> -->
</template>

<script>
function navigateTo(url) {
  window.location.href = url
}
</script>

<style scoped>
.switcher-container {
  display: flex;
  gap: 1rem;
}

.switcher-button {
  padding: 0.5rem 1rem;
  border: none;
  background: #007aff;
  color: #fff;
  cursor: pointer;
  border-radius: 4px;
}

.switcher-button:hover {
  background: #005bb5;
}
</style>
