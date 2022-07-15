/* eslint-disable no-undef */
import { precacheAndRoute } from 'workbox-precaching'
precacheAndRoute(self.__WB_MANIFEST)

//Only if you use google analytics and wants to send the offline views
workbox.googleAnalytics.initialize()

// Use cache but update cache files in the background ASAP
workbox.routing.registerRoute(
  /.*\.(?:css|js)/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: 'live'
  })
)

//Cache first, but defining duration and maximum files
workbox.routing.registerRoute(
  /.*\.(?:png|jpg|jpeg|svg|gif)/,
  workbox.strategies.cacheFirst({
    cacheName: 'images',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 20,
        maxAgeSeconds: 7 * 24 * 60 * 60
      })
    ]
  })
)

workbox.routing.registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  workbox.strategies.cacheFirst({
    cacheName: 'googleapis',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 30
      })
    ]
  })
)