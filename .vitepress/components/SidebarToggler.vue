<template>
  <button class="sidebar-toggler" @click="toggleSidebar">
    Toggle Sidebar
  </button>
</template>

<script setup>
const toggleSidebar = () => {
  const sidebar = document.querySelector('.VPSidebar')
  if (sidebar) {
    sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none'
  }
}
</script>

<style scoped>
.sidebar-toggler {
  position: fixed;
  top: 10px;
  left: 10px;
  z-index: 1000;
  background-color: #0078d7;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
