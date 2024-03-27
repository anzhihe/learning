<template>
    <div id="contextMenu-box" class="contextMenu-box" @mouseover="isShowChildIndex = null" @click="removeDom" @contextmenu.prevent="removeDom">
        <ul id="contextMenu" class="contextMenuPlugin" :style="{left:left,top:top}">
            <li v-for="(m,index) in items.items" :key="index" @click.stop="rightClick(m.action)" @mouseover.stop="isShowChildIndex = index">
            <div class="ellipsis">
                <i class="iconfont" v-if="m.icon" v-html="m.icon"></i>
                <span>{{m.label}}</span>
                <i class="iconfont right" v-if="m.items">&#xe665;</i>
            </div>
                <ul class="contextMenuPlugin" v-if='m.items' v-show="index == isShowChildIndex">
                    <li v-for="(j,k) in m.items" @click.stop="rightClick(j.action)">
                        <div class="ellipsis">
                             <i class="iconfont" v-if="j.icon" v-html="j.icon"></i>
                             <span>{{j.label}}</span>
                        </div >
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<style scoped lang="scss">
.contextMenu-box{
    position:absolute;
    width:100%;
    height:100%;
    top:0;
    z-index:9999;
}
.contextMenuPlugin {
  position:absolute;
  -webkit-user-select: none;
  font-size: 11px;
  position: absolute;
  min-width:110px;
  max-width:140px;
  list-style-type: none;
  margin: 0;
  background-color: #fff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.15);
  border-radius: 3px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -o-border-radius: 3px;
  li{
    height:30px;
    line-height:30px;
    position:relative;
    padding: 0 15px;
    cursor: default; 
    i:first-of-type{
        margin-right:10px;
    }
    i.right{
        float:right;
    }
    &:hover{
        background:#f5f6fa;
    }
    .contextMenuPlugin{
         position:absolute;
         left:100%;
         top:0
    }
  }

}   
</style>