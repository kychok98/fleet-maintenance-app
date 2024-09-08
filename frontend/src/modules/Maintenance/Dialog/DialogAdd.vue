<script setup lang="ts">
import FormDateField from "@/components/Form/FormDateField.vue";
import FormInputField from "@/components/Form/FormInputField.vue";
import FormSelectField from "@/components/Form/FormSelectField.vue";
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
import { getVehicles } from "@/modules/Vehicle/services/VehicleService.ts";
import { useMutation, useQuery, useQueryClient } from "@tanstack/vue-query";
import {
  DialogRootEmits,
  DialogRootProps,
  useForwardPropsEmits,
} from "radix-vue";
import { ref } from "vue";
import { addMaintenance } from "../services/MaintenanceService.ts";

const props = defineProps<DialogRootProps>();
const emits = defineEmits<DialogRootEmits>();
const forwarded = useForwardPropsEmits(props, emits);

const { toast } = useToast();
const queryClient = useQueryClient();

const state = ref({
  vehicle_id: undefined,
  schedule_date: undefined,
  description: "",
});

const { data: inactiveVehicles } = useQuery({
  queryKey: ["vehicles-inactive"],
  queryFn: async () => {
    const vehicles = await getVehicles({ status: "inactive", sort_by: "id" });

    return vehicles.reduce((acc, vehicle) => {
      return [
        ...acc,
        {
          label: `${vehicle.id} - ${vehicle.year} ${vehicle.make} ${vehicle.model}`,
          value: vehicle.id + "",
        },
      ];
    }, [] as ISelectItem[]);
  },
});

const { isPending, mutate } = useMutation({
  mutationFn: async () => {
    const vehicle = await addMaintenance(state.value);
    emits("update:open", false);
    return vehicle;
  },
  onSettled: async (data) => {
    if (data) {
      await queryClient.invalidateQueries({ queryKey: ["maintenances"] });
      await queryClient.invalidateQueries({ queryKey: ["vehicles"] });
      toast({
        title: "Maintenance Added Success!",
        description: `${data.id} have been added.`,
        variant: "success",
      });
    }
  },
  onError: (err) => {
    toast({
      title: "Maintenance Add Error",
      description: err.message,
      variant: "destructive",
    });
  },
});
</script>
<template>
  <Dialog v-bind="forwarded">
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Add Maintenance</DialogTitle>
        <DialogDescription class="text-sm">
          Click add when you're done.
        </DialogDescription>
        <div class="mt-4">
          <FormSelectField
            id="vehicle_id"
            v-model="state.vehicle_id"
            placeholder="Select a vehicle"
            label="Vehicle"
            :items="inactiveVehicles || []"
          />
          <FormDateField
            id="schedule_date"
            v-model="state.schedule_date"
            label="Date"
          />
          <FormInputField
            id="make"
            v-model="state.description"
            label="Description"
            placeholder="Normal maintenance"
          />
        </div>
      </DialogHeader>
      <DialogFooter>
        <Button type="submit" :loading="isPending" @click="mutate">
          Add
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
