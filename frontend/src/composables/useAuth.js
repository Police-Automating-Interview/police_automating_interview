// src/composables/useAuth.js
import { reactive } from 'vue';

// This state is reactive and can be shared across components
const state = reactive({
  isAuthenticated: false
});

// Function to simulate login
function login() {
  state.isAuthenticated = true;  // Set isAuthenticated to true when user logs in
}

// Function to simulate logout
function logout() {
  state.isAuthenticated = false;  // Set isAuthenticated to false when user logs out
}

// The function exported here can be imported in any component
export default function useAuth() {
  return { state, login, logout };
}
