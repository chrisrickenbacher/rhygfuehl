if(!self.define){let e,s={};const r=(r,i)=>(r=new URL(r+".js",i).href,s[r]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=r,e.onload=s,document.head.appendChild(e)}else e=r,importScripts(r),s()})).then((()=>{let e=s[r];if(!e)throw new Error(`Module ${r} didn’t register its module`);return e})));self.define=(i,n)=>{const l=e||("document"in self?document.currentScript.src:"")||location.href;if(s[l])return;let o={};const u=e=>r(e,l),c={module:{uri:l},exports:o,require:u};s[l]=Promise.all(i.map((e=>c[e]||u(e)))).then((e=>(n(...e),o)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/css/app.0d090761.css",revision:null},{url:"/index.html",revision:"e4fc8046609d270cca2dce146df0fd58"},{url:"/js/10.6e26760b.js",revision:null},{url:"/js/13.c7ebfc4f.js",revision:null},{url:"/js/169.db8fbd62.js",revision:null},{url:"/js/656.5a9bcb17.js",revision:null},{url:"/js/about.7dc92c64.js",revision:null},{url:"/js/app.2c90d643.js",revision:null},{url:"/js/chunk-vendors.cdafba02.js",revision:null},{url:"/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/sitemap.xml",revision:"158edabd177053311d99d7d86570873e"}],{})}));
//# sourceMappingURL=service-worker.js.map
