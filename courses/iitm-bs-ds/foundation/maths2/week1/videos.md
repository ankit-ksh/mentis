<script setup>
import contents from '../contents.json';
const videoData = contents.week2;
</script>
<VideoPlayer :videoData="videoData" />
