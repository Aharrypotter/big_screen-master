function echarts_31() {
  // 基于准备好的dom，初始化echarts实例
  var echarts_31 = echarts.init(document.getElementById("fb1"));
  option = {
    tooltip: {
      trigger: "item",
      formatter: "{b}: {c} ({d}%)",
      position: function (p) {
        //其中p为当前鼠标的位置
        return [p[0] + 10, p[1] - 10];
      },
    },
    legend: {
      top: "0%",
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12",
      },
    },
    series: [
      {
        name: "当前图书馆在馆人数情况",
        type: "pie",
        color: [
          "#065aab",
          "#066eab",
          "#0682ab",
          "#0696ab",
          "#06a0ab",
          "#06b4ab",
          "#06c8ab",
          "#06dcab",
          "#06f0ab",
        ],
        label: {
          show: true, // 显示标签
          position: "inside", // 标签显示在饼图内部
          formatter: "{b}:{c}({d}%)", // 设置标签的显示格式
          textStyle: {
            color: "rgba(255,255,255,.5)", // 标签文字颜色
            fontSize: "14",
          },
        },
        labelLine: { show: false },
      },
    ],
  };
  // 使用刚指定的配置项和数据显示图表。
  echarts_31.setOption(option);
  window.addEventListener("resize", function () {
    echarts_31.resize();
  });
}
function updateChart_31() {
  // 发起异步请求获取数据
  $.get("/api/library_stats").done(function (data) {
    // 根据获取的数据更新图表的配置项和数据
    var option = {
      // 更新x轴数据
      legend: {
        data: data.xAxis,
      },
      // 更新数据系列
      series: [
        {
          data: data.data,
        },
      ],
    };
    // 将更新后的配置项设置给图表
    echarts_31.setOption(option);
  });
}

function echarts_32() {
  var echarts_32 = echarts.init(document.getElementById("fb2"));
  option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    grid: {
      top: "10%",
      left: "3%",
      right: "3%",
      bottom: "3%", //调整边距，使柱状图能够更好地占据块内的空间
      containLabel: true,
    },
    yAxis: {
      type: "value",
      axisLine: {
        lineStyle: {
          color: "rgba(255,255,255,.5)",
        },
      },
      axisLabel: {
        textStyle: {
          color: "rgba(255,255,255,.5)",
          fontSize: "12",
        },
      },
      splitLine: {
        lineStyle: {
          color: "rgba(255,255,255,.1)",
        },
      },
    },
    legend: {
      // top:'0%',
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12",
      },
    },
    xAxis: {
      type: "category",
      axisLine: {
        lineStyle: {
          color: "rgba(255,255,255,.5)",
        },
      },
      axisLabel: {
        textStyle: {
          show: true,
          color: "rgba(255,255,255,.5)",
          fontSize: "12",
        },
      },
    },
    series: [
      {
        name: "{{form.echarts3_2.title}}",
        type: "bar",
        barWidth: "100%", //柱子宽度
        // barGap: 1, //柱子之间间距
        itemStyle: {
          color: function (params) {
            // 定义基准颜色
            var baseColor1 = "#087a73";
            var baseColor2 = "#6a1479";
            // 生成颜色插值器
            var colorInterpolator = chroma
              .scale([baseColor1, baseColor2])
              .mode("lch")
              .colors(10);
            // 定义颜色数组
            var colorList = colorInterpolator.map(function (color) {
              return color;
            });
            return colorList[params.dataIndex % colorList.length];
          },
        },
        label: {
          show: true, // 显示标签
          position: "outside", // 标签显示在直方图外部
          formatter: "{b}", // 设置标签的显示格式
          textStyle: {
            color: "rgba(255,255,255,.5)", // 标签文字颜色
            fontSize: "12",
          },
        },
      },
    ],
  };
  echarts_32.setOption(option);
  window.addEventListener("resize", function () {
    echarts_32.resize();
  });
}
function updateChart_32() {
  // 发起异步请求获取数据
  $.get("/api/dept_inlib").done(function (data) {
    // 根据获取的数据更新图表的配置项和数据
    var option = {
      // 更新x轴数据
      legend: {
        data: data.xAxis,
      },
      xAxis: {
        data: data.data,
      },
      // 更新数据系列
      series: [
        {
          data: data.data,
        },
      ],
    };
    // 将更新后的配置项设置给图表
    echarts_32.setOption(option);
  });
}

function echarts_4() {
  // 基于准备好的dom，初始化echarts实例
  var echarts_4 = echarts.init(document.getElementById("echart4"));
  option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        lineStyle: {
          color: "#dddc6b",
        },
      },
      formatter: function (params) {
        var result = params[0].name + "<br/>"; // x轴数据
        for (var i = 0; i < params.length; i++) {
          var seriesName = params[i].seriesName; // 系列名称
          var value = params[i].value; // 数据值
          result += seriesName + ": " + value + "%<br/>"; // 拼接每个系列的名称和数据值
        }
        return result;
      },
    },
    grid: {
      left: "10",
      top: "30",
      right: "10",
      bottom: "10",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12,
          },
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.2)",
          },
        },
      },
      {
        axisPointer: { show: false },
        axisLine: { show: false },
        position: "bottom",
        offset: 20,
      },
    ],
    yAxis: [
      {
        type: "value",
        min: 0, // 设置最小值为0
        max: 100, // 设置最大值为100
        axisTick: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)",
          },
        },
        axisLabel: {
          formatter: "{value}%", // 设置刻度标签的格式为百分比形式
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12,
          },
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)",
          },
        },
      },
    ],
    legend: {
      right: "0%",
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12",
      },
    },
    series: [
      {
        name: "时段在馆人数/总座位数",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#0184d5",
            width: 2,
          },
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                {
                  offset: 0,
                  color: "rgba(1, 132, 213, 0.4)",
                },
                {
                  offset: 0.8,
                  color: "rgba(1, 132, 213, 0.1)",
                },
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)",
          },
        },
        itemStyle: {
          normal: {
            color: "#0184d5",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12,
          },
        },
        label: {
          show: true, // 显示标签
          position: "top", // 标签位置，默认值是 'top'
          formatter: "{c}%", // 标签格式化函数，这里表示显示数据值并加上百分号
          textStyle: {
            color: "rgba(255, 255, 255, .7)", // 标签文字颜色
            fontSize: 12, // 标签文字字号
          },
        },
      },
    ],
  };
  // 使用刚指定的配置项和数据显示图表。
  echarts_4.setOption(option);
  window.addEventListener("resize", function () {
    echarts_4.resize();
  });
}
function updateChart_4() {
  // 发起异步请求获取数据
  $.get("/api/hourly_utilization").done(function (data) {
    // 根据获取的数据更新图表的配置项和数据
    var option = {
      // 更新x轴数据
      legend: {
        data: data.xAxis,
      },
      xAxis: {
        data: data.data,
      },
      // 更新数据系列
      series: [
        {
          data: data.data,
        },
      ],
    };
    // 将更新后的配置项设置给图表
    echarts_4.setOption(option);
  });
}
