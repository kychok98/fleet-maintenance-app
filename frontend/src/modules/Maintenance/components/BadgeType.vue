<script setup lang="ts">
import Badge from "@/lib/ui/badge/Badge.vue";
import { TMaintenance } from "@/modules/Maintenance/services/schema.ts";

interface IProps {
  type: TMaintenance["schedule_type"];
}

const typeVariant = {
  auto: "outline",
  manual: "default",
} as const;

defineProps<IProps>();
</script>

<template>
  <Badge :variant="typeVariant[type]">
    {{ type.toUpperCase() }}
  </Badge>
</template>
