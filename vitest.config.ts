/// <reference types="vitest" />
import { defineConfig } from 'vitest/config';

export default defineConfig({
	test: {
		environment: 'jsdom',
		setupFiles: ['./vitest-setup.ts'],
		include: ['tests/unit/**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}'],
		reporters: process.env.CI ? ['default', 'junit'] : ['default'],
		outputFile: process.env.CI ? { junit: 'test-results/vitest-results.xml' } : undefined,
	},
});
