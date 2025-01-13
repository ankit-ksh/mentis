<script setup>
import contents from '../contents.json';

const topic = week11;
</script>

<CoursePage :contents="contents" :topic="topic" />