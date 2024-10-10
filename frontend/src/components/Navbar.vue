<template>
    <aside class="sidebar">
      <h2>Dashboard</h2>
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/analytics">Analytics</router-link></li>
        <li><router-link to="/ai">AI Feature</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
      </ul>
    </aside>
  </template>
  
  <script>
  export default {};
  </script>
  
  <style scoped>
  .sidebar {
    width: 250px;
    background-color: #2c3e50;
    color: white;
    padding: 20px;
  }
  
  .sidebar h2 {
    color: #ecf0f1;
  }
  
  .nav-links {
    list-style-type: none;
    padding: 0;
  }
  
  .nav-links li {
    margin-bottom: 15px;
  }
  
  .nav-links a {
    text-decoration: none;
    color: #ecf0f1;
    font-size: 18px;
  }
  
  .nav-links a:hover {
    color: #3498db;
  }
  </style>
  