<script setup lang="ts">
import FormDateField from "@/components/Form/FormDateField.vue";
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
import { formatDate } from "@/lib/utils.ts";
import BadgeType from "@/modules/Maintenance/components/BadgeType.vue";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import { Row } from "@tanstack/vue-table";

import {
  DialogRootEmits,
  DialogRootProps,
  useForwardPropsEmits,
} from "radix-vue";
import { computed, ref } from "vue";
import { updateMaintenance } from "../services/MaintenanceService.ts";
import { type TMaintenance } from "../services/schema.ts";

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

const readOnly = computed(() => {
  const { completion_date } = props.row.original;
  return Boolean(completion_date);
});

const state = ref({
  schedule_date: undefined,
  completion_date: undefined,
  description: props.row.original.description,
});

const { toast } = useToast();
const queryClient = useQueryClient();

const { isPending, mutate } = useMutation({
  mutationFn: async (id: number) => {
    const maintenance = await updateMaintenance(id, {
      completion_date: state.value.completion_date
        ? formatDate(state.value.completion_date)
        : undefined,
      schedule_date: state.value.schedule_date
        ? formatDate(state.value.schedule_date)
        : undefined,
      description: state.value.description,
    });
    await queryClient.invalidateQueries({ queryKey: ["maintenances"] });
    emits("update:open", false);
    return maintenance;
  },
  onSettled: async (data) => {
    if (data) {
      toast({
        title: "Maintenance Updated Success!",
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
          <FormDateField
            id="schedule_date"
            v-model="state.schedule_date"
            label="Schedule Date"
            :placeholder="row.original.schedule_date || ''"
            :disabled="readOnly"
          />
          <FormDateField
            id="completion_date"
            v-model="state.completion_date"
            label="Completion Date"
            :placeholder="row.original.completion_date || ''"
            :disabled="readOnly"
          />
          <FormInputField
            id="description"
            v-model="state.description"
            label="Description"
          />
          <fieldset class="mb-[15px] flex items-center gap-2">
            <label class="w-[130px] text-right text-[15px]">
              Schedule Type
            </label>
            <div class="flex items-center space-x-2 px-3">
              <BadgeType :type="row.original.schedule_type" />
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
