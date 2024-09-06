import DataTableColumnHeader from "@/components/DataTable/DataTableColumnHeader.vue";
import { formatNumberWithCommas } from "@/lib/utils.ts";
import { getLabel } from "@/modules/Vehicle/utils.ts";
import type { ColumnDef } from "@tanstack/vue-table";
import { twMerge } from "tailwind-merge";
import { h } from "vue";
import type { TVehicle } from "./services/schema.ts";
import BadgeStatus from "./components/BadgeStatus.vue";
import DataTableRowActions from "./components/DataTableRowActions.vue";

export const columns: ColumnDef<TVehicle>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "ID" }),
    cell: ({ row }) => h("div", { class: "w-12" }, row.getValue("id")),
    enableHiding: false,
  },
  {
    accessorKey: "model",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Car Model" }),
    cell: ({ row }) => {
      return h("div", { class: "truncate min-w-40" }, getLabel(row.original));
    },
  },
  {
    accessorKey: "mileage",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Mileage (KM)" }),
    cell: ({ row }) => {
      const label = formatNumberWithCommas(row.getValue("mileage"));
      return h("div", { class: "text-right w-20" }, label);
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    id: "Last service date",
    accessorKey: "last_service_date",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Last service date" }),
    cell: ({ row }) => {
      return h(
        "div",
        { class: "text-right w-28" },
        row.original.last_service_date,
      );
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    accessorKey: "status",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Status" }),
    cell: ({ row }) => {
      const status = row.getValue("status") as TVehicle["status"];
      return h("div", { class: twMerge("text-center w-12") }, [
        h(BadgeStatus, { status: status }),
      ]);
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
