<script setup lang="ts">
import type { TVehicle } from "@/modules/Vehicle/services/schema.ts";
import type { Table } from "@tanstack/vue-table";
import DataTableViewOptions from "./DataTableViewOptions.vue";

interface DataTableToolbarProps {
  table: Table<TVehicle>;
}

defineProps<DataTableToolbarProps>();
</script>

<template>
  <div class="flex items-center justify-between">
    <DataTableViewOptions :table="table" />
  </div>
</template>
