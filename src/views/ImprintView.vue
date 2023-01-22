<template>
  <div class="max-w-7xl mx-auto py-12 px-4 sm:py-16 sm:px-6 lg:px-8">
        <div class="max-w-3xl mx-auto divide-y divide-darkblue dark:divide-white">
            <h2 class="text-center text-2xl font-bold text-darkblue dark:text-white sm:text-4xl">
            {{$t('imprint')}}
            </h2>
        </div>
        <main class="prose text-darkblue dark:text-white">
            <h3 class="text-darkblue dark:text-white">{{$t('Data')}}</h3>
            <p class="text-darkblue dark:text-white">{{$t('Source')}}: <a class="text-darkblue dark:text-white" href="https://data.bs.ch/pages/home/" target="_blank">Data Basel-Stadt</a></p>
            <p class="text-darkblue dark:text-white">{{$t('waterTemp')}}: <a class="text-darkblue dark:text-white" href="https://data.bs.ch/explore/dataset/100046/information/?sort=startzeitpunkt" target="_blank">Rheinüberwachungsstation Weil am Rhein</a></p>
            <p class="text-darkblue dark:text-white">{{$t('airTemp')}}: <a class="text-darkblue dark:text-white" href="https://data.bs.ch/explore/dataset/100082/table/?disjunctive.name_original&disjunctive.name_custom&sort=name_custom&q=0340AD8C" target="_blank">Mess-Station Unterer Rheinweg Basel</a></p>
            <p class="text-darkblue dark:text-white">Pegelstand: <a class="text-darkblue dark:text-white" href="https://data.bs.ch/explore/dataset/100089/table/?sort=timestamp" target="_blank">Mess-Station auf der Kleinbasler Seite auf Höhe des Birs-Zuflusses</a></p>
            <h3 class="text-darkblue dark:text-white">{{$t('Contact')}}</h3>
            <div class="inline-flex text-darkblue dark:text-white">
                <span class="material-icons text-sm mr-2">open_in_new</span>
                <a class="underline text-darkblue dark:text-white" target="_blank" href="https://github.com/chrisrickenbacher/rhygfuehl">GitHub</a>
            </div>
            <div class="inline-flex text-darkblue dark:text-white">
                <span class="material-icons text-sm mr-2 ml-4">mail</span>
                <a class="underline text-darkblue dark:text-white" target="_blank" href="mailto:rhygfuehl@cric.dev">rhygfuehl@cric.dev</a>
            </div>
        </main>
    </div>
</template>

<script setup>

</script>
