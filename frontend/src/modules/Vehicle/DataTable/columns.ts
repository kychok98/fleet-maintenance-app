import { Badge } from "@/lib/ui/badge";
import { formatNumberWithCommas } from "@/lib/utils.ts";
import type { ColumnDef } from "@tanstack/vue-table";
import { twMerge } from "tailwind-merge";
import { h } from "vue";
import { statusVariants } from "../constants.ts";
import type { TVehicle } from "../services/schema.ts";
import DataTableColumnHeader from "./DataTableColumnHeader.vue";
import DataTableRowActions from "./DataTableRowActions.vue";

export const columns: ColumnDef<TVehicle>[] = [
  {
    accessorKey: "vin",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "VIN" }),
    cell: ({ row }) => h("div", { class: "w-12" }, row.getValue("vin")),
    enableHiding: false,
  },
  {
    accessorKey: "model",
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: "Car Model" }),
    cell: ({ row }) => {
      const label = `${row.original.make} ${row.original.model}`;
      return h("div", { class: "truncate min-w-40" }, label);
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
      const key = row.getValue("status") as TVehicle["status"];
      return h("div", { class: twMerge("text-center w-12") }, [
        h(Badge, { variant: statusVariants[key] }, () => key.toUpperCase()),
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
