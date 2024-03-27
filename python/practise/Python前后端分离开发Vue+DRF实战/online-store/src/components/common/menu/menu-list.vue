<template>
    <div class="menu">
        <div class="menulist-title menu-item">
            <h5>{{title}}</h5>
            <i class="iconfont iconfont-hidden">&#xe63b;</i>
            <Badge v-if="badgeCount" class="badge-count" :count="badgeCount" overflow-count="9999"></Badge>
        </div>
        <div>
            <ul v-for="(item, index) in data">

                <li class="menu-item menu-folder" :id="item.folderId" @click="openMenu(item, index,item.folderId)" @contextmenu.prevent="show(item)">
                    <span class="list-title">{{ item.folderName }}</span>
                    <i class="iconfont" :class="{'iconfont-hidden':!item.children.length}" v-if="item.children">&#xe63b;</i>
                    <Badge :count="item.targetCount" class="badge" overflow-count="9999"></Badge>
                </li>
                
               <li class="menu-item menu-item-children" v-if="item.children" v-for="(childItem,childIndex) in item.children" v-show="dataArr[index]" 
               :id="childItem.folderId" :class="{'menu-active':activeChildIndex === childIndex && activeIndex === index}" @click="menuActive(index, childIndex,childItem.folderId)" @contextmenu.prevent="subShow(childItem ,item.folderName)">
                    <span class="list-title">{{ childItem.folderName }}</span>
                    <i class="iconfont iconfont-hidden">&#xe63b;</i>
                    <Badge count="458" class="badge" overflow-count="999"></Badge>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>

    export default {
        data () {
            return {
                dataArr: [],
                activeChildIndex: '',
                activeIndex: '',
            };
        },
        props: {
            title: String,
            badgeCount:{
                type: Number,
                default: 0
            },
            data: {
                type: Array,
                default: function () {
                    return []
                }
            }
        },
        watch: {
            data(val) {
                this.data = val;
                this.dataArr = new Array(this.data.length).fill(false);
            }
         },
        created () {
            this.dataArr = new Array(this.data.length).fill(false);
         
        },
        computed: {

        },
        methods: {
            openMenu (item, index) {
                this.dataArr.splice(index, 1, !this.dataArr[index]);
            },
            menuActive (index, childIndex,id) {
                this.activeChildIndex = childIndex;
                this.activeIndex = index;
                this.$emit('on-menu-active', {index, childIndex,id});
            },
            show (id) {
                this.$emit('contextmenu', id);
            },
            subShow (id) {
                this.$emit('subContextmenu', id);
            },
            
         }
    }
</script>
<style scoped lang='scss'>
    h5 {
        font-size: 12px;
    }
    .menu-item {
        width: 100%;
        height: 50px;
        line-height: 50px;
        border-bottom: 1px solid #e1e6eb;
        padding: 0 20px;
        cursor: pointer;
        
        &:hover {
            color: #e9615f;
        }
        .badge {
            float: right;
            height: 50px;
            line-height: 50px;
            padding: 15px;
        }
        .iconfont {
            float: right;
            height: 50px;
            line-height: 50px;
            cursor: pointer;
        }
        .iconfont-hidden {
            visibility: hidden;
        }   
        
    }
    .menu-active {
        color: #e9615f;
        border-left: 2px solid #e44935;
    }
    .menu-item-children {
        background: #f5f6fa;
    }
    h5 {
        float: left;
    }
    .badge-count {
        float: right;
        height: 50px;
        line-height: 50px;
        padding: 15px;
    }
    
</style>
