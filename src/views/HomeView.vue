<template>
  <div class="mt-5 md:max-w-screen-md md:mx-auto">
    <div
      v-if="refresh"
      class="text-center fixed bottom-0 w-full md:static mb-20 md:mb-2"
    >
      <button
        @click="refreshNow"
        type="button"
        class="inline-flex items-center px-6 py-3 border rounded-full shadow-xl text-white dark:text-darkblue bg-darkblue dark:bg-white"
      >
        <span class="material-icons -ml-1 mr-3">refresh</span>
        Refresh data
      </button>
    </div>
    <main class="p-2 grid grid-cols-1 md:grid-cols-2">
      <section v-for="(d, dIdx) in data" :key="dIdx" class="mb-5">
        <div
          class="flex text-2xl font-normal text-darkblue dark:text-white p-2"
        >
          <h2>{{ $t(d.name) }}</h2>
          <div class="flex content-start">
            <div
              v-if="d.isBeta"
              class="dark:bg-white bg-darkblue rounded-full dark:text-darkblue text-white px-3 py-1 text-xs uppercase font-bold ml-2 h-min"
            >
              Beta
            </div>
          </div>
        </div>

        <!-- Measurement -->
        <transition
          v-if="d.layout === 'measurement'"
          leave-active-class="transition ease-out duration-50"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <div
            :class="[d.name === currentSection ? 'mx-0' : 'mx-2']"
            class="transition-all duration-100 p-3 flex flex-col bg-darkblue dark:bg-white rounded-lg"
          >
            <transition
              enter-active-class="transition ease-out duration-500"
              enter-from-class="opacity-0"
              enter-to-class="opacity-100"
            >
              <div v-if="d.name === currentSection" class="mb-2">
                <div class="flex mb-2">
                  <nav class="flex-grow flex space-x-2" aria-label="Tabs">
                    <a
                      v-for="t in timeseries"
                      :key="t.name"
                      @click="currentTime = t.name"
                      :class="[
                        t.name === currentTime
                          ? 'bg-gray-200'
                          : 'text-white dark:text-darkblue hover:text-darkblue hover:bg-gray-100',
                        'text-darkblue px-2 py-1 text-xs rounded-full',
                      ]"
                      :aria-current="
                        t.name === currentTime ? 'page' : undefined
                      "
                    >
                      {{ $t(t.name) }}
                    </a>
                  </nav>
                  <div
                    class="flex-0 text-white dark:text-darkblue text-xs font-thin"
                  >
                    Updated: {{ formatDate(d.lastUpdate) }}h
                  </div>
                </div>
                <line-chart
                  :data="d.chart[currentTime]"
                  :ticks="yLabel(d.chart[currentTime], 'num')"
                  :labels="{
                    yLabels: yLabel(d.chart[currentTime], 'num'),
                    yLabelsTextFormatter: (val) => Math.round(val),
                  }"
                  :min="yLabel(d.chart[currentTime], 'min')"
                  :max="yLabel(d.chart[currentTime], 'max')"
                >
                </line-chart>
                <div class="mt-4 text-white dark:text-darkblue">
                  {{ $t(d.description) }}
                </div>
              </div>
            </transition>
            <div class="flex flex-row">
              <div
                class="flex-grow text-white dark:text-darkblue text-4xl font-thin"
              >
                {{ formatNumber(d.actualValue) }} {{ d.unit }}
              </div>
              <div class="flex-grow-0 items-baseline align-middle">
                <span
                  v-if="d.name === currentSection"
                  @click="currentSection = null"
                  class="material-icons text-white dark:text-darkblue align-middle leading-10 rounded-full"
                  >unfold_less</span
                >
                <span
                  v-if="d.name != currentSection"
                  @click="currentSection = d.name"
                  class="material-icons text-white dark:text-darkblue align-middle leading-10 hover:bg-gray-200 focus:bg-none rounded-full"
                  >unfold_more</span
                >
              </div>
            </div>
          </div>
        </transition>

        <!-- Quality -->
        <transition
          v-else-if="d.layout === 'quality'"
          leave-active-class="transition ease-out duration-50"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <div
            :class="[d.name === currentSection ? 'mx-0' : 'mx-2']"
            class="transition-all duration-100 p-3 flex flex-col bg-darkblue dark:bg-white rounded-lg"
          >
            <transition
              enter-active-class="transition ease-out duration-500"
              enter-from-class="opacity-0"
              enter-to-class="opacity-100"
            >
              <div v-if="d.name === currentSection" class="mb-2">
                <div class="flex mb-2">
                  <nav class="flex-grow flex space-x-2" aria-label="Tabs">
                    <a
                      v-for="t in timeseries"
                      :key="t.name"
                      @click="currentTime = t.name"
                      :class="[
                        t.name === currentTime
                          ? 'bg-gray-200'
                          : 'text-white dark:text-darkblue hover:text-darkblue hover:bg-gray-100',
                        'text-darkblue px-2 py-1 text-xs rounded-full',
                      ]"
                      :aria-current="
                        t.name === currentTime ? 'page' : undefined
                      "
                    >
                      {{ $t(t.name) }}
                    </a>
                  </nav>
                  <div
                    class="flex-0 text-white dark:text-darkblue text-xs font-thin"
                  >
                    Updated: {{ formatDate(d.lastUpdate) }}h
                  </div>
                </div>
                <div v-for="m in d.data" :key="m.measure">
                  <div class="mt-4 text-white dark:text-darkblue">
                    {{ $t(m.measure) }}
                  </div>
                  <line-chart
                    :data="m.chart[currentTime]"
                    :ticks="yLabel(m.chart[currentTime], 'num')"
                    :labels="{
                      yLabels: yLabel(m.chart[currentTime], 'num'),
                      yLabelsTextFormatter: (val) => Math.round(val),
                    }"
                    :min="yLabel(m.chart[currentTime], 'min')"
                    :max="yLabel(m.chart[currentTime], 'max')"
                  >
                  </line-chart>
                </div>
                <div class="mt-4 text-white dark:text-darkblue">
                  {{ $t(d.description) }}
                </div>
              </div>
            </transition>
            <div class="flex flex-row gap-2">
              <div
                class="flex-grow text-white dark:text-darkblue text-4xl font-thin"
              >
                {{
                  d.quality == 1
                    ? $t("bad")
                    : d.quality == 2
                    ? $t("good")
                    : $t("perfect")
                }}
              </div>
              <div
                class="flex flex-row justify-center text-center content-center basis-1/3"
              >
                <div
                  class="flex items-center justify-center basis-1/3 rounded-l-lg"
                  :class="
                    d.quality == 1
                      ? 'dark:bg-darkblue bg-white rounded-lg text-darkblue dark:text-white'
                      : 'dark:bg-darkblue/10 bg-white/10 dark:border-white border-darkblue border-4 text-white dark:text-darkblue'
                  "
                >
                  1
                </div>
                <div
                  class="flex items-center justify-center basis-1/3"
                  :class="
                    d.quality == 2
                      ? 'dark:bg-darkblue bg-white rounded-lg text-darkblue dark:text-white'
                      : 'dark:bg-darkblue/10 bg-white/10 dark:border-white border-darkblue border-4 text-white dark:text-darkblue'
                  "
                >
                  2
                </div>
                <div
                  class="flex items-center justify-center basis-1/3 rounded-r-lg"
                  :class="
                    d.quality == 3
                      ? 'dark:bg-darkblue bg-white rounded-lg text-darkblue dark:text-white'
                      : 'dark:bg-darkblue/10 bg-white/10 dark:border-white border-darkblue border-4 text-white dark:text-darkblue'
                  "
                >
                  3
                </div>
              </div>

              <div class="flex-grow-0 items-baseline align-middle">
                <span
                  v-if="d.name === currentSection"
                  @click="currentSection = null"
                  class="material-icons text-white dark:text-darkblue align-middle leading-10 rounded-full"
                  >unfold_less</span
                >
                <span
                  v-if="d.name != currentSection"
                  @click="currentSection = d.name"
                  class="material-icons text-white dark:text-darkblue align-middle leading-10 hover:bg-gray-200 focus:bg-none rounded-full"
                  >unfold_more</span
                >
              </div>
            </div>
          </div>
        </transition>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, onBeforeMount } from "vue";
