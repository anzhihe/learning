<template>

<div style="margin-top:0px;background: url(../../static/images/register/loginBg1.jpg)no-repeat">
<div class="c-box bg-box" >
    <div class="login-box clearfix"style="margin-top:10px">

        <div class="fr form-box">
            <div class="tab">
                <h2 class="active">手机注册</h2>

            </div>
            <div class="tab-form">
                <form id="mobile_register_form" autocomplete="off">
                    <input type="hidden" name="csrfmiddlewaretoken" value="ywSlOHdiGsK6VFB6iyhnB1B30khmz8SU">

                    <div class="form-group marb8">
                        <label>手&nbsp;机&nbsp;号</label>
                        <input id="jsRegMobile" name="account" v-model="mobile" type="text" placeholder="请输入您的手机号码">
                    </div>
                    <p class="error-text marb8" v-show="error.mobile">{{error.mobile}}</p>

                    <div class="clearfix">
                        <div class="form-group marb8 verify-code">
                            <label>短信验证码</label>
                            <input id="jsPhoneRegCaptcha" v-model="code" type="text" placeholder="输入手机验证码">
                        </div>
                        <input class="verify-code-btn sendcode" type="button" id="jsSendCode" @click="seedMessage" :value="getMessageText">
                    </div>
                     <p class="error-text marb8" v-show="error.code">{{error.code}}</p>

                    <div class="form-group marb8">
                        <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
                        <input id="jsPhoneRegPwd" name="password_m" type="password" v-model="password" placeholder="请输入6-20位非中文字符密码">
                    </div>
                     <p class="error-text marb8" v-show="error.password">{{error.password}}</p>
                    <div class="error btns" id="jsMobileTips"></div>
                    <div class="auto-box marb8">

                    </div>
                    <input class="btn btn-green" id="jsMobileRegBtn" @click="isRegister" type="button" value="注册并登录">
                </form>
            </div>

            <p class="form-p">已有账号？ <router-link :to="'/app/login'">[立即登录]</router-link></p>
        </div>
    </div>
</div>
</div>
</template>
<script>
import { register ,getMessage} from '../../api/api'
import cookie from '../../static/js/cookie';
export default{
    data(){
        return{
            getMessageText:"免费获取验证码",
            mobile:'',
            password:'',
            username:'' ,
            code:'',
            error:{
                mobile:'',
                password:'',
                username:'' ,
                code:'',
            }
        }
    },
    methods:{
        isRegister(){
            var that = this;
            register({
                password:that.password,
                username:that.mobile ,
                code:that.code,
            }).then((response)=> {
              cookie.setCookie('name',response.data.username,7);
              cookie.setCookie('token',response.data.token,7)
              //存储在store
              // 更新store数据
              that.$store.dispatch('setInfo');
              //跳转到首页页面
              this.$router.push({ name: 'index'})

          })
          .catch(function (error) {
            that.error.mobile = error.username?error.username[0]:'';
            that.error.password = error.password?error.password[0]:'';
            that.error.username = error.mobile?error.mobile[0]:'';
            that.error.code = error.code?error.code[0]:'';
          });
        },
        seedMessage(){
            var that = this;
            //开启倒计时
            var countdown=60;
             settime()
            function settime() {
                if (countdown == 0) {
                    that.getMessageText="免费获取验证码";
                    countdown = 60;
                    return;
                } else {
                    that.getMessageText="重新发送(" + countdown + ")";
                    countdown--;
                }
                setTimeout(function() {
                    settime()
                 },1000)
                }
            getMessage({
                    mobile:that.mobile
                }).then((response)=> {

              })
              .catch(function (error) {

          });

        }
    }
}
</script>
<style  scoped>
  .error-text{
    color:#fa8341;
  }
.c-box{
    width:100%;
    min-width: 1190px;
    overflow:hidden;
}
.bg-box{
    background:url(../../static/images/register/loginBg1.jpg) no-repeat center center;
}
.login-box{
    width:853px;
    margin:0px auto;
}
.clearfix::after {
    clear: both;
    content: " ";
    display: block;
    font-size: 0;
    height: 0;
    visibility: hidden;
}

