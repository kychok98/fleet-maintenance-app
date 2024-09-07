import axios from "@/lib/axios";
import type {
  TMaintenance,
  MaintenanceAddParam,
  MaintenanceUpdateParam,
} from "./schema.ts";

const BASE_URL = "/maintenance";

export const getMaintenances = async () => {
  const res = await axios<TMaintenance[]>(`${BASE_URL}/`);
  return res.data;
};

export const deleteMaintenance = async (id: number) => {
  const res = await axios.delete<void>(`${BASE_URL}/${id}/`);
  return res.data;
};

export const updateMaintenance = async (
  id: number,

  data: MaintenanceUpdateParam,
) => {
  const res = await axios.put<TMaintenance>(`${BASE_URL}/${id}/`, data);
  return res.data;
};

export const addMaintenance = async (data: MaintenanceAddParam) => {
  const res = await axios.post<TMaintenance>(`${BASE_URL}/add/`, data);
  return res.data;
};
