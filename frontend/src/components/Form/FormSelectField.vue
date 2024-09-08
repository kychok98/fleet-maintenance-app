<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/lib/ui/select";
import { useVModel } from "@vueuse/core";
import { computed } from "vue";

interface FormSelectProps {
  id: string;
  label: string;
  items: ISelectItem[];
  placeholder: string;
  modelValue: string | undefined;
}

const props = defineProps<FormSelectProps>();
const delegatedProps = computed(() => {
  const { label: _, ...delegated } = props;
  return delegated;
});

const model = useVModel(props, "modelValue");
</script>

<template>
  <fieldset class="mb-3 flex items-center gap-2">
    <label :for="id" class="w-[190px] text-right text-[15px]">
      {{ label }}:
    </label>

    <Select v-bind="delegatedProps" v-model="model">
      <SelectTrigger>
        <SelectValue :placeholder="placeholder" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectItem
            v-for="item in items"
            :key="item.value"
            :value="item.value"
          >
            {{ item.label }}
          </SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
  </fieldset>
</template>
