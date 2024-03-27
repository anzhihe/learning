<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
        <div class="box">
            <div class="box_1">
                <div class="userCenterBox boxCenterList clearfix" style="_height:1%; font-size:14px;">

                    <h5><span>我的收藏</span></h5>
                    <div class="blank"></div>
                    <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                      <tbody>
                        <tr align="center">
                            <th width="35%" bgcolor="#ffffff">商品名称</th>
                            <th width="30%" bgcolor="#ffffff">价格</th>
                            <th width="35%" bgcolor="#ffffff">操作</th>
                        </tr>
                        <tr v-for="(item,index) in collections">
                            <td bgcolor="#ffffff">
                                <router-link :to="'/app/home/productDetail/'+item.goods.id" class="f6" target="_blank">{{item.goods.name}}</router-link>
                            </td>
                            <td bgcolor="#ffffff">本店价<span class="goods-price">￥{{item.goods.shop_price}}元</span>
                            </td>
                            <td align="center" bgcolor="#ffffff">
                                <a class="f6" @click="deletePro(index, item.goods.id)">删除</a>
                            </td>
                        </tr>
                        <!-- <tr>
                            <td bgcolor="#ffffff"><a href="http://sx.web51.youxueshop.com/goods.php?id=2" class="f6">田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛</a></td>
                            <td bgcolor="#ffffff">          本店价<span class="goods-price">￥70元</span>
                            </td>
                            <td align="center" bgcolor="#ffffff">
                                <a href="javascript:if (confirm(&#39;确定将此商品加入关注列表么？&#39;)) location.href=&#39;user.php?act=add_to_attention&amp;rec_id=30&#39;" class="f6">关注</a>
                                <a href="javascript:addToCart(2)" class="f6">加入购物车</a> <a href="javascript:if (confirm(&#39;您确定要从收藏夹中删除选定的商品吗？&#39;)) location.href=&#39;user.php?act=delete_collection&amp;collection_id=30&#39;" class="f6">删除</a>
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#ffffff"><a href="http://sx.web51.youxueshop.com/goods.php?id=1" class="f6">新鲜水果甜蜜香脆单果约800克</a></td>
                            <td bgcolor="#ffffff">          促销价<span class="goods-price">￥156元</span>
                            </td>
                            <td align="center" bgcolor="#ffffff">
                                <a href="javascript:if (confirm(&#39;确定将此商品加入关注列表么？&#39;)) location.href=&#39;user.php?act=add_to_attention&amp;rec_id=29&#39;" class="f6">关注</a>
                                <a href="javascript:addToCart(1)" class="f6">加入购物车</a> <a href="javascript:if (confirm(&#39;您确定要从收藏夹中删除选定的商品吗？&#39;)) location.href=&#39;user.php?act=delete_collection&amp;collection_id=29&#39;" class="f6">删除</a>
                            </td>
                        </tr> -->
                      </tbody>
                    </table>
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
  import {getAllFavs, delFav} from '../../api/api'
    export default {
        data () {
            return {
                collections: [
                    // {
                    //     id: '3243', // 商品ID
                    //     title: '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛', // 商品名称
                    //     price: 24 //价格
                    // },
                    // {
                    //     id: 'dsfsd', // 商品ID
                    //     title: '新鲜水果甜蜜香脆单果约800克', // 商品名称
                    //     price: 24 //价格
                    // },
                    // {
                    //     id: 'fsdfg', // 商品ID
                    //     title: '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛', // 商品名称
                    //     price: 24 //价格
                    // },

                ]
            };
        },
        props: {

        },
        components: {

        },
        created () {
            this.getCollection();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            getCollection () { //获取收藏列表
              getAllFavs().then((response)=> {
                    this.collections = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            // toProductionDetail (id) { //商品详情页
            //     this.$router.push({name:'productDetail', params: {productId: id}});
            // },
            concern (id) { //加入关注
                this.$http.post('/addConcern', {
                    params: {
                        productId: id, // 商品id
                    }
                }).then((response)=> {
                    console.log(response.data);
                    alert('已加入关注');
                }).catch(function (error) {
                    console.log(error);
                });
            },
            addToCart (id) { //加入购物车
                this.$http.post('/product/addShoppingCart', {
                    params: {
                        productId: id, // 商品id
                        num: this.proDetail.purNum, // 购买数量
                    }
                }).then((response)=> {
                    console.log(response.data);
                    alert('已成功加入购物车');
                }).catch(function (error) {
                    console.log(error);
                });


            },
            deletePro (index, id) { //删除收藏商品
                alert('您确定要从收藏夹中删除选定的商品吗？');
                delFav(id).then((response)=> {
                    this.collections.splice(index,1);
                    alert('已删除商品');
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
<style scoped>

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
