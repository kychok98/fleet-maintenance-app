import { toast } from "@/lib/ui/toast";
import type { AxiosError } from "axios";
import axios from "axios";
import { BASE_URL } from "./constants.ts";

axios.defaults.baseURL = BASE_URL;

axios.interceptors.request.use(
  async (config) => {
    return config;
  },
  (err) => {
    console.error(err);
    return Promise.reject(err);
  },
);

axios.interceptors.response.use(
  async (response) => {
    return response;
  },
  async (err: AxiosError<{ error?: string; message?: string }>) => {
    toast({
      title: "API Error",
      description:
        err.response?.data?.error ?? err.response?.data?.message ?? err.message,
      variant: "destructive",
    });
    console.error(err);
    return Promise.reject(err);
  },
);

export default axios;
