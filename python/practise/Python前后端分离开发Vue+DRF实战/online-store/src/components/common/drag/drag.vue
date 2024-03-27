<script type="text/javascript">
import Vue from 'vue'
 Vue.directive('drag', function (el, opt) {
            var oDiv=el;
            oDiv.onmousedown=function(ev){
                var disX=ev.clientX-oDiv.getBoundingClientRect().left;
                var disY=ev.clientY-oDiv.getBoundingClientRect().top;
                //克隆
                var newOdiv = oDiv.cloneNode(true);
                newOdiv.style.position = 'absolute';
                newOdiv.id = 'drag-box';
                var targetId=null;
                var targets = document.getElementsByClassName(opt.value.target);
                var xy=[];
                for(var i=0;i<targets.length;i++){
                    xy[i]={};                       
                    xy[i].top=targets[i].getBoundingClientRect().top;
                    xy[i].left=targets[i].getBoundingClientRect().left;
                    xy[i].width=targets[i].offsetWidth;
                    xy[i].height=targets[i].offsetHeight;                                             
                }; 
                document.onmousemove=function(ev){
                    document.body.appendChild(newOdiv);
                    var ox = ev.clientX;
                    var oy = ev.clientY;
                    var l = ox-disX;
                    var t = oy-disY;
                    newOdiv.style.left=l+'px';
                    newOdiv.style.top=t+'px';
                    //循环判断到达了哪一个目标的上面
                    for(var j=0;j<targets.length;j++){
                        if(oy>xy[j].top&&oy<xy[j].top+xy[j].height&&ox>xy[j].left&&ox<xy[j].left+xy[j].width){  
                            //console.log(targets[j].getAttribute('id'))  
                            targetId = targets[j].getAttribute('id'); 
                            opt.value.moverCallback(targetId)
                            return    
                        }
                        if(!(oy>xy[j].top&&oy<xy[j].top+xy[j].height&&ox>xy[j].left&&ox<xy[j].left+xy[j].width)){  
                            targetId = null    
                        }
                    }; 
                };
                document.onmouseup=function(){
                    if(targetId){
                        opt.value.upCallback(targetId)
                    }
                    var isNewbox = document.getElementById('drag-box');
                    isNewbox.parentNode.removeChild(isNewbox);
                    document.onmousemove=null;
                    document.onmouseup=null;
                };
            };
            return false ; 
})
</script>