<style scoped lang="scss">
.model-box{
    background:rgba(0,0,0,0.3);
    position: relative;
}
.add_ok {
    display: none;
    background: #fff;
    padding: 40px 0;
    text-align: center;
    width: 480px;
    border: 3px solid #09c762;
    border-radius: 10px;
    -moz-border-radius: 10px;
}
.add_ok .tip {
    font-size: 30px;
    margin-bottom: 20px;
}
.add_ok .tip i {
    font-size: 60px;
    color: #6dc415;
    vertical-align: -4px;
    margin-right: 15px;
}
.add_ok .go a.back {
    color: #09c762;
    margin-right: 90px;
}
.add_ok .go a {
    font-size: 18px;
}
.add_ok .go a.btn {
    padding: 10px 45px 12px;
}


</style>

<template>
    <div class="full-height full-width model-box" v-show="modelShow">
        <div id="easyDialogBox" style="margin: -117.5px 0px 0px -243px; padding: 0px; border: none; z-index: 10000; position: fixed; top: 50%; left: 50%; display: block;"><div class="add_ok" id="cart_show" style="display: block; margin: 0px;">
            <div class="tip">
                <i class="iconfont">&#xe60b;</i>商品已成功加入购物车
            </div>
            <div class="go">
                <a class="back" @click="close">&lt;&lt;继续购物</a>
                 <router-link class="btn" :to="'/app/shoppingcart/cart'">去结算</router-link>
            </div>
        </div>
    </div>
      
    </div>
</template>
<script>
    export default {
        data(){
            return {modelShow:false}
        },
        methods:{
            setShow(){
                this.modelShow = true
            },
            close(){
                this.modelShow = false;
            },
            ok(){
                this.modelShow = true;
            }
          
        }
    }
</script>