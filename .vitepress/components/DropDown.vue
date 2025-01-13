<!-- src/components/Dropdown.vue -->
<template>
    <details>
      <summary>{{ title }}</summary>
      <div class="dropdown-content">
        <slot></slot>
      </div>
    </details>
  </template>
  
  <script setup>
  const props = defineProps({
    title: {
      type: String,
      required: true
    }
  })
  </script>
  
  <style scoped>
  details {
    background-color: #f9f9f9;
    padding: 1em;
    border: 1px solid #ddd;
  }
  
  summary {
    font-weight: bold;
    cursor: pointer;
  }
  
  .dropdown-content {
    padding-top: 10px;
  }
  </style>
  