<template>
    <div class="course-page-layout">
      <Sidebar />
      <div class="course-content">
        <slot />
      </div>
    </div>
  </template>
  
  <script setup>
  import Sidebar from '../components/Sidebar.vue';
  </script>
  
  <style scoped>
  .course-page-layout {
    display: flex;
    gap: 20px;
  }
  
  .course-content {
    flex: 1;
    padding: 20px;
    background-color: #fff;
  }
  </style>
  