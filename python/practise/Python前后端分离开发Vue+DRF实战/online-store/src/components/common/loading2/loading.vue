<template>
 <div class="pio-loading2" v-if="flag">
  	<div class="demo-spin-container">
        <Spin fix size="large"></Spin>
    </div>
 </div>
</template>
<script>
    export default {
        
    }
</script>
<style scoped>
	.pio-loading2 {
	  width: 100%;
	  height: 100%;
	  position: absolute;
	  top: 0px;
	  left: 0px;
	  z-index: 9999999;
	}
	.demo-spin-container{
    	display: inline-block;
        width: 100%;
        height: 100%;
        position: relative;
    }
</style>