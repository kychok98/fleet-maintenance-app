import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwind from "tailwindcss";
import autoprefixer from "autoprefixer";
import path from "node:path";

// https://vitejs.dev/config/
export default defineConfig({
  css: {
    postcss: {
      plugins: [tailwind(), autoprefixer()],
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://backend-dj:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  preview: {
    port: 3000,
    strictPort: true,
  },
});
