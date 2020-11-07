<template>
  <div>
    <h2>Liste des sujets</h2>
    <ul v-for='subject in subjects' :key=subject.id class="list-group">
      <li class="list-group-item">{{ subject.content }}</li>
    </ul>
    
  </div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import VueAxios from 'vue-axios'
  
  Vue.use(VueAxios, axios)
    
  export default {
    name: "SubjectsList",
    data() {
      return {
        subjects: [],
      };
    },
    computed: {
      subjects_count () {
        return this.subjects.length;
      }
    },
    mounted () {
      axios
      .get('http://localhost:5000/subjects')
      .then(response => (this.subjects = response.data['subjects']))
      .catch(error => console.log(error))
    },
  }
</script>