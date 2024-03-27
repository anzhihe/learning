<template>
    <div class="productlist">
        <ul class="cle">
            <li v-for="item in listData" >
                <router-link :to="'/app/home/productDetail/'+item.id" target="_blank" class="productitem">
                    <span class="productimg">
                        <img width="150" height="150" :title="item.productname" :alt="item.productname" :src="item.goods_front_image" style="display: block;">
                    </span>
                    <span class="nalaprice xszk">
                        <b>
                        ￥{{item.shop_price}}元
                        </b>
                    </span>
                    <span class="productname">{{item.name}}</span>
                    <span class="description">{{item.goods_brief}}</span>
                    <!-- <span class="price">{{item.price}}</span> -->
                    <span class="salerow">销量：<span class="sales">{{item.sold_num}}</span>件 </span>
                </router-link>
                <!--<a class="addcart" target="_blank" rel="nofollow" @click="addShoppingCart">加入购物车</a>-->
            </li>
        </ul>
    <br clear="all">
</div>
</template>
<script>

    export default {
        data () {
            return {

            };
        },
        props: {
            listData: {
                type: Array,
                default: function() {
                    return [];
                }
            }

        },
        created () {
        },
        watch: {

        },
        computed: {

        },
        methods: {
            addShoppingCart () { //加入购物车

                this.$http.post('/product/addShoppingCart', {
                    params: {
                        productId: this.productId, // 商品id
                        num: this.proDetail.purNum, // 购买数量
                    }
                }).then((response)=> {
                    console.log(response.data);
                    alert('已成功加入购物车');
                }).catch(function (error) {
                    console.log(error);
                });
            },
            // toProductDetail(id) {
            //     this.$router.push({name:'productDetail', params: {productId: id}});
            // }
        }
    }
</script>
<style scoped>
html {

    color:#333;
    _background-attachment:fixed
}

body,h1,h2,h3,h4,h5,h6,hr,p,blockquote,dl,dt,dd,ul,ol,li,pre,form,fieldset,legend,button,input,select,textarea,th,td {
    margin:0;
    padding:0
}
body,button,input,select,textarea {
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
address,cite,dfn,em,var,i {
    font-style:normal
}
ul,ol {
    list-style:none
}
fieldset,img {
    border:0
}
h1 {
    font-size:18px
}
h2 {
    font-size:14px;
    font-weight:bold
}
h3 {
    font-size:14px;
    font-weight:400
}
h4,h5 {
    font-size:12px;
    font-weight:400
}
input,textarea,button,select {
    font-size:12px;
    outline:0;
    resize:none;
    color:#333
}
button {
    cursor:pointer
}
table {
    border-collapse:collapse;
    border-spacing:0
}
.clear {
    clear:both;
    height:0;
    font-size:0;
    line-height:0;
    overflow:hidden
}
.cle:after,.clearfix:after,.clear_f:after,.cle_float:after {
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle,.clearfix,.clear_f,.cle_float {
    *zoom:1
}
.fl {
    float:left
}
.fr {
    float:right
}
a {
    text-decoration:none;
    color:#333;
    -webkit-transition:color .2s;
    -moz-transition:color .2s;
    -o-transition:color .2s;
    -ms-transition:color .2s;
    transition:color .2s
}
a:hover {
    color:#09c762
}
a:focus,area:focus {
    outline:0
}
::selection {
    background:#09c762;
    color:#fff
}
canvas {
    -ms-touch-action:double-tap-zoom
}


a.productitem {
    display:block;
+zoom:1;
    cursor:pointer;
    background-color:#fff;
    border:1px solid #eee;
    padding-bottom:8px;
    position:relative;
    overflow:hidden
}
a.productitem span {
    padding:0 10px
}
a.productitem span.productimg {
    display:block;
    /*background:url(images/loading-16.gif) center center no-repeat;*/
    margin-bottom:10px;
    padding:0
}
a.productitem span.productimg img {
    vertical-align:top;
    display:block
}
a.productitem span.nalaprice {
    color:#09c762;
    font-size:14px;
    display:block
}
a.productitem span.productname {
    display:block;
    height:35px;
    line-height:16px;
    overflow:hidden;
    color:#666
}
a.productitem span.description {
    display:block;
    height:16px;
    overflow:hidden;
    color:#999
}
a.productitem span.salerow {
    display:block;
    color:#999
}
a.productitem span.sales {
    color:#09c762;
    padding:0 2px
}
a.productitem span.xszk {
    padding-left:55px;
    /*background:url(images/xsdz-ico.png?0226) 10px center no-repeat*/
}
a.productitem span.price {
    display:none
}
a.productitem:hover {
    text-decoration:none;
    border-color:#09c762
}

.productlist{width:970px;overflow:hidden}
.productlist ul{margin-right:-20px}
.productlist li{width:232px;height:342px;position:relative;float:left;margin:0 14px 14px 0;overflow:hidden;display:inline}
.productlist li a.productitem span.productimg img{width:230px;height:230px}

</style>
