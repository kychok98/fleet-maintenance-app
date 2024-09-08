import { z } from "zod";

export const maintenanceSchema = z.object({
  id: z.number(),
  schedule_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/), // Validating date format YYYY-MM-DD
  completion_date: z
    .string()
    .regex(/^\d{4}-\d{2}-\d{2}$/)
    .nullable(), // Validating date format YYYY-MM-DD
  vehicle: z.string(),
  description: z.string(),
  schedule_type: z.enum(["auto", "manual"]),
});

export type TMaintenance = z.infer<typeof maintenanceSchema>;

export const maintenanceUpdateSchema = z.object({
  schedule_date: z
    .string()
    .regex(/^\d{4}-\d{2}-\d{2}$/)
    .optional(), // Validating date format YYYY-MM-DD
  completion_date: z
    .string()
    .regex(/^\d{4}-\d{2}-\d{2}$/)
    .optional(), // Validating date format YYYY-MM-DD
  description: z.string(),
});

export type MaintenanceUpdateParam = z.infer<typeof maintenanceUpdateSchema>;

export const maintenanceAddSchema = z.object({
  vehicle_id: z.number().min(0, "Vehicle ID is required").optional(),
  schedule_date: z.date().optional(),
  description: z.string(),
});

export type MaintenanceAddParam = z.infer<typeof maintenanceAddSchema>;
