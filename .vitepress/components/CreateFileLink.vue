<template>
    
      {{ includeLine }}
    
  </template>
  
  <script setup>
  // Define constants for baseUrl and filePath
  const baseUrl = '@iitm-bs-ds/foundation/maths2';
  const filePath = 'week2/notes.md';
  
  // Generate the inclusion line using constants
  const includeLine = `<!-- @include: ${baseUrl}/${filePath} -->`;
  </script>
  