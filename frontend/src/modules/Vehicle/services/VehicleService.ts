import axios from "@/lib/axios";
import { type TVehicle } from "./schema.ts";

export const getVehicles = async () => {
  const res = await axios<TVehicle[]>("/vehicles/");
  return res.data;
};

export const deleteVehicles = async (id: number) => {
  const res = await axios.delete<void>(`/vehicles/${id}/`);
  return res.data;
};
