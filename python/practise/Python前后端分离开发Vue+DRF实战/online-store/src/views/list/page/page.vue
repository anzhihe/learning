<template>
<div>
    <footer class="footer" style="margin-top:30px;">
        <div class="footerK">
            <div class="pageNav" >
                <span v-for="page in apages" @click="pageCallback(page.page)" class="page"  :class="[page.active?'cPageNum':'pageNum']" >
                {{page.text}}
                </span>
            </div>
        </div>
    </footer>  
</div>
</template>
<script>

  export default {
    props:{
      preText:{
        type:String,
        default:'上一页'
      },
      nextText:{
         type:String,
         default:'下一页'
      },
      endShow:{
        type:String,
        default:'false'
      },
      page:[String, Number],
      totalPage:[String, Number]
    },
    methods:{
      nav: function(a, b) {
      var c = [];
      if (1 >= b) return this.pn = this.p = 1, 
        c.push({page:1,text:'1'});
        b < a && (a = b);
        1 >= a ? a = 1 : ( c.push({page:a - 1,text:this.preText}),c.push({page:1,text:"1"}));
        this.p = a;
        this.pn = b;
        var d = 2,
          e = 9 > b ? b : 9;
        7 <= a && (c.push({page:'',text:'...'}), d = a - 4, e = a + 4, e = b < e ? b : e);
        for (; d < a; d++) c.push({page:d,text:d});
        c.push({page:a,text:a,active:true});
        for (d = a + 1; d <= e; d++)c.push({page:d,text:d});
        if (this.endShow=='true') {
          e < b && (c.push({page:b,text:'...'}) , c.push({page:b,text:b}));
        }
        a < b && (c.push({page:a + 1,text:this.nextText}));
        return c
      },
      pageCallback:function(page){
        this.$emit('pagefn',{page:page,totalPage:this.totalPage})
      }
    },
    computed:{
      apages:function(){
        return  this.nav(this.page,parseInt(this.totalPage))
      }
    }
}
</script>
<style lang='scss'>
footer {
  width: 100%;
  height: 60px;
  float: left;
}
.footerK {
  height: 100%;
  margin: 0px auto;
  line-height: 60px;
  text-align: right;
  position: relative;
}
.page{
    border: 1px solid #ddd;
    padding: 8px 12px;
    margin-left: 10px;
    text-align: center;
    cursor:pointer;
    &:hover{
        color:#09c762;
        border-color:#09c762;

    }
}
.footerK a,
.cPageNum {
  line-height: 35px;
  font-size: 12px;

  color: #939393;
  border: none;
  tencursor: pointer;
}
.cPageNum {
  color: #333333;
  font-weight: bold;

}
.footerK a:hover {
  color: #fff;
  background: #68a0fc;
}
</style>
