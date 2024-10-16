<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/dashboard">Dashboard</router-link>
  </nav>
  <div class="dashboard-container">
    <!-- Sidebar stays static on all pages -->
    <!-- <Sidebar /> -->

    <!-- Main Content -->
    <div class="main-content">
      <!-- Top Bar stays static on all pages -->
      <TopBar />


      <!-- Dynamic content from Vue Router -->
      <router-view></router-view>
    </div>
  </div>

</template>

<script>
// import Sidebar from '@/components/Sidebar.vue';
import TopBar from '@/components/TopBar.vue';

export default {
  components: {

    TopBar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
