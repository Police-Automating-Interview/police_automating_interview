<template>
  <body>
    <div class="login-container">
      <div class="form-container">
        <!-- Updated form tag to include method and event listener for submit -->
        <form class="form" @submit.prevent="login">
          <div class="input-group">
            <label for="username">
              Gebruikersnaam
            </label>
            <!-- Added v-model to bind username -->
            <input id="username" type="text" placeholder="Gebruikersnaam" v-model="username">
          </div>
          <div class="input-group">
            <label for="password">
              Wachtwoord
            </label>
            <!-- Added v-model to bind password -->
            <input id="password" type="password" placeholder="**********" v-model="password">
          </div>
          <div class="submit-container">
            <!-- Changed button type to submit -->
            <button type="submit">
              Inloggen
            </button>
          </div>
        </form>
      </div>
    </div>
  </body>
</template>

<script>
import axios from 'axios';
import useAuth from '@/composables/useAuth';

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      errors: ''
    };
  },
  methods: {
    login() {
      const { login: setLogin } = useAuth();  // Accessing the login method from useAuth
      axios.post('http://localhost:8000/api/login/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log('Complete response:', response);
        console.log('Login successful:', response.data);
        setLogin();  // Update the global state to reflect the user is authenticated
        this.$router.push('/analytics');
      })
      .catch(error => {
        console.error('Login error:', error.response.data);
        this.errors = error.response.data.detail || 'Failed to login. Please try again.';
      });
    }
  }
}
</script>



<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F6F8F7; 
  color: white;
}

.form-container {
  width: 100%;
  max-width: 400px;
}

.form {
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
  padding: 2rem;
  margin-bottom: 1rem;
}

.input-group {
  margin-bottom: 1rem;
}

.input-group label {
  display: block;
  color: #003E7E; 
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.input-group input {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.06);
  border: 1px solid #ddd;
  border-radius: 0.375rem;
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  color: gray;
  outline: none;
}

.submit-container {
  display: flex;
  justify-content: flex-end;
}

.submit-container button {
  background-color: #003E7E; 
  color: white;
  font-weight: bold;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-container button:hover {
  background-color: #002855; 
}

body {
  font-family: 'Roboto', sans-serif;
}

</style>
