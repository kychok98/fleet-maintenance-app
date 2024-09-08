import DataTableColumnHeader from "@/components/DataTable/DataTableColumnHeader.vue";
import type { ColumnDef } from "@tanstack/vue-table";
import { h } from "vue";
import BadgeType from "./components/BadgeType.vue";
import DataTableRowActions from "./components/DataTableRowActions.vue";
import type { TMaintenance } from "./services/schema.ts";

export const columns: ColumnDef<TMaintenance>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "ID" }),
    cell: ({ row }) => h("div", { class: "w-12" }, row.getValue("id")),
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
        class: "w-24",
        column,
        title: "Completion date",
      }),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-center w-24" },
        row.original.completion_date || "-",
      );
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
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
