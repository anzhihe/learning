<template>
    <div class="associate-file">
        <Modal v-model="modalShow" title="关联档案" @on-ok="ok" @on-cancel="cancel">
            <div class="wrap">
                <div class="selected-box border-bottom" >
                    <div class="selected-box" ref="selectedBox" :style

                    ="{height: height}">
                        <!--选择的内容-->
                        <slot name="selectList"></slot>
                    </div>
                    <div @click="spread" class="bottom-state">
                        <span class="state">{{state}}</span>
                        <span class="control" v-if="isSpread">
                            <span>收起</span>
                            <i class="iconfont">&#xe664;</i>
                        </span>
                        <span class="control" v-else>
                            <span>展开</span>
                            <i class="iconfont">&#xe63b;</i>
                        </span>
                    </div>
                </div>
                <Input placeholder="请输入搜索内容" ><i class="iconfont" slot="append">&#xe64a;</i></Input>
                <ul>
                    <li v-for="item in fileAll" class="fileItem border-bottom">
                        <img src="../../../static/images/file.png"  class="float-left">
                        <p>Jackspace King</p>
                        <i class="iconfont">&#xe719;</i>
                        <Button type="ghost" class="associate-btn">取消关联</Button>
                    </li>
                </ul>
            </div>
            
            
        </Modal>

    </div>
</template>
<script>

    export default {
        data () {
            return {
                modalShow: false,
                isSpread: false,
                fileAll: [
                    {
                        id: 1,
                    },
                    {
                        id: 2
                    }
                ]

            };
        },
        props: {
            value: {
                type: Boolean,
                default: false
            },
            height: {
                type: String,
                default: 0
            },
            state: String, // 说明
            // associateFile: {
            //     type: Object,
            //     default: function () {
            //         return {}
            //     }
            // }
        },
        created () {
            
        },
        watch: {
            value (val) {
                
                this.modalShow = val;
            }
        },
        computed: {

        },
        methods: {
            spread() { //是否展开
                if (!this.isSpread) {
                    this.$refs.selectedBox.style.overflow = 'auto'
                    this.$refs.selectedBox.style.height = 'inherit';
                } else {
                    this.$refs.selectedBox.style.overflow = 'hidden'
                    this.$refs.selectedBox.style.height = this.height;
                }
                this.isSpread = !this.isSpread;
            },
            ok () {
                
                this.$emit('ok');
            },
            cancel () {
                
                this.$emit('cancel')
            }
        }
    }
</script>
<style scoped lang='scss'>
    .wrap {
        padding: 8px;
    }
    .selected-box {
        margin-bottom: 20px;
        overflow: hidden;
    }
    .iconfont {
        cursor: pointer;
    }
    .fileItem {
        height: 90px;
        padding: 14px 0;
        position: relative;
        img {
            margin-right: 10px; 
        }
        p {
            margin-bottom: 10px;
        }
        .associate-btn {
            right: 0;
            top: 50%;
            position: absolute;
            transform: translateY(-50%);
        }
        
    }
    .bottom-state {
        text-align: center;
        margin-bottom: 20px;
    }
    .control {
        // 颜色要改 加一个统一的类
        color: #5bbede;
        cursor: pointer;
    }
</style>

