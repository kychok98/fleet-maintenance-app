<script setup lang="ts">
import DataTableViewOptions from "@/components/DataTable/DataTableViewOptions.vue";
import { Button } from "@/lib/ui/button";
import { useToast } from "@/lib/ui/toast";
import { CheckIcon, PlusIcon, ResetIcon } from "@radix-icons/vue";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import type { Table } from "@tanstack/vue-table";
import { ref } from "vue";
import DialogAdd from "../Dialog/DialogAdd.vue";
import { markMaintenanceAsComplete } from "../services/MaintenanceService.ts";
import type { TMaintenance } from "../services/schema.ts";

interface DataTableToolbarProps {
  table: Table<TMaintenance>;
}

const props = defineProps<DataTableToolbarProps>();

const { toast } = useToast();
const queryClient = useQueryClient();

const openAdd = ref(false);

const { isPending, mutate } = useMutation({
  mutationFn: async (maintenanceIds: number[]) => {
    const maintenance = await markMaintenanceAsComplete(maintenanceIds);
    await queryClient.invalidateQueries({ queryKey: ["maintenances"] });
    return maintenance;
  },
  onSettled: async (data) => {
    if (data) {
      props.table.resetRowSelection();
      toast({
        title: data.message,
        variant: "success",
      });
    }
  },
});

const handleMarkAsCompleted = () => {
  const selectedRow = props.table.getFilteredSelectedRowModel().rows;
  const vehicleIds = selectedRow.map((row) => +row.original.id);
  mutate(vehicleIds);
};

const handleReset = () => {
  const { table } = props;
  table.resetSorting();
  table.resetColumnVisibility();
  table.resetRowSelection();
};
</script>

<template>
  <div class="mt-2 flex items-center justify-between">
    <Button size="sm" class="h-8" @click="openAdd = true">
      <PlusIcon class="mr-1 h-4 w-4" />
      Add
    </Button>
    <div class="space-x-2">
      <Button
        :loading="isPending"
        :disabled="table.getFilteredSelectedRowModel().rows.length <= 0"
        size="sm"
        class="h-8"
        @click="handleMarkAsCompleted"
      >
        <CheckIcon class="mr-1 h-4 w-4" />
        Mark as completed
      </Button>
      <Button variant="outline" size="sm" class="h-8" @click="handleReset">
        <ResetIcon class="mr-1 h-4 w-4" />
        Reset
      </Button>
      <DataTableViewOptions :table="table" />
    </div>
  </div>

  <DialogAdd
    :key="JSON.stringify(openAdd)"
    :open="openAdd"
    @update:open="(val: boolean) => (openAdd = val)"
  />
</template>
