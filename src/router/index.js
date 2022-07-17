import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const routes = [
  {
    path: '/',
    name: 'bs_rhein',
    component: HomeView,
    meta: {
      isSection: true
    }
  },
  {
    path: '/imprint',
    name: 'imprint',
    component: () => import(/* webpackChunkName: "about" */ '../views/ImprintView.vue'),
    meta: {
      isSite: true
    }
  },
  {
    path: '/faq',
    name: 'faq',
    component: () => import(/* webpackChunkName: "about" */ '../views/FaqView.vue'),
  },
  {
    path: '/en',
    redirect: '/'
  },
  {
    path: '/en/:slug',
    redirect: to => {
      return to.params.slug
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
