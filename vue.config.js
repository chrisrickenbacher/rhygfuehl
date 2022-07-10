const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: 'rhygfuehl',
    themeColor: '#213A4E',
    msTileColor: '#213A4E',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    iconPath: {
      faviconSVG: 'img/icons/favicon.svg', 
    }
  }
})
