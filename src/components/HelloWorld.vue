<template>
  <div class="hello">
    <h1>{{ this.msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'test',
    }
  },
  methods: {
    getExample() {
      axios.get('http://localhost:5000/example')
        .then((response) => {
          this.msg = response.data.msg;
        })
        .catch((error) => {
          console.log(error);
        })
    }
  },
  created() {
    this.getExample();
  }
}
</script>
