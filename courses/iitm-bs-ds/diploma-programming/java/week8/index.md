<script setup>
import contents from '../contents.json';

const topic = week8;
</script>

<CoursePage :contents="contents" :topic="topic" />