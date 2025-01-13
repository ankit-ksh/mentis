<template>
    <div class="video-page">
      <iframe
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      data: {
        type: Object,
        default: () => ({}),
      },
    },
    computed: {
      videoId() {
        return this.data.videoId || 'dQw4w9WgXcQ'; // Replace with default ID or data-driven ID
      },
    },
  };
  </script>
  
  <style scoped>
  .video-page iframe {
    width: 100%;
    height: 500px;
  }
  </style>
  