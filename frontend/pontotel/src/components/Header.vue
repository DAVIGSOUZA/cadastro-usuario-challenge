<template>
  <header class="header mt-2 mb-3 px-2 py-1">
    <div>
      <b-nav class="justify-content-between align-items-center">
        <h1>Pontotel</h1>
        <div class="d-flex align-items-center">
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
export default {
  name: 'Header'
}
</script>

<style>
.header {
  background-color: lightgray;
}
</style>