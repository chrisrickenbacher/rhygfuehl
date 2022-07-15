/* eslint-disable no-undef */
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst } from 'workbox-strategies';
import { Plugin } from 'workbox-expiration';
import { precacheAndRoute } from 'workbox-precaching'
precacheAndRoute(self.__WB_MANIFEST)

// //Only if you use google analytics and wants to send the offline views
// workbox.googleAnalytics.initialize()

// Use cache but update cache files in the background ASAP
registerRoute(
  /.*\.(?:css|js)/,
  new StaleWhileRevalidate({
    cacheName: 'live'
  })
)

//Cache first, but defining duration and maximum files
registerRoute(
  /.*\.(?:png|jpg|jpeg|svg|gif)/,
  new CacheFirst({
    cacheName: 'images',
    plugins: [
      new Plugin({
        maxEntries: 20,
        maxAgeSeconds: 7 * 24 * 60 * 60
      })
    ]
  })
)

registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  new CacheFirst({
    cacheName: 'googleapis',
    plugins: [
      new Plugin({
        maxEntries: 30
      })
    ]
  })
)