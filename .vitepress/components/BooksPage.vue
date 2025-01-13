<template>
    <div class="books-page">
      <p>Books for {{ data?.name || 'this topic' }}:</p>
      <ul>
        <li v-for="book in data?.books || []" :key="book.id">{{ book.title }}</li>
      </ul>
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
  .books-page ul {
    padding: 0;
    list-style: none;
  }
  
  .books-page ul li {
    margin: 5px 0;
  }
  </style>
  