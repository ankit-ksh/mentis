<script setup>
import contents from '../contents.json';

const topic = week6;
</script>

<CoursePage :contents="contents" :topic="topic" />