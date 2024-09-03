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
import {
  VehicleAddParam,
  vehicleAddSchema,
} from "@/modules/Vehicle/services/schema.ts";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import {
  DialogRootEmits,
  DialogRootProps,
  useForwardPropsEmits,
} from "radix-vue";
import { ref } from "vue";
import { ZodError } from "zod";
import EditableField from "../components/EditableField.vue";
import { addVehicle } from "../services/VehicleService.ts";

const props = defineProps<DialogRootProps>();
const emits = defineEmits<DialogRootEmits>();
const forwarded = useForwardPropsEmits(props, emits);

const state = ref<VehicleAddParam>({
  make: "",
  model: "",
  year: 2024,
});

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async () => {
    const vehicle = await addVehicle(state.value);
    emits("update:open", false);
    return vehicle;
  },
  onSettled: async (data) => {
    if (data) {
      await queryClient.invalidateQueries({ queryKey: ["vehicles"] });
      toast({
        title: "Vehicle Added Success!",
        description: `${data.vin} have been added.`,
        variant: "success",
      });
    }
  },
});
const handleSave = () => {
  try {
    vehicleAddSchema.parse(state.value);
    mutate();
  } catch (error) {
    const zodError = error as ZodError;
    toast({
      title: "Validation Error",
      description: zodError.message,
      variant: "destructive",
    });
  }
};
</script>
<template>
  <Dialog v-bind="forwarded">
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Add Vehicle</DialogTitle>
        <DialogDescription> Click save when you're done. </DialogDescription>
        <div class="mt-4">
          <EditableField
            id="make"
            v-model="state.make"
            label="Make"
            placeholder="Toyota"
          />
          <EditableField
            id="model"
            v-model="state.model"
            label="Model"
            placeholder="Civic"
          />
          <EditableField id="year" v-model="state.year" label="Year" />
        </div>
      </DialogHeader>
      <DialogFooter>
        <Button type="submit" :loading="isPending" @click="handleSave">
          Save
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
