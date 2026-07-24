<template>
  <div class="dashboard">
    <h2>Custody History Dashboard</h2>
    <p>View all recent asset scan events and anchoring status.</p>
    <CustodyTimeline />
  </div>
</template>

<script setup>
import CustodyTimeline from '../components/CustodyTimeline.vue'
</script>
