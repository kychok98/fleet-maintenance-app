<script setup lang="ts">
import type { TVehicle } from "@/modules/Vehicle/services/schema.ts";
import { Button } from "@/lib/ui/button";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/lib/ui/dropdown-menu";
import { DotsHorizontalIcon } from "@radix-icons/vue";
import type { Row } from "@tanstack/vue-table";

interface DataTableRowActionsProps {
  row: Row<TVehicle>;
}
defineProps<DataTableRowActionsProps>();
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button
        variant="ghost"
        class="data-[state=open]:bg-muted flex h-8 w-8 p-0"
      >
        <DotsHorizontalIcon class="h-4 w-4" />
        <span class="sr-only">Open menu</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end" class="w-[160px]">
      <DropdownMenuItem>Edit</DropdownMenuItem>
      <DropdownMenuItem>Make a copy</DropdownMenuItem>
      <DropdownMenuItem>Favorite</DropdownMenuItem>
      <DropdownMenuSeparator />
      <DropdownMenuSeparator />
      <DropdownMenuItem>
        Delete
        <DropdownMenuShortcut>⌘⌫</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
