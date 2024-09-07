<script setup lang="ts">
import DataTableViewOptions from "@/components/DataTable/DataTableViewOptions.vue";
import { Button } from "@/lib/ui/button";
import { PlusIcon, ResetIcon } from "@radix-icons/vue";
import type { Table } from "@tanstack/vue-table";
import { ref } from "vue";
import DialogAdd from "../Dialog/DialogAdd.vue";
import type { TMaintenance } from "../services/schema.ts";

interface DataTableToolbarProps {
  table: Table<TMaintenance>;
}

const props = defineProps<DataTableToolbarProps>();

const openAdd = ref(false);

const handleReset = () => {
  const { table } = props;
  table.resetSorting();
  table.resetColumnVisibility();
};
</script>

<template>
  <div class="mt-2 flex items-center justify-between">
    <Button size="sm" class="h-8" @click="openAdd = true">
      <PlusIcon class="mr-1 h-4 w-4" />
      Add
    </Button>
    <div class="space-x-2">
      <Button variant="outline" size="sm" class="h-8" @click="handleReset">
        <ResetIcon class="mr-1 h-4 w-4" />
        Reset
      </Button>
      <DataTableViewOptions :table="table" />
    </div>
  </div>

  <DialogAdd :open="openAdd" @update:open="(val: boolean) => (openAdd = val)" />
</template>
