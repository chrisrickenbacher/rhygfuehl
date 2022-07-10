import './assets/index.css';
import { createApp } from 'vue';
import App from './App.vue';
import './registerServiceWorker'
import router from './router'
import store from './store/index';
import { createI18n } from 'vue-i18n';
import en from './locales/en.json'
import de from './locales/de.json'

const i18n = createI18n({
    legacy: false,
    locale: 'de',
    fallbackLocale: 'de',
    messages: { en: en, de: de},
    globalInjection: true
})

createApp(App)
    .use(router)
    .use(store)
    .use(i18n)
    .mount('#app')
