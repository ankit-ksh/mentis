<template>
    <div class="book-list">
      <h2>Books</h2>
      <ul>
        <li 
          v-for="(book, index) in books" 
          :key="index"
          @click="openBook(book.link)"
          class="book-item"
        >
          {{ book.title }}
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    books: {
      type: Array,
      required: true,
      default: () => []
    }
  });
  
  const openBook = (link) => {
    // Construct the URL for PDF.js viewer with the provided link
    const pdfViewerUrl = `https://mozilla.github.io/pdf.js/web/viewer.html?file=${encodeURIComponent(link)}`;
    window.open(pdfViewerUrl, '_blank');
  };
  </script>
  
  <style scoped>
  .book-list {
    width: 100%;
    padding: 0;
    margin: 0;
  }
  
  .book-item {
    background-color: #f9f9f9;
    border-radius: 6px;
    padding: 12px 20px;
    margin: 8px 0;
    cursor: pointer;
    text-align: left; /* Align text to the left */
    transition: background-color 0.3s ease;
    border: 1px solid transparent; /* For border effect without shadow */
  }
  
  .book-item:hover {
    background-color: #e0e0e0; /* Slight color change on hover */
  }
  
  .book-item:active {
    background-color: #d0d0d0; /* Slight color change when clicked */
  }
  
  .book-item {
    list-style-type: none; /* No list style (dots) */
  }
  </style>
  