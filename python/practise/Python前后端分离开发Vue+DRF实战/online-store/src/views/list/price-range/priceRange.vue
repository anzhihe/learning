<template>

    <div class="search-options" id="search-options">
    <div class="bd">
        <dl>
            <dt>价格：</dt>
            <dd class="dd-price" style="height: 48px;">
                <div class="items cle w500">
                    <div class="link" v-for="item in priceRange" @click="changePriceRange(item.min,item.max)"> <a class="item">{{item.min}}&nbsp;-&nbsp;{{item.max}}</a> </div>
                    <!-- <div class="link"> <a class="item">20&nbsp;-&nbsp;70</a> </div>
                    <div class="link"> <a class="item">70&nbsp;-&nbsp;120</a> </div>
                    <div class="link"> <a class="item">120&nbsp;-&nbsp;170</a> </div>
                    <div class="link"> <a class="item">170&nbsp;-&nbsp;220</a> </div>
                    <div class="link"> <a class="item">220&nbsp;-&nbsp;270</a> </div> -->
                </div>
                <div class="priceform" id="priceform" v-clickoutside="handleClickOutside">
                    <div class="form-bg">
                        <form id="freepriceform" >
                            <span class="rmb"></span>
                            <input type="text" value="" name="price_min" id="pricemin" v-model="price_min" @focus="focus=true">
                            <span class="rmb rmb2"></span>
                            <input type="text" value="" name="price_max" id="pricemax" v-model="price_max" @focus="focus=true">
                            <input v-show="focus" value="确定" @click="changePriceRange(price_min, price_max)" class="submit">
                        </form>
                    </div>
                </div>
            </dd>
        </dl>

    </div>
</div>
  
</template>
<script>
import clickoutside from '../../../static/js/clickoutside';
  export default {
    data () {
        return {
            price_min: '',
            price_max: '',
            focus: false //是否获得焦点
        };
    },
    directives: {
            clickoutside
        },
    components: {
        
    },
    props: {
        priceRange: {
            type: Array,
            default: [],
        }
    },
    created () {
        
    },
    watch: {
        
    },
    computed: {

    },
    methods: {
        changePriceRange (min, max) {
            this.$emit('on-change', {min, max});
        },
        handleClickOutside () {
            this.focus = false;

        }
    }
}
</script>
<style >

.maincon{width:970px;float:right}
.search-options{margin-bottom:12px;background-color:#fff}
.search-options .bd{border:1px solid #eee;border-bottom:0;+zoom:1}
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

/*.bd a span{background:url(images/search-page-bg.png) 0 -9999px no-repeat}*/
/*.bd {*/
    /*padding:0 0 6px 14px;*/
    /*margin-right:-10px;*/
    /*height:43px;*/
    /*overflow:hidden*/
/*}*/
/*.main_cata li .bd a {*/
    /*color:#999;*/
    /*display:inline-block;*/
    /*margin-right:14px;*/
    /*line-height:22px*/
/*}*/

.priceform{position:absolute;top:-11px;left:500px;z-index:10}
.priceform .form-bg{width:270px;border:1px solid #fff;border-top-color:#eee;padding:8px 15px;+padding-bottom:7px;font-size:0}
.priceform input{font-size:12px;border:1px solid #eaeaea;padding:3px;height:18px;width:60px;line-height:18px}
.priceform input.submit{text-align: center;margin-left: 20px;height:26px;padding:0;line-height:16px;cursor:pointer;background-color:#eaeaea;width:68px;border-color:#e1e1e1;background-color:#eaeaea;background-image:-moz-linear-gradient(#fefefe,#eaeaea);background-image:-webkit-linear-gradient(#fefefe,#eaeaea);background-image:linear-gradient(#fefefe,#eaeaea)}
.priceform input.submit:hover{background-color:#e4e4e4}
.priceform span{height:26px;width:12px;display:inline-block;vertical-align:-9px;+vertical-align:-1px;font-size:12px}
.priceform span.rmb{background-position:-10px -272px}
.priceform span.rmb2{padding-left:20px;background-position:8px -272px}
/*.priceform form p{display:none;text-align:right;padding-top:4px}*/
.priceform form p{text-align:right;padding-top:4px}
#priceform.focus .form-bg{background-color:#f6f6f6;border-color:#e4e4e4;height:28px;box-shadow:0 1px 3px rgba(100,100,100,0.1)}
#priceform.focus form p{display:inline;padding-left:15px}
a.more-btn,.rmb,.search-selected a.item,.sort .bd a span{background:url(./images/search-page-bg.png) 0 -9999px no-repeat}








.sort .bd{float:left;font-size:0;padding-right:12px}
.sort .bd a{display:inline-block;font-size:12px;margin-right:-1px;+margin-right:-2px;position:relative;z-index:1}
.sort .bd a span{display:block;padding:5px 26px 5px 15px;background-position:right -128px;+background-position:right -127px}
.sort .curr .search_DESC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -104px;+background-position:right -102px;color:#09c762;text-shadow:1px 1px 1px #fff}
.sort .curr .search_ASC{border:1px solid #fff;padding:4px 26px 4px 15px;background-position:right -330px;+background-position:right -328px;color:#09c762;text-shadow:1px 1px 1px #fff}
.sort .bd a:hover{z-index:2;text-decoration:none}
.sort .bd a.default span{background-image:none;padding-right:15px}
.sort .bd a.promotion span{padding-right:15px;padding-left:30px;background-position:10px -153px}
.sort .bd a.clicked span{background-position:10px -184px}

</style>
