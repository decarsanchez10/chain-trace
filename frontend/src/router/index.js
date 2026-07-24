import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import DashboardView from '../views/DashboardView.vue'
import AssetDetailView from '../views/AssetDetailView.vue'
import VerifyView from '../views/VerifyView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  { path: '/', name: 'Landing', component: LandingView },
  { path: '/dashboard', name: 'Dashboard', component: DashboardView },
  { path: '/asset/:id', name: 'AssetDetail', component: AssetDetailView, props: true },
  { path: '/verify', name: 'Verify', component: VerifyView },
  { path: '/login', name: 'Login', component: LoginView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
