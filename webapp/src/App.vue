<template>
  
  <div id="app">
    <h1>Droiche</h1>
    <div class="row">
      <div class="col-md-4">
        <SubjectsList />
      </div>
      <div class="col-md-4">
        <!-- display topic -->
      </div>
      <div class="col-md-4">
        <CreateSubject />
      </div> 
    </div>
  </div>
</template>

<script>
  import CreateSubject from './components/CreateSubject.vue'
  import SubjectsList from './components/SubjectsList.vue'

  export default {
    name: 'App',
    components: {
      CreateSubject,
      SubjectsList,
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
