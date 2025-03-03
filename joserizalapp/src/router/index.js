import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Landmarks from '../views/Landmarks.vue'
import AboutLandmarks from '../views/AboutLandmarks.vue'
import MapView from '../views/MapView.vue'
import Creators from '../views/Creators.vue'
import AdminPage from '../views/AdminPage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/landmarks',
    name: 'Landmarks',
    component: Landmarks
  },
  {
    path: '/landmarks/:id',
    name: 'AboutLandmarks',
    component: AboutLandmarks
  },
  {
    path: '/map',
    name: 'MapView',
    component: MapView
  },
  {
    path: '/creators',
    name: 'Creators',
    component: Creators
  },
  {
    path: '/admin',
    name: 'AdminPage',
    component: AdminPage
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
