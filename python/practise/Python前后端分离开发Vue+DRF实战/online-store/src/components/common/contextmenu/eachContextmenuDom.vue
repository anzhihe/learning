<template>
    <div>
        <ul class="contextMenuPlugin">
            <li v-for="(m,index) in items" :key="index">
                <a>
                    <i class="iconfont" v-if="m.icon" v-html="m.icon"></i>
                    <span>{{m.label}}</span>
                    <i class="iconfont right" v-if="m.items">&#xe649;</i>
                </a>
                <solt></solt>
            </li>
        </ul>
    </div>
</template>
<script type="text/javascript">
  export default {
    props:{
      items:Object
    }
  }
</script>