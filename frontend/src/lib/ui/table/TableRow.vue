<script setup lang="ts">
import { cn } from "@/lib/utils.ts";
import type { HTMLAttributes } from "vue";
import { computed } from "vue";

const props = defineProps<{
  class?: HTMLAttributes["class"];
  status?: string; // Add status prop
}>();

const rowClass = computed(() => {
  return cn(
    "data-[status=success]:text-green-600 data-[status=pending]:text-yellow-600 border-b transition-colors hover:bg-slate-100/50 data-[state=selected]:bg-slate-100",
    props.class,
  );
});
</script>

<template>
  <tr :class="rowClass">
    <slot />
  </tr>
</template>
