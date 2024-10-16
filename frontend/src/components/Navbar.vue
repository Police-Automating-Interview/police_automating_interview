<template>
  <body>
  <nav class="navbar">
    <h2>Politie Dashboard</h2> <!-- Translated "Dashboard" to Dutch -->
    <ul class="nav-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/analytics">Analyse</router-link></li> <!-- Translated "Analytics" to Dutch -->
      <li><router-link to="/ai">AI Functie</router-link></li> <!-- Translated "AI Feature" to Dutch -->
      <li><router-link to="/settings">Instellingen</router-link></li> <!-- Translated "Settings" to Dutch -->
    </ul>
  </nav>
  </body>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped>
.navbar {
  background-color: #003E7E;
  color: white;
  padding: 10px 20px; /* Adjusted padding for a balanced appearance */
  display: flex; /* Makes the navbar flex container */
  align-items: center; /* Centers the items vertically */
  justify-content: space-between; /* Separates title and links */
}

.navbar h2 {
  color: #F6F8F7;  /* Light color for contrast */
  margin: 0; /* Removes default margin */
}

.nav-links {
  display: flex; /* Aligns links horizontally */
  list-style-type: none; /* Removes bullet points */
  margin: 0; /* Removes default margin */
  padding: 0; /* Removes default padding */
}

.nav-links li {
  margin: 0 10px; /* Adds horizontal margin for separation */
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
