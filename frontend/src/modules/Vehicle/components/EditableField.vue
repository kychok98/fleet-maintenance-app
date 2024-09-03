<script setup lang="ts">
import { Input } from "@/lib/ui/input";
import { useVModel } from "@vueuse/core";
import { computed } from "vue";

interface EditableFieldProps {
  id: string;
  label: string;
  modelValue: string | number;
  readonly?: boolean;
}

const props = defineProps<EditableFieldProps>();
const delegatedProps = computed(() => {
  const { label: _, ...delegated } = props;
  return delegated;
});

const vmodel = useVModel(props, "modelValue");
</script>

<template>
  <fieldset class="mb-3 flex items-center gap-2">
    <label :for="id" class="text-grass11 w-[130px] text-right text-[15px]">
      {{ label }}:
    </label>

    <Input v-model="vmodel" v-bind="delegatedProps" class="flex-1" />
  </fieldset>
</template>
