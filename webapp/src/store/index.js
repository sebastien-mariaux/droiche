
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
    urlRoot: 'http://localhost:5000/',
  },
  getters: {},
  mutations: {
    subject(state, payload) {
      state.subject = payload;
    },
    previousSubject(state, payload) {
      state.previousSubject = payload;
    }
  },
  actions: {
    getSubject({ commit, state }) {
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
  }
});

