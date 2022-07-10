<template>
    <Line 
        :chart-options="{
            responsive: true,
            plugins: {
                legends: {
                    display: false
                }
            },
            elements: {
                point:{
                    radius: 0
                },
                line: {
                    borderColor: color,
                    borderWidth: 4,
                    borderCapStyle: 'round'
                }
            },
            transistions: {
                show: {
                    duration: 0
                }
            },
            scales: {
                y: {
                    min: props.min,
                    max: props.max,
                    ticks: {
                        stepSize: 1,
                        maxTicksLimit: props.ticks
                    }
                },
                x: {
                    display: false
                }
            }
        }"
        :chart-data="{
            datasets: [ { data: data, tension: 0.4 } ],
            labels: data,
        }"
        chart-id="chartId"
        height="200"

    />
</template>

<script setup>
import tailwindconfig from '@/../tailwind.config.js'
import { defineProps } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, LineElement,LinearScale, PointElement, CategoryScale } from 'chart.js'
ChartJS.register( Title, LineElement, LinearScale, PointElement, CategoryScale )

// eslint-disable-next-line
const props = defineProps({
    data: {
        type: Array
    },
    min: {
        type: Number
    },
    max:  {
        type: Number
    },
    ticks: {
        type: Number
    }
})
const color = tailwindconfig.theme.colors.darkblue
</script>