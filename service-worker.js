if(!self.define){let e,s={};const r=(r,i)=>(r=new URL(r+".js",i).href,s[r]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=r,e.onload=s,document.head.appendChild(e)}else e=r,importScripts(r),s()})).then((()=>{let e=s[r];if(!e)throw new Error(`Module ${r} didn’t register its module`);return e})));self.define=(i,n)=>{const l=e||("document"in self?document.currentScript.src:"")||location.href;if(s[l])return;let o={};const u=e=>r(e,l),c={module:{uri:l},exports:o,require:u};s[l]=Promise.all(i.map((e=>c[e]||u(e)))).then((e=>(n(...e),o)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/css/app.ffb15583.css",revision:null},{url:"/index.html",revision:"50da22d7b91f5f08b3c3a1e756193c8c"},{url:"/js/10.6e3650c5.js",revision:null},{url:"/js/13.6b7c0dcb.js",revision:null},{url:"/js/169.6988c5f5.js",revision:null},{url:"/js/about.b1853fa0.js",revision:null},{url:"/js/app.06d1e633.js",revision:null},{url:"/js/chunk-vendors.cdafba02.js",revision:null},{url:"/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/sitemap.xml",revision:"15ed7f8da2812360ea450dbcb1943875"}],{})}));
//# sourceMappingURL=service-worker.js.map
