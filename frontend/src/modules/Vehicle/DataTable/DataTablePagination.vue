<script setup lang="ts">
import type { TVehicle } from "@/modules/Vehicle/services/schema.ts";
import type { Table } from "@tanstack/vue-table";

interface DataTablePaginationProps {
  table: Table<TVehicle>;
}
defineProps<DataTablePaginationProps>();
</script>

<template>
  <div class="flex items-center justify-between px-2">
    <div class="text-muted-foreground flex-1 text-sm">
      {{ table.getFilteredSelectedRowModel().rows.length }} of
      {{ table.getFilteredRowModel().rows.length }} row(s) selected.
    </div>
  </div>
</template>
