<template>
    <div>
        <banner></banner>
        <newP></newP>
        <seriesList></seriesList>
    </div>
</template>
<script>
//新品
import newP from './new';
//list
import seriesList from './series-list';
//banner
import banner from './banners';

export default {
    components:{
        newP,seriesList,banner
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
    color:#09c762
}
.gray999,.gray,a.gray,a.gray:hover {
    color:#999
}

</style>
