  $.ajax({
         url: '/bar_data',
         type: 'post',
         dataType: 'json',
          async:true,
         success : function(result) {
             console.log(result)
             if (result)
             { //把result(即Json数据)以参数形式放入Echarts代码中
                bind(result);
             }
             },
         error : function(errorMsg) { alert("加载数据失败"); }

     });

    // 基于准备好的dom，初始化echarts实例
    //var myChart1 = echarts.init(document.getElementById('main1'));
    var myChart2 = echarts.init(document.getElementById('main3'));
    var myChart3 = echarts.init(document.getElementById('main2'));
    var myChart4 = echarts.init(document.getElementById('main4'));
    //var myChart5 = echarts.init(document.getElementById('main5'));
function bind(result) {
    var myChart1 = echarts.init(document.getElementById('main1'));
    myChart1.showLoading()
    var option1 = {
            title : {
                text: '绕线机故障主要原因历史数据统计',
                subtext: '近30天数据统计',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient : 'vertical',
                x : 'left',
                data:['利用率','停机时间']
            },
           toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            series : [
                {
                    name:'访问来源',
                    type:'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[
                        {value:335, name:'利用率'},
                        {value:310, name:'停机时间'},

                    ]
                }
            ]
    };

    myChart1.setOption(option1);
    myChart1.hideLoading()

}

        var   option2 = {
                title : {
                    text: '电机温度监测',
                    subtext: '模拟数据'
                },
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:['1号电机','2号电机']
            },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : ['0:00','3:00','6:00','9:00','12:00','15:00','18:00','21:00']
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    axisLabel : {
                        formatter: '{value} °C'
                    }
                }
            ],
            series : [
                {
                    name:'1号电机',
                    type:'line',
                    data:[11, 11, 15, 13, 12, 13, 10,14],
                    markPoint : {
                        data : [
                            {type : 'max', name: '最大值'},
                            {type : 'min', name: '最小值'}
                        ]
                    },
                    markLine : {
                        data : [
                            {type : 'average', name: '平均值'}
                        ]
                    }
                },
                {
                    name:'2号电机',
                    type:'line',
                    data:[3, 5, 1, 4, 3, 2, 0,6],
                    markPoint : {
                        data : [
                            {name : '周最低', value : -2, xAxis: 1, yAxis: -1.5}
                        ]
                    },
                    markLine : {
                        data : [
                            {type : 'average', name : '平均值'}
                        ]
                    }
                }
            ]
        };




        var   option3 = {
            title : {
                text: '绕线机故障主要原因历史数据统计',
                subtext: '近30天数据统计',
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient : 'vertical',
                x : 'left',
                data:['自动上下料机构','张力器','运动控制器','主轴箱','压线机构']
            },
           toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            series : [
                {
                    name:'访问来源',
                    type:'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:[
                        {value:335, name:'自动上下料机构'},
                        {value:310, name:'张力器'},
                        {value:234, name:'运动控制器'},
                        {value:135, name:'主轴箱'},
                        {value:1548, name:'压线机构'}
                    ]
                }
            ]
        };
