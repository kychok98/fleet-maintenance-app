<script setup lang="ts">
import LayoutHeader from "./LayoutHeader.vue";
import LayoutNav from "./LayoutNav.vue";
</script>
<template>
  <div class="container my-4 rounded border py-4 shadow">
    <div
      class="mb-2 flex items-baseline justify-between border-b-2 md:justify-normal md:space-x-12"
    >
      <LayoutHeader />
      <LayoutNav />
    </div>
    <slot />
  </div>
</template>
