<template>
    <div>
      <h2>Login</h2>
      <form>
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginView',
    data() {
      return {
        username: '',
        password: ''
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>