<script setup lang="ts">
import Badge from "@/lib/ui/badge/Badge.vue";
import { TVehicle } from "@/modules/Vehicle/services/schema.ts";

interface IProps {
  status: TVehicle["status"];
}

const statusVariants = {
  active: "success",
  inactive: "destructive",
  pending: "warning",
} as const;

defineProps<IProps>();
</script>

<template>
  <Badge :variant="statusVariants[status]">
    {{ status.toUpperCase() }}
  </Badge>
</template>
