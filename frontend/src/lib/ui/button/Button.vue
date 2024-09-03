<script setup lang="ts">
import SVGSpinner from "@/components/Loading/SVGSpinner.vue";
import type { HTMLAttributes } from "vue";
import { Primitive, type PrimitiveProps } from "radix-vue";
import { type ButtonVariants, buttonVariants } from "./index.ts";
import { cn } from "@/lib/utils.ts";

interface Props extends PrimitiveProps {
  variant?: ButtonVariants["variant"];
  size?: ButtonVariants["size"];
  class?: HTMLAttributes["class"];
  loading?: boolean;
  disabled?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  as: "button",
  loading: false,
});
</script>

<template>
  <Primitive
    :as="as"
    :as-child="asChild"
    :class="cn(buttonVariants({ variant, size }), props.class)"
    :disabled="disabled || loading"
  >
    <SVGSpinner v-if="loading" class="mr-2 w-4" />
    <slot />
  </Primitive>
</template>
