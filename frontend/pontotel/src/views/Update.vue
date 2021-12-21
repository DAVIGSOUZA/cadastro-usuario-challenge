<template>
  <div class="p-3">
    <h2>Editar Cadastro</h2>
    <hr>
    <p>Campos com * são obrigatórios.</p>
    <form method="post" class="d-flex flex-column">

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

      <button type="button" class="btn btn-primary px-3 my-3" @click="update">Salvar Alterações</button>
      
      <p v-if="error" class="text-danger"> {{ error }} </p>

      <b-button 
        v-b-modal.delete 
        type="button" 
        class="btn btn-danger px-3 my-3" 
      >
        Apagar usuário
      </b-button>
    </form>

    <b-modal id="delete" title="Confirmar" hide-header-close @ok="deleteUser" >
      <p>Tem certeza que deseja apagar seus dados?</p>
      <p>Isso irá te deslogar da plataforma</p>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from "../utils"

export default {
  name: 'Update',
  data() {
    return {
      user: {},
      error: ''
    }
  },
  beforeMount() {
    axios.get(`${BASE_URL}/profile`, {headers: {'x-access-token': localStorage.getItem('token')}})
      .then((res) => this.user = res.data)
      .catch(() => {
        localStorage.clear()
        this.$router.push('/login')
      })
  },
  methods: {
    update() {
      axios.post(`${BASE_URL}/profile`, this.user, {headers: {'x-access-token': localStorage.getItem('token')}})
        .then(() => this.$router.push('/'))
        .catch((err) => this.error = err)
    },
    deleteUser() {
      axios.delete(`${BASE_URL}/profile`,{headers: {'x-access-token': localStorage.getItem('token')}})
        .then(() => {
          localStorage.clear()
          this.$router.push('/login')
        })
        .catch((err) => this.error = err)
    }
  }
  
};
</script>

<style>
</style>