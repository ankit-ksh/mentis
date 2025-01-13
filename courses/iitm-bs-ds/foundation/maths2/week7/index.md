<script setup>
import contents from '../contents.json';

const topic = week7;
</script>

<CoursePage :contents="contents" :topic="topic" />