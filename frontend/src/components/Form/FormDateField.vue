<script setup lang="ts">
import { Button } from "@/lib/ui/button";
import { Calendar } from "@/lib/ui/calendar";
import { Popover, PopoverContent, PopoverTrigger } from "@/lib/ui/popover";
import { cn, formatDate } from "@/lib/utils.ts";
import { DateValue } from "@internationalized/date";
import { useVModel } from "@vueuse/core";
import { Calendar as CalendarIcon } from "lucide-vue-next";
import { useForwardPropsEmits } from "radix-vue";

interface FormSelectProps {
  id: string;
  label: string;
  modelValue: DateValue | undefined;
  placeholder?: string;
  disabled?: boolean;
}

const props = defineProps<FormSelectProps>();
const forwarded = useForwardPropsEmits(props);
const value = useVModel(props, "modelValue");
</script>

<template>
  <fieldset class="mb-3 flex items-center gap-2">
    <label :for="id" class="w-[190px] text-right text-[15px]">
      {{ label }}:
    </label>

    <Popover>
      <PopoverTrigger as-child>
        <Button
          v-bind="forwarded"
          variant="outline"
          :class="cn('w-full justify-start text-left font-normal')"
        >
          <CalendarIcon class="mr-2 h-4 w-4" />
          <span v-if="value"> {{ formatDate(value) }} </span>
          <span v-else>{{ placeholder || "Pick a date" }}</span>
        </Button>
      </PopoverTrigger>
      <PopoverContent class="w-auto p-0">
        <Calendar v-model="value" initial-focus />
      </PopoverContent>
    </Popover>
  </fieldset>
</template>
