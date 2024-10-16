<template>
  <body>
  <div class="login-container">
    <div class="form-container">
      <form class="form">
        <div class="input-group">
          <label for="username">
            Gebruikersnaam
          </label>
          <input id="username" type="text" placeholder="Gebruikersnaam">
        </div>
        <div class="input-group">
          <label for="password">
            Wachtwoord
          </label>
          <input id="password" type="password" placeholder="**********">
        </div>
        <div class="submit-container">
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
export default {
  name: 'LoginView'
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F6F8F7; /* Dark blue, police-blue */
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
  color: #003E7E; /* Dark blue, police-blue */
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
  background-color: #003E7E; /* Dark blue, police-blue */
  color: white;
  font-weight: bold;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-container button:hover {
  background-color: #002855; /* Darker shade for hover effect */
}

body {
  font-family: 'Roboto', sans-serif;
}

</style>
