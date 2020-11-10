
import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    subject: [],
    previousSubject: [],
    urlRoot: process.env.VUE_APP_API_URL,
    thumbs: {
      isUpSelected: false,
      isDownSelected: false,
    }
  },
  getters: {
    totalVote: () => (subject) => {
      return subject.far_left_count + subject.left_count+ 
      subject.right_count + subject.far_right_count
    },
    previousPercentage: (state, getters) => ( orientation) => {
      return getters.percentage(state.previousSubject, orientation)
    },
    percentage: (state, getters) => (subject, orientation) => {
      return Math.round(subject[orientation] / 
             getters.totalVote(subject) * 100)
    },
    maxVote: () => (subject) =>  {
      return Math.max(subject.far_left_count, subject.left_count, 
                      subject.right_count, subject.far_right_count)
    },
    winner: (state, getters) => {
      let winner = "";
      ['far_left_count', 'left_count', 
       'right_count', 'far_right_count'].forEach( function(side) {
                if (state.previousSubject[side] == getters.maxVote(state.previousSubject))  {
                  if (winner.length) { winner = 'unclear' } else { winner = side }
                }
              })
      return getters.mapWinner(winner);
    },
    currentThumb: (state) => () => {
      if (state.thumbs.isUpSelected) { return 'up' }
      if (state.thumbs.isDownSelected) { return 'down' }
      return null ;
    },
    mapWinner: () => (winner) => {
      let text = "";
      switch(winner) {
        case 'far_left_count':
          text = "d'extrême gauche !"
          break;
        case 'left_count':
          text = "de gauche !"
          break;
        case 'right_count':
          text = "de droite !"
          break;
        case 'far_right_count':
          text = "d'extrême droite !"
          break;
        default: 
          text = 'indeterminé...'
      } 
      return text;
    }
  },  
  mutations: {
    subject(state, payload) {
      state.subject = payload;
    },
    previousSubject(state, payload) {
      state.previousSubject = payload;
      state.thumbs.isDownSelected = false;
      state.thumbs.isUpSelected = false;
    },
    thumbsUp(state) {
      state.thumbs.isUpSelected = true;
      state.thumbs.isDownSelected = false;
    },
    thumbsDown(state) {
      state.thumbs.isUpSelected = false;
      state.thumbs.isDownSelected = true;
    }
  },
  actions: {
    getSubject({ commit, state }) {
      console.log(typeof(state.urlRoot))
      axios
        .get(`${state.urlRoot}subjects/random/`)
        .then(response => commit("subject", response.data))
        .catch(error => console.log(error))
    },
    sendVote({ commit, state, dispatch }, payload) {
      let url = `${state.urlRoot}subjects/${state.subject.id}/vote/`;
      axios
        .post(url, payload)
        .then(function (response) {
          commit("previousSubject", response.data);
          dispatch("getSubject");
        })
        .catch(error => console.log(error))
    },
    thumbsUp({state, commit, getters}) {
      let url = `${state.urlRoot}subjects/${state.previousSubject.id}/thumbs/`;
      axios
        .post(url, {'thumb': 'up', 'previous_thumb': getters.currentThumb()})
        .then(function (response) {
          commit("previousSubject", response.data);
          commit("thumbsUp")
        })
        .catch(error => console.log(error))
    },
    thumbsDown({state, commit, getters}) {
      let url = `${state.urlRoot}subjects/${state.previousSubject.id}/thumbs/`;
      axios
        .post(url, {'thumb': 'down', 'previous_thumb': getters.currentThumb()})
        .then(function (response) {
          commit("previousSubject", response.data);
          commit("thumbsDown")
        })
        .catch(error => console.log(error))
    },
  }
});

