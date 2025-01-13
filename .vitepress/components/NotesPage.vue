<template>
    <div class="notes-page">
      <p>{{ data?.notes || 'No notes available.' }}</p>
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
  };
  </script>
  
  <style scoped>
  .notes-page {
    padding: 10px;
    font-size: 16px;
    line-height: 1.5;
  }
  </style>
  