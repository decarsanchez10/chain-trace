<template>
  <div id="app" class="app-container">
    <header class="navbar">
      <h1>ChainTrace</h1>
      <nav>
        <router-link to="/">Dashboard</router-link>
        <router-link to="/verify">Verify</router-link>
        <router-link to="/login">Login</router-link>
      </nav>
    </header>
    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style>
.app-container {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #333;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #1a1a2e;
  color: #fff;
}
.navbar nav a {
  color: #fff;
  margin-left: 1.5rem;
  text-decoration: none;
}
.navbar nav a.router-link-active {
  font-weight: bold;
  color: #00d2d3;
}
.content {
  padding: 2rem;
}
</style>
