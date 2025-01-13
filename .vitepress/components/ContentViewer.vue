<template>
    <div>
      <h3>{{ contentType }} for {{ currentWeek }}</h3>
      <div v-if="contentType === 'videos'">
        <div v-for="(video, index) in videos" :key="index">
          <p>Video {{ index + 1 }}: {{ video }}</p>
        </div>
      </div>
      <div v-if="contentType === 'notes'">
        <p>Notes: {{ notes }}</p>
      </div>
      <div v-if="contentType === 'questions'">
        <p>Questions: {{ questions }}</p>
      </div>
  
      <div>
        <button v-for="(version, index) in versions" :key="index" @click="switchVersion(version)">
          Version {{ index + 1 }}
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed, ref } from 'vue'
  
  const props = defineProps({
    contentType: String,
    currentWeek: String,
    courseData: Object,
  })
  
  const content = computed(() => {
    return props.courseData.contents[props.currentWeek][props.contentType] || {}
  })
  
  const versions = computed(() => {
    return content.value ? Object.keys(content.value) : []
  })
  
  const switchVersion = (version) => {
    console.log(`Switching to ${version} for ${props.contentType}`)
  }
  
  const videos = computed(() => content.value['videos'] || [])
  const notes = computed(() => content.value['notes'] || '')
  const questions = computed(() => content.value['questions'] || '')
  </script>
  