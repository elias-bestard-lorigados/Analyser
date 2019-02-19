from highcharts import Highchart
from api import an_known_format as formats

class AreaRangeChart:
    """ Crear un grafico de area por rango """
    def __init__(self):
        self.type="arearange"
        self.kf_permited=[formats.NumSeries,formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="chart_container_" +
                          str(self.g_id))
        chart.set_options('chart', {'zoomType': 'xy'})
        options = {
            'title': {
                'text': self.type+' chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.y} </b>',
                'shared': True,
                'crosshairs': True,
            },
            'plotOptions': {
                'column': {
                    'allowPointSelect': True,
                    'dataLabels': {
                        'enabled': True
                    }}
            }}
        chart.set_dict_options(options)
        for item in format_known.elements:
            chart.add_data_set(
                format_known.elements[item],series_type=self.type, name=item)
        chart.buildhtml()
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += chart.content
        return text_to_return
