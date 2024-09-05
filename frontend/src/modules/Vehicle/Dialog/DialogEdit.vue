<script setup lang="ts">
import Badge from "@/lib/ui/badge/Badge.vue";
import { Button } from "@/lib/ui/button";
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/lib/ui/dialog";
import DialogDescription from "@/lib/ui/dialog/DialogDescription.vue";
import { useToast } from "@/lib/ui/toast";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import { Row } from "@tanstack/vue-table";
import {
  DialogRootEmits,
  DialogRootProps,
  useForwardPropsEmits,
} from "radix-vue";
import { computed, ref, toRaw } from "vue";
import EditableField from "../components/EditableField.vue";
import { statusVariants } from "../constants.ts";
import { type TVehicle, vehicleUpdateSchema } from "../services/schema.ts";
import { updateVehicle } from "../services/VehicleService.ts";

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

const state = ref(structuredClone(toRaw(props.row.original)));

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async (id: number) => {
    const vehicle = await updateVehicle(
      id,
      vehicleUpdateSchema.parse(state.value),
    );
    emits("update:open", false);
    return vehicle;
  },
  onSettled: async (data) => {
    if (data) {
      await queryClient.invalidateQueries({ queryKey: ["vehicles"] });
      toast({
        title: "Vehicle Updated Success!",
        description: `${data.vin} have been updated.`,
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
        <DialogTitle>Edit Vehicle</DialogTitle>
        <DialogDescription class="text-sm">
          Click save changes when you're done.
        </DialogDescription>
        <div class="mt-4">
          <EditableField id="vin" v-model="state.vin" label="VIN" readonly />
          <EditableField id="make" v-model="state.make" label="Make" />
          <EditableField id="model" v-model="state.model" label="Model" />
          <EditableField id="year" v-model="state.year" label="Year" />
          <EditableField id="mileage" v-model="state.mileage" label="Mileage" />

          <fieldset class="mb-[15px] flex items-center gap-2">
            <label class="w-[130px] text-right text-[15px]">
              Last Service Date:
            </label>
            <div class="flex items-center space-x-2 px-3">
              <span> {{ state.last_service_date }} </span>
              <Badge :variant="statusVariants[state.status]">
                {{ state.status.toUpperCase() }}
              </Badge>
            </div>
          </fieldset>
        </div>
      </DialogHeader>
      <DialogFooter>
        <Button
          type="submit"
          :loading="isPending"
          @click="mutate(row.original.id)"
        >
          Save Changes
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
