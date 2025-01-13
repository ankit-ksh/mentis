<script setup>
import contents from '../contents.json';

const topic = week4;
</script>

<CoursePage :contents="contents" :topic="topic" />