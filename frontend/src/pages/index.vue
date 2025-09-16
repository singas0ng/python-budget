<script lang="ts" setup>
import axios from 'axios'
import { onMounted } from 'vue';

interface Money {
  category: number
  id: number
  description: string
  money_type: string
  value: number
  io_date: string
}

const moneyList = ref<Money[]>([])
const headers = [
  { title: '카테고리 ID', key: 'category' },
  { title: '#', key: 'id' },
  { title: '설명', key: 'description' },
  { title: '입/출금 구분', key: 'money_type' },
  { title: '금액', key: 'value' },
  { title: '날짜', key: 'io_date' },
]

onMounted(async ()=>{
  const request = await axios.get('http://localhost:8000/money')
  moneyList.value = request.data;

  console.log(moneyList.value)
});


</script>

<template>
  <v-breadcrumbs :items="['메인']"></v-breadcrumbs>

  <v-data-table
    :headers="headers"
    :items="moneyList">
  </v-data-table>
</template>

<style>

</style>