<template>
  <div>
    <h2>« {{ this.$store.state.subject.content }} »</h2>
    <p> C'est...</p>
    <div class="omega actions">
      <div v-on:click="sendVote('far_left')" 
           class="btn far-left btn-primary">
        <p>D'extrême gauche</p>
      </div>
      <div v-on:click="sendVote('left')" 
           class="btn left btn-tertiary">
        <p>De gauche</p>
      </div>
      <div v-on:click="sendVote('right')" 
           class="btn right btn-tetrary">
        <p>De droite</p>
      </div>
      <div v-on:click="sendVote('far_right')" 
           class="btn far-right btn-secondary">
        <p>D'extrême droite</p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Vote",
    methods: {
      sendVote: function(vote) {
        this.$store.dispatch( "sendVote", { vote: vote } );
      },
    },
    mounted () {
      this.$store.dispatch("getSubject");
    },
  }
</script>
