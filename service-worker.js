if(!self.define){let e,s={};const r=(r,i)=>(r=new URL(r+".js",i).href,s[r]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=r,e.onload=s,document.head.appendChild(e)}else e=r,importScripts(r),s()})).then((()=>{let e=s[r];if(!e)throw new Error(`Module ${r} didn’t register its module`);return e})));self.define=(i,n)=>{const l=e||("document"in self?document.currentScript.src:"")||location.href;if(s[l])return;let o={};const u=e=>r(e,l),t={module:{uri:l},exports:o,require:u};s[l]=Promise.all(i.map((e=>t[e]||u(e)))).then((e=>(n(...e),o)))}}define(["./workbox-2d118ab0"],(function(e){"use strict";e.setCacheNameDetails({prefix:"rhygfuehl"}),self.skipWaiting(),e.precacheAndRoute([{url:"/css/app.ffb15583.css",revision:null},{url:"/index.html",revision:"b7a3e249a1909de3e162ea95301d2182"},{url:"/js/10.fce7e30c.js",revision:null},{url:"/js/13.e518cfb3.js",revision:null},{url:"/js/169.3b83b61f.js",revision:null},{url:"/js/about.751b7c0b.js",revision:null},{url:"/js/app.9bd77ec4.js",revision:null},{url:"/js/chunk-vendors.2fa1a1dc.js",revision:null},{url:"/manifest.json",revision:"4872884c319e3cb20d8152f2d5f2d9b9"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/sitemap.xml",revision:"181de5a2b49ce96670231a14a6c544b2"}],{})}));
//# sourceMappingURL=service-worker.js.map
