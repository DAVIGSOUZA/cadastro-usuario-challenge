<template>
  <header class="header mt-md-3 mb-3 px-2 py-1">
    <div>
      <b-nav class="justify-content-between align-items-center">
        <h1>Pontotel</h1>

        <div v-if="userName" class="d-flex align-items-center">
          <p class="m-0">Olá {{userName}}</p>
          <b-nav-item>
            <router-link :to="{ name: 'Home' }">
              <span> Perfil </span>
            </router-link>
          </b-nav-item>
          <b-nav-item active @click="logout">
              <span> Logout </span>
          </b-nav-item>
        </div>

        <div v-else class="d-flex align-items-center">
          <p class="m-0">Olá visitante</p>
          <b-nav-item>
            <router-link :to="{ name: 'Register' }">
              <span> Cadastre-se </span>
            </router-link>
          </b-nav-item>
          <b-nav-item active>
            <router-link :to="{ name: 'Login' }">
              <span> Login </span>
            </router-link>
          </b-nav-item>
        </div>

      </b-nav>
    </div>
  </header>
</template>

<script>
import axios from "axios";
import { BASE_URL } from "../utils";

export default {
  name: 'Header',
  data() {
    return {
      userName: ''
    }
  },
  watch: {
    $route () {
      if (localStorage.token) {
        axios.get(`${BASE_URL}/profile`, {headers: {'x-access-token': localStorage.getItem('token')}})
          .then((res) => this.userName = res.data.name)
          .catch(() => this.userName = '')
      }
    }
  },
  methods: {
    logout() {
      localStorage.clear()
      this.userName = ''
      this.$router.push('/login')
    }
  }
  
}
</script>

<style>
.header {
  background-color: lightgray;
}
</style>