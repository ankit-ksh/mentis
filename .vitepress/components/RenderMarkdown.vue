<template>
    <div v-if="markdownContent" v-html="markdownContent"></div>
    <div v-else>Loading...</div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  
  // Props
  defineProps({
    filePath: {
      type: String,
      required: true,
    },
  });
  
  const markdownContent = ref(null);
  
  watch(
    () => filePath,
    async (newPath) => {
      try {
        // Dynamically import the markdown file
        const module = await import(newPath);
        markdownContent.value = module.default; // Access the Markdown content as text
      } catch (error) {
        console.error(`Error loading file at ${newPath}:`, error);
        markdownContent.value = `<p style="color: red;">Error: Unable to load file ${newPath}</p>`;
      }
    },
    { immediate: true }
  );
  </script>
  