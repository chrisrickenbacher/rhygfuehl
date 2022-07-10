import { createStore } from "vuex"
import navigation from './modules/navigation'
import theme from './modules/theme'

const store = createStore({
  modules: {
    nav: navigation,
    theme
  }
})

export default store