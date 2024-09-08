<script setup lang="ts">
import DataTable from "@/components/DataTable/DataTable.vue";
import Loading from "@/components/Loading/Loading.vue";
import { useQuery } from "@tanstack/vue-query";
import { columns } from "./columns.ts";
import DataTableToolbar from "./components/DataTableToolbar.vue";
import { getVehicles } from "./services/VehicleService.ts";

const { isLoading, data } = useQuery({
  queryKey: ["vehicles"],
  queryFn: () => getVehicles(),
});
</script>

<template>
  <Loading v-if="isLoading" />
  <div v-else class="h-full flex-1 flex-col md:flex">
    <DataTable :data="data || []" :columns="columns">
      <template #toolbar="{ table }">
        <DataTableToolbar :table="table" />
      </template>
    </DataTable>
  </div>
</template>
