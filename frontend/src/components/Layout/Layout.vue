<script setup lang="ts">
import LayoutHeader from "./LayoutHeader.vue";
import LayoutNav from "./LayoutNav.vue";
</script>
<template>
  <div class="container my-4 rounded border shadow">
    <div
      class="my-4 flex items-baseline justify-between md:justify-normal md:space-x-12"
    >
      <LayoutHeader />
      <LayoutNav />
    </div>
    <slot />
  </div>
</template>
