<script setup lang="ts">
import { Button } from "@/lib/ui/button";
import { PlusIcon } from "@radix-icons/vue";
import type { Table } from "@tanstack/vue-table";
import { ref } from "vue";
import DialogAdd from "../Dialog/DialogAdd.vue";
import type { TVehicle } from "../services/schema.ts";
import DataTableViewOptions from "./DataTableViewOptions.vue";

interface DataTableToolbarProps {
  table: Table<TVehicle>;
}

defineProps<DataTableToolbarProps>();

const openAdd = ref(false);
</script>

<template>
  <div class="flex items-center justify-end space-x-2">
    <Button variant="outline" size="sm" class="h-8" @click="openAdd = true">
      <PlusIcon class="mr-1 h-4 w-4" />
      Add
    </Button>
    <DataTableViewOptions :table="table" />
  </div>

  <DialogAdd :open="openAdd" @update:open="(val: boolean) => (openAdd = val)" />
</template>
