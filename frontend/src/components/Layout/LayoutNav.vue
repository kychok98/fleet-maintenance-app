<script setup lang="ts">
import SVGCar from "@/components/SVG/SVGCar.vue";
import SVGRepair from "@/components/SVG/SVGRepair.vue";
import { ROUTE_NAME } from "@/router/constants.ts";
import { twMerge } from "tailwind-merge";
import { computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const currentRouteName = computed(() => route.name);
</script>
<template>
  <div class="flex space-x-4">
    <RouterLink
      :to="{ name: ROUTE_NAME.Vehicle }"
      :class="
        twMerge(
          `flex items-center text-xl hover:fill-slate-900 hover:text-slate-900`,
          currentRouteName === ROUTE_NAME.Vehicle
            ? 'border-b-2 border-slate-600 text-slate-900'
            : 'text-slate-500 ',
        )
      "
    >
      <SVGCar class="mr-2" />
      <span class="hidden md:block">Vehicles</span>
    </RouterLink>
    <RouterLink
      :to="{ name: ROUTE_NAME.Maintenance }"
      :class="
        twMerge(
          `flex items-center text-xl hover:fill-slate-900 hover:text-slate-900`,
          currentRouteName === ROUTE_NAME.Maintenance
            ? 'border-b-2 border-slate-600 text-slate-900'
            : 'text-slate-500',
        )
      "
    >
      <SVGRepair class="mr-2" />
      <span class="hidden md:block">Maintenance</span>
    </RouterLink>
  </div>
</template>
