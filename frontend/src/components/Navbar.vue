<template>
  <body>
  <nav class="navbar">
    <h2>Politie Dashboard</h2> 
    <ul class="nav-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link v-if="auth.state.isAuthenticated" to="/analytics">Analyse</router-link></li> 
      <li><router-link v-if="auth.state.isAuthenticated" to="/ai">AI Functie</router-link></li>
      <li><router-link v-if="auth.state.isAuthenticated" to="/settings">Instellingen</router-link></li> 
      <button v-if="auth.state.isAuthenticated" @click="auth.logout">Logout</button>
    </ul>
  </nav>
  </body>
</template>

<script>
import useAuth from '@/composables/useAuth';

export default {
  name: 'NavBar',
  setup() {
    const auth = useAuth();
    return { auth };
  }
};
</script>

<style scoped>
.navbar {
  background-color: #003E7E;
  color: white;
  padding: 10px 20px; 
  display: flex; 
  align-items: center; 
  justify-content: space-between; 
}

.navbar h2 {
  color: #F6F8F7;  
  margin: 0; 
}

.nav-links {
  display: flex; 
  list-style-type: none; 
  margin: 0; 
  padding: 0; 
}

.nav-links li {
  margin: 0 10px; 
}

.nav-links li:hover{
  background-color: white;
}

.nav-links a {
  text-decoration: none;
  color: #F6F8F7; 
  font-size: 14px;
}

.nav-links a:hover {
  color: #3498db; 
}

body {
  font-family: 'Roboto', sans-serif;
}

</style>
