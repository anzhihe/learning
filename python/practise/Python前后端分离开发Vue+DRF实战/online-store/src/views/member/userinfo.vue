<template>

    <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
            <div class="box">
                <div class="box_1">
                    <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                        <h5><span>个人资料</span></h5>
                        <div class="blank"></div>
                        <form name="formEdit" action="" method="post" >
                            <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                                <tbody>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">姓名： </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input name="email" type="text" placeholder="" size="25" class="inputBg" v-model="userInfo.name"></td>
                                    </tr>
                                    <tr>
                                        <td width="28%" align="right" bgcolor="#FFFFFF">出生日期： </td>
                                        <td width="72%" align="left" bgcolor="#FFFFFF">
                                            <datepicker language="ch"  v-model="userInfo.birthday"></datepicker>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td width="28%" align="right" bgcolor="#FFFFFF">性　别： </td>
                                        <td width="72%" align="left" bgcolor="#FFFFFF">
                                            <input type="radio" id="male" value="male" v-model="userInfo.gender">
                                            <label for="male">男</label>
                                            <input type="radio" id="female" value="female" v-model="userInfo.gender">
                                            <label for="female">女</label>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td width="28%" align="right" bgcolor="#FFFFFF">电子邮件地址： </td>
                                        <td width="72%" align="left" bgcolor="#FFFFFF"><input name="email" type="text" placeholder="xxxx@xx.com" size="25" class="inputBg" v-model="userInfo.email"></td>
                                    </tr>
                                    <tr>
                                        <td width="28%" align="right" bgcolor="#FFFFFF" id="extend_field5i">手机：</td>
                                        <td width="72%" align="left" bgcolor="#FFFFFF">
                                            <input disabled name="extend_field5" type="text" class="inputBg" v-model="userInfo.mobile"><span style="color:#FF0000"> *</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" align="center" bgcolor="#FFFFFF">
                                            <!-- <input name="act" type="hidden" value="act_edit_profile"> -->
<!--                                            <button class="btn_blue_1" style="border:none;" @click="getUserInfo()">确认修改</button>-->
                                          <span name="submit" type="submit" value="确认修改" @click="confirmModify()" class="btn_blue_1" style="border:none;">确认修改</span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import datepicker from 'vue-date'
import {getUserDetail, updateUserInfo} from '../../api/api'
    export default {
        data () {
            return {
                userInfo: {
                    birthday: '',
                    sex: '',
                    email: '',
                    phone: '',
                }
            };
        },
        props: {

        },
        components: {
            datepicker
        },
        created () {
            this.getUserInfo();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            getUserInfo () { //请求用户信息
              getUserDetail().then((response)=> {
                    this.userInfo = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            confirmModify () { // 确认修改
                updateUserInfo(this.userInfo).then((response)=> {
                    alert('修改成功');
                }).catch(function (error) {
                    console.log(error);
                    alert('修改出错！')
                });
            }
        }
    }
</script>
<style scoped>



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
.btn_blue_1{
  display: inline-block;
  padding: 4px 12px;
  height: 24px;
  line-height: 25px;
  _line-height: 18px;
  border: 1px solid #1e9246;
  border-radius: 3px;
  font-size: 100%;
  color: #fff;
  background-color: #09c762;
  overflow: hidden;
  vertical-align: middle;
  cursor: pointer;
  text-decoration: none;
  vertical-align: middle;
}




</style>




