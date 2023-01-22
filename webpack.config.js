const SitemapPlugin = require('sitemap-webpack-plugin').default;

const paths = [
  '/',
  '/imprint',
  '/faq',
  '/en',
  '/en/faq'
];


module.exports = {
  module: {
    loaders: [
      {
        test: /\.json$/,
        loader: 'json-loader'
      }
    ]
  },
  plugins: [
    new SitemapPlugin({ base: 'https://rhygfuehl.ch', paths })
  ]
}