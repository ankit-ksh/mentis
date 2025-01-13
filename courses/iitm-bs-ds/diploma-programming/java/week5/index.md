<script setup>
import contents from '../contents.json';

const topic = week5;
</script>

<CoursePage :contents="contents" :topic="topic" />