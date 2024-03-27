<template>
    <div class="sort">
        <div class="bd">
            <form name="listform">
                <!-- <a title="销量" href="http://sx.web51.youxueshop.com/category.php?category=2&amp;display=grid&amp;brand=0&amp;price_min=0&amp;price_max=0&amp;filter_attr=0&amp;page=1&amp;sort=sales_volume_base&amp;order=ASC#goods_list" class="curr" rel="nofollow"><span class="search_DESC">销量</span></a>
                <a title="价格" href="http://sx.web51.youxueshop.com/category.php?category=2&amp;display=grid&amp;brand=0&amp;price_min=0&amp;price_max=0&amp;filter_attr=0&amp;page=1&amp;sort=shop_price&amp;order=ASC#goods_list" rel="nofollow"><span class="">价格</span></a> -->
                <a title="销量" class="curr" rel="nofollow" @click="sortType('-sold_num')"><span :class="{search_DESC: cur==='-sold_num'}">销量</span></a>
                <a title="价格" class="curr" rel="nofollow" @click="sortType('-shop_price')"><span :class="{search_DESC: cur==='-shop_price'}">价格</span></a>
                <!-- <input type="hidden" name="category" value="2">
                <input type="hidden" name="display" value="grid" id="display">
                <input type="hidden" name="brand" value="0">
                <input type="hidden" name="price_min" value="0">
                <input type="hidden" name="price_max" value="0">
                <input type="hidden" name="filter_attr" value="0">
                <input type="hidden" name="page" value="1">
                <input type="hidden" name="sort" value="sales_volume_base">
                <input type="hidden" name="order" value="DESC"> -->
            </form>
        </div>
        <div class="search_num">共<b>{{proNum}}</b>个商品 <span id="search_btn" class="search_btn"></span> </div>
    </div>

</template>
<script>
  export default {
    data () {
        return {
            cur: '-sold_num'
        };
    },
    components: {
    },
    props: {
        proNum: { //商品数量
            type: Number,
            default: 0
        }
    },
    created () {

    },
    watch: {

    },
    computed: {

    },
    methods: {
        // 排序方式
        sortType (type) {
            this.cur = type;
            this.$emit('on-sort', type);
        }
    }
}
</script>
<style >

body,button,input {
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
em,i {
    font-style:normal
}

img {
    border:0
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

.clear {
    clear:both;
    height:0;
    font-size:0;
    line-height:0;
    overflow:hidden
}
.cle:after {
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle {
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

.sort {
    margin-bottom: 10px;
    height: 30px;
    border: 1px solid #eee;
    border-bottom: 2px solid #ccc;
    padding: 5px 0;
    background: #fff;
}

.sort .bd a span{background:url(./images/search-page-bg.png) 0 -9999px no-repeat}


.sort .bd{float:left;font-size:0;padding-right:12px}
.sort .bd a{display:inline-block;font-size:12px;margin-right:-1px;+margin-right:-2px;position:relative;z-index:1}
.sort .bd a span{display:block;padding:5px 26px 5px 15px;background-position:right -128px;+background-position:right -127px}
.sort .curr .search_DESC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -104px;+background-position:right -102px;color:#09c762;text-shadow:1px 1px 1px #fff}
.sort .curr .search_ASC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -330px;+background-position:right -328px;color:#09c762;text-shadow:1px 1px 1px #fff}
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


</style>
