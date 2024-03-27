<template>
    <div class="line_bar-warp" :id="id">

    </div>
</template>
<script type="text/javascript">
    var Highcharts = require('highcharts');
    export default {
        name:'line_bar',
        props:{
            id:String,
            data:Object
        },
        methods:{
            drawChart:function(data){
                var thisId = this.id;
                //var data = this.data;
                //this.$nextTick(function(){
                //加载vps信息
                Highcharts.chart(thisId,{
                    chart: {
                                type: 'bar'
                            },
                    title: false,
                    xAxis: {
                        categories: data.y
                    },
                    yAxis:{
                        title:{
                            enabled:false
                        }
                    },
                    series: [{
                        data: data.x,
                        color:'#4690cd'
                    }],
                    credits:{
                         enabled:false // 禁用版权信息
                    },
                    legend:false,
                    plotOptions: {
                        bar: {
                                dataLabels: {
                                    enabled: true,
                                    allowOverlap: true
                                }
                            }
                    },
                    responsive: {
                        rules: [{
                            condition: {
                                maxWidth: 500
                            },
                            // Make the labels less space demanding on mobile
                            chartOptions: {
                                xAxis: {
                                     title: false
                                },
                                yAxis: false
                            }
                        }]
                    }
                })
           // }
        }
    }
}
</script>
<style type="text/css">
    .line_bar-warp{
        width:100%;
        height:100%;
        padding:0 20px;
    }
</style>
