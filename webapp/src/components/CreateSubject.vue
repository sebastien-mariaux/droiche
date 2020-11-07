<template>
  <div>
    <h2>Ajouter un sujet</h2>
    <input
          type="text"
          placeholder="Add your subject here"
          v-model="content"
        >
    <button v-on:click="addSubject">Add</button>
  </div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import VueAxios from 'vue-axios'
  
  Vue.use(VueAxios, axios)
  
  export default {
    name: "CreateSubject",
    data() {
      return {
        content: "",
      };
    },
    http: {
      root: 'http://localhost:5000'
    },
    methods: {
      addSubject: function() {
        let formData = { "content": this.content }
        axios
        .post('http://localhost:5000/subjects/create', formData)
        .then(response => console.log(response))
        .catch(error => console.log(error))
      }
    }
  }
</script>