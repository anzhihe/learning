<template>
<div>
<div class="series_list" v-for="items in list">
    <div class="series_box cle">
            <div class="series_info">
                <div class="series_name name_hufu">
                    <h2>{{items.name}}</h2>
                </div>
                <ul class="brand">

                    <li v-for="brand in items.brands">
                       <router-link :to="'/app/home/list/'+brand.id" >
                       <a :title="brand.name" target="_blank">
                            <img :src="brand.image" :alt="brand.name" style="display: inline;">
                        </a>
                        </router-link>
                    </li>
                </ul>
                <div class="brand_cata">
                   <router-link  v-for="label in items.sub_cat" :key="label.id" :title="label.name"   :to="'/app/home/list/'+label.id"  >
                    {{label.name}}
                    </router-link>
                </div>

            </div>
                <div class="series_pic">
                    <router-link :to="'/app/home/productDetail/'+items.ad_goods.id" target = _blank>
                       <img :src="items.ad_goods.goods_front_image" width="340" height="400">
                    </router-link>
                </div>

                <div class="pro_list">
                    <ul class="cle">
                        <li v-for="list in items.goods">
                             <router-link :to="'/app/home/productDetail/'+list.id" target = _blank>
                                <p class="pic">
                                 <img :src="list.goods_front_image" style="display: inline;">
                                 </p>
                                <h3>{{list.name}}</h3>
                                <p class="price">
                                    ￥{{list.shop_price}}元
                                </p>
                            </router-link>
                         </li>

                    </ul>
                </div>
        </div>
    </div>
</div>
</template>
<script>
    import { queryCategorygoods } from '../../api/api';
    export default {
        data(){
            return {
                list:[]
            }
        },
        methods:{
            getList(){
              queryCategorygoods()
                .then((response)=> {
                   //跳转到首页页response.body面
                  console.log(response)
                    this.list = response.data
                })
                .catch(function (error) {
                  console.log(error);
                });
            }
    },
    created(){
        this.getList();
    }
}

</script>
<style  lang='scss'>
html {
    /*background:#fafafa;*/
    color:#333;
    _background-attachment:fixed
}

body,h1,h2,h3,h4,h5,h6,p,ul,ol,li,button,input {
    margin:0;
    padding:0
}
body,button,input {
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
em,i {
    font-style:normal
}
ul{
    list-style:none
}
img {
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
input,button {
    font-size:12px;
    outline:0;
    resize:none;
    color:#333
}
button {
    cursor:pointer
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
/*@font-face {
    font-family:'lizi';
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot');
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot?#iefix') format('embedded-opentype'),url('http://at.alicdn.com/t/font_1412819191_5742776.woff') format('woff'),url('http://at.alicdn.com/t/font_1412819191_5742776.ttf') format('truetype'),url('http://at.alicdn.com/t/font_1412819191_5742776.svg#iconfont') format('svg')
}*/
.red,a.red,a.red:hover,.pink,a.pink,a.pink:hover {
    color:#09c762;
}
.gray999,.gray,a.gray,a.gray:hover {
    color:#999;
}



.series_list {
    width:1196px;
    margin:0 auto;
    overflow:hidden;
}
.series_list .series_pic {
    width:340px;
    float:left;
    overflow:hidden;
    margin-right:-10px
}
.series_list .series_pic img {
    width:340px;
    height:400px;
    vertical-align:top;
    -webkit-transition:all 4s;
    -moz-transition:all 4s;
    -ms-transition:all 4s;
    -o-transition:all 4s;
    transition:all 4s;
    -webkit-transform:scale(1)
}
.series_list .series_pic img:hover {
    -webkit-transform:scale(1.08)
}
.series_list .pro_list {
    width:654px;
    height:398px;
    overflow:hidden;
    float:right;
    border:1px solid #ccc
}
.series_list .pro_list ul {
    margin-right:-30px;
    zoom:1
}
.series_list .pro_list li {
    float:left;
    _display:inline;
    width:179px;
    height:179px;
    border-right:1px solid #ccc;
    border-bottom:1px solid #ccc;
    padding:10px 20px;
    overflow:hidden
}
.series_list .pro_list li .pic {
    text-align:center
}
.series_list .pro_list li .pic img {
    width:120px;
    height:120px;
    vertical-align:top
}
.series_list .pro_list li h3 {
    color:#666;
    height:18px;
    overflow:hidden;
    font-size:12px;
    margin:10px 0 5px
}
.series_list .pro_list li .price {
    color:#09c762;
    font-size:14px
}
.series_list .pro_list li a {
    display:block;
    text-decoration:none
}
.series_list .pro_list li a:hover img {
    opacity:.7;
    filter:Alpha(opacity=70)
}
.series_box {
    margin-bottom:30px;
    background-color:#fff
}
.series_info {
    width:200px;
    height:399px;
    border-bottom:1px solid #ccc;
    float:left;
    overflow:hidden
}
.series_info .brand {
    border-left:1px solid #ccc;
    padding:8px 0;
    border-right:1px solid #ccc
}
.series_info .brand li {
    padding:10px 0;
    height:50px;
    overflow:hidden;
    text-align:center
}
.series_info .brand li img {
    width:100px;
    height:50px;
    vertical-align:top
}
.series_info .brand li img:hover {
    -webkit-animation:imgShark 1s
}
.series_info .brand_cata {
    padding:12px 0 12px 12px;
    height:73px;
    overflow:hidden;
    background-color:#f5f5f5;
    border-left:1px solid #ccc;
    border-right:1px solid #ccc
}
.series_info .brand_cata a {
    display:inline-block;
    font-size:13px;
    height:24px;
    line-height:24px;
    color:#666;
    width:80px;
    margin-right:10px;
    overflow:hidden;
}
.series_info .series_name {
    padding:20px 0
}
.series_info .series_name h2 {
    font-size:24px;
    color:#fff;
    text-align:center;
    font-weight:normal
}
.series_info .name_hufu {
    background-color:#09c762
}
.series_info .name_caizhuang {
    background-color:#f3646a
}
.series_info .name_rihua {
    background-color:#f9b548
}
.series_info .name_gongju {
    background-color:#09c762
}
</style>
