import './assets/index.css';
import { createApp } from 'vue';
import App from './App.vue';
import './registerServiceWorker'
import router from './router'
import store from './store/index';
import { createHead } from '@vueuse/head'
import { createI18n } from 'vue-i18n';
import en from './locales/en.json'
import de from './locales/de.json'
import VueGtag from "vue-gtag";

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
    .use(createHead())
    .use(VueGtag, {
        config: { id: "G-84G53SESL5" }
    })
    .use(i18n)
    .mount('#app')
