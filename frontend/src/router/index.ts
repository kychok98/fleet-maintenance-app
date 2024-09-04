import { createRouter, createWebHistory } from "vue-router";
import routes from "./routes";

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

router.beforeEach(async (_, __, next) => {
  return next();
});

export default router;
