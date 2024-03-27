<template>
    <div class="pagenav" id="pagenav">
        <ul>
            <li>
                <span class="currentStep">1</span>
                <a href="http://sx.web51.youxueshop.com/category.php?id=2&amp;price_min=0&amp;price_max=0&amp;page=2&amp;sort=sales_volume_base&amp;order=DESC" class="step">2</a>
                <a class="nextLink" href="http://sx.web51.youxueshop.com/category.php?id=2&amp;price_min=0&amp;price_max=0&amp;page=2&amp;sort=sales_volume_base&amp;order=DESC">下一页</a>

            </li>
        </ul>
        <div class="clear"></div>
    </div>
  
</template>
<script>

  export default {
    data () {
        return {
            
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
<style lang='scss'>

ul {
    list-style:none
}


input {
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
a:focus{
    outline:0
}
::selection {
    background:#09c762;
    color:#fff
}
canvas {
    -ms-touch-action:double-tap-zoom
}

.pagenav {
    padding:10px 0;
    font-size:14px;
    text-align:right
}
.pagenav a {
    margin-left:4px;
    padding:4px 10px;
    font-size:14px;
    border:1px solid #eee;
    background-color:#fff;
    border-radius:2px
}
.pagenav a:hover {
    color:#09c762;
    border-color:#09c762;
    text-decoration:none
}
.pagenav span.currentStep {
    padding:4px 8px;
    margin-left:3px;
    font-weight:bold
}
.pagenav span.step {
    color:#999;
    margin:0 5px
}

</style>
