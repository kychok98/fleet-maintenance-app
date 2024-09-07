<script setup lang="ts">
import { Button } from "@/lib/ui/button";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/lib/ui/dropdown-menu";
import { DotsHorizontalIcon } from "@radix-icons/vue";
import type { Row } from "@tanstack/vue-table";
import { ref } from "vue";
import DialogDelete from "../Dialog/DialogDelete.vue";
import DialogEdit from "../Dialog/DialogEdit.vue";
import DialogView from "../Dialog/DialogView.vue";
import type { TMaintenance } from "../services/schema.ts";

interface DataTableRowActionsProps {
  row: Row<TMaintenance>;
}
defineProps<DataTableRowActionsProps>();

const openView = ref(false);
const openDelete = ref(false);
const openEdit = ref(false);
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger>
      <Button
        variant="ghost"
        class="data-[state=open]:bg-muted flex h-8 w-8 p-0"
      >
        <DotsHorizontalIcon class="h-4 w-4" />
        <span class="sr-only">Open menu</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end" class="w-[160px]">
      <DropdownMenuItem @click="openView = true">View Details</DropdownMenuItem>
      <DropdownMenuItem @click="openEdit = true">Edit</DropdownMenuItem>
      <DropdownMenuItem @click="openDelete = true">Delete</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>

  <DialogView
    v-if="openView"
    :row="row"
    open
    @update:open="(val: boolean) => (openView = val)"
  />
  <DialogEdit
    v-if="openEdit"
    :row="row"
    open
    @update:open="(val: boolean) => (openEdit = val)"
  />
  <DialogDelete
    :row="row"
    :open="openDelete"
    @update:open="(val: boolean) => (openDelete = val)"
  />
</template>
