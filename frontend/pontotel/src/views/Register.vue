<template>
  <div class="p-3">
    <h2 v-if="user.name">Editar Cadastro</h2>
    <h2 v-else>Cadastre-se</h2>
    <hr>
    <p>Campos com * são obrigatórios.</p>
    <form method="post" class="d-flex flex-column">
      <label for="email">Email*</label>
      <input type="email" name="email" id="email" required />
      <label for="password">Senha*</label>
      <input type="password" name="password" id="password" required />
      <label for="name">Nome*</label>
      <input name="name" id="name" required />
      <label for="country">País*</label>
      <input name="country" id="country" required />
      <label for="federal_state">Estado*</label>
      <input name="federal_state" id="federal_state" required />
      <label for="city">Cidade*</label>
      <input name="city" id="city" required />
      <label for="cep">CEP*</label>
      <input name="cep" id="cep" required />
      <label for="street">Rua*</label>
      <input name="street" id="street" required />
      <label for="residential_number">Número*</label>
      <input name="residential_number" id="residential_number" required />
      <label for="aditional_address_info">Complemento</label>
      <input name="aditional_address_info" id="aditional_address_info" />
      <label for="cpf">CPF*</label>
      <input name="cpf" id="cpf" required />
      <label for="pis">PIS*</label>
      <input name="pis" id="pis" required />

      <input type="submit" value="Cadastrar" class="mt-3"/>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
// import { BASE_URL } from "../utils"

export default {
  name: 'Register',
  data() {
    return {
      user: {}
    }
  },
};
</script>

<style>
</style>