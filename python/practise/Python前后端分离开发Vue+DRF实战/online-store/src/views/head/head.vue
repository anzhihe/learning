<template>
  <div id="header" class="new_header">
    <div class="hd_bar">
        <div class="bd_bar_bd cle">
            <ul class="welcome">
                <li id="ECS_MEMBERZONE" v-if="userInfo.name">
                <router-link :to="'/app/home/member/userinfo'">{{userInfo.name}}</router-link>
                &nbsp;[
                <a @click="loginOut">退出</a>
                ]</li>
                <li id="ECS_MEMBERZONE" v-else>
                <router-link :to="'/app/login'">请登录</router-link>
                <s>|</s>
                 <router-link :to="'/app/register'">免费注册</router-link>
                </li>

            </ul>
            <ul id="userinfo-bar">
                <li class="more-menu" @mouseover="isShowVip=true" @mouseout="isShowVip=false"> <a>会员中心</a><i class="iconfont arrow"> </i>
                    <div class="more-bd" :class="{show:isShowVip}">
                        <div class="list">
                        <router-link :to="'/app/home/member/order'">我的订单</router-link>
                        <router-link :to="'/app/home/member/collection'">我的收藏</router-link>
                        <router-link :to="'/app/home/member/receive'">修改收货地址</router-link>
                        </div>
                    </div>
                </li>
                </ul>
        </div>
    </div>
    <div class="hd_main cle">
        <div class="logo">
        <router-link to="/app/home/index" class="lizi_logo">
            <img src="../../static/images/head/logo.gif" alt="慕学生鲜商城">
        </router-link>

        </div>
        <div class="search_box">
                <input class="sea_input" type="text" name="keywords" id="keyword" v-model="searchWord">
                <button  class="sea_submit" @click="searchSubmit">搜索</button>
        </div>
        <div class="head_search_hot">
         <span>热搜榜：</span>
          <router-link v-for="item in hotSearch" :to="'/app/home/search/'+item.keywords" :key="item.keywords">
            {{item.keywords}}
          </router-link>
        </div>
        <div class="intro">
            <ul>
                <li class="no1"><a href="javascript:void(0);" target="_blank">
                    <h4>正品保障</h4>
                    <p>100%正品低价</p>
                </a></li>
                <li class="no2"><a href="javascript:void(0);" target="_blank">
                    <h4>30天退换货</h4>
                    <p>购物有保障</p>
                </a></li>
                <li class="no3"><a href="javascript:void(0);" target="_blank">
                    <h4>满99就包邮</h4>
                    <p>闪电发货</p>
                </a></li>
            </ul>
        </div>
    </div>
    <div class="hd_nav">
        <div class="hd_nav_bd cle">
            <div class="main_nav main_nav_hover" id="main_nav">
                <div class="main_nav_link" @mouseover="overAllmenu" @mouseout="outAllmenu">
                    <a class="meunAll">全部商品分类
                        <i class="iconfont">&#xe643;</i>
                    </a>
                    <div class="main_cata" id="J_mainCata" v-show="showAllmenu">
                        <ul>
                            <li class="first" v-for="(item,index) in allMenuLabel" @mouseover="overChildrenmenu(index)" @mouseout="outChildrenmenu(index)">
                              <h3 style="background:url(../images/1449088788518670880.png) 20px center no-repeat;">
                                <router-link :to="'/app/home/list/'+item.id">{{item.name}}</router-link> </h3>
                                <div class="J_subCata" id="J_subCata" v-show="showChildrenMenu ===index"  style=" left: 215px; top: 0px;">
                                    <div class="J_subView" >
                                      <div v-for="list in item.sub_cat">
                                        <dl>
                                          <dt>
                                            <router-link :to="'/app/home/list/'+list.id">{{list.name}}</router-link>
                                          </dt>

                                          <dd>
                                            <router-link  v-for="childrenList in list.sub_cat" :key="childrenList.id" :to="'/app/home/list/'+childrenList.id">{{childrenList.name}}</router-link>
                                          </dd>
                                        </dl>
                                        <div class="clear"></div>
                                      </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <ul class="sub_nav cle" id="sub_nav">
                <li>
                    <router-link to="/app/home/index">首页</router-link>
                </li>
                <template v-for="(item,index) in allMenuLabel">
                  <li>
                    <div v-if="item.is_tab">
                      <router-link :to="'/app/home/list/'+item.id" >{{item.name}}</router-link>
                    </div>
                  </li>
                </template>

            </ul>
            <div class="hd_cart" id="ECS_CARTINFO"  @mouseover="overShopCar" @mouseout="outShopCar">
             <router-link class="tit" :to="'/app/shoppingcart/cart'" target = _blank>

                    <b class="iconfont">&#xe600;</b>去购物车结算<span><i class="iconfont">&#xe645;</i></span>
                    <em class="num" id="hd_cartnum" style="visibility: visible;">{{goods_list.goods_list.length}}</em></router-link>
                        <div class="list" v-show="showShopCar">
                            <div class="data">
                               <dl v-for="(item,index) in goods_list.goods_list">
                                <dt><router-link :to="'/app/home/productDetail/'+item.goods.id" target = _blank><img :src="item.goods.goods_front_image"></router-link></dt>
                                <dd>
                                  <h4><router-link :to="'/app/home/productDetail/'+item.goods.id" target = _blank>{{item.goods.name}}</router-link></h4>
                                  <p><span class="red">{{item.goods.shop_price}}</span>&nbsp;<i>X</i>&nbsp;{{item.nums}}</p>
                                  <a title="删除" class="iconfont del" @click="deleteGoods(index,item.goods.id)">×</a></dd>
                              </dl>
                            </div>
                            <div class="count">共<span class="red" id="hd_cart_count">{{goods_list.length}}</span>件商品哦~
                                  <p>总价:<span class="red"><em id="hd_cart_total">{{goods_list.totalPrice}}</em></span>
                                  <router-link class="btn" :to="'/app/shoppingcart/cart'" target = _blank>去结算
                                  </router-link>
                                  </p>
                            </div>
                        </div>
            </div>
        </div>
    </div>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import cookie from '../../static/js/cookie';
