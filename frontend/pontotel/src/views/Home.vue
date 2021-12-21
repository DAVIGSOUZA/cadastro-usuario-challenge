<template>
  <div class="p-3">
    <h2>{{ user.name }}</h2>
    <router-link to="Register"> Editar</router-link>
    <hr>
    <div>
      <h2>Informações pessoais</h2>
      <p class="body">Email: {{ user.email }}</p>
      <p class="body">CPF: {{ user.cpf }}</p>
      <p class="body">PIS: {{ user.pis }}</p>
    </div>
    <div>
      <h2>Endereço</h2>
      <p class="body">País: {{ user.country }}</p>
      <p class="body">Estado: {{ user.federal_state }}</p>
      <p class="body">Cidade: {{ user.city }}</p>
      <p class="body">CEP: {{ user.cep }}</p>
      <p class="body">Rua: {{ user.street }}</p>
      <p class="body">Número: {{ user.residential_number }}</p>
      <p class="body">Complemento: {{ user.aditional_address_info }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from "../utils"

export default {
  name: 'Home',
  data() {
    return {
      user: {}
    }
  },
  beforeMount() {
    axios.get(`${BASE_URL}/profile`, {headers: {'x-access-token': localStorage.getItem('token')}})
      .then((res) => this.user = res.data)
      .catch(() => this.$router.push('/login'))
  }
};
</script>

<style>
</style>