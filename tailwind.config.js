const colors = require("tailwindcss/colors")
module.exports = {
  content: ['./src/**/*.{vue,js}', './node_modules/paw/**/*.vue'],
  darkMode: 'class',
  theme: {
    extend: {
      strokeWidth: {
        '3': '3',
        '4': '4'
      }
    },
    colors: {
      darkblue: '#213A4E',
      white: '#FFFFFF',
      gray: colors.gray
    },
    fontFamily: {
      sans: ['Roboto']
    }
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography')
  ]
}