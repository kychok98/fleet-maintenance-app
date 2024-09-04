import { ROUTE_NAME } from "@/router/constants";
import ErrorView from "@/views/ErrorView.vue";
import LandingView from "@/views/LandingView.vue";
import MaintenanceView from "@/views/MaintenanceView.vue";
import VehicleView from "@/views/VehicleView.vue";
import { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  {
    path: "/:catchAll(.*)*",
    name: ROUTE_NAME.Error,
    component: ErrorView,
  },
  {
    path: "/",
    component: LandingView,
    redirect: () => {
      return { name: ROUTE_NAME.Vehicle };
    },
    children: [
      {
        path: "vehicle",
        name: ROUTE_NAME.Vehicle,
        component: VehicleView,
      },
      {
        path: "maintenance",
        name: ROUTE_NAME.Maintenance,
        component: MaintenanceView,
      },
    ],
  },
];

export default routes;
