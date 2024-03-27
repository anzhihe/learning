//这个是全局文件

import mock from '../mock/mock.js'

//全局引入jq
import $ from 'jquery';
//全局引入vue
import Vue from 'vue';


//全局引入共用css
import './styles/common.scss';
//引入字体样式
import './styles/fonts/iconfont.css';
//全局引入路由配置
import router from './router';


//全局状态控制引入
import store from './store/store';


//全局加载resource拦截器
import './axios/';
import Axios from 'axios';
Vue.prototype.$http = Axios


//引入需要渲染的视图组件
import App from './App';

//创建全局实例
new Vue({
    el:'#app',
    router,
    store,
    template:'<App/>',
    components:{App}
})


