import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/n8n": {
        target: "https://spalaciom9.app.n8n.cloud",
        changeOrigin: true,
        secure: true,
        rewrite: (path) => path.replace(/^\/n8n/, ""),
      },
    },
  },
});