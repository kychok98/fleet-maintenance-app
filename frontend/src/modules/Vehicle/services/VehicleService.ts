import axios from "@/lib/axios";
import { buildParams } from "@/lib/utils.ts";
import type {
  TVehicle,
  VehicleAddParam,
  VehicleUpdateParam,
} from "./schema.ts";

export const getVehicles = async (
  param: { status?: string; sort_by?: string } = {},
) => {
  const res = await axios<TVehicle[]>("/vehicles/?" + buildParams(param));
  return res.data;
};

export const getVehicleById = async (id: number) => {
  const res = await axios<TVehicle>(`/vehicles/${id}/`);
  return res.data;
};

export const deleteVehicle = async (id: number) => {
  const res = await axios.delete<void>(`/vehicles/${id}/`);
  return res.data;
};

export const updateVehicle = async (id: number, data: VehicleUpdateParam) => {
  const res = await axios.put<TVehicle>(`/vehicles/${id}/`, data);
  return res.data;
};

export const addVehicle = async (data: VehicleAddParam) => {
  const res = await axios.post<TVehicle>(`/vehicles/add/`, data);
  return res.data;
};
