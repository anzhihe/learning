import LoadingComponent from './loading.vue'
//这里是初始值
const defaults={
	target:"",
	text:"",
	flag:true,
}
function merag(target) {
  for (let i = 1, j = arguments.length; i < j; i++) {
    let source = arguments[i] || {};
    for (let prop in source) {
      if (source.hasOwnProperty(prop)) {
        let value = source[prop];
        if (value !== undefined) {
          target[prop] = value;
        }
      }
    }
  }
  return target;
};
const loading = {
  install: function(Vue) {
    var LoadingConstructor = Vue.extend(LoadingComponent);
    Vue.prototype.$addLoading = function(options){
    	console.log(options);

    	var data = merag({},defaults,options);
    	var loadings = new LoadingConstructor({
    		data(){
    			return data;
    		},
    		methods:{
    			close(){
    				this.flag = false
    			}
    		}
    	})
      Vue.nextTick(function(){
        //判断target元素中是否添加了loading  如果有移除
        var target = document.querySelector(data.target);
        console.log(target);
        var loadingDom = target.getElementsByClassName("pio-loading2");
        if(loadingDom.length>0){
          target.removeChild(loadingDom[0]);
        }
        //将loading组件插入到target元素上
        document.querySelector(data.target).appendChild(loadings.$mount().$el); 
      })

      return loadings;
    }
  }
}
export default loading;