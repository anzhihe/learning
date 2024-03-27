<template>
    <div class="line_bar-warp" :id="id">

    </div>
</template>
<script type="text/javascript">
    var Highcharts = require('highcharts');
    export default {
        props:{
            id:String,
            data:Object
        },
        mounted(){

    },
    methods:{
        drawChart(data){
            var thisId = this.id;
           // var data = this.data;
           // this.$nextTick(function(){
                //加载vps信息
                Highcharts.chart(thisId,{
                           chart: {
                                plotBackgroundColor: null,
                                plotBorderWidth: null,
                                plotShadow: false
                            },
                            title:false,
                            tooltip: {
                                headerFormat: '{series.name}<br>',
                                pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
                            },
                            credits:{
                                 enabled:false // 禁用版权信息
                            },
                            plotOptions: {
                                pie: {
                                    allowPointSelect: true,
                                    cursor: 'pointer',
                                    dataLabels: {
                                        enabled: false
                                    },
                                    showInLegend: true
                                }
                            },
                            series: [{
                                type: 'pie',
                                data: data
                            }]
                })
        }
    }
}
</script>
<style type="text/css">
    .line_bar-warp{
        width:100%;
        height:100%;
        padding:10px;
    }
</style>