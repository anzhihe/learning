var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var Proxy = require('./proxy');
var fs = require('fs')
// 定义文件夹的路径
var ROOT_PATH = path.resolve(__dirname);

module.exports = {
	devtool: 'source-map', // 配置生成Source Maps 选择合适的选项
	// entry: './app/main.js', // 入口文件
	// entry: './src/main.js',// 入口文件 app: path.resolve(__dirname,'./src/main.js')
	entry: {
		// app: path.resolve(__dirname,'./src/main.js'),
		index: './src/main.js',
	},
	output: {
		path: __dirname + '/build', // 打包后文件存放位置
		filename: "[name].[hash].entry.js",
		chunkFilename: "[name].[hash].min.js"
		//publicPath: '/build/'
	},
	resolve: {
		// require时省略的扩展名
		extensions: ['.js', '.vue', '.json'],
		alias: {
			'vue$': 'vue/dist/vue.common.js'
		}
	},
	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		// new ExtractTextPlugin('style.css'),
		new HtmlWebpackPlugin({
			filename: 'index.html',
			template: 'template.html',
			inject: true
		}),
		//new webpack.optimize.CommonsChunkPlugin({name:'vendor',filename:'vendor.bundle.js'})

		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery',
			'window.$': 'jquery',
		})
	],
	/*
	externals: {
		jquery: 'window.$'
	}, */
	devServer: {
		//contentBase: './public', // 本地服务器所加载的页面所在的目录
		historyApiFallback: true, // 不跳转
		inline: true, // 实时刷新
		hot: true,
		proxy:Proxy
	},
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
				/*
				use: ExtractTextPlugin.extract({
					use: 'css-loader',
					fallback: 'style-loader'
				}) */
				loader: 'style-loader!css-loader'
				/*
				loader: 'style-loader!css-loader',
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
				test: /\.(png|jpe?g|gif|svg|jgp)(\?.*)?$/,
				loader: 'url-loader',
				options: {
					limit: 10000,
					name: 'static/images/[name].[hash:7].[ext]'
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
			// {
			// 	test: /\.js$/,
			// 	loader: 'babel-loader',
			// 	query: {
			// 		compact: false
			// 	}
			// },
			{
				test: /iview.src.*?js$/,
				loader: 'babel-loader'
			},
			{
				test: /\.js$/,
				loader: 'babel-loader',
				exclude: /node_modules/
			},
			{
		        test: /\.exec\.js$/,
		        use: [ 'script-loader' ]
		    }
		]
	},
}
