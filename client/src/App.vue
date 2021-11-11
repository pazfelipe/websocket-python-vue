<template>
  <img
    alt="Vue logo"
    src="./assets/logo.png"
  >
  <form style="display: block; display: flex; flex-direction: column; gap: 10px; width: 350px; margin: 0 auto;">
    <input
      v-model="user"
      placeholder="Insira um usuário"
      :readonly="userSelected"
      :disabled="userSelected"
    />

    <button
      @click.stop.prevent="onUserSelected"
      v-if="!userSelected"
      :disabled="!user"
    >Entrar</button>

    <div v-if="userSelected">
      <textarea
        v-model="message"
        placeholder="Envia sua mensagem"
        ref="msgRef"
        @keydown.enter.stop.prevent="send"
      />
      <button
        @click.stop.prevent="send"
        :disabled="!message || message.length < 3"
      >Send message</button>
    </div>
  </form>
  <div style="display:block;">
    <HelloWorld
      :messages="messages"
      :user="user"
    />

  </div>

</template>

<script>
import { nextTick, ref } from 'vue';
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld
  },

  setup() {
    const messages = ref([]);
    const user = ref(null);
    const message = ref(null);
    const socket = ref(null);
    const msgRef = ref(null);
    const userSelected = ref(false);

    const onConnected = () => {
      socket.value = new WebSocket('ws://localhost:5000/room1');

      socket.value.addEventListener('open', () => console.info('Connected to the server!!!'));

      socket.value.addEventListener('close', () => {
        socket.value.send(`User ${user.value} has been disconnected.`);
        console.warn('Disconnected from the server!!!');
      });

      socket.value.addEventListener('message', ({ data }) => {
        messages.value.push(JSON.parse(data));

        nextTick(() => {
          const container = document.querySelector('.msg-container');
          container.scrollTop = container.scrollHeight + 150;
        });
      });
    };


    const send = () => {
      socket.value.send(
        JSON.stringify({
          user: user.value,
          message: message.value,
          date: new Date()
        })
      );
      message.value = null;
      msgRef.value.focus();
    };

    const onUserSelected = () => {
      userSelected.value = true;
      onConnected();
      nextTick(() => {
        msgRef.value.focus();
      });
    };

    return {
      msgRef,
      messages,
      message,
      user,
      send,
      onConnected,
      userSelected,
      onUserSelected
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

form {
  display: block;
}

form div {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
