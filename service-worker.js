if(!self.define){let e,s={};const r=(r,i)=>(r=new URL(r+".js",i).href,s[r]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=r,e.onload=s,document.head.appendChild(e)}else e=r,importScripts(r),s()})).then((()=>{let e=s[r];if(!e)throw new Error(`Module ${r} didn’t register its module`);return e})));self.define=(i,n)=>{const l=e||("document"in self?document.currentScript.src:"")||location.href;if(s[l])return;let o={};const u=e=>r(e,l),t={module:{uri:l},exports:o,require:u};s[l]=Promise.all(i.map((e=>t[e]||u(e)))).then((e=>(n(...e),o)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/css/app.0d090761.css",revision:null},{url:"/index.html",revision:"7ca82373d8ae70b0ce725b4443c01d61"},{url:"/js/10.913fb790.js",revision:null},{url:"/js/13.96a71539.js",revision:null},{url:"/js/169.1d579ed7.js",revision:null},{url:"/js/656.c69347f0.js",revision:null},{url:"/js/about.b1853fa0.js",revision:null},{url:"/js/app.d9800951.js",revision:null},{url:"/js/chunk-vendors.cdafba02.js",revision:null},{url:"/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/sitemap.xml",revision:"158edabd177053311d99d7d86570873e"}],{})}));
//# sourceMappingURL=service-worker.js.map
