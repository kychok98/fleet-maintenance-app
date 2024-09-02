<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { cn } from "@/lib/utils.ts";

const props = defineProps<{
  class?: HTMLAttributes["class"];
}>();
</script>

<template>
  <thead
    :class="cn('sticky top-0 z-50 bg-white [&_tr]:shadow-sm', props.class)"
  >
    <slot />
  </thead>
</template>
