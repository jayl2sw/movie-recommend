const HOST = 'http://localhost:8000/api/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
// const REVIEW = 'review/'
const REVIEWS = 'reviews/'
const COLLECTIONS = 'collections/'
// const BINGOS = 'bingos/'
// const COMMUNITY = 'community/'
const LIKE = 'like/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}`,
    followuser: userPk => HOST + ACCOUNTS + 'profile/' + `${userPk}/` + 'follow/',
  },
  movies: {
    // /articles/
    
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}`,
    wishMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'wish',
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    // review: (articlePk, commentPk) =>
    //   HOST + MOVIES + `${articlePk}/` + REVIEWS + `${commentPk}/`,
  },
  collections: {
    collection_list: () => HOST + COLLECTIONS,
    main_collections: () => HOST + COLLECTIONS +  'main',
    collection_detail: collectionPk => HOST + COLLECTIONS + `${collectionPk}`,
    like_collection: collectionPk => HOST + COLLECTIONS + `${collectionPk}/` + LIKE
  }
}
