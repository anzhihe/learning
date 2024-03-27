<template>
    <div class="tag-panel white-bg box-shadow" v-show="visible">
        <div class="tag-title">
            <span>标签</span>
            <Checkbox v-model="noTagFile" @on-change="notagChange">无标签文件</Checkbox>
        </div>
        <div class="tag-content">
            <i class="iconfont">&#xe711;</i>
            <Tag class="tag" :class="{'main-color': tagSelectedArr[index]}" v-for="(item,index) in tagdata" :key="index" @click="selectTag(item,index)">{{item}}</Tag>
        </div>
    </div>
</template>
<script>

    export default {
        props: {
            
            value: {
                type: Boolean,
                default: false
            }

        },
        data () {
            return {
                visible: this.value,
                noTagFile: false,
                tagdata: [],
                tagSelected: [],
                tagSelectedArr: []
            };
        },
        watch: {
            value (val) {
                this.visible = val;
            }
        },
        created () {
            // 请求tag数据
            this.getTags();
            
        },
        computed: {

        },
        methods: {
            getTags () {
                this.$http({
                    url: '/system/tags',
                    method: 'get',
                }).then(res => {
                    this.tagdata = res.body;
                    this.tagSelectedArr = new Array(this.tagdata.length).fill(false);
                }).catch(res => {
                    
                });
            },
            selectTag (item, index) {
                this.tagSelectedArr.splice(index, 1, !this.tagSelectedArr[index]);
                this.tagSelected = [];
                for(var i = 0; i < this.tagSelectedArr.length; i++) {
                    if(this.tagSelectedArr[i]) {
                        this.tagSelected.push(this.tagdata[i]);
                    }
                }
                this.$emit('on-tag-select',this.tagSelected);
            },
            notagChange () {
                this.$emit('on-notagfile-select', this.noTagFile);
            }
        }
    }
</script>
<style scoped lang='scss'>
    .tag-panel {
        position: absolute;
        padding: 0 20px;
        z-index: 200;
        width: 100%;
        .tag-title {
            height: 40px;
            line-height: 50px;
            border-bottom: 1px solid #ddd;
            span {
                margin-right: 12px;
            }
        }
        .tag-content {
            padding: 20px 0;
            .tag {
                margin-right: 12px; 
            }
        }
    }
</style>
