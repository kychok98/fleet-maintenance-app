<script setup lang="ts">
import { formatNumberWithCommas } from "@/lib/utils.ts";
import { TVehicle } from "@/modules/Vehicle/services/schema.ts";

interface IProps {
  records: TVehicle["maintenances"];
}

defineProps<IProps>();
</script>

<template>
  <ul
    class="mb-1 grid grid-cols-[65px_130px_130px_130px] text-sm text-slate-600"
  >
    <li class="text-right">Mileage</li>
    <li class="text-center">Schedule Date</li>
    <li class="text-center">Completion Date</li>
  </ul>
  <div class="space-y-0.5 text-slate-900">
    <ul
      v-for="(maintenance, idx) in records"
      :key="maintenance.id"
      class="grid grid-cols-[65px_130px_130px_130px] rounded hover:cursor-pointer hover:bg-slate-200"
    >
      <li class="text-right">
        {{ formatNumberWithCommas(5000 * (records.length - idx)) }}
      </li>
      <li class="text-center">{{ maintenance.schedule_date }}</li>
      <li class="text-center">
        {{ maintenance.completion_date || "-" }}
      </li>
    </ul>
  </div>
</template>
