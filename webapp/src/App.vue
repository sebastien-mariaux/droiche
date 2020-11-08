
<template>
  <div id="app">
    <section class="vote">
      <Vote />
    </section>
    <section class="results">
      <Results />
    </section>
  </div>
</template>

<script>
  import Vote from './components/Vote.vue'
  import Results from './components/Results.vue'

  export default {
    name: 'App',
    components: {
      Vote,
      Results,
    }
  }
</script>