.hd-login{
    position:relative;
    height:68px;
    line-height:68px;
    margin-bottom:15px;
    padding-top:32px;
    padding-left:190px;
   /* background:url(../../static/images/register/logo.png) no-repeat 0 center;*/
}
.index-logo{
    position:absolute;
    left:0;
    top:0;
    display:block;
    width:190px;
    height:100px;
    cursor: pointer;
}
.index-font{
    float:right;
    height:20px;
    line-height:20px;
    margin-top:48px;
    padding-left:20px;
    color:#fff;
  /*  background:url(../../static/images/register/homepage.png) no-repeat 0 top;*/
}
.fl{float:left!important;}
.fr{float:right!important;}
.slide{
    position: relative;
    width: 483px;
    height: 472px;
    background:#fff;
    overflow: hidden;
}
.imgslide {
    width:100%;
    height:100%;
}
.imgslide li {
    float:left;
}
.imgslide .dots{
    position:absolute;
    bottom:10px;
    left:50%;
    width:80px;
    margin-left:-40px;
}
.imgslide .dots li{
    float:left;
    margin:5px;
    background:#fff;
    width:12px;
    height:12px;
    border-radius:50%;
    color:#fff;
    text-align:center;
    cursor:pointer;
    overflow: hidden;
}
.imgslide .dots li.active{
    background:#6ec559;
    color:#6ec559;
}
.unslider-arrow {
    position: absolute;
    width:33px;
    height:50px;
    top: 45%;
    cursor: pointer;
    z-index:100;
}
.unslider-arrow.prev {
    left: 0;
    background:url(../../static/images/register/slide_l.png) no-repeat center center;
}
.unslider-arrow.prev:hover {
    background:url(../../static/images/register/slide_l_1.png) no-repeat center center;
}
.unslider-arrow.next{
    right:0;
    background:url(../../static/images/register/slide_r.png) no-repeat center center;
}
.unslider-arrow.next:hover{
    background:url(../../static/images/register/slide_r_1.png) no-repeat center center;
}
.hd-login > h1{
    float:left;
    color:#fff;
    font-size:30px;
    font-weight: normal;
}
.form-box{
    position:relative;
    width:290px;
    height: 472px;
    padding:0 40px;
    background:#fff;
    color:#666;
}
.form-box > h2,
.form-box > .tab{
    height:54px;
    line-height:54px;
    margin-bottom:34px;
    font-size:18px;
    font-weight:normal;
    color:#333;
    border-bottom:1px solid #eaeaea;
}
.form-box > .tab > h2{
    float:left;
    width:90px;
    height:53px;
    line-height:53px;
    cursor: pointer;
    font-weight:normal;
    text-align:center;
}
/*.form-box > .tab > h2.active{*/
    /*border-bottom:3px solid #6ec55a;*/
    /*color:#333;*/
/*}*/
.form-group{
    position:relative;
    width:288px;
    height:38px;
    border:1px solid #dedede;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    overflow:hidden;
}
.form-group > label{
    float:left;
    width:72px;
    height:20px;
    line-height:20px;
    margin-top:9px;
    border-right:1px solid #eaeaea;
    text-align:center;
}
.form-group > input{
    float:left;
    width:195px;
    line-height:24px;
    padding:7px 10px;
    border:0;
    line-height:normal\9;
    padding:12px 10px 9px\9;
}
.form-box .form-group.blur,
.form-box  .valcode.blur {
    border-color: #ccc;
}
.form-box .form-group.errorput,
.form-box .valcode.errorput input {
    border-color: #f00;
    box-shadow: 0 0 5px #aa0b0b;
}
.form-group .mobile-register-captcha{
    width:85px;
}
.form-group .captcha{
    cursor: pointer;
}
.marb20{
    margin-bottom:20px;
}
.marb8{
    margin-bottom:8px;
}
.marb38{
    margin-bottom:38px;
}
.verify-code{
    float:left;
    width:180px;
}
.verify-code > input{
    width:87px;
}
.verify-code-btn{
    float:left;
    width:103px;
    margin-left:3px;
    height:38px;
    line-height:38px;
    border:1px solid #dedede;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    background:#f5f5f5;
    color:#666;
    text-align: center;
    cursor: pointer;
}

.form-box .form-group.focus,
.form-box .valcode.error {
    border-color: #6ec558;
    box-shadow: 0 0 5px #6ec558;
}
.auto-box{
    height:18px;
    line-height:18px;
}
.auto-box > label > input{
    vertical-align: sub;
}
.auto-box > label > a{
    color:#6ec559;
}
.btn{
    width:100%;
    height:42px;
    line-height:42px;
    font-size:14px;
    color:#fff;
    border:0;
    cursor:pointer;
}
.btn-green{
    background:#6ec55a;
}
.btn-green:hover{
    background:#5dbf45;
}
.hide{display: none!important;}
.form-p{
    position:absolute;
    left:40px;
    bottom:25px;
}
.form-p > a{
    color:#fa8341;
}
.form-p > a:hover{
    color:#666;
}

</style>
