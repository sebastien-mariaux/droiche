<template>
  <div>
    <h2>« {{ subject.content }} »</h2>
    <p> C'est...</p>
    <div class="actions">
      <button v-on:click="sendVote('far_left')" class="far-left">
        D'extrême gauche
      </button>
      <button v-on:click="sendVote('left')" class=left>
        De gauche
      </button>
      <button v-on:click="sendVote('right')" class=right>
        De droite
      </button>
      <button v-on:click="sendVote('far_right')" class=far-right>
        D'extrême droite
      </button>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import VueAxios from 'vue-axios'
  
  Vue.use(VueAxios, axios)
    
  export default {
    name: "Vote",
    data() {
      return {
        subject: [],
        previousSubject: [],
      };
    },
    methods: {
      randomSubject: function() {
        axios
          .get('http://localhost:5000/subjects/random/')
          .then(response => (this.subject = response.data))
          .catch(error => console.log(error))
      },
      updatePreviousSubject: function(response) {
        this.previousSubject = response.data;
        this.subject = this.randomSubject();
      },
      sendVote: function(vote) {
        let formData = { "vote": vote };
        let url = `http://localhost:5000/subjects/${this.subject.id}/vote/`;
        axios
        .post(url, formData)
        .then(response => this.updatePreviousSubject(response))
        .catch(error => console.log(error))
      },
    },
    mounted () {
      this.randomSubject();
    },
  }
</script>
