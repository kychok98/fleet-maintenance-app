<script setup lang="ts">
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/lib/ui/dialog";
import { Row } from "@tanstack/vue-table";
import {
  DialogRootEmits,
  DialogRootProps,
  Separator,
  useForwardPropsEmits,
} from "radix-vue";
import { computed } from "vue";
import BadgeStatus from "../components/BadgeStatus.vue";
import DialogViewRecords from "../components/DialogViewRecords.vue";
import { type TVehicle } from "../services/schema.ts";

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
</script>
<template>
  <Dialog v-bind="forwarded">
    <DialogContent>
      <DialogHeader>
        <DialogTitle class="flex items-center">
          View Vehicle Details
        </DialogTitle>
        <div class="my-2 flex flex-col">
          <Separator class="my-1 h-[1px] bg-slate-200" />
          <div
            class="grid grid-cols-[140px_1fr] items-center gap-x-2 gap-y-1 [&>*:nth-child(even)]:text-slate-600"
          >
            <span class="text-right"> Year: </span>
            <span class="text-left">{{ row.original.year }}</span>
            <span class="text-right"> Make: </span>
            <span class="text-left">{{ row.original.make }}</span>
            <span class="text-right"> Model: </span>
            <span class="text-left">{{ row.original.model }}</span>
            <span class="text-right"> Mileage: </span>
            <span class="text-left"> {{ row.original.mileage }} KM </span>
            <span class="text-right"> Last service date: </span>
            <span class="flex items-center space-x-2 text-left">
              <span>{{ row.original.last_service_date }}</span>
              <BadgeStatus :status="row.original.status" />
            </span>
          </div>

          <Separator class="my-2 h-[1px] bg-slate-200" />

          <DialogViewRecords
            v-if="row.original.maintenances.length > 0"
            :records="row.original.maintenances"
          />
        </div>
      </DialogHeader>
    </DialogContent>
  </Dialog>
</template>
