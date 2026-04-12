import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import AstroPWA from '@vite-pwa/astro';
import icon from 'astro-icon';

export default defineConfig({
  integrations: [
    tailwind(),
    icon(),
    AstroPWA({
      registerType: 'prompt',
      manifest: {
        name: 'rhygfuehl',
        short_name: 'rhygfuehl',
        description: '☀️ current Rhine temperature in Basel',
        theme_color: '#002855',
        background_color: '#002855',
        display: 'standalone',
        icons: [
          {
            src: '/pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: '/pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
          {
            src: '/maskable-icon-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable',
          },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico,webmanifest}'],
        navigateFallback: null,
      },
      devOptions: {
        enabled: true,
        type: 'module',
      },
    }),
  ],
  output: 'static',
});
