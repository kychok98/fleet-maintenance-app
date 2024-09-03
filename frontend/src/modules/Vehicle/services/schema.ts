import { z } from "zod";

export const vehicleSchema = z.object({
  id: z.number(),
  make: z.string(),
  model: z.string(),
  year: z.number().int().min(1886),
  vin: z.string(),
  mileage: z.number().int().nonnegative(),
  last_service_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/), // Validating date format YYYY-MM-DD
  status: z.enum(["active", "inactive", "pending"]),
});

export type TVehicle = z.infer<typeof vehicleSchema>;

export const vehicleUpdateSchema = z.object({
  make: z.string(),
  model: z.string(),
  year: z.number().int().min(1886),
  mileage: z.number().int().nonnegative(),
});

export type VehicleUpdateParam = z.infer<typeof vehicleUpdateSchema>;
