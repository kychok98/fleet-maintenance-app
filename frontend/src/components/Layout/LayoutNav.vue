<script setup lang="ts">
import { ROUTE_NAME } from "@/router/constants.ts";
import { twMerge } from "tailwind-merge";
import { computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const currentRouteName = computed(() => route.name);
</script>
<template>
  <div class="space-x-4">
    <RouterLink
      :to="{ name: ROUTE_NAME.Vehicle }"
      :class="
        twMerge(
          `text-xl hover:text-slate-900`,
          currentRouteName === ROUTE_NAME.Vehicle
            ? 'border-b-2 border-slate-600 text-slate-900'
            : 'text-slate-500',
        )
      "
    >
      Vehicles
    </RouterLink>
    <RouterLink
      :to="{ name: ROUTE_NAME.Maintenance }"
      :class="
        twMerge(
          `text-xl hover:text-slate-900`,
          currentRouteName === ROUTE_NAME.Maintenance
            ? 'border-b-2 border-slate-600 text-slate-900'
            : 'text-slate-500',
        )
      "
    >
      Maintenance
    </RouterLink>
  </div>
</template>
