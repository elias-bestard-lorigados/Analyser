
class MyChart:
    def __init__(self):
        self.type = "line"
        self.kf_permited = []

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self._make_js_code(format_known)

    def _make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        js_code = self.add_js_code(format_known)
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += js_code
        return text_to_return

    def add_js_code(self,kf):
        chart_name = self.type+" chart"
        series = []
        data = kf.elements
        keys = kf.keys

        for item in data:
            new_data = {}
            new_data["data"] = data[item]
            new_data["type"] = self.type
            new_data["name"] = item
            if keys != []:
                new_data["keys"] = keys
            series.append(new_data)

        js_code = """
        <div id="chart_container_"""+str(self.g_id)+""" ">Loading....</div>
        <script>
        $(function(){
            Highcharts.setOptions({"global": {}, "lang": {}});
            var option = {
                "chart": {
                    "renderTo": "chart_container_"""+str(self.g_id)+""" ",
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
                        'dataLabels': {
                            'enabled': true,
                            'format': '{point.name}'
                            }
                        },
                        "sankey":{
                        'tooltip': {"pointFormat": "{series.name}: <b>{point.from}, {point.to} :{point.weight} </b>"}
                        }},
                "series": {}, "subtitle": {},
                "title": {"text": '"""+str(chart_name)+"""'},
                "tooltip": {"pointFormat": "{series.name}: <b>x={point.x} ,y={point.y} </b>"},
                "xAxis": {"categories":"""+str(kf.categories)+ """ },
                "yAxis": {}};
            var chart = new Highcharts.Chart(option);
            var data = """+str(series) + """;
            var dataLen = data.length;
            for (var ix = 0; ix < dataLen; ix++) {
                chart.addSeries(data[ix]);
            }
        });
        </script> """
        return js_code
