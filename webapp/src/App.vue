<template>
  <div class="container">
    <header>
      <h1>Droiche</h1>
      <p>Un sous titre à trouver...</p>
    </header>
    <div id="app">
      <section class="vote">
        <Vote />
      </section>
      <section class="results">
        <Results />
      </section>
    </div>
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
