<template>
  <div v-if="this.$store.state.previousSubject.content">
    <h2>De source sûre, {{ this.$store.state.previousSubject.content }}, c'est :</h2>
    <p>{{ this.$store.getters.winner }}</p>
    <div class="display">
      <div class='graph'>
        <div class="far-left data"
             v-bind:style="{ flex: this.$store.state.previousSubject.far_left_count}">
          <p>{{ this.$store.getters.previousPercentage('far_left_count')}}%</p>
        </div>
        <div class="left data"
             v-bind:style="{ flex: this.$store.state.previousSubject.left_count}">
          <p>{{ this.$store.getters.previousPercentage('left_count')}}%</p>
        </div>
        <div class="right data"
             v-bind:style="{ flex: this.$store.state.previousSubject.right_count}">
          <p>{{ this.$store.getters.previousPercentage('right_count')}}%</p>
        </div>
        <div class="far-right data"
             v-bind:style="{ flex: this.$store.state.previousSubject.far_right_count}">
          <p>{{ this.$store.getters.previousPercentage('far_right_count')}}%</p>
        </div>
      </div>
      <div class="details">
          <p>Sur la base de {{ this.$store.state.previousSubject.votes_count }} votes.</p>
          <p>
            <span v-on:click="thumbs('up')"
                  @mouseover="isUpActive = true" @mouseleave="isUpActive = false" >
              <i class="fa-thumbs-up red"
                 v-bind:class="[isUpActive || this.$store.state.thumbs.isUpSelected ? 'fas' : 'far']"></i>
              {{ this.$store.state.previousSubject.likes_count }}
            </span>
            <span v-on:click="thumbs('down')"
                  @mouseover="isDownActive = true" @mouseleave="isDownActive = false" >
              <i class="fa-thumbs-down blue"
                 v-bind:class="[isDownActive || this.$store.state.thumbs.isDownSelected ? 'fas' : 'far']"></i>
              {{ this.$store.state.previousSubject.dislikes_count }}
            </span>
          </p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Results",
    data () {
      return {
        isUpActive: false,
        isDownActive: false,
      }
    },
    methods: {
      thumbs: function(upDown) {
        if (upDown === 'up') {
          this.like()
        } else if (upDown === 'down') {
          this.unlike()
        }
      },
      like: function() {
        this.$store.dispatch('thumbsUp')
      },
      unlike: function() {
        this.$store.dispatch('thumbsDown')
      }
    },
    mounted () {},
  }
</script>
