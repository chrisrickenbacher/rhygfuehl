<template>
    <div class="max-w-7xl mx-auto py-12 px-4 sm:py-16 sm:px-6 lg:px-8">
      <div class="max-w-3xl mx-auto divide-y divide-darkblue dark:divide-white">
        <h2 class="text-center text-2xl font-bold text-darkblue dark:text-white sm:text-4xl">
          {{$t('Frequently asked questions')}}
        </h2>
        <dl class="mt-6 space-y-6 divide-y divide-darkblue dark:divide-white">
            <div v-for="faq in faqs" :key="faq.question" class="pt-6">
                <dt class="text-lg">
                    <button @click="faq.isOpen=!faq.isOpen" type="button" class="text-left w-full flex justify-between items-start text-darkblue dark:text-white focus:outline-none">
                    <span class="font-medium text-darkblue dark:text-white">
                        {{dynamicVar($t(faq.question))}}
                    </span>
                    <span class="ml-6 h-7 flex items-center">
                        <span :class="[faq.isOpen ? '-rotate-180' : 'rotate-0']" class="material-icons h-6 w-6 transform">expand_more</span>
                    </span>
                    </button>
                </dt>
                <dd v-if="faq.isOpen" class="mt-2 pr-12" id="faq-0">
                    <p class="text-base text-darkblue dark:text-white">
                        {{dynamicVar($t(faq.answer))}}
                    </p>
                </dd>
            </div>
        </dl>
      </div>
    </div>
</template>

<script setup>
import { ref, reactive } from "vue"
const faqs = ref([
    {
        question: "How warm is the Rhine?",
        answer: "The Rhine in Basel currently has a water temperature of %waterTemp% °C.",
        isOpen: true
    },
    {
        question: "What is the air temperature on the Rhine in Basel?",
        answer: "The air temperature at the Rhine in Basel is currently %airTemp% °C.",
        isOpen: false
    }
])
const replacers = reactive([])


const collections = [
  {
    name: 'waterTemp',
    file: 'waterData.json',
    unit: '°C',
    description: 'Aktuelle Wassertemperatur',
    position: 1
  },
  {
    name: 'airTemp',
    file: 'airData.json',
    unit: '°C',
    description: 'Aktuelle Temperatur am Unteren Rheinweg',
    position: 2
  }
]

collections.forEach(c => {
  import(`./../../data/data/${c.file}`)
    .then(d => { replacers.push({
        code: `%${c.name}%`,
        replace: d.actualValue.toFixed(2)
    })})
});

const dynamicVar = (str) => {
    replacers.forEach(r => {
        str =  str.replace(r.code, r.replace);
    });
    return str
}
</script>
