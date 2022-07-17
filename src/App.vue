<template>
  <metainfo>
    <template v-slot:title="{ content }">{{ content ? `${content}` : '' }}</template>
  </metainfo>
  <div :class="theme">
    <div class="min-h-screen dark:bg-darkblue bg-white">
      <div class="px-5 pt-4 flex items-center justify-between">
        <div class="flex-grow-0">
          <button type="button" @click="toggle()" class="inline-flex items-center justify-center dark:text-white light:text-darkblue focus:outline-none">
            <span class="sr-only">Open main menu</span>
            <span class="text-2xl h-6 w-6 material-icons">menu</span>
          </button>
        </div>
        <div class="flex-grow text-darkblue dark:text-white font-bold text-2xl mx-4">
          <h1><router-link :to="actualSection.path" >{{$t(actualSection.name)}}</router-link></h1>
        </div>
      </div>
      <MainNavigation :sections="sections" :sites="sites" />
      <router-view> </router-view>
      <footer class="mt-20 w-full text-center text-darkblue dark:text-white text-sm">
        <div>Support this project</div>
        <div class="inline-flex ">
          <span class="material-icons text-sm mr-2">open_in_new</span>
          <a class="underline" target="_blank" href="https://www.buymeacoffee.com/rhygfuehl">Buy me a coffee</a>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { useStore } from 'vuex';
import { computed, onBeforeMount, ref } from 'vue';
import { useRouter } from "vue-router";
import { useHead } from '@vueuse/head';
import { useI18n } from 'vue-i18n';
import MainNavigation from "./components/MainNavigation.vue";

const store = useStore()
const toggle = () => { store.commit('toggle') };

const router = useRouter();

const theme = computed(() => store.state.theme.theme);

onBeforeMount(() => {
   store.dispatch("initTheme");
})

const sections = computed(() => {
  const sr = []
  router.options.routes.forEach(r => {
    if(r['meta']){
      if ( r.meta.isSection === true ) {
          sr.push(r)
      }
    }
  })
  return sr
});

const actualSection = ref(sections.value[0])

const sites = computed(() => {
  const sr = []
  router.options.routes.forEach(r => {
    if(r['meta']){
      if ( r.meta.isSite === true ) {
          sr.push(r)
      }
    }
  })
  return sr
});

const { t } = useI18n({ useScope: 'global' })

useHead({
  title: computed(() => t('seo.title')),
  meta: [
    {
      name: `description`,
      content: computed(() => t('seo.description')),
    },
    { 
      name: 'keywords', 
      content: 'basel, rheintemperatur, rhein, rhy, schwimmen, wassertemperatur, temperatur'
    },
  ],
})

</script>