<template>

<div class="slidebar">
    <h3 class="my_nala">
        <a @click="member">会员中心</a>
    </h3>
    <ul class="slide_item">
        <li class="item">
            <div class="root_node"><i class="iconfont">&#xe645;</i>订单中心</div>
            <ul>
                <li>
                    <a :class="{on: current==='order'}" @click="toOrder">我的订单</a>
                    <a :class="{on: current==='receive'}"  @click="toReceive">收货地址</a>
                </li>
            </ul>
        </li>
        <li class="item">
            <div class="root_node"><i class="iconfont">&#xe645;</i>会员中心</div>
            <ul>
                <li>
                    <a :class="{on: current==='userinfo'}" @click="toUserInfo">用户信息</a>
                    <a :class="{on: current==='collection'}" @click="toCollection">我的收藏</a>
                    <a :class="{on: current==='message'}" @click="toMessage">我的留言</a>
                </li>
            </ul>
        </li>
    </ul>
</div>
</template>
<script>

    export default {
        data () {
            return {
                current: 'userinfo'
            };
        },
        props: {
            
        },
        created () {

            var temp = this.$route.path.split('/');
            this.current = temp[temp.length - 1];


        },
        watch: {
            
        },
        computed: {

        },
        methods: {
            member () { // 会员中心
                this.$router.push({name: 'member'});
            },
            toOrder () {  // 我的订单
                this.current = 'order';
                this.$router.push({name: 'order'});
            },
            toReceive () { // 收货地址
                this.current = 'receive';
                this.$router.push({name: 'receive'});
            },
            toUserInfo () { // 用户信息
                this.current = 'userinfo';
                this.$router.push({name: 'userinfo'});
            },
            toCollection () { //我的收藏
                this.current = 'collection';
                this.$router.push({name: 'collection'});
            },
            toMessage () { //我的留言
                this.current = 'message';
                this.$router.push({name: 'message'});
            }
        }
    }
</script>
<style scoped>



.slidebar {
    float:left;
    width:214px
}
.slidebar .slide_item {
+zoom:1;
    border:1px solid #e7e7e7;
    border-bottom:0;
    margin-bottom:10px;
    background-color:#fff
}
.slidebar .root_node {
    border-bottom:solid 1px #e7e7e7;
    padding:14px 0 14px 14px;
    font-size:14px
}
.slidebar .root_node i {
    color:#ccc;
    margin-right:8px;
    font-size:12px
}
.slidebar .item ul {
    border-bottom:solid 1px #e7e7e7
}
.slidebar li {
    margin-bottom:1px
}
.slidebar li a {
    display:block;
    height:20px;
    line-height:20px;
    padding:10px 0 10px 40px;
    color:#111
}
.slidebar li a i {
    font-size:18px;
    color:#999;
    margin-right:6px
}
.slidebar li a:hover,.slidebar li a.on {
    background-color:#f1f1f1;
    color:#09c762;
    text-decoration:none
}
.slidebar li a:hover i,.slidebar li a.on i {
    color:#09c762;
    -webkit-animation:pop_ico .5s
}
.slidebar .root_item {
    border-bottom:solid 1px #e7e7e7
}
.slidebar .root_item a {
    font-size:14px;
    padding:14px 0 14px 15px
}
.slidebar .root_item a i {
    font-size:22px
}

h3.my_nala {
    height:60px;
    border:1px solid #e7e7e7;
    border-bottom:0
}
 h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
 h3.my_nala a:hover {
    text-decoration:none
}

</style>
