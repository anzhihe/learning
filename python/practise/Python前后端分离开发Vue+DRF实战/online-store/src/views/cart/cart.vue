<template>
  <div id="main">
    <div class="top-next cle">
      <div class="fr"> <a class="graybtn" @click="continueShopping">继续购物</a>
        <a  class="btn" id="checkout-top" @click="balanceCount">&nbsp;去结算&nbsp;</a> </div>
    </div>
    <div class="cart-box" id="cart-box">
      <div class="hd"> <span class="no2" id="itemsnum-top">{{goods.goods_list.length}}件商品</span>
        <span class="no4">单价</span> <span>数量</span> <span>小计</span>
      </div>
      <div class="goods-list">
        <ul>
          <li class="cle hover" style="border-bottom-style: none;" v-for="(item,index) in goods.goods_list">
            <div class="pic">
              <a target="_blank"> <img :alt="item.goods.name" :src="item.goods.goods_front_image"></a>
            </div>
            <div class="name">
              <a target="_blank">{{item.goods.name}}</a>
              <p></p>
            </div>
            <div class="price-xj">
              <p><em>￥{{item.goods.shop_price}}元</em></p>
            </div>
            <div class="nums" id="nums">
              <span class="minus" title="减少1个数量" @click="reduceCartNum(index, item.goods.id);">-</span>
              <input type="text"  v-model="item.nums" >
              <span class="add" title="增加1个数量" @click="addCartNum(index, item.goods.id);">+</span>
            </div>
            <div class="price-xj"><span></span>
              <em id="total_items_3137">￥{{item.goods.shop_price * item.nums}}元</em>
            </div>
            <div class="del">
              <a class="btn-del" @click="deleteGoods(index, item.goods.id)">删除</a>
            </div>
          </li>
        </ul>
      </div>

      <div class="fd cle">
        <div class="fl">
          <p class="no1"> <a id="del-all" @click="delAll">清空购物车</a> </p>
          <p><a class="graybtn" @click="continueShopping">继续购物</a></p>
        </div>
        <div class="fr" id="price-total">
          <p><span id="selectedCount">{{goods.goods_list.length}}</span>件商品，总价：<span class="red"><strong id="totalSkuPrice">￥{{totalPrice}}元</strong></span></p>
        </div>
        <div class="extr">
          <div class="address">
            <p class="title">配送地址</p>
            <ul>
              <li class="add" @click="addAddr">
                <router-link :to="'/app/home/member/receive'" target = _blank>
                  +
                  点击添加地址</router-link>
              </li>
              <li v-for="item in addrInfo" :class="{'addressActive':addressActive==item.id}" @click="selectAddr(item.id)">
                <p class="item">地址：{{item.province}} {{item.city}} {{item.district}} {{item.address}}</p>
                <p class="item">电话：{{item.signer_mobile}}</p>
                <p class="item">姓名：{{item.signer_name}}</p>
              </li>
            </ul>
          </div>
          <div class="pay">
            <p class="title">选择支付方式</p>
            <p class="payWrap"><img v-for="item in payWrapList" src="../../static/images/alipay.jpg" :class="{'payWrapActive':payWrapActive==item.id}" @click="selectPay(item.id)"></p>
          </div>
        </div>
        <textarea type="text" v-model="post_script" placeholder="请输入留言" style="margin-top: 10px; height:50px;width: 100%;">
        </textarea>
        <p class="sumup"><a class="btn" @click="balanceCount">去结算</a></p>
      </div>
    </div>
  </div>

