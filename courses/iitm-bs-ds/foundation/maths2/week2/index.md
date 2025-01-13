<script setup>
import contents from '../contents.json';

const topic = week2;
</script>

<CoursePage :contents="contents" :topic="topic" />