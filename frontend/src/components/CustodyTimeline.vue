<template>
  <div class="timeline">
    <div class="timeline-item">
      <h4>Initial Handoff</h4>
      <p>Timestamp: 2026-07-24 10:00:00</p>
      <HashBadge :verified="true" hash="a1b2c3d4e5f67890" />
    </div>
  </div>
</template>

<script setup>
import HashBadge from './HashBadge.vue'
</script>

<style scoped>
.timeline-item {
  border-left: 2px solid #00d2d3;
  padding-left: 1rem;
  margin-bottom: 1rem;
}
</style>
