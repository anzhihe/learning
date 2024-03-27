<script type="text/javascript">
import Vue from 'vue'
import '../../common/contextmenu/contextmenu.css'
 Vue.directive('contextmenu', function (el, opt) {
    el.oncontextmenu = function(ev){
        var items = opt.value
        var thisDOM=gitContextmenuDom(items);
        document.body.appendChild(thisDOM);
        var menu = document.getElementById('contextmenu');
        var left = ev.clientX + 5, /* nudge to the right, so the pointer is covering the title */
            top = ev.clientY;
        if (top + menu.offsetHeight >= document.body.clientHeight) {
            top -= menu.offsetHeight;
        }
        if (left + menu.offsetWidth >= document.body.clientWidth) {
            left -= menu.offsetWidth;
        }
        menu.style.zIndex=1000001;
        menu.style.left=left+'px';
        menu.style.top=top+'px';
        return false
        }
})

//根据数据得到dom结构
function gitContextmenuDom(items){
    var Dom=document.createElement("ul");
    for(var i=0 ;i<items.length;i++){
        var node = document.createElement('li'); 
        var icon = document.createElement('i'); 
        icon.className = "iconfont";
        //添加icon
        if(items[i].icon){
            //var iconFont = document.createTextNode(items[i].icon); 
            //icon.appendChild(iconFont)    
            icon.innerHTML(items[i].icon);         
        }
        node.appendChild(icon);
        var title = document.createElement('span'); 
        var label = document.createTextNode(items[i].label);
        //添加标题
        title.appendChild(label);
        node.appendChild(title);
        //判断当前有无子级
        if(items[i].items){
            var childDom = gitContextmenuDom(items[i].items);
            node.appendChild(childDom);
        }
        Dom.appendChild(node);
    }
    Dom.id="contextmenu";
    Dom.style.position='absolute';
    Dom.style.width=120+'px';
    return Dom;
}
</script>