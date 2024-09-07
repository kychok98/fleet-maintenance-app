<script setup lang="ts">
import FormInputField from "@/components/Form/FormInputField.vue";
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
import { type TMaintenance, maintenanceUpdateSchema } from "../services/schema.ts";
import { updateMaintenance } from "../services/MaintenanceService.ts";

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

const state = ref(structuredClone(toRaw(props.row.original)));

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async (id: number) => {
    const maintenance = await updateMaintenance(
      id,
      maintenanceUpdateSchema.parse(state.value),
    );
    emits("update:open", false);
    return maintenance;
  },
  onSettled: async (data) => {
    if (data) {
      await queryClient.invalidateQueries({ queryKey: ["maintenances"] });
      toast({
        title: "Maintenance Updated Success!",
        description: `${data} have been updated.`,
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
        <DialogTitle>Edit Maintenance</DialogTitle>
        <DialogDescription class="text-sm">
          Click save changes when you're done.
        </DialogDescription>
        <div class="mt-4">
          <FormInputField id="year" v-model="state.year" label="Year" readonly />
          <FormInputField id="make" v-model="state.make" label="Make" />
          <FormInputField id="model" v-model="state.model" label="Model" />
          <FormInputField id="year" v-model="state.year" label="Year" />
          <FormInputField id="mileage" v-model="state.mileage" label="Mileage" />

          <fieldset class="mb-[15px] flex items-center gap-2">
            <label class="w-[130px] text-right text-[15px]">
              Last Service Date:
            </label>
            <div class="flex items-center space-x-2 px-3">
              <span> {{ state.last_service_date }} </span>
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
