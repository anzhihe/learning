<template>
    <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
            <div class="box">
                <div class="box_1">
                    <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                        <h5><span>收货人信息</span></h5>
                        <div class="blank"></div>
                        <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd" v-for="(item, index) in receiveInfoArr">
                            <tbody>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">配送区域：</td>
                                    <td colspan="3" align="left" bgcolor="#ffffff">
                                        <div class="addr" @click="bubble(index)">
                                            <v-distpicker :province="item.province" :city="item.city" :area="item.district" @province="updateProvince"  @city="updateCity" @area="updateArea"></v-distpicker>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">收货人姓名：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="consignee" type="text" class="inputBg" id="consignee_0" value="ssss" v-model="item.signer_name">
                                        <span :class = "{error:item.signer_name==''}">(必填)</span>
                                        </td>

                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">详细地址：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="address" type="text" class="inputBg" id="address_0" v-model="item.address">
                                        <span :class = "{error:item.address==''}">(必填)</span></td>
                                </tr>
                                <tr>

                                    <td align="right" bgcolor="#ffffff">手机：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="mobile" type="text" class="inputBg" id="mobile_0" v-model="item.signer_mobile"><span :class = "{error:item.signer_mobile==''}">(必填)</span></td>
                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">&nbsp;</td>
                                    <td colspan="3" align="center" bgcolor="#ffffff">
                                    <!-- <input type="submit" name="submit" class="bnt_blue_2" value="新增收货地址"> -->

                                    <button class="bnt_blue_2" @click="confirmUpdate(item.id, index)">确定修改</button>
                                    <button class="bnt_blue_2" @click="deleteInfo(item.id)">删除</button>
                                    <!-- <input type="hidden" name="act" value="act_edit_address">
                                    <input name="address_id" type="hidden" value="320"> -->
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                            <tbody>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">配送区域：</td>
                                    <td colspan="3" align="left" bgcolor="#ffffff">
                                        <div class="addr">
                                            <!-- <v-distpicker :placeholder="newInfo.dist" @province="getProvince" @city="getCity" @selected="getArea"></v-distpicker> -->
                                            <v-distpicker :province="newInfo.province" :city="newInfo.city" :area="newInfo.district" @province="getProvince" @city="getCity" @area="getArea"></v-distpicker>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">收货人姓名：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="consignee" type="text" class="inputBg" id="consignee_0" value="ssss" v-model="newInfo.signer_name">
                                        <span :class = "{error:newInfo.signer_name==''}">(必填)</span> </td>

                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">详细地址：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="address" type="text" class="inputBg" id="address_0" v-model="newInfo.address">
                                       <span :class = "{error:newInfo.address==''}">(必填)</span></td>
                                </tr>
                                <tr>

                                    <td align="right" bgcolor="#ffffff">手机：</td>
                                    <td align="left" bgcolor="#ffffff"><input name="mobile" type="text" class="inputBg" id="mobile_0" v-model="newInfo.signer_mobile"><span :class = "{error:newInfo.signer_mobile==''}">(必填)</span></td>
                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">&nbsp;</td>
                                    <td colspan="3" align="center" bgcolor="#ffffff">
                                    <!-- <input type="submit" name="submit" class="bnt_blue_2" value="新增收货地址"> -->
                                    <button class="bnt_blue_2" @click="addReceive">新增收货地址</button>

                                    <!-- <input type="hidden" name="act" value="act_edit_address">
                                    <input name="address_id" type="hidden" value="320"> -->
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import VDistpicker from 'v-distpicker'
import {getAddress, addAddress, updateAddress, delAddress} from '../../api/api'
    export default {
        data () {
            return {
                updateIndex: '',
                newInfoEmpty: {
                    province: '', //省
                    city: '', // 市
                    area: '', // 区
                    receiveName: '', // 收件人姓名
                    addr: '', // 详细地址
                },
                newInfo: {
                    province: '', //省
                    city: '', // 市
                    area: '', // 区
                    receiveName: '', // 收件人姓名
                    addr: '', // 详细地址
                    phone:''
                },
                receiveInfoArr: [
                    // {
                    //     id: '',
                    //     province: '', //省
                    //     city: '', // 市
                    //     area: '', // 区
                    //     receiveName: '', // 收件人姓名
                    //     addr: '', // 详细地址
                    // }
                ]


            };
        },
        props: {

        },
        components: {
            'v-distpicker': VDistpicker
        },
        created () {
            this.getReceiveInfo();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            bubble (index) {
                this.currentIndex = index;
            },
            updateProvince (data) {
                this.receiveInfoArr[this.currentIndex].province = data.value;
            },
            updateCity (data) {
                this.receiveInfoArr[this.currentIndex].city = data.value;
            },
            updateArea (data) {
                this.receiveInfoArr[this.currentIndex].district = data.value;
            },


            getProvince (data) {
                this.newInfo.province = data.value;
            },
            getCity (data) {
                this.newInfo.city = data.value;
            },
            getArea (data) {
                this.newInfo.district = data.value;
            },
            getReceiveInfo() { //获取收件人信息
                getAddress().then((response)=> {
                    console.log(response.data);
                    this.receiveInfoArr = response.data;

                }).catch(function (error) {
                    console.log(error);
                });

            },

            addReceive () { //提交收获信息
                addAddress(this.newInfo).then((response)=> {
                    alert('添加成功');
                    // 重置新的
                    this.getReceiveInfo();
                    this.newInfo = Object.assign({}, this.newInfoEmpty);

                }).catch(function (error) {
                    console.log(error);
                });
            },
            confirmUpdate (id, index) { // 更新收获信息
                updateAddress(id, this.receiveInfoArr[index]).then((response)=> {
                    alert('修改成功');
                    this.getReceiveInfo();
                }).catch(function (error) {
                    console.log(error);
                });

            },
            deleteInfo (id, index) { // 删除收获人信息
                delAddress(id).then((response)=> {
                    alert('删除成功');
                    this.getReceiveInfo();
                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
<style scoped>
.error{
  color:#fa8341;
}
table {
    margin-bottom: 20px;
}
select {
    min-width: 80px;
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
.bnt_blue_1,.bnt_blue,.bnt_bonus,.bnt_blue_2 {
    display:inline-block;
    padding:4px 12px;
    height:24px;
    line-height:16px;
    _line-height:18px;
    border:1px solid #1e9246;
    border-radius:3px;
    font-size:100%;
    color:#fff;
    background-color:#09c762;
    overflow:hidden;
    vertical-align:middle;
    cursor:pointer
}


</style>
<style type="text/css">
    .addr .address {
        height: 35px;
    }
    .addr .address select{
        height: inherit;
        font-size: inherit;
        border-radius: initial;
        width: 130px;
        padding:0
    }
</style>
