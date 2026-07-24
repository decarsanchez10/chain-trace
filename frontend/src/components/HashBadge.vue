<template>
  <span :class="['hash-badge', verified ? 'verified' : 'unverified']">
    {{ verified ? 'Verified' : 'Unverified' }} ({{ hash ? hash.substring(0, 10) + '...' : '' }})
  </span>
</template>

<script setup>
defineProps({
  verified: Boolean,
  hash: String
})
</script>

<style scoped>
.hash-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-family: monospace;
}
.verified {
  background-color: #d4edda;
  color: #155724;
}
.unverified {
  background-color: #fff3cd;
  color: #856404;
}
</style>
