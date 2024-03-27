var webpack = require('webpack');
var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var ROOT_PATH = path.resolve(__dirname);

module.exports = {
   // devtool: 'source-map', // 配置生成Source Maps 选择合适的选项
    entry: {
        // app: path.resolve(__dirname,'./src/main.js'),
        index: './src/main.js',
    },
    output: {
        // path: __dirname + '/public', // 打包后文件存放位置
        //path: __dirname + '/dist', // 打包后文件存放位置
        path: path.resolve(__dirname, 'dist'),
        filename: "[name].entry.js",
        chunkFilename: "[name].min.js",
        publicPath: ''
    },
    plugins: [
        /*
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENY: '"production'
            }
        }), */
        // 压缩代码
        new webpack.optimize.UglifyJsPlugin({
          compress: {
            warnings: false
          },
          sourceMap: true
        }),
        // new webpack.optimize.UglifyJsPlugin({minimize: true}),
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: 'template.html',
            inject: true
        }),
        // new webpack.optimize.CommonsChunkPlugin({name:'vendor',filename:'vendor.bundle.js'})
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
            'window.$': 'jquery',
        })
    ],
    resolve: {
        // require时省略的扩展名
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    /*
    externals: {
        jquery: 'window.$'
    }, */
    module: {
        loaders: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                /*
                options: {
                    loaders: {
                        css: ExtractTextPlugin.extract({
                            use: 'css-loader',
                            fallback: 'vue-style-loader'
                        })
                    }
                } */
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
                /*

                options: {
                    loaders: {
                        css: ExtractTextPlugin.extract({
                            use: 'css-loader'
                        })
                    }
                } */
            },
            {
                test: /\.scss$/,
                loader: 'style-loader!css-loader!sass-loader'
            },
            {
                test: /\.json$/,
                loader: 'json-loader'
            },
            {
                test: /\.(png|jpe?g|gif|svg|jpg)(\?.*)?$/,
                loader: 'url-loader',
                options: {
                    limit: 100000,
                    name: '/static/images/[name].[hash:7].[ext]'
                }
            },
            {
                test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
                loader: 'url-loader',
                options: {
                    limit: 10000,
                    name: 'static/fonts/[name].[hash:7].[ext]'
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                query: {
                    compact: false
                }
            },
            {
                test: /\.exec\.js$/,
                use: [ 'script-loader' ]
            }
        ]
    },
}
