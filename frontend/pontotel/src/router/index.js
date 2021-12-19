import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/Login')
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('@/views/Register')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router