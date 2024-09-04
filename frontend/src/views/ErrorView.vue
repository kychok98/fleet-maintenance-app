<template>
  <div class="container space-y-2 p-4">
    <div class="text-4xl">Page not available...</div>
    <p class="text-lg">
      <RouterLink :to="{ name: ROUTE_NAME.Vehicle }" class="text-blue-500">
        back to home
      </RouterLink>
    </p>
  </div>
</template>
<script setup lang="ts">
import { ROUTE_NAME } from "@/router/constants.ts";
</script>
