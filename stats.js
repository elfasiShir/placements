var app = {};

var chartDom = document.getElementById("main");
var myChart = echarts.init(chartDom);
var option;

const posList = [
  "left",
  "right",
  "top",
  "bottom",
  "inside",
  "insideTop",
  "insideLeft",
  "insideRight",
  "insideBottom",
  "insideTopLeft",
  "insideTopRight",
  "insideBottomLeft",
  "insideBottomRight",
];
app.configParameters = {
  rotate: {
    min: -90,
    max: 90,
  },
  align: {
    options: {
      left: "left",
      center: "center",
      right: "right",
    },
  },
  verticalAlign: {
    options: {
      top: "top",
      middle: "middle",
      bottom: "bottom",
    },
  },
  position: {
    options: posList.reduce(function (map, pos) {
      map[pos] = pos;
      return map;
    }, {}),
  },
  distance: {
    min: 0,
    max: 100,
  },
};
app.config = {
  rotate: 90,
  align: "left",
  verticalAlign: "middle",
  position: "insideBottom",
  distance: 15,
  onChange: function () {
    const labelOption = {
      rotate: app.config.rotate,
      align: app.config.align,
      verticalAlign: app.config.verticalAlign,
      position: app.config.position,
      distance: app.config.distance,
    };
    myChart.setOption({
      series: [
        {
          label: labelOption,
        },
        {
          label: labelOption,
        },
        {
          label: labelOption,
        },
        {
          label: labelOption,
        },
      ],
    });
  },
};
const labelOption = {
  show: true,
  position: app.config.position,
  distance: app.config.distance,
  align: app.config.align,
  verticalAlign: app.config.verticalAlign,
  rotate: app.config.rotate,
  formatter: "{c}  {name|{a}}",
  fontSize: 13,
  rich: {
    name: {},
  },
};
option = {
  color: [
    "#b5e48c",
    "#99d98c",
    "#76c893",
    "#52b69a",
    "#34a0a4",
    "#168aad",
    "#1a759f",
    "#1e6091",
  ],
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow",
    },
  },
  legend: {
    data: ["CSE", "ECE", "EEE", "MECH", "CIV", "CHE"],
  },
  toolbox: {
    show: true,
    orient: "vertical",
    left: "right",
    top: "center",
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ["line", "bar", "stack"] },
      restore: { show: true },
      saveAsImage: { show: true },
    },
  },
  xAxis: [
    {
      type: "category",
      axisTick: { show: false },
      data: ["Infosys", "Deloitte", "Napier", "fanatics", "Amazon"],
    },
  ],
  yAxis: [
    {
      type: "value",
      offset: 1.5,
      name: "Students Placed",
      nameLocation: "middle",
      nameTextStyle: {
        padding: [22, 22, 22, 22],
      },
    },
  ],
  series: [
    {
      name: "CSE",
      type: "bar",
      barGap: 0,
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [9, 3, 0, 2, 7, 5, 1, 6],
    },
    {
      name: "ECE",
      type: "bar",
      barGap: 0,
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [1, 7, 5, 18, 3, 19, 10, 4],
    },
    {
      name: "EEE",
      type: "bar",
      barGap: 0,
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [3, 1, 4, 2, 5, 2, 3],
    },
    {
      name: "MECH",
      type: "bar",
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [10, 13, 11, 14, 17, 16, 19, 15],
    },
    {
      name: "CIV",
      type: "bar",
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [16, 10, 18, 11, 19, 7, 9, 6],
    },
    {
      name: "CHE",
      type: "bar",
      label: labelOption,
      emphasis: {
        focus: "series",
      },
      data: [6, 17, 9, 10, 12, 5, 7, 16],
    },
  ],
};

option && myChart.setOption(option);

function branchStats(){
  var branch=document.getElementById("branchSelect").value;
  var students=document.getElementById("students");
  var companies=document.getElementById("companies");
  var highctc=document.getElementById("highctc");
  var lowctc=document.getElementById("lowctc");
  var avgctc=document.getElementById("avgctc");
  if(branch == 'CSE'){
    students.innerHTML="65";
    companies.innerHTML="Infosis, Deloitte, Amazon";
    highctc.innerHTML="16 LPA";
    lowctc.innerHTML="4 LPA";
    avgctc.innerHTML="7 LPA";
  }
  else if(branch == 'ECE'){
    students.innerHTML="55";
    companies.innerHTML="Napier, Deloitte, Amazon";
    highctc.innerHTML="13 LPA";
    lowctc.innerHTML="3 LPA";
    avgctc.innerHTML="5 LPA";
  }
  else if(branch == 'EEE'){
    students.innerHTML="49";
    companies.innerHTML="Infosis, Amazon, Fanatics";
    highctc.innerHTML="10 LPA";
    lowctc.innerHTML="3 LPA";
    avgctc.innerHTML="4.5 LPA";
  }
  else if(branch == 'MECH'){
    students.innerHTML="35";
    companies.innerHTML="Deloitte, Fanatics";
    highctc.innerHTML="8 LPA";
    lowctc.innerHTML="2 LPA";
    avgctc.innerHTML="3.5 LPA";
  } 
  else if(branch == 'CIVIL'){
    students.innerHTML="29";
    companies.innerHTML="Napier, Deloitte";
    highctc.innerHTML="8 LPA";
    lowctc.innerHTML="2 LPA";
    avgctc.innerHTML="2.5 LPA";
  }
  else if(branch == 'CHEM'){
    students.innerHTML="20";
    companies.innerHTML="Fanatics, Napier";
    highctc.innerHTML="8 LPA";
    lowctc.innerHTML="2 LPA";
    avgctc.innerHTML="3 LPA";
  }
}