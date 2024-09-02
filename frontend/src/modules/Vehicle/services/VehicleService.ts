import { type TVehicle } from "./schema.ts";
import axios from "axios";

export const getVehicles = async () => {
  const res = await axios<TVehicle[]>("/api/vehicles/");
  console.log("res:", res.data);
  return res.data;
};
