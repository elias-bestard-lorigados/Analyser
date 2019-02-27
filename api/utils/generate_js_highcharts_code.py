def add_js_code(data,chart_name="Chart",type='line',chart_id=1,keys=[]):
    series=[]
    for item in data:
        new_data={}
        new_data["data"]=data[item]
        new_data["type"]=type
        new_data["name"]=item
        if  keys!=[]:
            new_data["keys"]=keys
        series.append(new_data)

    js_code="""
    <div id="chart_container_"""+str(chart_id)+""" ">Loading....</div>
    <script>
        $(function(){
            Highcharts.setOptions({"global": {}, "lang": {}});
            var option = {
                "chart": {
                    "renderTo": "chart_container_"""+str(chart_id)+""" ",
                    "zoomType": "xy"
                    },
                "colors": {}, "credits": {"enabled": false}, "drilldown": {}, "exporting": {},
                "labels": {}, "legend": {}, "loading": {}, "navigation": {}, "pane": {},
                "plotOptions": {
                    "column": {"allowPointSelect": true, "dataLabels": {"enabled": true}},
                    "packedbubble": {
                        'dataLabels': {
                        'enabled': true,
                        'format': '{point.name}',
                        'style': {
                          'color': 'black',
                          'textOutline': 'none',
                          'fontWeight': 'normal'}},
                        'minPointSize': 5
                        },
                    "tilemap":{
                        dataLabels: {
                        enabled: true,
                        format: '{point.name}',
                    },
                "series": {}, "subtitle": {},
                "title": {"text": '"""+str(chart_name)+"""'},
                "tooltip": {"pointFormat": "{series.name}: <b>x={point.x} ,y={point.y} </b>"},
                "xAxis": {}, "yAxis": {}};
            var chart = new Highcharts.Chart(option);
            var data = """+str(series) +""";
            var dataLen = data.length;
            for (var ix = 0; ix < dataLen; ix++) {
                chart.addSeries(data[ix]);
            }
        });
    </script> """
    return js_code