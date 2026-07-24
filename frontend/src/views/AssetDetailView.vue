<template>
  <div class="asset-detail">
    <h2>Asset Custody Chain</h2>
    <p>Asset ID: {{ id }}</p>
  </div>
</template>

<script setup>
defineProps({
  id: String
})
</script>
