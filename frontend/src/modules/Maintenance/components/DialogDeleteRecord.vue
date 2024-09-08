<script setup lang="ts">
import Loading from "@/components/Loading/Loading.vue";
import { TMaintenance } from "@/modules/Maintenance/services/schema.ts";
import { getVehicleById } from "@/modules/Vehicle/services/VehicleService.ts";
import { getLabel } from "@/modules/Vehicle/utils.ts";
import { useQuery } from "@tanstack/vue-query";
import { computed } from "vue";

interface IProps {
  maintenance: TMaintenance;
}

const props = defineProps<IProps>();

const { isLoading, data } = useQuery({
  queryKey: ["vehicle", props.maintenance.id],
  queryFn: async () => getVehicleById(props.maintenance.id),
});

const vehicleLabel = computed(() => {
  if (!data.value) return "-";
  return `${props.maintenance.vehicle} ${getLabel(data.value)}`;
});
</script>

<template>
  <Loading v-if="isLoading" />

  <div
    v-else
    class="grid grid-cols-[140px_1fr] items-center gap-x-2 gap-y-1 text-sm [&>*:nth-child(even)]:text-slate-600"
  >
    <span class="text-right"> Maintenance ID: </span>
    <span class="text-left">{{ maintenance.id }}</span>
    <span class="text-right"> Description: </span>
    <span class="text-left">{{ maintenance.description }}</span>
    <span class="text-right"> Vehicle Info: </span>
    <span class="text-left">{{ vehicleLabel }}</span>
    <span class="text-right"> Schedule Date: </span>
    <span class="text-left"> {{ maintenance.schedule_date }}</span>
  </div>
</template>
