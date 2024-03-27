<template>
    <div class="sidebar">
        <div class="cate-menu" id="cate-menu">
            <h3><a href=""><strong>生鲜食品</strong><i id="total_count">商品共14件</i></a></h3>
<!--             <dl>
                <dt>精品肉类</dt>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=64">羊肉</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=65">禽类</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=66">猪肉</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=67">牛肉</a> </dd>

                <dt>海鲜水产</dt>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=68">参鲍</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=69">鱼</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=70">虾</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=71">蟹/贝</a> </dd>

                <dt>蛋制品</dt>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=72">松花蛋/咸鸭蛋</a> </dd>
                <dd> <a href="http://sx.web51.youxueshop.com/category.php?id=73">鸡蛋</a> </dd>

            </dl> -->
            <dl>
                <template v-for="item in cateMenu">
                    <dt>{{ item.name }}</dt>
                    <dd v-for="subItem in item.children">
                        <a href="http://sx.web51.youxueshop.com/category.php?id=64">{{ subItem.name}}</a>
                    </dd>
                </template>
                
            </dl>
        </div>
    <!--<div class="fixed-want" id="fixed-want">-->
        <!--<div class="hd">大牌推荐</div>-->
        <!--<div class="bd" style="border-top:0;">-->


            <!--<dl class="brand">-->
                <!--<dd>-->
                    <!--<a href="http://sx.web51.youxueshop.com/category.php?id=2&amp;brand=9" target="_blank" rel="nofollow">金赏</a>-->
                    <!--<a href="http://sx.web51.youxueshop.com/category.php?id=2&amp;brand=1" target="_blank" rel="nofollow">艾尔Aier</a>-->
                    <!--<a href="http://sx.web51.youxueshop.com/category.php?id=2&amp;brand=2" target="_blank" rel="nofollow">发育宝Haipet</a>-->
                    <!--<p class="more"><a href="http://sx.web51.youxueshop.com/brand.php">更多&gt;</a></p>-->
                <!--</dd>-->
            <!--</dl>-->
        <!--</div>-->
    <!--</div>-->
    </div>
  
</template>
<script>
  export default {
    data () {
        return {
            cateMenu: [
                {
                    id: 123,
                    name: '精品肉类',
                    link: '',
                    children: [
                        {
                            id: 111,
                            name: '羊肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '牛肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '猪肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '鸡肉',
                            link: ''
                        },

                    ]
                },
                {
                    id: 123,
                    name: '海鲜水产',
                    link: '',
                    children: [
                        {
                            id: 111,
                            name: '鱼',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '虾',
                            link: ''
                        }

                    ]
                },
                {
                    id: 123,
                    name: '精品肉类',
                    link: '',
                    children: [
                        {
                            id: 111,
                            name: '羊肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '牛肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '猪肉',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '鸡肉',
                            link: ''
                        },

                    ]
                },
                {
                    id: 123,
                    name: '叶菜类',
                    link: '',
                    children: [
                        {
                            id: 111,
                            name: '生菜',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '菠菜',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '圆椒',
                            link: ''
                        },
                        {
                            id: 111,
                            name: '西兰花',
                            link: ''
                        },

                    ]
                },
                {
                    id: 123,
                    name: '叶菜类',
                    link: ''
                },
            ]
        };
    },
    components: {
        
    },
    props: {
        
    },
    created () {
        
    },
    watch: {
        
    },
    computed: {

    },
    methods: {
        
    }
}
</script>
<style >
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
@font-face {
    font-family:'lizi';
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot');
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot?#iefix') format('embedded-opentype'),url('http://at.alicdn.com/t/font_1412819191_5742776.woff') format('woff'),url('http://at.alicdn.com/t/font_1412819191_5742776.ttf') format('truetype'),url('http://at.alicdn.com/t/font_1412819191_5742776.svg#iconfont') format('svg')
}
.here{padding:5px 0;color:#bbb}
.here i.iconfont{font-size:14px}
.here h1{display:inline;font-size:12px;color:#333;font-weight:normal}
.sidebar{width:214px;float:left}
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

</style>
