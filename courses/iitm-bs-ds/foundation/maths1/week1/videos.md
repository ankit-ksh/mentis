<script setup>
import { ref } from 'vue';

// Fetch the JSON file
const videoData = ref(null);

fetch('../contents.json') // Adjust the path to match the part's folder
  .then((response) => response.json())
  .then((data) => {
    // Assume 'week1' is the key for this part's data
    videoData.value = {
      title: data.week1.title,
      videoList: data.week1.videos,
    };
  })
  .catch((error) => {
    console.error('Error loading video data:', error);
  });
</script>

<div v-if="videoData">
  <VideoPlayer :videoData="videoData" />
</div>

<div v-else>
  Loading videos...
</div>
