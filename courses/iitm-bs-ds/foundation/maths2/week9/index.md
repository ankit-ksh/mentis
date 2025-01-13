<script setup>
import contents from '../contents.json';

const topic = week9;
</script>

<CoursePage :contents="contents" :topic="topic" />