
/* eslint-disable no-console */
import { register } from 'register-service-worker'
 
if (process.env.NODE_ENV === 'production') {
 register(`${process.env.BASE_URL}sw.js`, {
   ready () {
     console.log(
       'App is being served from cache by a service worker.'
     )
   },
   cached () {
     console.log('Content has been cached for offline use.')
   },
   updated () {
    window.location.reload(true)
   },
   offline () {
     console.log('No internet connection found. App is running in offline mode.')
   },
   error (error) {
     console.error('Error during service worker registration:', error)
   }
 })
}