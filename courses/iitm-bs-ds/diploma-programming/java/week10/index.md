<script setup>
import contents from '../contents.json';

const topic = week10;
</script>

<CoursePage :contents="contents" :topic="topic" />