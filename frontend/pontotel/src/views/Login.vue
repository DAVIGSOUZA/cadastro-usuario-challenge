<template>
  <div class="p-3">
    <h2>Login</h2>
    <hr>
      <label for="email" class="d-block">Email: </label>
      <input 
        class="d-block w-100 p-1 mb-2" 
        name="email" 
        id="email" 
        v-model="email" 
        required
      />

      <label for="password" class="d-block">Password</label>
      <input 
        class="d-block w-100 p-1 mb-2" 
        type="password" 
        name="password" 
        id="password" 
        v-model="password" 
        required 
      />

      <button type="button" class="btn btn-primary px-3 mb-2" @click="login">Login</button>
    <div>
      <span>Ainda não tem cadastro? Faça </span>
      <router-link to="Register"> aqui</router-link>
    </div>
    <div class="alert alert-danger" role="alert" v-if="error">
      {{error}}
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { BASE_URL } from "../utils";

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    login: function () {
      const body = {
        email: this.email,
        password: this.password
      }
      axios.post(`${BASE_URL}/login`, body)
        .then(res => {
          this.error = ''
          localStorage.setItem('token', res.data.token)
          this.$router.push('/')
        })
        .catch(() => this.error = "Erro: verifique usuário e senha ou cadastre-se")
    }
  }
};
</script>

<style>
</style>