</template>
<script>
  import {getShopCarts, createOrder, updateShopCart, deleteShopCart, getAddress} from '../../api/api'
  export default {
    data () {
      return {
        addrInfo: [
        ],
        payWrapList:[
          {
            id:1,
            img:'../../static/images/alipay.jpg'
          }
        ],
        payWrapActive:null,
        addressActive:null,
        totalPrice:0,
        post_script:'',
        address:'',
        signer_name:'',
        signer_mobile:'',
        goods: {
          totalPrice:null,
          goods_list: [
          ],
        }
      };
    },
    components: {

    },
    props: {

    },
    created () {
      // 请求购物车商品
      getShopCarts().then((response)=> {
        console.log(response.data)
        // 更新store数据
        //this.goods_list = response.data;
        var totalPrice = 0
        this.goods.goods_list = response.data;
        response.data.forEach(function(entry) {
          totalPrice += entry.goods.shop_price*entry.nums
          console.log(entry.goods.shop_price);
        });

        this.goods.totalPrice = totalPrice
        this.totalPrice = totalPrice
      }).catch(function (error) {
      });
      this.getAllAddr ()

    },
    watch: {

    },
    computed: {

    },
    methods: {
      addCartNum(index, id) { //添加数量
        updateShopCart(id,{
          nums: this.goods.goods_list[index].nums+1
        }).then((response)=> {
          this.goods.goods_list[index].nums = this.goods.goods_list[index].nums + 1;
          // 更新store数据
          this.$store.dispatch('setShopList');
          //更新总价
          this.setTotalPrice();

        }).catch(function (error) {
          console.log(error);
        });
      },
      setTotalPrice(){
        var goods_list = this.goods.goods_list;
        var totalPrice = 0;
        for(var i = 0;i<goods_list.length;i++){
          totalPrice=totalPrice+goods_list[i].nums* goods_list[i].goods.shop_price;
        }
        this.totalPrice = totalPrice;
      },
      deleteGoods(index,id) { //移除购物车
        alert('您确定把该商品移除购物车吗');
        deleteShopCart(id).then((response)=> {
          console.log(response.data);
          //this.goods.goods_list.splice(index,1);
          this.goods_list.goods_list.splice(index, 1);

          // 更新store数据
          this.$store.dispatch('setShopList');

        }).catch(function (error) {
          console.log(error);
        });
      },
      reduceCartNum(index, id) { //删除数量
        if(this.goods.goods_list[index].nums<=1){
          this.deleteGoods(index, id)
        }else{
          updateShopCart(id,{
            nums: this.goods.goods_list[index].nums-1
          }).then((response)=> {
            this.goods.goods_list[index].nums = this.goods.goods_list[index].nums - 1;
            // 更新store数据
            this.$store.dispatch('setShopList');
            //更新总价
            this.setTotalPrice();

          }).catch(function (error) {
            console.log(error);
          });
        }


      },
      continueShopping () { // 继续购物
        this.$router.push({name: 'index'});
      },
      delAll () { //清空购物车

        this.$http.post('/shoppingCart/clear', {

        }).then((response)=> {
          console.log(response.data);
          this.goods.goods_list.splice(0, this.goods.goods_list.length);
          // 更新store数据
          this.$store.dispatch('setShopList');

        }).catch(function (error) {
          console.log(error);
        });
      },
      selectPay(id){
        this.payWrapActive = id;
      },
      getAllAddr () { //获得所有配送地址
        getAddress().then((response)=> {
          this.addrInfo = response.data;
        }).catch(function (error) {
          console.log(error);
        });
      },
      addAddr () { //添加地址

      },
      selectAddr (id) { //选择配送地址
        this.addressActive = id;
        var cur_address = ''
        var cur_name = ''
        var cur_mobile = ''
        this.addrInfo.forEach(function(addrItem) {
          if(addrItem.id == id){
            cur_address = addrItem.province+addrItem.city+addrItem.district+addrItem.address
            cur_name = addrItem.signer_name
            cur_mobile = addrItem.signer_mobile
          }
        });
        this.address = cur_address
        this.signer_mobile = cur_mobile
        this.signer_name = cur_name
      },
      balanceCount () { // 结算
          if(this.addrInfo.length==0){
              alert("请选择收货地址")
          }else{
            createOrder(
              {
                post_script:this.post_script,
                address:this.address,
                signer_name:this.signer_name,
                singer_mobile:this.signer_mobile,
                order_mount:this.totalPrice
              }
            ).then((response)=> {
              alert('订单创建成功')
              window.location.href=response.data.alipay_url;
            }).catch(function (error) {
              console.log(error);
            });
          }
      },
    }
  }
