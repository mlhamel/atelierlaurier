const path = require('path')
const webpack = require('webpack');

module.exports = {
    mode: 'production',
    entry: {
        vendor: [
            path.resolve(__dirname, "node_modules/jquery/dist/jquery.js"),
            path.resolve(__dirname, "node_modules/bootstrap/dist/js/bootstrap.bundle.js"),
            path.resolve(__dirname, 'node_modules/magnific-popup/dist/jquery.magnific-popup.js')
        ]
    },
    output: {
      filename: 'atelierlaurier.js',
      path: path.resolve(__dirname, 'atelierlaurier/static/js/')
    }
  }