import { TVehicle } from "./services/schema.ts";

export const getLabel = (data: TVehicle) => {
  return `${data.year} ${data.make} ${data.model}`;
};
