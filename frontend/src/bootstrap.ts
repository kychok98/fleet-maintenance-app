import "@/assets/index.css";
import router from "@/router";

import { VueQueryPlugin } from "@tanstack/vue-query";
import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);

app.use(router).use(VueQueryPlugin);

app.mount("#app");