import { getHotSearch, getCategory ,deleteShopCart } from  '../../api/api'
export default {
    data(){
        return {
            hotSearch:[],//热词
            searchWord:'',//搜索词
            showAllmenu:false,//菜单显示控制
            allMenuLabel:[],//菜单
            showChildrenMenu:-1,//菜单显示控制
            showShopCar:false,//购物车显示控制
            isShowVip:false,
        }
    },
    computed: {
        ...mapGetters({
          goods_list: 'goods_list',
          userInfo:'userInfo'
        })
    },
    methods:{
        loginOut(){
          cookie.delCookie('token');
          cookie.delCookie('name');
          //跳转到登录
          this.$router.push({name: 'login'})
            // this.$http.get('/getMenu')
            //     .then((response)=> {

                    //跳转到登录
                    // this.$router.push({ name: 'login' })
            //     })
            //     .catch(function (error) {
            //       console.log(error);
            // });
        },
        overAllmenu(){
            this.showAllmenu = true;
        },
        outAllmenu(){
             this.showAllmenu = false;
        },
        searchSubmit(){
            if(this.searchWord){
                //跳转到登录
                this.$router.push({ name: 'search', params: { keyword: this.searchWord }});
            }
        },
        deleteGoods(index,id) { //移除购物车
            deleteShopCart(id).then((response)=> {
                console.log(response.data);
                this.goods_list.goods_list.splice(index,1);

                // 更新store数据
                this.$store.dispatch('setShopList');

            }).catch(function (error) {
                console.log(error);
            });
        },
        clickHotWord(word){
            this.searchWord = word;
            //跳转搜索结果页
        },
        overChildrenmenu(index){
            this.showChildrenMenu = index;
        },
        outChildrenmenu(){
            this.showChildrenMenu = -1;
        },
        overShopCar(){
            this.showShopCar = true;
        },
        outShopCar(){
            this.showShopCar = false;
        },
        getMenu(){//获取菜单
          getCategory({
            params:{}
          }).then((response)=> {
                    console.log(response)
                    this.allMenuLabel = response.data
                })
                .catch(function (error) {
                  console.log(error);
                });
        },
        getHotSearch(){//获取热搜
          getHotSearch()
                .then((response)=> {
                    this.hotSearch = response.data
                })
                .catch(function (error) {
                  console.log(error);
                });
        }
    },
    created(){
        this.getMenu()//获取菜单
        this.getHotSearch()//获取热词
        // 更新store数据
        this.$store.dispatch('setShopList');//获取购物车数据
    },

}
</script>
<style scoped  lang='scss'>
html {
    background:#fafafa;
    color:#333;
    _background-attachment:fixed
}
html.isPhone {
    min-width:1196px
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
fieldset,img {
    border:0
}

#header {
    background:#fff;
    zoom:1
}
#header .hd_main {
    width:1196px;
    margin:15px auto 0;
    position:relative;
    z-index:2001
}

/*需要---------整理*/
.new_header .search_result {
    margin:27px 0 0 -9px;
    width:380px
}
.new_header .hd_cart {
    top:0
}
.new_header .hd_cart .tit {
    border-color:#1e9246
}
.new_header .hd_cart .tit span {
    background-color:#1e9246
}

.hd_cart .tit b {
    color:#aaa;
    margin:0 8px 0 12px;
    font-size:16px;
    cursor:pointer
}
.hd_cart .tit span {
    position:absolute;
    right:0;
    top:-1px;
    display:block;
    width:34px;
    height:28px;
    padding-top:7px;
    background-color:#09c762;
    text-align:center;
    font-size:12px;
    color:#fff;
    cursor:pointer
}
.hd_cart .tit span i {
    display:inline-block;
    width:20px;
    height:20px;
    -webkit-transition:all .3s;
    -moz-transition:all .3s;
    -ms-transition:all .3s;
    transition:all .3s;
    -webkit-backface-visibility:hidden
}
.hd_cart .tit em {
    position:absolute;
    left:17px;
    top:-6px;
    text-align:center;
    font-size:12px;
    color:#fff;
    border:2px solid #fff;
    box-shadow:1px 1px 1px rgba(0,0,0,0.3);
    background-color:#09c762;
    border-radius:10px;
    padding:0 5px;
    line-height:16px;
    visibility:hidden
}
.hd_cart_hover .tit span i {
    -moz-transform:rotate(90deg);
    -webkit-transform:rotate(90deg);
    -ms-transform:rotate(90deg);
    transform:rotate(90deg)
}
#header.new_header .hd_main {
    margin-top:20px;
    height:90px;
    padding-bottom:5px
}
.new_header .hd_main .intro {
    margin:0;
    position:absolute;
    right:0;
    width:352px
}
.new_header .hd_main .intro li {
    width:125px
}
.new_header .hd_main .intro li.no2 {
    width:116px
}
.new_header .hd_main .intro li.no3 {
    width:110px
}
#header.new_header .search_box {
    right:394px;
    top:14px;
    width:460px;
    height:32px;
    border-color:#09c762
}
#header.new_header .search_box .sea_input {
    margin:7px 8px 0;
    width:360px
}
#header.new_header .search_box .sea_submit {
    background-color:#09c762;
    width:80px;
    height:32px
}

