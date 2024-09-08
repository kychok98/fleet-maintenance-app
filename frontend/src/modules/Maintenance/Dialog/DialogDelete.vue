<script setup lang="ts">
import { Button } from "@/lib/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/lib/ui/dialog";
import { useToast } from "@/lib/ui/toast";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import { Row } from "@tanstack/vue-table";
import {
  DialogRootEmits,
  DialogRootProps,
  useForwardPropsEmits,
} from "radix-vue";
import { computed } from "vue";
import DialogDeleteRecord from "../components/DialogDeleteRecord.vue";
import { deleteMaintenance } from "../services/MaintenanceService.ts";
import { TMaintenance } from "../services/schema.ts";

interface IProps extends DialogRootProps {
  row: Row<TMaintenance>;
}

const props = defineProps<IProps>();
const emits = defineEmits<DialogRootEmits>();
const delegatedProps = computed(() => {
  const { row: _, ...delegated } = props;
  return delegated;
});

const forwarded = useForwardPropsEmits(delegatedProps, emits);

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async (id: number) => {
    await deleteMaintenance(id);
    await queryClient.invalidateQueries({ queryKey: ["maintenances"] });
    emits("update:open", false);
    return true;
  },
  onSettled: async (data) => {
    if (data) {
      toast({
        title: "Maintenance Removal Success!",
        variant: "success",
      });
    }
  },
});
</script>
<template>
  <Dialog v-bind="forwarded">
    <DialogContent>
      <DialogHeader>
        <DialogTitle class="text-xl text-red-800">
          Are you sure you want to remove?
        </DialogTitle>
        <DialogDescription class="flex flex-col space-y-2 text-sm">
          This action cannot be undone, and will permanently delete the
          scheduled maintenance.
        </DialogDescription>
        <div class="flex items-center space-x-2">
          <DialogDeleteRecord :maintenance="row.original" />
        </div>
      </DialogHeader>
      <DialogFooter>
        <Button
          type="submit"
          variant="destructive"
          :loading="isPending"
          @click="mutate(row.original.id)"
        >
          Confirm
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
