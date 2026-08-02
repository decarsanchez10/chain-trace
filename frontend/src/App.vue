<template>
  <div id="app" class="app-container">
    <main :class="['content', { 'content-fullscreen': isFullScreen }]">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isFullScreen = computed(() => ['Landing', 'Verify'].includes(route.name))
</script>

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  background: #050816;
  color: #F8FAFC;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.content { padding: 2rem; flex: 1; }
.content-fullscreen { padding: 0; flex: 1; }
</style>
