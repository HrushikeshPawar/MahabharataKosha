import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import eslintConfigPrettier from "eslint-config-prettier";

// The new syntax exports the array directly, fixing the deprecation warning.
export default [
  // 1. Global ignores
  {
    ignores: ["dist", "node_modules"],
  },

  // 2. Base configuration for all JS/TS files
  js.configs.recommended,
  ...tseslint.configs.recommended,

  // 3. Configuration specific to React (TSX files)
  {
    files: ["**/*.{ts,tsx}"],
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    languageOptions: {
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      // These are the rules that were previously in 'extends'
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn",
      "react-refresh/only-export-components": "warn",
    },
  },

  // 4. Prettier config MUST be last.
  // This turns off any ESLint rules that would conflict with Prettier.
  eslintConfigPrettier,
];
