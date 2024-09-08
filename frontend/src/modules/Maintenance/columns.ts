import DataTableColumnHeader from "@/components/DataTable/DataTableColumnHeader.vue";
import { Checkbox } from "@/lib/ui/checkbox";
import type { ColumnDef } from "@tanstack/vue-table";
import { h } from "vue";
import BadgeType from "./components/BadgeType.vue";
import DataTableRowActions from "./components/DataTableRowActions.vue";
import type { TMaintenance } from "./services/schema.ts";

export const columns: ColumnDef<TMaintenance>[] = [
  {
    id: "select",
    header: ({ table }) =>
      h(Checkbox, {
        checked:
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && "indeterminate"),
        "onUpdate:checked": (value) => table.toggleAllPageRowsSelected(!!value),
        ariaLabel: "Select all",
        class: "translate-y-0.5",
      }),
    cell: ({ row }) =>
      h(Checkbox, {
        checked: row.getIsSelected(),
        "onUpdate:checked": (value) => row.toggleSelected(!!value),
        ariaLabel: "Select row",
        class: "translate-y-0.5",
      }),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "schedule_date",
    header: ({ column }) =>
      h(DataTableColumnHeader, {
        class: "w-24",
        column,
        title: "Schedule date",
      }),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center w-24" },
        row.original.schedule_date,
      );
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
    enableHiding: false,
  },
  {
    accessorKey: "completion_date",
    header: ({ column }) =>
      h(DataTableColumnHeader, {
        class: "w-[120px]",
        column,
        title: "Completion date",
      }),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center w-[120px]" },
        row.original.completion_date || "-",
      );
    },
    filterFn: (row, id, value) => {
      if (value.length > 1) return true;

      if (value.includes("pending")) {
        return row.getValue(id) === null;
      }
      return row.getValue(id) !== null;
    },
    enableHiding: false,
  },
  {
    accessorKey: "vehicle",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Vehicle ID" }),
    cell: ({ row }) => {
      return h("div", { class: "text-right w-16" }, row.original.vehicle);
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    accessorKey: "description",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Description" }),
    cell: ({ row }) => {
      return h("div", { class: "truncate min-w-40" }, row.original.description);
    },
  },
  {
    accessorKey: "schedule_type",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "Type" }),
    cell: ({ row }) => {
      const type = row.getValue(
        "schedule_type",
      ) as TMaintenance["schedule_type"];
      return h("div", { class: "text-center w-[80px]" }, [
        h(BadgeType, { type }),
      ]);
    },
  },
  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
