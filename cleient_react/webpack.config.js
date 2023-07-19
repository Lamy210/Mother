// webpack.config.js
const path = require('path');

module.exports = {
  // ...他の設定
  resolve: {
    fallback: {
      stream: require.resolve('stream-browserify'),
      util: require.resolve('util/'),
      url: require.resolve('url/'),
      zlib: require.resolve('browserify-zlib'),
      path: require.resolve('path-browserify')
    }
  }
};
