<template>
    <div class="result-list">
        <ul>
            <li v-for="(item,index) in resultData" class="result-item" :class="{'hover':hoverIndex===index}" @mouseover="mouseover(index)" @contextmenu.prevent="contextmenuFn(item.objectId)">
                <div class="item-fix float-left clearfix">
                    <Checkbox class="checkbox float-left" :value="isSelectAllItem" @on-change="itemSelected(index)"></Checkbox>
                    <img src="../../../static/images/file.png">
                </div>
                <div class="item-intro">
                    <p><span class="item-title" @click="itemClick(index)">{{ item.name }}来源于什么什么什么</span><i class="iconfont">&#xe682;</i><span class="item-time float-right">{{item.updateTime}}</span></p>
                    
                    <i class="iconfont icon-tag">&#xe711;</i>
                    <span v-if="!item.tags.length">暂无</span>
                    <Tag v-if="item.tags.length" class="tag-btn" v-for="(tagItem,index) in item.tags" :key="index">{{tagItem.tagName}}</Tag>
                </div>
            </li>
        </ul>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                // isSelect: this.value,
                hoverIndex: '',
                selectCount: 0,
                isSelectAllItem: false,
                selectedArr: []
            };
        },
        props: {
            resultData: {
                type: Array,
                default: []
            },
            isSelectAll: {
                type: Boolean,
                default: false,
            }
        },
        created () {
            
        },
        watch: {
            isSelectAll (val) {
                this.isSelectAllItem = val;
            }


        },
        computed: {

        },
        methods: {
            mouseover (index) {

            },
            itemSelected (materialId) {
                
                // 已存在
                if (this.selectedArr.indexOf(materialId) !== -1) {
                    this.selectedArr.splice(this.selectedArr.indexOf(materialId), 1);
                } else {
                    this.selectedArr.push(materialId);
                }
                
                this.selectCount = this.selectedArr.length;
                this.$emit('on-select-item', this.selectCount);
            },
            itemClick (index) {
                this.$emit('on-item-click', index);

            },
            contextmenuFn(id){
                this.$emit('resultContextmenu', id);
            }
        }
    }
</script>
<style scoped lang='scss'>
    .result-list {
        .result-item {
            min-height: 80px;
            padding: 0 20px;
            border-bottom: 1px solid #ddd;
            .item-fix {
                width: 80px;
                height: 80px;
                img {
                    width: 52px;
                    height: 50px;
                    position: absolute;
                    top: 50%;
                    margin-top: -25px;
                    margin-left: 28px;
                }
                .checkbox {
                    width: 14px;
                    height: 16px;
                    position: absolute;
                    top: 50%;
                    margin-top: -8px;
                    
                }
            }

            .item-intro {
                min-height: 78px;
                margin-left: 90px;
                padding: 14px 0 4px 0;
                .item-title {
                    cursor: pointer;
                }
                p {
                    margin-bottom: 10px;
                    .iconfont {
                        margin-left: 10px;
                    }
                    .item-time {
                       margin-right: 215px;
                    }
                }
                .icon-tag {
                    margin-right: 6px;
                    font-size: 20px;
                }
                .tag-btn {
                    margin-right: 10px;
                    margin-bottom: 10px;
                }
            }

        }
        
    }

</style>










