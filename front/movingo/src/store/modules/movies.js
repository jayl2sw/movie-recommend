import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'



export default {
    // namespaced: true,
    state: {
      movies: [],
      movie: {},
      reviews: [],
      trailerURI: "",
    },
  
    getters: {
      movies: state => state.movies,
      movie: state => state.movie,
      reviews: state => state.reviews,
      trailerURI: state => state.trailerURI,
      // isAuthor: (state, getters) => {
      //   return state.movie.user?.username === getters.currentUser.username
      // },
      isMovie: state => !_.isEmpty(state.movie),
    },
  
    mutations: {
      SET_MOVIES: (state, movies) => state.movies1 = movies,
      SET_MOVIE: (state, movie) => state.movie = movie,
      SET_REVIEWS: (state, reviews) => state.reviews = reviews,
      SET_trailerURI: (state, trailerURI) => state.trailerURI = trailerURI,
      SET_MOVIE_REVIEW: (state, comments) => (state.movie.comments = comments),
    },
  
    actions: {
      fetchMovies({ commit, getters }, { list, page, keyword}) {
        /* 게시글 목록 받아오기
        GET: articles URL (token)
          성공하면
            응답으로 받은 게시글들을 state.articles에 저장
          실패하면
            에러 메시지 표시
        */
        let query = "?"
        if (page) {
          query += `page=${page}`
        }
        if (keyword) {
          query += `keyword=${keyword}`
        }

        axios({
          url: drf.movies.movies()+query,
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit(`SET_MOVIES${list}`, res.data)
          })
          .catch(err => console.error(err.response))
      },

      fetchMovie({ commit, getters }, moviePk) {
        /* 단일 게시글 받아오기
        GET: article URL (token)
          성공하면
            응답으로 받은 게시글들을 state.articles에 저장
          실패하면
            단순 에러일 때는
              에러 메시지 표시
            404 에러일 때는
              NotFound404 로 이동
        */
        axios({
          url: drf.movies.movie(moviePk),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            console.log(res.data)
            commit('SET_MOVIE', res.data)
          })
            
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      },
      
      fetchcollection({ commit, getters }, collection_pk) {
        /* 게시글 목록 받아오기
        GET: articles URL (token)
          성공하면
            응답으로 받은 게시글들을 state.articles에 저장
          실패하면
            에러 메시지 표시
        */

        axios({
          url: drf.collections.collection(collection_pk),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIES4', res.data.movies)
            commit('SET_MOVIES4TITLE', res.data.title)
          })
          .catch(err => console.error(err.response))
      },
      
      fetchTrailerURI({ commit }, keyword) {
        /* 게시글 목록 받아오기
        GET: articles URL (token)
          성공하면
            응답으로 받은 게시글들을 state.articles에 저장
          실패하면
            에러 메시지 표시
        */

        // const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
        const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        commit('SET_trailerURI', '')
        const params = {
            part: 'snippet',
            type: 'video',
            key: 'AIzaSyD37bRUcl9fOP48kunhwm2i8Gj8cOclAHg',
            q: keyword + ' trailer',
          }
        axios.get(API_URL,{params})
        .then(res => {
          console.log(res.data, res.data.items[0])
          commit('SET_trailerURI', `https://www.youtube.com/embed/${res.data.items[0].id.videoId}`)
        })
        .catch(err => {
          console.log(err)
        })
      },
      fetchReviews({ commit, getters }, moviePk) {
        axios({
          url: drf.movies.reviews(moviePk),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          console.log("log", res.data)
          commit()
          // commit('', res.data)
        }) 
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
      }
    }
  }
