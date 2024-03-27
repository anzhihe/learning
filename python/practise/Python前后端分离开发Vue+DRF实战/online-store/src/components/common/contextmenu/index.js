
import contextmenuComponent from './contextmenu'
//这里是初始值
const defaults={
    event:''

}

//合并函数
function merge(target) {
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

//插件注册
const contextmenu = {
  install: function(Vue) {
    var contextmenuConstructor = Vue.extend(contextmenuComponent);

    Vue.prototype.$contextmenu = function(options){
        //console.log(options)
        var event =event||window.event;
        //var data = merge({},defaults,options);
        var contextmenuVm = new contextmenuConstructor({
            data(){
                return {
                    top:'-500px',
                    left:'-500px',
                    items:options,
                    isShowChildIndex:null
                };
            },
            methods:{
                removeDom:function(){
                    var menu = document.getElementById('contextMenu-box');
                    if(menu){
                        menu.parentNode.removeChild(menu)
                    }
                },
                rightClick(fn){
                    fn()//执行事件
                    //删除dom
                    this.removeDom()
                }
            }
        })
       Vue.nextTick(function(){
         //将loading组件插入到target元素上
        document.body.appendChild(contextmenuVm.$mount().$el); 
        var menu = document.getElementById('contextMenu');
        var left = event.clientX + 5, /* nudge to the right, so the pointer is covering the title */
            top = event.clientY;
        if (top + menu.offsetHeight >= document.body.clientHeight) {
            top -= menu.offsetHeight;
        }
        if (left + menu.offsetWidth >= document.body.clientWidth) {
            left -= menu.offsetWidth;
        }
        menu.style.zIndex=1000001;
        menu.style.left=left+'px';
        menu.style.top=top+'px';
       })
      return contextmenuVm;
    }
  }
}
export default contextmenu;