/*----------*/
.hd_bar {
    height:34px;
    border-bottom:1px solid #e5e5e5;
    background-color:#f5f5f5;
    position:relative;
    z-index:2002
}


/*hd_bar ul*/

.hd_bar ul {
    padding-top:4px;
    float:left
}
.hd_bar ul.welcome {
    margin-left:-10px
}
.hd_bar ul.welcome li .iconfont {
    color:#999;
    margin-right:4px
}

.hd_bar ul#userinfo-bar {
    float:right
}
.hd_bar ul#userinfo-bar li .vipico {
    width:12px;
    height:17px;
   /*background:url(../../static/images/head/wap.png) no-repeat;*/
    float:left;
    margin-right:4px;
    font-size:18px
}
.hd_bar li {
    float:left;
    position:relative;
    z-index:2000;
    height:17px;
    line-height:17px;
    padding:5px 10px
}
.hd_bar li s {
    color:#ccc;
    margin:0 8px;
    text-decoration:none
}
.hd_bar li a:hover {
    text-decoration:none
}
.hd_bar ul.welcome li .iconfont {
    color:#999;
    margin-right:4px
}
.bd_bar_bd {
    width:1196px;
    margin:0 auto
}
.hd_bar li a.vip-ico {
    background-position:0 3px;
    padding-left:18px
}
.hd_bar li a.svip-ico {
    background-position:0 -23px;
    padding-left:18px
}
.hd_bar li.more-menu {
    padding-right:20px
}
.hd_bar li.more-menu i.arrow {
    position:absolute;
    top:5px;
    right:5px;
    font-size:16px;
    line-height:16px;
    z-index:2002;
    -webkit-transition:all .5s;
    -moz-transition:all .5s;
    -ms-transition:all .5s;
    transition:all .5s;
    color:#bbb;
    -webkit-backface-visibility:hidden
}
.hd_bar li.more-menu .more-bd {
    position:absolute;
    top:37px;
    right:5px;
    z-index:2000;
    opacity:0;
    visibility:hidden;
    box-shadow:1px 1px 3px rgba(100,100,100,0.3);
    -webkit-transition:all .4s;
    -moz-transition:all .4s;
    -ms-transition:all .4s;
    transition:all .4s;
}
.show{
    opacity:1 !important;
    visibility:visible !important;
}
/*.hd_bar .more-bd .list {*/
    /*width:94px;*/
    /*border:1px solid #ddd;*/
    /*background:#fff*/
/*}*/
/*.hd_bar .more-bd .hezuo_list {*/
    /*width:72px*/
/*}*/
/*.hd_bar .more-bd .list a {*/
    /*display:block;*/
    /*background-color:#fff;*/
    /*border-bottom:1px dashed #d7d7d7;*/
    /*padding:6px 10px;*/
    /*height:17px;*/
    /*overflow:hidden*/
/*}*/
/*.hd_bar .more-bd .list a:hover {*/
    /*background:#f8f8f8;*/
    /*color:#333;*/
    /*text-decoration:none*/
/*}*/
/*.hd_bar .more-bd .list a.last {*/
    /*border-bottom:0*/
/*}*/
.hd_bar li.hover a.menu-link {
    color:#09c762
}
.hd_bar li.hover i.arrow {
    -moz-transform:rotate(180deg);
    -webkit-transform:rotate(180deg);
    -ms-transform:rotate(180deg);
    transform:rotate(180deg)
}
.hd_bar li.hover .more-bd {
    top:27px;
    opacity:1;
    visibility:visible
}

