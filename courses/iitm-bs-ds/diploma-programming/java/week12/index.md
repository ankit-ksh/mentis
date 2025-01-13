<script setup>
import contents from '../contents.json';

const topic = week12;
</script>

<CoursePage :contents="contents" :topic="topic" />