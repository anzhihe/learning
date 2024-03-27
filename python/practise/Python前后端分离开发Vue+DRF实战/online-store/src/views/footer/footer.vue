<template>
<div id="footer">
    <div class="ft-bg">
        <div class="w-ensure mb20">
            <div class="w-main">
                <ul>
                    <li><a>
                        <img width="300" height="90" src="../../static/images/footer/ft-svr1.gif">
                    </a></li>
                    <li><a>
                    <img width="300" height="90" src="../../static/images/footer/ft-svr2.gif">
                    </a></li>
                    <li><a >
                    <img width="300" height="90" src="../../static/images/footer/ft-svr3.gif">
                    </a></li>
                    <li><a>
                    <img width="300" height="90" src="../../static/images/footer/ft-svr4.gif">
                    </a></li>
                </ul>
            </div>

        <div class="ft_main">
            </div>
            <div class="ft_txt">
                <p class="ft_contact"> <span>服务时间：09:00-23:00</span>
                    <span class="ft_phone">客服热线: <em>010-88888888</em></span>
                </p>
            </div>
        </div>
    </div>
</div>
</template>
<script>

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
body,p,ul,li {
    margin:0;
    padding:0
}
body{
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
i {
    font-style:normal
}
ul {
    list-style:none
}
img {
    border:0
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



#footer {
    border-top:1px solid #eee;
    background:#fff;
}
#footer .ft_main {
    width:1196px;
    margin:0 auto
}
#footer .ft_cata {
    display:none
}
#footer .w-ensure {
    background: #09c762 none repeat scroll 0 0;
    height: 90px;
}
#footer .w-main {
    margin: 0 auto;
    width: 1200px;
}
#footer .w-main::after {
    clear: both;
    content: "";
    display: table;
}
#footer .w-ensure li {
    float: left;
    font-size: 0;
}
#footer .ft_nav {
    height:22px;
    padding:20px 0 15px;
    text-align:center
}
#footer .ft_nav a {
    display:inline-block;
    padding:0 20px 0 21px;
    /*background:url(../../../static/images/footer/border-right.png) no-repeat 0 center*/
}
#footer .ft_nav a.noborder {
    background:0
}

#footer .ft_txt {
    text-align:center;
    padding:8px 0
}
#footer .ft_txt p {
    padding:5px 0;
    color:#666
}
#footer .ft_txt .ft_phone {
    font-size:14px
}
#footer .ft_txt .ft_phone em {
    color:#09c762;
    font-weight:bold;
    font-size:24px
}
#footer .ft_txt .ft_contact span {
    display:inline-block;
    padding:0 20px
}


</style>
