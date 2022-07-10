export default {
    state: {
        isOpen: false,
    },
    mutations: {
        toggle (state) {
            state.isOpen = !state.isOpen
        }
    }
}