</script>
<style scoped>
  .address {
    margin-bottom: 20px;
  }
  .addressActive,.payWrapActive{
    border:1px solid red !important;
  }
  .payWrap{
    padding:0 10px;
  }
  .extr {
    padding: 0 0px;
    border: 1px solid #ddd;
  }
  .extr .title{
    height: 28px;
    line-height: 28px;
    background-color: #ddd;
    font-weight: bold;
    font-size: 14px;
    padding: 0 10px;
  }
  .address .add {
    width: 100px;
    cursor: pointer;
    height: 72px;
  }
  .address ul li {
    vertical-align: top;
    width: 150px;
    border: 1px solid #ddd;
    display: inline-block;
    margin-left: 5px;
    padding: 5px;
    cursor: pointer;
  }
  .address ul li .item {
    margin-bottom: 0px;
  }
  .sumup {
    margin-top: 20px;
    text-align: right;
  }
  .pay img{
    width: 150px;
    height: 80px;
    cursor: pointer;
  }
  #main{
    width:1008px;
    margin:30px auto 50px;
  }
  .top-next {
    color:#666;
    padding-bottom:10px
  }
  .top-next a {
    margin-left:5px
  }
  .top-next .fl {
    padding-top:5px
  }
  .top-next .fl a {
    font-weight:bold
  }
  .top-next .fr {
    padding-bottom:2px
  }
  .top-next .fr span {
    margin-right:10px
  }
  .top-next .fr span.red {
    margin-right:0;
    color:#09c762
  }
  .cart-box .hd {
    border:1px solid #e4e4e4;
    border-bottom-color:#bbb;
    background-color:#fff;
    padding:15px;
    color:#111;
    font-size:0
  }
  .cart-box .hd span {
    display:inline-block;
    width:108px;
    font-size:14px
  }
  .cart-box .hd span.no1 {
    width:35px
  }
  .cart-box .hd span.no1 input {
    vertical-align:-1px
  }
  .cart-box .hd span.no2 {
    width:420px
  }
  .cart-box .hd span.no3 {
    width:224px
  }
  .cart-box .hd span.no4 {
    width:170px
  }
  .goods-list {
    margin-bottom:8px
  }
  .goods-list ul {
    border:1px solid #e4e4e4;
    background-color:#fff
  }
  .goods-list li {
  +display:inline;
    zoom:1;
    width:1006px;
    border-bottom:1px dotted #cbcbcb;
    color:#666;
    padding:10px
  }
  .goods-list li a {
    color:#666
  }
  .goods-list li .check {
    height:20px;
    width:35px;
    padding:18px 0 0 15px;
    float:left
  }
  .goods-list li .pic {
    height:62px;
    width:62px;
    float:left
  }
  .goods-list li .pic img {
    height:60px;
    width:60px;
    vertical-align:top;
    border:1px solid #eee
  }
  .goods-list li .name {
    width:290px;
    height:auto;
    line-height:18px;
    float:left;
    padding:5px 60px 0 10px
  }
  .goods-list li .name i {
    background-color:#fff2f2;
    color:#09c762;
    padding:0 2px;
    border-radius:2px
  }
  .goods-list li .name .isfree {
    background-color:#95ce67;
    color:#fff
  }
  .goods-list li .name .isfree_2 {
    background-color:#53a90e;
    color:#fff
  }
  .goods-list li .name p {
    margin-top:5px
  }
  .goods-list li .price-one {
    padding:22px 0 0 0;
    width:200px;
    float:left;
    font-size:12px
  }
  .goods-list li .price-one p.mt {
    margin-top:-18px
  }
  .goods-list li .price-one span {
    margin-right:4px
  }
  .goods-list li .price-one cite {
    font-size:14px;
    margin-right:3px
  }
  .goods-list li .price-one .time {
    color:#f30
  }
  .goods-list li .nums {
    padding-top:18px;
    width:128px;
    float:left;
    position:relative
  }
  .goods-list li .nums span {
    float:left;
    display:block;
    visibility:hidden;
    width:20px;
    height:20px;
    border:1px solid #e8e8e8;
    background-color:#e8e8e8;
    text-shadow:1px 1px 1px #fff;
    text-align:center;
    font-size:18px;
    cursor:pointer;
    overflow:hidden;
    line-height:18px
  }
  .goods-list li .nums span:hover {
    background-color:#fff
  }
  .goods-list li .nums span.disabled {
    cursor:not-allowed;
    color:#ddd;
    background-color:#f1f1f1
  }
  .goods-list li .nums input {
    float:left;
    width:30px;
    height:18px;
    padding-bottom:2px;
    border:0;
    border-top:1px solid #fff;
    border-bottom:1px solid #fff;
    text-align:center;
    color:#666;
    font-size:14px
  }
  .goods-list li .nums .only1 {
    margin-left:33px;
    font-size:14px
  }
  .goods-list li .price-xj {
    padding:18px 0 0 0;
    width:150px;
    float:left
  }
  .goods-list li .price-xj span {
    font-size:12px
  }
  .goods-list li .price-xj em {
    font-size:14px
  }
  .goods-list li .price-xj cite {
    font-size:14px;
    color:#09c762;
    margin:0 3px
  }
  .goods-list li .del {
    padding:20px 0 0 0;
    width:98px;
    float:right;
    text-align:center
  }
  .goods-list li .del p {
    margin-top:-10px;
    margin-bottom:5px
  }
  .goods-list li.multi-item .item-list {
    float:left;
    width:380px
  }
  .goods-list li.multi-item .item-list div {
    margin-bottom:5px
  }
  .goods-list li.hover .nums span {
    visibility:visible
  }
  .goods-list li.hover .nums input {
    border-color:#e8e8e8;
    background:#Fff
  }
  .goods-list li.disabled .nums span {
    visibility:hidden
  }
  .goods-list li.disabled .nums input {
    background:0;
    border:0
  }
  .goods-list li.disabled .del {
    line-height:24px
  }
  .goods-list li.disabled .del span.red {
    padding:3px 8px;
    font-size:12px;
    background-color:#ddd;
    border-radius:2px;
    color:#333
  }
  .goods-list li.disabled {
    background-color:#f1f1f1;
    opacity:.6;
    filter:Alpha(opacity=60)
  }
  .goods-list li.disabled .price-one .time {
    color:#999
  }

  .cart-box .fd {
    padding-top:20px
  }
  .cart-box .fd .no1 input {
    vertical-align:-2px
  }
  .cart-box .fd .no1 a {
    padding:3px 5px
  }
  .cart-box .fd .no1 a:hover {
    text-decoration:none;
    background-color:#ffe6e6
  }
  .cart-box .fd .graybtn {
    font-size:14px;
    padding:10px 15px;
    color:#333;
    cursor: pointer;
  }
  .cart-box .fd .graybtn i {
    margin-right:2px;
    vertical-align:1px
  }
  .cart-box .fd .btn {
    font-size:14px;
    padding:10px 25px;
    margin-left:20px
  }
  .cart-box .fd .btn i {
    vertical-align:2px;
    margin-left:2px
  }
  .cart-box .fd .btn img {
    vertical-align:-2px;
    height:16px
  }
  .cart-box .fd p {
    margin-bottom:20px
  }
  .cart-box .fd strong {
    font-size:20px;
    font-family:arial;
    margin:0 3px
  }
  .cart-box .fd .fr {
    margin-top:-11px
  }
  .cart-box .fd .fr p {
    text-align:right;
    margin-bottom:16px
  }

  .graybtn {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    border:1px solid #c4c4c4;
    border-radius:2px;
    font-size:100%;
    color:#666;
    background-color:#efefef;
    background-image:-webkit-linear-gradient(#f8f8f8,#e5e5e5);
    background-image:-moz-linear-gradient(#f8f8f8,#e5e5e5);
    background-image:linear-gradient(#f8f8f8,#e5e5e5);
    background-repeat:repeat-x;
    vertical-align:middle;
    cursor: pointer;
  }
  .graybtn:hover {
    text-decoration:none;
    color:#666;
    background:#e5e5e5
  }
  .btn,.btn-css3 {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    _line-height:18px;
    border:1px solid #1e9246;
    border-radius:3px;
    font-size:100%;
    color:#fff;
    background-color:#09c762;
    overflow:hidden;
    vertical-align:middle
  }
  .btn:hover,.btn-css3:hover {
    text-decoration:none;
    color:#fff;
    background:#1e9246
  }
  .btn img,.btn-css3 img {
    vertical-align:middle
  }
  #login-nala-form li.last .btn {
    height:50px;
    width:100%;
    text-align:center;
    color:#fff;
    letter-spacing:5px;
    cursor:pointer;
    font-size:18px;
    border:0
  }

  .none-box a.btn {
    margin-left:36px;
    font-size:12px
  }
  a {
    cursor: pointer;
  }
</style>
