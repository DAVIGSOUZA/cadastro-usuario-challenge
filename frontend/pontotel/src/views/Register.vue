<template>
  <div class="p-3">
    <h2>Cadastre-se</h2>
    <hr>
    <p>Campos com * são obrigatórios.</p>
    <form method="post" class="d-flex flex-column">

      <label for="email">Email*</label>
      <input type="email" name="email" id="email" required v-model="user.email"/>

      <label for="password">Senha*</label>
      <input type="password" name="password" id="password" required v-model="user.password"/>

      <label for="name">Nome*</label>
      <input name="name" id="name" required v-model="user.name"/>

      <label for="country">País*</label>
      <input name="country" id="country" required v-model="user.country"/>

      <label for="federal_state">Estado*</label>
      <input name="federal_state" id="federal_state" required v-model="user.federal_state"/>

      <label for="city">Cidade*</label>
      <input name="city" id="city" required v-model="user.city"/>

      <label for="cep">CEP*</label>
      <input name="cep" id="cep" required v-model="user.cep"/>

      <label for="street">Rua*</label>
      <input name="street" id="street" required v-model="user.street"/>

      <label for="residential_number">Número*</label>
      <input name="residential_number" id="residential_number" required v-model="user.residential_number"/>

      <label for="aditional_address_info">Complemento</label>
      <input name="aditional_address_info" id="aditional_address_info" v-model="user.aditional_address_info"/>

      <label for="cpf">CPF*</label>
      <input name="cpf" id="cpf" required v-model="user.cpf"/>

      <label for="pis">PIS*</label>
      <input name="pis" id="pis" required v-model="user.pis"/>

      <button type="button" class="btn btn-primary px-3 my-3" @click="register">Cadastrar</button>
      
      <p v-if="error" class="text-danger"> {{ error }} </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from "../utils"

export default {
  name: 'Register',
  data() {
    return {
      user: {},
      error: ''
    }
  },
  methods: {
    register() {
      // register and login user
      axios.post(`${BASE_URL}/register`, this.user)
        .then(() => {
          const body = {
            email: this.user.email,
            password: this.user.password
          }
          axios.post(`${BASE_URL}/login`, body)
            .then((res) => {
              this.error = ''
              localStorage.setItem('token', res.data.token)
              this.$router.push('/')
            })
            .catch((err) => this.error = err)
        })
        .catch((err) => this.error = err)
    },
  }
};
</script>

<style>
</style>