import LineChart from "./../components/LineChart.vue";
import moment from "moment";
import numeral from "numeral";

const timeseries = ref([
  {
    name: "week",
  },
  {
    name: "month",
  },
]);

const collections = [
  {
    name: "waterTemp",
    layout: "measurement",
    file: "waterData.json",
    unit: "°C",
    description: "Current water temperature",
    position: 1,
  },
  // {
  //   name: 'waterQuality',
  //   isBeta: true,
  //   layout: 'quality',
  //   file: 'qualityData.json',
  //   description: 'Current water quality for swimming based on sunshine and rain over the last few days.',
  //   position: 2
  // },
  {
    name: "airTemp",
    layout: "measurement",
    file: "airData.json",
    unit: "°C",
    description: "Current temperature at Mittlere Brücke",
    position: 3,
  },
  {
    name: "waterLevel",
    layout: "measurement",
    file: "levelData.json",
    unit: "m",
    description: "Level in m.a.s.l. or deviation from the last annual average",
    position: 4,
  },
];

const currentTime = ref("month");
const currentSection = ref(null);
const view = ref({
  atTopOfPage: true,
});

const data = reactive([]);
collections.forEach((c) => {
  import(`./../../data/data/${c.file}`)
    .then((d) => {
      data.push({ ...c, ...d.default });
    })
    .then(() => {
      data.sort((a, b) => {
        return a.position - b.position;
      });
    });
});
const handleScroll = () => {
  if (window.pageYOffset > 0) {
    if (view.value.atTopOfPage) view.value.atTopOfPage = false;
  } else {
    if (!view.value.atTopOfPage) view.value.atTopOfPage = true;
  }
};

const refresh = ref(false);
const refreshInt = setInterval(() => {
  refresh.value = true;
}, 10 * 60 * 100);

const refreshNow = () => {
  clearInterval(refreshInt);
  window.location.reload();
};

function formatDate(value) {
  return moment(value).format("DD.MM.YY - HH:mm");
}

function formatNumber(value) {
  return numeral(value).format("0.0");
}

const yLabel = (data, type) => {
  var min = Math.floor(Math.min.apply(Math, data));
  var max = Math.ceil(Math.max.apply(Math, data));
  var diff = max - min;
  do {
    diff = Math.floor(diff / 2);
  } while (diff > 5);
  diff = diff < 2 ? 2 : diff;
  switch (type) {
    case "min":
      return min;
    case "max":
      return max;
    case "num":
      return diff;
    default:
      return false;
  }
};

onBeforeMount(() => {
  window.addEventListener("scroll", handleScroll);
});
</script>
