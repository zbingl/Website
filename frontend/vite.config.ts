import deno from "@deno/vite-plugin";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vitest/config";

export default defineConfig({
  plugins: [
    deno(),
    react(),
    tailwindcss(),
  ],
  build: {
    commonjsOptions: {
      include: [
        /registry.npmjs.org/,
        /node_modules/,
      ],
      transformMixedEsModules: true,
    },
  },
  test: {
    globals: true,
    environment: "happy-dom",
    setupFiles: "./src/setupTests.ts",
  },
});
