import { DateValue, getLocalTimeZone } from "@internationalized/date";
import type { Updater } from "@tanstack/vue-table";
import { formatDate as VueUseFormatDate } from "@vueuse/core";
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import type { Ref } from "vue";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function valueUpdater<T extends Updater<any>>(
  updaterOrValue: T,
  ref: Ref,
) {
  ref.value =
    typeof updaterOrValue === "function"
      ? updaterOrValue(ref.value)
      : updaterOrValue;
}

export function formatNumberWithCommas(num: number): string {
  return num.toLocaleString("en-US");
}

export function buildParams(data: Record<any, any>) {
  const params = new URLSearchParams();

  Object.entries(data).forEach(([key, value]) => {
    if (Array.isArray(value)) {
      value.forEach((value) => params.append(key, value.toString()));
    } else {
      params.append(key, (value || false).toString());
    }
  });

  return params.toString();
}

export function formatDate(value: DateValue, format = "YYYY-MM-DD") {
  return VueUseFormatDate(value.toDate(getLocalTimeZone()), format);
}
