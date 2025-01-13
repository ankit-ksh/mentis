<script setup>
import contents from '../contents.json';

const topic = week3;
</script>

<CoursePage :contents="contents" :topic="topic" />