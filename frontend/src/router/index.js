import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import AnalyticsView from '@/views/AnalyticsView.vue'
import SettingsView from '@/views/SettingsView.vue'
import useAuth  from '@/composables/useAuth'



const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/analytics',
    name: 'analytics',
    component: AnalyticsView,
    meta: {
      requiresAuth: true
    }

  },
  {
    path: '/settings',
    name: 'settings',
    component: SettingsView
  }

]



const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const { state } = useAuth();
  if (to.meta.requiresAuth && !state.isAuthenticated) {
    next({ path: '/login' });
  } else {
    next();
  }
});

export default router
