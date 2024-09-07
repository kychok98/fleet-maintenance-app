<script setup lang="ts">
import { Input } from "@/lib/ui/input";
import { InputProps } from "@/lib/ui/input/Input.vue";
import { useVModel } from "@vueuse/core";
import { computed } from "vue";

interface EditableFieldProps extends InputProps {
  id: string;
  label: string;
}

const props = defineProps<EditableFieldProps>();
const delegatedProps = computed(() => {
  const { label: _, ...delegated } = props;
  return delegated;
});

const model = useVModel(props, "modelValue");
</script>

<template>
  <fieldset class="mb-3 flex items-center gap-2">
    <label :for="id" class="w-[130px] text-right text-[15px]">
      {{ label }}:
    </label>

    <div v-if="readonly" class="flex items-center space-x-2 px-3">
      <span> {{ modelValue }} </span>
    </div>
    <Input v-else v-bind="delegatedProps" v-model="model" class="flex-1" />
  </fieldset>
</template>
