<template>
    <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
            <div class="box">
                <div class="box_1">
                    <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                        <h5><span>我的订单</span></h5>
                        <div class="blank"></div>
                        <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                            <tbody>
                                <tr align="center">
                                    <td bgcolor="#ffffff">订单号</td>
                                    <td bgcolor="#ffffff">下单时间</td>
                                    <td bgcolor="#ffffff">订单总金额</td>
                                    <td bgcolor="#ffffff">订单状态</td>
                                    <td bgcolor="#ffffff">操作</td>
                                </tr>
                                <tr v-for="item in orders">
                                    <td align="center" bgcolor="#ffffff"><a class="f6" @click="goDetail(item.id)">{{item.order_sn}}</a></td>
                                    <td align="center" bgcolor="#ffffff">{{item.add_time}}</td>
                                    <td align="right" bgcolor="#ffffff">￥{{item.order_mount}}元</td>
                                    <td v-if="item.pay_status == 'paying' " align="center" bgcolor="#ffffff">待支付</td>
                                    <td v-if="item.pay_status == 'TRADE_SUCCESS' " align="center" bgcolor="#ffffff">已支付</td>
                                    <td align="center" bgcolor="#ffffff"><font class="f6"><a @click="cancelOrder(item.id)">取消订单</a></font></td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="blank5"></div>
                        <form name="selectPageForm" action="" method="get">
                            <div class="pagenav" id="pagenav">
                                <ul>
                                    <li>
                                    </li>
                                </ul>
                                <div class="clear"></div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
  import { getOrders, createOrder, delOrder } from '../../api/api'
    export default {
        data () {
            return {
                orders: [
                    // {
                    //     orderId: 122324, //订单号
                    //     time: '2017-07-07 13:48:53', //下单时间
                    //     totalPrice: '123', //订单总金额
                    //     state: '未付款',
                    // },
                    // {
                    //     orderId: 122324, //订单号
                    //     time: '2017-07-07 13:48:53', //下单时间
                    //     totalPrice: '123', //订单总金额
                    //     state: '未付款',
                    // },
                ]
            };
        },
        props: {

        },
        components: {

        },
        created () {
            this.getOrder();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            getOrder () {
                getOrders().then((response)=> {
                    this.orders = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            cancelOrder (id) {
                alert('您确认要取消该订单吗？取消后此订单将视为无效订单');
                delOrder(id).then((response)=> {
                  alert('订单删除成功')
                }).catch(function (error) {
                    console.log(error);
                });
            },
            goDetail (id) {
                this.$router.push({name: 'orderDetail', params: {orderId: id}});
            }
        }
    }
</script>
<style scoped>

html {
    background:#fafafa;
    color:#333;
    _background-attachment:fixed
}
html.isPhone {
    min-width:1196px
}
body{
    margin:0;
    padding:0
}
body{
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
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
/*.fl {*/
/*float:left*/
/*}*/
/*.fr {*/
/*float:right*/
/*}*/
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
    text-decoration:underline;
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
.fs14 {
    font-size:14px
}
.red,a.red,a.red:hover,.pink,a.pink,a.pink:hover {
    color:#09c762
}
.gray999,.gray,a.gray,a.gray:hover {
    color:#999
}
.green {
    color:#2b9b2d
}
.blue,.blue:hover {
    color:#09f
}
@font-face {
    font-family:'lizi';
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot');
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot?#iefix') format('embedded-opentype'),url('http://at.alicdn.com/t/font_1412819191_5742776.woff') format('woff'),url('http://at.alicdn.com/t/font_1412819191_5742776.ttf') format('truetype'),url('http://at.alicdn.com/t/font_1412819191_5742776.svg#iconfont') format('svg')
}
.iconfont {
    font-family:"lizi";
    font-size:100%;
    font-style:normal;
    font-weight:normal;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale
}

.my_nala_main h3.my_nala {
    height:60px;
    border:1px solid #e7e7e7;
    border-bottom:0
}
.my_nala_main h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
.my_nala_main h3.my_nala a:hover {
    text-decoration:none
}

.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.my_nala_centre .trade_mod .h301 a.more {
    font-size:14px;
    color:#666;
    font-weight:normal
}
.my_nala_centre .trade_mod .h301 a.more:hover {
    color:#09c762
}
.my_nala_centre .something_interesting {
    margin-top:10px
}
.my_nala_centre .something_interesting ul {
    margin-left:20px
}
.my_nala_centre .something_interesting li {
    width:130px;
    text-align:center;
    float:left
}
.my_nala_centre .something_interesting b {
    font-weight:normal
}
.my_nala_centre .something_interesting em {
    font-size:12px;
    font-weight:bold;
    color:#09c762
}
.my_nala_centre .relate_goods {
    border:1px solid #e4e4e4;
    border-top:0
}
.my_nala_centre .pagenav {
    padding:15px 10px;
    border-top:1px solid #e4e4e4
}


.ilizi_centre {
    background:0
}

.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff
}
.ilizi .face,.iface .face {
    display:block;
    float:left;
    width:100px;
    height:100px;
    position:relative
}
.ilizi .edit_face,.iface .edit_face {
    position:absolute;
    height:20px;
    line-height:20px;
    width:100px;
    display:block;
    background:rgba(0,0,0,0.5);
    text-align:center;
    color:#fff;
    left:1px;
    bottom:-1px;
    _bottom:0;
    filter:progid:DXImageTransform.Microsoft.gradient(enabled='true',startColorstr='#77000000',endColorstr='#77000000');
    visibility:hidden;
    margin:0
}
.ilizi .face img,.iface .face img {
    width:100px;
    height:100px;
    border:1px solid #e4e4e4
}
.ilizi .ilizi_info {
    width:800px;
    float:right;
    height:100px
}


</style>




