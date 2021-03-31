import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Home'
import Contact from '@/pages/Contact'
import Review from '@/pages/Review'
import About from '@/pages/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/review',
      name: 'Review',
      component: Review
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
  ]
})
