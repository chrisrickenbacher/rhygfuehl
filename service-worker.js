if(!self.define){let e,r={};const s=(s,l)=>(s=new URL(s+".js",l).href,r[s]||new Promise((r=>{if("document"in self){const e=document.createElement("script");e.src=s,e.onload=r,document.head.appendChild(e)}else e=s,importScripts(s),r()})).then((()=>{let e=r[s];if(!e)throw new Error(`Module ${s} didn’t register its module`);return e})));self.define=(l,u)=>{const i=e||("document"in self?document.currentScript.src:"")||location.href;if(r[i])return;let n={};const o=e=>s(e,i),f={module:{uri:i},exports:n,require:o};r[i]=Promise.all(l.map((e=>f[e]||o(e)))).then((e=>(u(...e),n)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/rhygfuehl/css/app.c695f0b2.css",revision:null},{url:"/rhygfuehl/index.html",revision:"8fed23bcc7db5cae8937b6655a34a69c"},{url:"/rhygfuehl/js/10.7178205a.js",revision:null},{url:"/rhygfuehl/js/13.4a166b8a.js",revision:null},{url:"/rhygfuehl/js/169.7bf7b242.js",revision:null},{url:"/rhygfuehl/js/about.ec58d0c7.js",revision:null},{url:"/rhygfuehl/js/app.e8a4efbf.js",revision:null},{url:"/rhygfuehl/js/chunk-vendors.9d9e26a0.js",revision:null},{url:"/rhygfuehl/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/rhygfuehl/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"}],{})}));
//# sourceMappingURL=service-worker.js.map
