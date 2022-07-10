<template>
    <transition 
      enter-active-class="duration-200 ease-out"
      enter-class="opacity-0" 
      enter-to-class="opacity-100" 
      leave-active-class="transition duration-300 ease-out" 
      leave-class="opacity-100" 
      leave-to-class="opacity-0" 
      appear>
      <div class="absolute top-0 inset-x-0 p-2 transform origin-top-right z-50 md:max-w-2xl" v-if="isOpen" >
          <div class="rounded-lg shadow-md dark:bg-white bg-darkblue overflow-hidden">
            <div class="px-2 pt-2 flex items-center justify-between">
              <div class="flex-grow">
                <button type="button" @click="toggle" class="inline-flex items-center justify-center text-white dark:text-darkblue focus:outline-none">
                  <span class="sr-only">Close main menu</span>
                  <span class="text-2xl w-8 h-8 material-icons">close</span>
                </button>
              </div>
              <div class="flex-grow-0 self-center h-full">
                <button type="button" @click="colorMode" :class="[theme==='dark' ? 'bg-darkblue'  : 'bg-white']" class="relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-white dark:border-darkblue rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none" aria-pressed="false">
                  <span class="sr-only">Dark mode</span>
                  <span :class="[theme==='dark' ? 'translate-x-5'  : 'translate-x-0']"  class="pointer-events-none relative inline-block h-5 w-5 rounded-full bg-darkblue dark:bg-white shadow-md transform ring-0 transition ease-in-out duration-100">
                    <span :class="[theme==='dark' ? 'opacity-0 ease-out duration-100'  : 'opacity-100 ease-in duration-200']" class="absolute inset-0 h-full w-full flex items-center justify-center transition-opacity" aria-hidden="true">
                      <span class="text-sm text-white dark:text-darkblue material-icons">dark_mode</span>
                    </span>
                    <span :class="[theme==='dark' ? 'opacity-100 ease-in duration-200'  : 'opacity-0 ease-out duration-100']" class="absolute inset-0 h-full w-full flex items-center justify-center transition-opacity" aria-hidden="true">
                      <span class="text-sm	text-white dark:text-darkblue material-icons">dark_mode</span>
                    </span>
                  </span>
                </button>
              </div>
            </div>
            <div class="flex flex-col space-y-2 mt-2 mb-3 px-3">
              <div v-for="(s, sIdx) in sections" :key="sIdx">
                <router-link :to="{name: s.name}" class="rounded-md text-2xl font-bold text-white dark:text-darkblue">{{$t(s.name)}}</router-link>
              </div>
            </div>
            <div class="flex flex-row space-x-2 px-3 mt-2 mb-3">
              <div class="flex-grow">
                <div v-for="(s, sIdx) in sites" :key="sIdx">
                  <router-link :to="{ name: s.name} " class="py-2 font-thin rounded-md text-base underline text-white dark:text-darkblue">{{$t(s.name)}}</router-link>
                </div>
              </div>
              <div class="flex-grow-0 flex flex-row space-x-2">
                <div v-for="(l, lIdx) in lang" :key="lIdx" class="uppercase">
                  <a href="#" @click.prevent="$i18n.locale = l" :class="[l === $i18n.locale ? 'font-bold' : '']" class="text-white dark:text-darkblue">{{l}}</a>
                </div>
              </div>
            </div>
          </div>
      </div>
    </transition>
</template>

<script setup>
import { useStore } from 'vuex';
import { defineProps, computed } from 'vue';

// eslint-disable-next-line
const props = defineProps({
  sections: Array,
  sites: Array
});

const lang = ['de', 'en']

const store = useStore()
const isOpen = computed(() => store.state.nav.isOpen )
const theme = computed(() => store.state.theme.theme)

const toggle = () => { store.commit('toggle') };
const colorMode = () => { store.dispatch("toggleTheme") };

</script>
