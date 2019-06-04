from api import an_known_format as formats
import random


class MyHighchart:
    def __init__(self):
        self.type = "line"
        self.kf_permited = []
        self.options = {
            "chart": {"zoomType": "xy"},
            "credits": {"enabled": 'false'},
            "drilldown": {}, "exporting": {}, "labels": {},
            "legend": {}, "loading": {}, "navigation": {},
            "pane": {}, "colors": {},"subtitle": {},
            "title": {"text": "chart"},
            "plotOptions": {},
            "series": [],
            "tooltip": {
                "pointFormat": "{series.name}: <b>{point.y} </b>",
                "shared": 'true',
                "crosshairs": 'true'
            },
            "xAxis": {}, "yAxis": {}
        }
        self.g_id = 0

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        self.options['series'].clear()
        return self._make_js_code(format_known)

    def _make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        self.options["chart"]["renderTo"] = "chart_container_" + str(self.g_id)
        self.options["xAxis"]["categories"] = format_known.categories
        for item in format_known.elements:
            data = {'data': format_known.elements[item],
                     'type': self.type, 'name': item}
            if format_known.keys!=[]:
                data['keys']=format_known.keys
            self.options['series'].append(data)
        js_code = """
            <div id="chart_container_"""+str(self.g_id)+"""">Loading....</div>
            <script>
            $(function(){
                Highcharts.setOptions({"global": {}, "lang": {}});
                var option ="""+str(self.options) + """;
                var chart = new Highcharts.Chart(option);
            });
            </script>"""

        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> El siguiente gráfico le es útil? </input>"
        text_to_return += js_code
        return text_to_return

    def generate(self, id):
        '''Genera un gráfico con valores aleatorios '''
        self.g_id = id
        elements = []
        series_nums = int(random.uniform(2, 7))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp = []
          for item in range(point_nums):
            temp.append([item, round(random.uniform(0, 15), 2)])
          elements.append(temp)
        my_format = formats.PairsSeries(elements)
        code = self.graphic(id, my_format)
        return code, my_format

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
        return count
