<script setup>
import contents from '../contents.json';

const topic = week1;
</script>

<CoursePage :contents="contents" :topic="topic" />