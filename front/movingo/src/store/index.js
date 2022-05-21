import Vue from 'vue'
import Vuex from 'vuex'

import movies from './modules/movies'
import accounts from './modules/accounts'
import collections from './modules/collections'
import modal from './modules/modal'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, movies, collections, modal },
})