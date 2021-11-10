<template>
  <img
    alt="Vue logo"
    src="./assets/logo.png"
  >
  <HelloWorld :msg="msg" />
</template>

<script>
import { onMounted, ref } from 'vue';
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld
  },

  setup() {
    const msg = ref('Welcome to Your Vue.js Websocket App');

    const websocket = new WebSocket('wss:localhost:3900');

    onMounted(() => {
      websocket.send('any message');
    });

    return {
      msg
    };
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
