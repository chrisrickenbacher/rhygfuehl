if(!self.define){let e,r={};const s=(s,l)=>(s=new URL(s+".js",l).href,r[s]||new Promise((r=>{if("document"in self){const e=document.createElement("script");e.src=s,e.onload=r,document.head.appendChild(e)}else e=s,importScripts(s),r()})).then((()=>{let e=r[s];if(!e)throw new Error(`Module ${s} didn’t register its module`);return e})));self.define=(l,u)=>{const i=e||("document"in self?document.currentScript.src:"")||location.href;if(r[i])return;let n={};const o=e=>s(e,i),t={module:{uri:i},exports:n,require:o};r[i]=Promise.all(l.map((e=>t[e]||o(e)))).then((e=>(u(...e),n)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/rhygfuehl/css/app.0b97b9e2.css",revision:null},{url:"/rhygfuehl/index.html",revision:"c0cc587b159acb0dde910b7707509699"},{url:"/rhygfuehl/js/10.46fdfb78.js",revision:null},{url:"/rhygfuehl/js/13.86b6eed2.js",revision:null},{url:"/rhygfuehl/js/169.dbd2f42f.js",revision:null},{url:"/rhygfuehl/js/about.ec58d0c7.js",revision:null},{url:"/rhygfuehl/js/app.89e5e3c7.js",revision:null},{url:"/rhygfuehl/js/chunk-vendors.9d9e26a0.js",revision:null},{url:"/rhygfuehl/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/rhygfuehl/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"}],{})}));
//# sourceMappingURL=service-worker.js.map
