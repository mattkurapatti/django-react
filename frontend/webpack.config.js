module.exports = {
    mode: 'development',
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            // {
            //     test: /\.css$/i,
            //     use: [
            //         {
            //             loader: ExtractCssChunks.loader,
            //             options: {hot: true}
            //         },
            //         {
            //             loader: "css-loader", //generating unique classname
            //             options: {
            //                 importLoaders: 1, // if specifying more loaders
            //                 modules: true,
            //                 sourceMap: false,
            //                 localIdentName: "[path]___[name]__[local]___[hash:base64:5]" //babel-plugin-css-module format
            //                 //localIdentName: "[path][name]__[local]" //recommended settings by cssloader#local-scope , this option generate unique classname for compiled css
            //             }
            //         }
            //     ]
            // }
        ]
    },
    devServer: {
        historyApiFallback: true,
        hot: true
    },
};