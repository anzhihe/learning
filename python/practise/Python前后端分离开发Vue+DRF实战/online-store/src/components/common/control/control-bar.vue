<template>
    <div class="control-bar">
        <Checkbox @on-change="selectAll" v-model="isSelect"></Checkbox>
        <!-- 未选中的时候显示 -->
        <div v-if="!isSelect" class="slot sort-type">
            <span class="item-slot">
                <slot name="item-slot"></slot>
            </span>
            <span class="sort-item" v-for="(item,index) in sortArr">
                <label>{{item}}</label>
                <span class="sort"><i class="iconfont icon-arrow-up" :class="{'icon-clicked':iconIndex === index && iconType === 'up'}" @click="sort(index, 'up')">&#xe664;</i><i class="iconfont icon-arrow-down" :class="{'icon-clicked':iconIndex === index && iconType === 'down'}" @click="sort(index, 'down')">&#xe63b;</i></span>
            </span>
        </div>
        <div v-if="!isSelect" class="right">
            <Checkbox @on-change="">只显示分组</Checkbox>
            <span>共{{resultCount}}条搜索结果</span>
        </div>
        <!-- 选中的时候显示 -->
        <div v-if="isSelect" class="slot">
            <span>已选中{{selectCount}}条结果</span>
            <Button type="ghost" class="main-color cancle-btn" @click="cancel">取消</Button>
        </div>
        <div v-if="isSelect" class="bar-operate">
            <slot name="bar-operate"></slot>
        </div>

    </div>
</template>
<script>

    export default {
        data () {
            return {
                isSelect: this.value,
                iconType: '',
                iconIndex: ''
            };
        },
        props: {
            value: {
                type: Boolean,
                default: false
            },
            select: Boolean,
            selectCount: {
                type: Number,
                default: 0
            },
            resultCount: {
                type: Number,
                default: 0
            },
            sortArr: {
                type: Array,
                default: function () {
                    return []
                }
            },
        },
        created () {
            
        },
        watch: {
            value (val) {
                this.isSelect = val;
            }
        },
        computed: {

        },
        methods: {
            selectAll (isSelect) {
                this.isSelect = isSelect;
                this.$emit('on-select-all', isSelect);
            },
            sort (index, type) {
                this.iconType = type;
                this.iconIndex = index;
                this.$emit('on-sort', {index, type});
            },
            cancel () {
                this.isSelect = false;
                this.selectAll(false);
            }
        }
    }
</script>
<style scoped lang='scss'>

    .control-bar {
        height: 40px;
        display: flex;
        align-items: center;
        background: #f6f7fb;
        padding: 0 20px;
        border-bottom: 1px solid #ddd;

        .cancle-btn {
            margin-left: 5px;
        }
        .slot {
            flex: auto;
        }
        .sort-type {
            display: flex;
            align-items: center;
            .item-slot {
                //margin-right: 130px;
                width: 200px;
            }
            .sort-item {
                display: flex;
                align-items: center;
                //margin-right: 130px;
                width: 200px;
                .sort {
                    width: 14px;
                    height: 20px;
                    display: inline-block;
                    margin-left: 5px;
                    position: relative;
                    text-align: center;
                    
                    .iconfont {
                        position: absolute;
                        cursor: pointer;
                        height: 10px;
                        line-height: 14px;
                        width: 14px;
                        display: inline-block;
                        text-align: center;
                        color: #999;
                    }
                    .icon-arrow-up {
                        top: 0;
                        left: 0;
                    }
                    .icon-arrow-down {
                        bottom: 0;
                        left: 0;
                    }
                    .icon-clicked {
                        color: #666;
                    }
                    
                }
                
            }
            
        }
        .right, .bar-operate {
            flex: 0 0  200px;
            text-align: right;
        }
        .bar-operate {
            flex: 0 0  350px;
        }
        
    }
        
</style>
