<template>
  <div v-if="this.$store.state.previousSubject.content">
    <h2>De source sûre, {{ this.$store.state.previousSubject.content }}, c'est :</h2>
    <div class="display">
      
      <div class='graph'>
        <div class="far-left results"
             v-bind:style="{ flex: this.$store.state.previousSubject.far_left_count}">
          <p>{{ this.$store.state.previousSubject.far_left_count }}</p>
        </div>
        <div class="left results"
             v-bind:style="{ flex: this.$store.state.previousSubject.left_count}">
          <p>{{ this.$store.state.previousSubject.left_count }}</p>
        </div>
        <div class="right results"
             v-bind:style="{ flex: this.$store.state.previousSubject.right_count}">
          <p>{{ this.$store.state.previousSubject.right_count }}</p>
        </div>
        <div class="far-right results"
             v-bind:style="{ flex: this.$store.state.previousSubject.far_right_count}">
          <p>{{ this.$store.state.previousSubject.far_right_count }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Results",
    methods: {
    },
    mounted () {},
  }
</script>
