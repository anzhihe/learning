<style scoped lang="scss">
.layout-header-box{
    height: 60px;
    line-height: 60px;
    background: #fff;
    border-bottom: 1px solid #ddd;
    width: 100%;
    padding: 0 20px;
}
.layout-header-left{
    h4{
        display:inline-block;
        margin-right: 5px;
        font-size: 14px;
    }
}
.operation-box{
    display:inline-block;
    float: right;
}
.layout-content-box{
    position:absolute;
    left:0;
    right:0;
    top:60px;
    
}
.page-false{
    bottom:0;
}
.page-true{
    bottom:60px;
}
.layout-page-box{
    height:60px;
    position:absolute;
    bottom:0;
    border-top: 1px solid #eee;
    text-align: center;
    padding: 15px;
    .page{
        display: inline-block;
    }
}
.content-reSet>div{
    height:100%;
    width:100%;
}
</style>

<template>
    <div class="full-height full-width">
        <slot name="header">
            <div class="layout-header-box">
                <div class="layout-header-left">   
                    <h4>{{title}}</h4><Badge v-if="badgeCount" class="layout-badge" :count="badgeCount" :overflow-count="badgeOverflowCount"></Badge>
                    <div class="operation-box">
                        <slot name="operation"></slot> 
                    </div>
                </div>
            </div>
        </slot>
        <div class="layout-content-box":class="{'page-false':!total,'page-true':total}" >
              <div class="full-height full-width content-reSet">
                    <slot name="content"></slot>  
              </div>  
    

        </div>
        <div v-if="total" class="layout-page-box full-width">
             <Page class="page" :current="current" :total="total" show-sizer placement="top" :page-size="15" :page-size-opts="pageSizeOpts" @on-change="pageChange" @on-page-size-change="pageSizeChange"></Page>
        </div>
    </div>
</template>
<script>
    export default {
        props:{
            title:String,
            badgeCount:{
                type:Number,
                default:0
            },
            badgeOverflowCount:{
                type:Number,
                default:9999
            },
            total:Number,
            current:{
                type:Number,
                default:1
            },
            pageSize:{
                type:Number,
                default:15
            },
            pageSizeOpts:{
                type:Array,
                default:function(){
                    return [15,25,50,100]
                }
            }
        },
        methods:{
            pageChange(data){
                this.$emit('on-page-change',data)
            },
            pageSizeChange(data){
                this.$emit('on-page-size-change',data)
            }
        }

    }
</script>