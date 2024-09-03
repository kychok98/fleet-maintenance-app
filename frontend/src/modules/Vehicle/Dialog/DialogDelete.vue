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
import { TVehicle } from "../services/schema.ts";
import { deleteVehicles } from "../services/VehicleService.ts";

interface IProps extends DialogRootProps {
  row: Row<TVehicle>;
}

const props = defineProps<IProps>();
const emits = defineEmits<DialogRootEmits>();
const delegatedProps = computed(() => {
  const { row: _, ...delegated } = props;
  return delegated;
});

const forwarded = useForwardPropsEmits(delegatedProps, emits);

const label = computed(() => {
  const { vin, make, model } = props.row.original;
  return `${vin} ${make} ${model}`;
});

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async (id: number) => {
    console.log("id: ", id);
    await deleteVehicles(id);
    await queryClient.invalidateQueries({ queryKey: ["vehicles"] });
    emits("update:open", false);
    return true;
  },
  onSettled: async (data) => {
    if (data) {
      toast({
        title: "Vehicle Removal Success!",
        description: `${label.value} have been removed.`,
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
        <DialogTitle>Are you sure you want to remove?</DialogTitle>
        <DialogDescription class="flex flex-col space-y-2">
          <b class="text-xl">{{ label }}</b>
          <span>
            This action cannot be undone, and will permanently delete all
            related maintenance record(s).
          </span>
        </DialogDescription>
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
