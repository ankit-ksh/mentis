<script setup>
import contents from '../contents.json';

const week1Data = contents.week1;
</script>

<VideoPlayer :videoData="week1Data" />

<HelloWorld />
