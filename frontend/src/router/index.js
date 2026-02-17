import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return {
        el: to.hash,
        top: 96,
        behavior: 'smooth'
      }
    }
    return { left: 0, top: 0 }
  },
  routes: [
    { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
    { path: '/about', name: 'about', component: () => import('../views/AboutView.vue') },
    { path: '/moose', name: 'moose', component: () => import('../views/MooseView.vue') },
    { path: '/volunteer', name: 'volunteer', component: () => import('../views/VolunteerView.vue') },
    { path: '/running-club', name: 'running-club', component: () => import('../views/RunningClubView.vue') },
    { path: '/bronze-club', redirect: '/running-club' },
    { path: '/schedule', name: 'schedule', component: () => import('../views/ScheduleView.vue') },
    { path: '/articles', name: 'articles', component: () => import('../views/ArticlesView.vue') },
    { path: '/articles/:id', name: 'article-single', component: () => import('../views/ArticlesSingleView.vue') },
    { path: '/news', name: 'news', component: () => import('../views/NewsView.vue') },
    { path: '/news/:id', name: 'news-single', component: () => import('../views/NewsSingleView.vue') },
    { path: '/services/:slugPath(.*)', name: 'service-detail', component: () => import('../views/ServiceDetailView.vue') },
    { path: '/contacts', name: 'contacts', component: () => import('../views/ContactsView.vue') },
    { path: '/privacy', name: 'privacy', component: () => import('../views/PrivacyView.vue') },
    { path: '/terms', name: 'terms', component: () => import('../views/TermsView.vue') },
    { path: '/brotherhood', redirect: '/moose' },
    { path: '/:pathMatch(.*)*', redirect: '/' }
  ]
})

export default router