/*cle*/
.cle:after {
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle{
    *zoom:1
}


/*hd-main*/
.logo {
    position:absolute;
    left:10px;
    top:5px;
    z-index:2
}

.search_box {
    position:absolute;
    right:0;
    top:0;
    width:300px;
    height:29px;
    border:2px solid #1e9246;
    border-right:0;
    background-color:#fff;
    overflow:hidden;
    box-shadow:2px 1px 1px rgba(200,200,200,0.5) inset
}
.sea_input {
    float:left;
    width:228px;
    margin:5px;
    height:20px;
    line-height:20px;
    color:#bbb;
    outline:0;
    border:0;
    background:0
}
.sea_submit {
    font-size:15px;
    color:#fff;
    float:right;
    height:29px;
    width:62px;
    padding-left:6px;
    border:0;
    background-color:#1e9246;
    cursor:pointer;
    letter-spacing:5px;
    overflow:hidden
}
.sea_submit:hover {
    color:#ffd736
}


/*热搜榜*/
.head_search_hot {
    position:absolute;
    top:58px;
    right:404px;
    width:450px;
    height:16px;
    overflow:hidden
}
.head_search_hot span {
    color:#999
}
.head_search_hot a {
    margin:0 8px 0 5px;
    color:#666
}
.head_search_hot a.red,.head_search_hot a:hover {
    color:#09c762
}
/*hd-main   .intro*/
.intro {
    height:58px;
    margin:0 190px 0 240px;
    padding-top:20px
}

.hd_main .intro ul {
    float:right;
    height:56px
}
.hd_main .intro li {
    float:left;
    width:150px;
    height:46px;
    background:url(../../static/images/head/webintro-ico.png) 0 -9999px no-repeat;
    overflow:hidden
}
.hd_main .intro li a {
    display:block;
    padding:0 0 0 42px;
    text-decoration:none
}
.hd_main .intro li h4 {
    font-weight:bold;
    font-size:12px
}
.hd_main .intro li p {
    color:#999
}
.hd_main .intro li.no1 {
    background-position:0 1px
}
.hd_main .intro li.no2 {
    background-position:0 -50px
}
.hd_main .intro li.no3 {
    background-position:0 -100px
}

.hd_nav {
    background-color:#09c762;
    height:35px
}

.hd_nav_bd {
    padding-left:214px;
    position:relative;
    z-index:1990;
    width:982px;
    margin:0 auto
}

.main_nav {
    position:absolute;
    top:0;
    left:0;
    z-index:1991
}
.hd_nav .main_nav .main_nav_link {
    width:214px;
    height:35px;
    color:#fff;
    background-color:#000;
    overflow:hidden
}
.hd_nav .main_nav .main_nav_link a.meunAll {
    display:block;
    padding:7px 10px 0 0;
    height:25px;
    font-size:14px;
    text-align:center;
    font-weight:bold;
    color:#fff;
    overflow:hidden
}
.hd_nav .main_nav .main_nav_link a:hover {
    color:#fff;
    text-decoration:none
}
.hd_nav .main_nav .main_nav_link i {
    position:absolute;
    top:10px;
    right:50px;
    -webkit-transition:all .5s;
    -moz-transition:all .5s;
    -ms-transition:all .5s;
    transition:all .5s;
    font-size:12px;
    line-height:16px;
    -webkit-backface-visibility:hidden
}
.hd_nav .main_nav_hover .main_nav_link i {
    -moz-transform:rotate(180deg);
    -webkit-transform:rotate(180deg);
    -ms-transform:rotate(180deg);
    transform:rotate(180deg);
}

.main_cata {
    width:214px;
    height:auto;
    opacity:1;
    position:absolute;
    left:0;
    top:35px;
    z-index:1999;
    padding-bottom:10px;
}
.main_cata ul {
    width:214px;
    padding:10px 0;
    overflow:hidden;
    background-color:#3b3b3b;
    border-bottom:1px solid #ccc;
    box-shadow:-2px 4px 4px rgba(200,200,200,0.3)
}
.main_cata li {
    width:100%;
    height:35px;
    line-height:35px;
    border:none;
    overflow:hidden;
    font-size:0;
}
.main_cata li a {
    font-size:12px
}
.main_cata li h3 {
    text-indent:58px;
}
.main_cata li h3 a {
    font-size:13px;
    font-family:Arial;
    color:#fff;
}
.main_cata li .bd {
    padding:0 0 6px 14px;
    margin-right:-10px;
    height:43px;
    overflow:hidden
}
.main_cata li .bd a {
    color:#999;
    display:inline-block;
    margin-right:14px;
    line-height:22px
}
.main_cata li.last {
    padding:0;
    box-shadow:0 4px 3px rgba(200,200,200,0.3)
}
.main_cata li.last a {
    display:inline-block;
    width:48%;
    height:54px;
    text-align:center;
    line-height:54px;
    overflow:hidden;
    font-weight:bold;
    font-size:14px
}
.main_cata li.last a.no2 {
    border-left:1px solid #ccc
}
.main_cata li.current {
    background-color:#eee;
    border-right-color:#eee;
    box-shadow:0 0 10px #eee
}
.main_cata li.current h3 a,.main_cata li.current a:hover {
    color:#09c762
}




.J_subCata {
    position:absolute;
    top:35px;
    left:100px;
    z-index:1998;
    -webkit-transition:all .2s ease;
    -moz-transition:all .2s ease;
    -ms-transition:all .2s ease;
    -o-transition:all .2s ease;
    transition:all .2s ease
}
.J_subCata .J_subView {
    border:1px solid #ccc;
    width:600px;
    min-height:228px;
    padding-top:5px;
    overflow:hidden;
    background-color:#eee;
    position:relative;
    box-shadow:3px 3px 4px rgba(0,0,0,0.3);
    padding:10px;
}
.J_subCata .J_subView dl {
    padding:0 12px 12px;
}
.J_subCata .J_subView dt {
    float:left;
    color: #000000;
    font-size: 15px;
    font-weight: bold;
    line-height: 30px;
    text-align:right;
    margin-bottom: 8px;
    margin-right: 5px;
    min-width: 80px;
    text-indent: 0;
    zoom:1;
}

.J_subCata .J_subView dd {
    float: left;
    line-height: 30px;
    margin-left: 10px;
    width: 460px;
}
.J_subCata .J_subView dd a {
    display:inline-block;
    color:#09c762;
    padding:0 8px;
    font-size: 13px;
}
.J_subCata .J_subView dd.kuan_cata a {
    margin-right:30px
}
.J_subCata .J_subView dd.brand_cata {
    font-size:0
}
.J_subCata .J_subView dd.brand_cata a {
    display:inline-block;
    width:84px;
    height:32px;
    border:1px solid #ccc;
    text-align:center;
    margin:0 13px 8px 0;
    overflow:hidden;
    background-color:#fff
}
.J_subCata .J_subView dd.brand_cata a img {
    width:64px;
    height:32px;
    vertical-align:top
}
.J_subCata .J_subView dd a:hover {
    color:#09c762;
    border-color:#09c762
}



.clear {
    clear:both;
    height:0;
    font-size:0;
    line-height:0;
    overflow:hidden
}

.hd_nav .sub_nav {
    float:left
}
.hd_nav .sub_nav li {
    float:left;
    height:35px;
    overflow:hidden;
    font-size:14px;
}
.hd_nav .sub_nav li a {
    display:inline-block;
    height:21px;
    overflow:hidden;
    padding:7px 28px;
    color:#fff;
}
.hd_nav .sub_nav li.current a,.hd_nav .sub_nav li a:hover {
    color:#fff;
    background-color:#1e9246;
    text-decoration:none
}

.hd_cart {
    top:0
}
.hd_cart {
    position:absolute;
    right:0;
    top:30px;
    z-index:200
}
.hd_cart a:hover {
    text-decoration:none
}
.new_header .hd_cart .tit {
    border-color:#1e9246
}
.new_header .hd_cart .tit span {
    background-color:#1e9246
}



.hd_cart .tit {
    display:block;
    width:168px;
    height:28px;
    padding-top:5px;
    position:relative;
    z-index:10;
    background:#f8f8f8;
    border:1px solid #ccc;
    border-right:0;
    font-size:14px;
    color:#666
}
.hd_cart .tit b {
    color:#aaa;
    margin:0 8px 0 12px;
    font-size:16px;
    cursor:pointer
}
.hd_cart .tit span {
    position:absolute;
    right:0;
    top:-1px;
    display:block;
    width:34px;
    height:28px;
    padding-top:7px;
    background-color:#09c762;
    text-align:center;
    font-size:12px;
    color:#fff;
    cursor:pointer
}
.hd_cart .tit span i {
    display:inline-block;
    width:20px;
    height:20px;
    -webkit-transition:all .3s;
    -moz-transition:all .3s;
    -ms-transition:all .3s;
    transition:all .3s;
    -webkit-backface-visibility:hidden
}
.hd_cart .tit em {
    position:absolute;
    left:17px;
    top:-6px;
    text-align:center;
    font-size:12px;
    color:#fff;
    border:2px solid #fff;
    box-shadow:1px 1px 1px rgba(0,0,0,0.3);
    background-color:#09c762;
    border-radius:10px;
    padding:0 5px;
    line-height:16px;
    visibility:hidden
}
.hd_cart_hover .tit span i {
    -moz-transform:rotate(90deg);
    -webkit-transform:rotate(90deg);
    -ms-transform:rotate(90deg);
    transform:rotate(90deg)
}

.hd_bar li.more-menu .more-bd {
    position:absolute;
    top:37px;
    right:5px;
    z-index:2000;
    opacity:0;
    visibility:hidden;
    box-shadow:1px 1px 3px rgba(100,100,100,0.3);
    -webkit-transition:all .4s;
    -moz-transition:all .4s;
    -ms-transition:all .4s;
    transition:all .4s
}
.hd_bar .more-bd .list {
    width:94px;
    border:1px solid #ddd;
    background:#fff
}
.hd_bar .more-bd .hezuo_list {
    width:72px
}
.hd_bar .more-bd .list a {
    display:block;
    background-color:#fff;
    border-bottom:1px dashed #d7d7d7;
    padding:6px 10px;
    height:17px;
    overflow:hidden
}
.hd_bar .more-bd .list a:hover {
    background:#f8f8f8;
    color:#333;
    text-decoration:none
}

.hd_bar li.hover .more-bd {
    top:27px;
    opacity:1;
    visibility:visible
}

.hd_cart .list {
    width:220px;
    position:absolute;
    right:0;
    top:35px;
    border:1px solid #09c762;
    background-color:#fff;
    -webkit-transition:all .3s;
    -moz-transition:all .3s;
    -ms-transition:all .3s;
    transition:all .3s
}
.hd_cart_hover .list {
    visibility:visible;
    opacity:1;
    top:34px
}
.hd_cart .list .load {
    height:100px
}
.hd_cart .list .fail {
    padding:10px 20px 20px;
    text-align:center;
    color:#999
}
.hd_cart .list .fail i {
    font-size:30px;
    color:#ddd
}
.hd_cart .list .data {
    position:relative;
    zoom:1;
    width:220px;
    overflow:hidden
}
.hd_cart .list .data_over {
    max-height:318px;
    _height:318px;
    overflow-y:auto
}
.hd_cart .list dl {
    padding:5px 8px;
    width:204px;
    height:42px;
    overflow:hidden;
    background:#fff;
    border-bottom:1px dashed #ddd
}
.hd_cart .list dt {
    float:left;
    width:42px
}
.hd_cart .list dt img {
    width:40px;
    height:40px;
    vertical-align:top;
    border:1px solid #ccc
}
.hd_cart .list dd {
    float:right;
    width:152px;
    color:#666;
    padding-top:2px;
    position:relative
}
.hd_cart .list .data_over dl {
    width:189px
}
.hd_cart .list .data_over dd {
    width:137px
}
.hd_cart .list dd a {
    color:#666
}
.hd_cart .list dd h4 {
    height:20px;
    overflow:hidden
}
.hd_cart .list dd i {
    display:inline-block;
    font-size:10px;
    -webkit-transform:scale(0.7)
}
.hd_cart .list dd .del {
    position:absolute;
    top:20px;
    right:0;
    color:#bbb
}
.hd_cart .list .count {
    background-color:#f5f5f5;
    color:#666;
    padding:10px 8px 14px;
    position:relative
}
.hd_cart .list .count span {
    margin:0 3px
}
.hd_cart .list .count em {
    font-size:14px;
    margin-left:2px
}
.hd_cart .list .count p {
    margin-top:12px
}
.hd_cart .list .count a {
    position:absolute;
    top:35px;
    right:10px;
    border-radius:0;
    border:0;
    padding:5px 15px 7px;
    font-size:14px;
    background: #09c762;
    color:#fff;
    &:hover{
      background: #1e9246;
    }
}



.fail {
    padding:10px 20px 20px;
    text-align:center;
    color:#999
}
.fail i {
    font-size:30px;
    color:#ddd
}

.here{padding:5px 0;color:#bbb}
.here i.iconfont{font-size:14px}
.here h1{display:inline;font-size:12px;color:#333;font-weight:normal}
.sidebar{width:214px;float:left}
.maincon{width:970px;float:right}
.cate-step{border:1px solid #eee;height:53px;overflow:hidden;padding-left:52px;margin-bottom:12px}
.cate-step a{display:block;height:21px;overflow:hidden;padding-top:34px;float:left;text-align:center}
.cate-step a:hover{text-decoration:none}
.hufu-step{background-position:0 0;background-color:#fdfdfd}
.hufu-step a.no1{width:106px}
.hufu-step a.no1:hover,#current-hstep1 a.no1{background-position:-52px -54px;color:#09c762}
.hufu-step a.no2{width:122px}
.hufu-step a.no2:hover,#current-hstep2 a.no2{background-position:-158px -54px;color:#09c762}
.hufu-step a.no3{width:109px}
.hufu-step a.no3:hover,#current-hstep3 a.no3{background-position:-280px -54px;color:#09c762}
.hufu-step a.no4{width:112px}
.hufu-step a.no4:hover,#current-hstep4 a.no4{background-position:-389px -54px;color:#09c762}
.hufu-step a.no5{width:117px}
.hufu-step a.no5:hover,#current-hstep5 a.no5{background-position:-501px -54px;color:#09c762}
.hufu-step a.no6{width:120px}
.hufu-step a.no6:hover,#current-hstep6 a.no6{background-position:-618px -54px;color:#09c762}
.hufu-step a.no7{width:104px}
.hufu-step a.no7:hover,#current-hstep7 a.no7{background-position:-738px -54px;color:#09c762}
.hufu-step a.no8{width:124px;padding-top:55px}
.hufu-step a.no8:hover,#current-hstep8 a.no8{background-position:-842px -54px;color:#09c762}
.caiz-step{background-position:0 -108px;background-color:#fdfdfd}
.caiz-step a.no1{width:88px}
.caiz-step a.no1:hover,#current-cstep1 a.no1{background-position:-52px -162px;color:#09c762}
.caiz-step a.no2{width:92px}
.caiz-step a.no2:hover,#current-cstep2 a.no2{background-position:-140px -162px;color:#09c762}
.caiz-step a.no3{width:84px}
.caiz-step a.no3:hover,#current-cstep3 a.no3{background-position:-232px -162px;color:#09c762}
.caiz-step a.no4{width:92px}
.caiz-step a.no4:hover,#current-cstep4 a.no4{background-position:-316px -162px;color:#09c762}
.caiz-step a.no5{width:86px}
.caiz-step a.no5:hover,#current-cstep5 a.no5{background-position:-408px -162px;color:#09c762}
.caiz-step a.no6{width:85px}
.caiz-step a.no6:hover,#current-cstep6 a.no6{background-position:-494px -162px;color:#09c762}
.caiz-step a.no7{width:95px}
.caiz-step a.no7:hover,#current-cstep7 a.no7{background-position:-579px -162px;color:#09c762}
.caiz-step a.no8{width:82px}
.caiz-step a.no8:hover,#current-cstep8 a.no8{background-position:-674px -162px;color:#09c762}
.caiz-step a.no9{width:90px}
.caiz-step a.no9:hover,#current-cstep9 a.no9{background-position:-756px -162px;color:#09c762}
.caiz-step a.no10{width:120px;padding-top:55px}
.caiz-step a.no10:hover,#current-cstep10 a.no10{background-position:-846px -162px;color:#09c762}
.cate-menu{margin-bottom:12px;background-color:#fff}
.cate-menu h3{border:1px solid #ddd}
.cate-menu h3 a{display:block;height:26px;padding:14px 0 12px 12px;background-color:#fff;position:relative}
.cate-menu h3 a:hover{background-color:#fafafa;text-decoration:none}
.cate-menu h3 strong{font-size:18px;color:#333;letter-spacing:3px;font-weight:400}
.cate-menu h3 i{position:absolute;right:10px;top:23px;color:#999;font-size:12px}
.cate-menu dl{border:1px solid #eee;padding:10px 0}
.cate-menu dt{font-size:14px;padding:5px 0 5px 12px;color:#888}
.cate-menu dd a{display:block;padding:7px 0 7px 27px;background-color:#fff}
.cate-menu dd a:hover{background-color:#fafafa;text-decoration:none}
.cate-menu dd a i{color:#bbb;margin-left:5px}
.cate-menu dd.current a,.cate-menu dd.current a:hover{color:#09c762;background-color:#f1f1f1}
.fixed-want{border:1px solid #eee;border-bottom:0;width:212px;background-color:#fff;top:0}
.fixed-want .hd{border-bottom:1px solid #ddd;font-size:14px;padding:8px 12px}
.fixed-want .bd{border-top:1px solid #eee}
.fixed-want dl{border-bottom:1px solid #eee;padding:10px 0}
.fixed-want .cate dt{border-right:1px dotted #eee;float:left;width:50px;padding:0 8px}
.fixed-want .cate dt a{display:block;height:68px;overflow:hidden;text-align:center}
.fixed-want .cate dt img{width:48px;height:48px;border:1px solid #eee}
.fixed-want .cate dd{margin-left:70px;height:68px;overflow:hidden}
.fixed-want dd a{display:inline-block;padding:1px 4px}
.fixed-want dd a.red{color:#09c762;background-color:#ffecf2;border-radius:3px}
.fixed-want .brand{padding:10px}
.fixed-want .brand dt{padding:0 10px 4px;border-bottom:1px dotted #eee}
.fixed-want .brand dd{padding-top:5px}
.fixed-want .brand p.more{text-align:right;margin-bottom:-5px}
.fixed-want .brand p.more a{color:#999}
a.more-btn,.rmb,.search-selected a.item,.sort .bd a span{
    /*background:url(images/search-page-bg.png) 0 -9999px no-repeat*/
}
.search-selected{background-color:#fff;border:1px solid #eee;border-bottom:1px solid #ccc;padding:9px 10px}
.search-selected span{display:inline-block;padding:4px 0 4px 0}
.search-selected a{display:inline-block;padding:4px 24px 4px 8px;color:#999}
.search-selected a.item{border:1px solid #ddd;background-color:#fff;margin-right:8px;background-position:right -245px;box-shadow:0 1px 1px #eee;color:#09c762}

.search-selected a.item:hover{background-color:#f2f2f2;background-position:right -217px;text-decoration:none}
.search-options{margin-bottom:12px;background-color:#fff;}
.search-options .bd{border:1px solid #eee;border-bottom:0;zoom:1;}
.search-options dl{padding:10px 0;border-bottom:1px solid #eee;width:100%;position:relative}
.search-options dt{position:absolute;top:10px;left:10px;font-size:14px}
.search-options dd{position:relative;padding:0 50px 0 63px;height:24px;overflow:hidden;-webkit-transition:height .3s;-moz-transition:height .3s;-o-transition:height .3s;transition:height .3s}
.search-options dd .items{padding-top:2px}
.search-options dd .w500{width:500px}
.search-options dd .items a{color:#666}
.search-options dd .items a:hover{color:#09c762}
.search-options dd .link{float:left;width:162px;height:18px;margin:0 10px 8px 0;overflow:hidden}
.search-options dd.dd-price .link{width:102px}
.search-options dd a.more-btn{position:absolute;top:3px;right:5px;margin-right:0;padding:0 20px 0 0;background-position:30px -381px;display:none;color:#09c762}
.search-options dd a.more-btn.clicked{background-position:30px -359px}
.search-options dd a.more-btn:hover{background-color:#fff;text-decoration:underline}
.search-options dd.dd-price{overflow:visible;z-index:10}
.priceform{position:absolute;top:-11px;left:500px;z-index:10}
.priceform .form-bg{width:270px;border:1px solid #fff;border-top-color:#eee;padding:8px 15px;padding-bottom:7px;font-size:0}
.priceform input{font-size:12px;border:1px solid #eaeaea;padding:3px;height:18px;width:60px;line-height:18px}
.priceform input.submit{height:26px;padding:0;line-height:16px;cursor:pointer;background-color:#eaeaea;width:68px;border-color:#e1e1e1;background-color:#eaeaea;background-image:-moz-linear-gradient(#fefefe,#eaeaea);background-image:-webkit-linear-gradient(#fefefe,#eaeaea);background-image:linear-gradient(#fefefe,#eaeaea)}
.priceform input.submit:hover{background-color:#e4e4e4}
.priceform span{height:26px;width:12px;display:inline-block;vertical-align:-9px;vertical-align:-1px;font-size:12px}
.priceform span.rmb{background-position:-10px -272px}
.priceform span.rmb2{padding-left:20px;background-position:8px -272px}
.priceform form p{display:none;text-align:right;padding-top:4px}
#priceform.focus .form-bg{background-color:#f6f6f6;border-color:#e4e4e4;height:28px;box-shadow:0 1px 3px rgba(100,100,100,0.1)}
#priceform.focus form p{display:inline;padding-left:15px}
.sort{margin-bottom:10px;height:30px;border:1px solid #eee;border-bottom:2px solid #ccc;padding:5px 0;background:#fff}
.sort .bd{float:left;font-size:0;padding-right:12px}
.sort .bd a{display:inline-block;font-size:12px;margin-right:-1px;margin-right:-2px;position:relative;z-index:1}
.sort .bd a span{display:block;padding:5px 26px 5px 15px;background-position:right -128px;background-position:right -127px}
.sort .curr .search_DESC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -104px;background-position:right -102px;color:#09c762;text-shadow:1px 1px 1px #fff}
.sort .curr .search_ASC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -330px;background-position:right -328px;color:#09c762;text-shadow:1px 1px 1px #fff}
.sort .bd a:hover{z-index:2;text-decoration:none}
.sort .bd a.default span{background-image:none;padding-right:15px}
.sort .bd a.promotion span{padding-right:15px;padding-left:30px;background-position:10px -153px}
.sort .bd a.clicked span{background-position:10px -184px}
.search_num{width:400px;float:right;text-align:right;line-height:30px;padding:0 15px}
.search_num b{color:#09c762}
.search_num span.search_btn{margin-left:10px;font-size:13px}
.search_num span.search_btn a{display:inline-block;width:26px;height:26px;line-height:28px;text-align:center;border:1px solid #e4e4e4;background-color:#fff;margin:0 5px;color:#999}
.search_num span.search_btn a:hover{border-color:#ccc;box-shadow:0 1px 1px #eee;text-decoration:none;color:#09c762}
.search_num span.search_btn span{color:#333}
.search_num span.search_btn span em{color:#09c762}
.productlist{width:970px;overflow:hidden}
.productlist ul{margin-right:-20px}
.productlist li{width:232px;height:342px;position:relative;float:left;margin:0 14px 14px 0;overflow:hidden;display:inline}
.productlist li a.productitem span.productimg img{width:230px;height:230px}
.cms-box{float:left;width:702px;padding-bottom:15px;display:none}
.cms-box h3{font-size:16px;margin-bottom:5px;padding-left:12px}
.cms-box h3 a{float:right;color:#999;font-size:12px;margin-top:5px}
.cms-box .bd{border:1px solid #eee;border-top-color:#000;padding:10px;background-color:#fff}
.cms-box .bd a:hover{text-decoration:none}
.cms-box .bd span.name{color:#666}
.cms-box .bd span.intro{color:#999}
.cms-box .bd span.price em{font-size:18px}
.cms-box .bd a:hover span.name{color:#09c762}
.baokuan-goods a,.baokuan-goods a span{display:block}
.baokuan-goods a span.price{color:#09c762}
.baokuan-goods a.no1{float:left;width:170px;padding:10px 5px 10px 15px;border-right:1px solid #eee;position:relative}
.baokuan-goods a.no1 img{width:150px;height:150px}

.baokuan-goods a.no2{float:right;width:450px;height:100px;overflow:hidden;padding:10px 15px}
.baokuan-goods a.no2 img{width:100px;height:100px;float:left}
.baokuan-goods a.no2 span{margin-left:110px}
.baokuan-goods a.no2 span.price{padding-top:30px}
.baokuan-goods a.border-btm{border-bottom:1px solid #eee}
.baokuan-goods a.no1 .guan-ico{position:absolute;left:10px;top:0;display:block;width:24px;height:20px}
.baokuan-goods a.no1:hover .guan-ico{background-position:0 0}
.new-goods{width:254px;float:right}
.new-goods .bd{position:relative;background-color:#fff}
.new-goods .list{position:relative;height:241px;width:170px;margin:0 auto;overflow:hidden}
.new-goods li{float:left;width:150px;padding:0 10px;height:241px;overflow:hidden}
.new-goods li a,.new-goods li span{display:block}
.new-goods li span.pic{margin-bottom:5px}
.new-goods li span.pic img{width:150px;height:150px}
.new-goods li span.name{font-size:14px;height:20px;overflow:hidden;margin-bottom:5px}
.new-goods .trg a{font-size:16px;color:#ddd;position:absolute;top:80px}
.new-goods .trg a:hover{text-decoration:none;color:#999}
.new-goods .trg a.prev{left:20px}
.new-goods .trg a.next{right:20px}
.week-hot{border:1px solid #eee;margin-bottom:12px;background-color:#fff;display:none}
.week-hot .hd{border-bottom:1px solid #eee;padding:0 12px;height:45px;overflow:hidden}
.week-hot .hd h3{font-size:16px;height:45px;line-height:45px}
.week-hot .bd{padding-bottom:10px}
.week-hot .item{float:left;width:180px;padding:0 30px;border-left:1px solid #f4f4f4;overflow:hidden;margin:10px 0}
.week-hot .nobrder{border-left:none}
.week-hot .item a{display:block;width:100%;position:relative}
.week-hot .item a:hover{text-decoration:none}
.week-hot .item img{display:block;width:180px;height:180px}
.week-hot span{display:block;margin-bottom:5px}
.week-hot .intro{font-size:14px}
.week-hot .name{color:#999;line-height:16px;height:16px;overflow:hidden}
.week-hot .price{color:#09c762}
.week-hot .price em{font-size:18px;font-family:arial;}
.week-hot .item .hot-ico{
   /* background:url(../../static/images/head/hot-ico-bg.png) -48px 0 no-repeat;*/
    display:block;width:40px;height:40px;overflow:hidden;position:absolute;top:0;left:0}
.week-hot .item .ico-mid{top:100px}
.week-hot .item a:hover .hot-ico{background-position:0 0}
.seemore_items{border:1px solid #ddd;float:right;width:212px;padding:10px 0;position:relative}
.seemore_items h3{position:relative;font-size:14px;color:#999;width:182px;margin:0 auto}
.seemore_items h3 a{position:absolute;right:0;top:-3px;font-size:24px;line-height:24px;color:#999}
.seemore_items h3 a:hover{text-decoration:none;color:#09c762}
.seemore_items .bd{width:162px;height:auto;position:relative;overflow:hidden;margin:0 auto}
.seemore_items .bd ul{width:162px}
.seemore_items li{height:220px;overflow:hidden;margin-bottom:10px}
.seemore_items li a{display:block;position:relative}
.seemore_items li a img{width:160px;height:160px;background-color:#fff;vertical-align:top}
.seemore_items li p.name{margin-top:5px;height:36px;overflow:hidden}
.clear_h_btn{display:block;width:100%;text-align:right;cursor:pointer;}

</style>
