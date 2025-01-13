<template>
  <div class="card-list-container">
    <a 
      v-for="(item, index) in items" 
      :key="index" 
      :href="item.link"
      rel="noopener noreferrer"
      class="card"
    >
      <span>{{ item.text }}</span>
    </a>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true,
    default: () => []
  }
});
</script>

<style scoped>
.card-list-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
  max-width: 1200px;
  margin: auto;
}

.card {
  background: #f9f9f9;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100px;
  flex-direction: column;
  color: #333;
  text-decoration: none; /* No underline on card */
  transition: background-color 0.2s;
}

.card span {
  color: inherit; /* Use inherited color from card */
  font-weight: bold;
}

.card:hover {
  background-color: #f0f0f0;
}

.card:hover {
  cursor: pointer;
}
</style>
