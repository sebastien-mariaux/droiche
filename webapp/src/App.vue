<template>
  <div id="app">
    <header>
      <h1>Droiche</h1>
    </header>
    <section class="vote">
      <Vote />
    </section>
  </div>
</template>

<script>
  import Vote from './components/Vote.vue'

  export default {
    name: 'App',
    components: {
      Vote,
    }
  }
</script>
