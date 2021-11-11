<template>
  <div class="msg-container">
    <ul>
      <li
        v-for="(msg, i) in messages"
        :key="i"
        :class="msg.user === user ? 'msg-owner': 'msg-user'"
        class="msg"
      >
        <div>
          {{msg.message}}
          <small>{{msg.date}}</small>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',

  props: {
    messages: { type: Array, default: () => [] },
    user: { type: String, default: null }
  },

  setup() {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  display: flex;
  flex-direction: column;
  padding: 0;
}
li {
  display: block;
  margin: 0 10px 5px;
}
a {
  color: #42b983;
}

.msg-container {
  max-height: 250px;
  overflow-y: auto;
  scrollbar-width: none;
}

.msg-container::-webkit-scrollbar {
  width: 0;
}

.msg {
  height: 100%;
  display: block;
  padding: 5px 10px;
  border-radius: 5px;
}

.msg small {
  display: block;
  font-size: 0.6em;
  color: #cccccc;
}

.msg-owner {
  background-color: red;
  color: white;
  text-align: right;
}

.msg-user {
  background-color: blue;
  color: lime;
  text-align: left;
}
</style>
