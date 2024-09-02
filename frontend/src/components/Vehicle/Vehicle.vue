<script setup lang="ts">
import tasks from "./data/tasks.json";
import { columns } from "./DataTable/columns.ts";
import DataTable from "./DataTable/DataTable.vue";
</script>

<template>
  <div class="h-full flex-1 flex-col space-y-8 p-8 md:flex">
    <div class="flex items-center justify-between space-y-2">
      <div>
        <h2 class="text-2xl font-bold tracking-tight">
          Fleet Maintenance Dashboard
        </h2>
      </div>
    </div>
    <DataTable :data="tasks" :columns="columns" />
  </div>
</template>
