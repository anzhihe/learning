<template>
    <div>
        <div class="w-max ct bgwh mb30 ovh border-eee">
        <div class="newopro-l fl">
          <a href=""><img src="../../static/images/new/xinpin.jpg" width="224" height="478"></a>
        </div>
        <div class="newopro-r fr">
            <h2 class="index-tt">
                <em class="ft18 c000">刚出炉新品</em>
                <router-link to="/app/home/list/more" target = _blank><a  class="fr c666">更多&gt;&gt;</a></router-link>
            </h2>
            <ul class="newgoods_fastbuy">
                <li class="prolist-cent clearfix have_num" v-for="item in newopro">
                    <div class="prolist-l fl">
                    <router-link :to="'/app/home/productDetail/'+item.id"  target = _blank> <a  :title="item.name" class="imgBox">
                    <img :src="item.goods_front_image" style="height: 158px;width: 158px;" class="zom" :alt="item.name">
                    </a></router-link>
                    </div>
                    <div class="prolist-r fl">
                        <h3 class="ft14 c333 bold">
                        <router-link :to="'/app/home/productDetail/'+item.id"  :title="item.name" target = _blank>{{item.name}}</router-link>
                        </h3>
                        <p><em class="c333"></em>{{item.goods_brief}}</p><div>
                        <span class="p-price"><em class="fastbuy_price">￥{{item.shop_price}}元</em><del>原价:￥{{item.market_price}}元</del></span>
                        <a href="" class="p-buy fr ibg">立即抢购</a>
                        <span class="p-time fr">销量：{{item.sold_num}}件</span>
                    </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>

</div>

</template>
<script>
  import { getGoods } from '../../api/api';
export default{
    data(){
        return {
            newopro:{}
        }
    },
    methods:{
        getOpro(){
          getGoods({
            "is_new":"true"
          })
            .then((response)=> {
               //跳转到首页页response.body面
                this.newopro = response.data.results
            })
            .catch(function (error) {
              console.log(error);
            });
        }
    },
    created(){
        this.getOpro();
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



.w-max{
    background:#fff;
    width:1200px;
}
.ct{margin:0 auto;}
.mb30{margin-bottom:30px;}
.ovh{overflow: hidden;}
.border-eee{border: 1px solid #eee;}
.newopro-l{ width: 224px;height: 478px;}
.newopro-l { width: 224px;height: 478px;}
.newopro-l img{ width: 224px;height: 478px;}
.fl {
    float:left
}
.fr {
    float:right
}
.index-tt{ line-height: 60px;}
.ft18{font-size: 18px;}
.c000{color: #000;}
.c333{ color: #333;}
.prolist-cent{ padding: 15px 0 30px; border-bottom: 1px solid #eee;}
.prolist-cent:last-child{border-bottom:none;}
.clearfix:after,.clear_f:after{
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0;
}
.clearfix{
    *zoom:1;
}
.prolist-l{ padding: 0 50px;}
.prolist-l .imgBox{ width: 158px; height: 158px;}

.prolist-r{ padding-left: 15px; width: 655px;}
.prolist-r h3{ line-height: 34px;}
.prolist-r p{ line-height: 20px; max-height: 40px; overflow: hidden; color: #999;}
.prolist-r div{line-height: 56px; padding-top: 12px;}
.ft14{font-size: 14px;}
.bold{font-weight:bold;}
.p-price{ color: #f40;}
.p-price i{font-size: 20px; }
.p-price em{font-size: 28px;margin-right: 10px;}
.p-time .ibg{ width: 17px; height: 17px; background-position: 0 -17px; margin-right: 5px;}
.ibg{
/* background: url(images/indexico.png) no-repeat;*/
  display: inline-block;}
.p-buy:hover{color: #fff;}
.p-buy{width: 188px; height: 56px; line-height: 56px; color: #fff; font-weight:bold; font-size: 18px; text-indent: 78px; background-position: 0 -36px; margin-left: 25px;}
.p-buy:hover{text-decoration: none;}

</style>
