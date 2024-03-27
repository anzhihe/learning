<template>
    <div v-show="flag" class="pio-nodata">
    	<div  :class="newSize">
    		<img :src="img" alt="">
    		<div class="pio-nodata-text" :style="{fontSize:fontSize+'px'}">{{text}}</div>
    	</div>
    </div>
</template>
<script>
	export default {      
    }
</script>
<style scoped>
	.pio-nodata{width:100%;height:100%;position:absolute;text-align:center;top:0;left:0;background:#fff}
	.pio-nodata .pio-nodata-content{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}
	.pio-nodata .pio-nodata-sm{width:200px}
	.pio-nodata .pio-nodata-md{width:350px}
	.pio-nodata .pio-nodata-lg{width:500px}
	.pio-nodata .pio-nodata-content img{width:100%}
	.pio-nodata .pio-nodata-text{width:100%;position:absolute;left:0;bottom:10px;text-align:center;color:#666}
</style>