<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
        <div class="box">
            <div class="box_1">
                <div class="userCenterBox boxCenterList clearfix" style="_height:1%; font-size:14px;">
                    <h5><span>我的留言</span></h5>
                    <div class="blank"></div>
                    <div class="blank"></div>
                    <div class="message-all">
                        <ul>
                            <li v-for="(item,index) in messageAll">
                                <div>
                                    <span v-if="item.message_type===1">留言：</span>
                                    <span v-if="item.message_type===2">投诉：</span>
                                    <span v-if="item.message_type===3">询问：</span>
                                    <span v-if="item.message_type===4">售后：</span>
                                    <span v-if="item.message_type===5">求购：</span>
                                    <span>{{item.subject}}</span>
                                    <span>（{{item.add_time}}）</span>
                                </div>
                                <div>
                                  {{item.message}}
                                </div>
                                <div>
                                    <a @click="deleteMessage(index, item.id)">删除</a>
                                    <a :href="(item.file)">查看上传的文件</a>

                                </div>

                            </li>
                        </ul>
                    </div>
                    <form action="" method="post" enctype="multipart/form-data" name="formMsg">
                        <table width="100%" border="0" cellpadding="3">
                            <tbody><tr>
                                <td align="right">留言类型：</td>
                                <td>
                                    <input type="radio" id="one" value="1" v-model="message_type">
                                    <label for="one">留言</label>
                                    <input type="radio" id="two" value="2" v-model="message_type">
                                    <label for="two">投诉</label>
                                    <input type="radio" id="three" value="3" v-model="message_type">
                                    <label for="three">询问</label>
                                    <input type="radio" id="four" value="4" v-model="message_type">
                                    <label for="four">售后</label>
                                    <input type="radio" id="five" value="5" v-model="message_type">
                                    <label for="five">求购</label>

                                    <!-- <input name="msg_type" type="radio" value="0" checked="checked">
                                    留言                        <input type="radio" name="msg_type" value="1">
                                    投诉                        <input type="radio" name="msg_type" value="2">
                                    询问                        <input type="radio" name="msg_type" value="3">
                                    售后                        <input type="radio" name="msg_type" value="4">
                                    求购 -->
                                </td>
                            </tr>
                            <tr>
                                <td align="right">主题：</td>
                                <td><input name="msg_title" type="text" size="30" class="inputBg" v-model="subject"></td>
                            </tr>
                            <tr>
                                <td align="right" valign="top">留言内容：</td>
                                <td><textarea name="msg_content" cols="50" rows="4" wrap="virtual" class="B_blue" v-model="message"></textarea></td>
                            </tr>
                            <tr>
                                <td align="right">上传文件：</td>
                                <td><input type="file" name="message_img" size="45" class="inputBg" @change="preview"></td>
                            </tr>
                            <tr>
                                <td>&nbsp;</td>
                                <td><input type="hidden" name="act" value="act_add_message">
                                    <!-- <input type="submit" value="提 交" class="bnt_bonus"> -->
                                    <a class="btn_blue_1" @click="submitMessage">提交</a>
                                </td>
                            </tr>
                            <tr>
                                <td>&nbsp;</td>
                                <td>
                                    <font color="red">小提示：</font><br>
                                    您可以上传以下格式的文件：<br>gif、jpg、png、word、excel、txt、zip、ppt、pdf                      </td>
                            </tr>
                            </tbody></table>
                    </form>


                </div>
            </div>
        </div>
    </div>

  </div>
</template>
<script>
  import {getMessages, addMessage, delMessages} from '../../api/api'
    export default {
        data () {
            return {
                message_type: '', // 留言类型
                subject: '', // 留言主题
                message: '', // 留言内容
                file: '',
                // 上传文件没做
                messageAll: [
                    // {
                    //     id: 1234,
                    //     message_type: 1,
                    //     theme: '留言主题',
                    //     message: '留言内容',
                    //     time: '2017-07-19 21:20:25',
                    // },
                    // {
                    //     id: 5678,
                    //     message_type: 2,
                    //     theme: '留言主题',
                    //     message: '留言内容',
                    //     time: '2017-07-19 21:20:25',
                    // }
                ]
            };
        },
        props: {

        },
        components: {

        },
        created () {
            this.getMessage();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            preview (e) {
                this.file = e.target.files[0]; //获取文件资源
                console.log(this.file);

            },
            submitMessage () { //提交留言
                const formData = new FormData();
                formData.append('file',this.file);
                formData.append('subject',this.subject);
                formData.append('message',this.message);
                formData.append('message_type',this.message_type);
                addMessage(formData).then((response)=> {
                    this.getMessage();

                }).catch(function (error) {
                    console.log(error);
                });
            },
            getMessage () { //获取留言
              getMessages().then((response)=> {
                    console.log(response.data);
                    this.messageAll = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            deleteMessage (index, id) { // 删除留言
                delMessages(id).then((response)=> {
                  alert("删除成功")
                  this.messageAll.splice(index,1);
                }).catch(function (error) {
                    console.log(error);
                });
            },
        }
    }
</script>
<style scoped>
.message-all {
    border-bottom: 1px solid #ccc;
}
.message-all  li{
    border-bottom: 1px solid #ddd;
    padding: 10px;
}

.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.ilizi_centre {
    background:0
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
