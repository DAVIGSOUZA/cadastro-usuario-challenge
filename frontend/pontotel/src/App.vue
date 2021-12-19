<template>
  <div id="app">
    <div>
      <Header/>
      <div>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  name: 'App',
  components: {
    Header    
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 600px;
  margin: 0 auto;
}
</style>
