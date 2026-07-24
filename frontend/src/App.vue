<template>
  <div id="app" class="app-container">
    <header class="navbar" v-if="!isLanding">
      <h1>ChainTrace</h1>
      <nav>
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/verify">Verify</router-link>
        <router-link to="/login">Login</router-link>
      </nav>
    </header>
    <main :class="['content', { 'content-landing': isLanding }]">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isLanding = computed(() => route.name === 'Landing')
</script>

<style>
* {
  box-sizing: border-box;
}
html, body {
  margin: 0;
  padding: 0;
  background-color: #050a1a;
  color: #fff;
}
.app-container {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: rgba(5, 10, 26, 0.95);
  border-bottom: 1px solid rgba(0, 210, 211, 0.2);
  color: #fff;
}
.navbar nav a {
  color: #a0a0b0;
  margin-left: 1.5rem;
  text-decoration: none;
  transition: color 0.3s;
}
.navbar nav a:hover {
  color: #00d2d3;
}
.navbar nav a.router-link-active {
  font-weight: bold;
  color: #00d2d3;
}
.content {
  padding: 2rem;
  flex: 1;
}
.content-landing {
  padding: 0;
}
</style>
