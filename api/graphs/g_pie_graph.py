from highcharts import Highchart
from api import an_known_format as formats

class PieGraph:
    """ Crear un grafico de Pie """
    def __init__(self):
        self.type = "pie"
        self.kf_permited=[formats.NumSeries,
                        formats.PairsSeries,
                        formats.LabeledPairSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        if  format_known.count>1:
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="chart_container_" +
                          str(self.g_id))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Pie Chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.y:.1f}</b>'
            },
            'plotOptions': {
                'pie': {
                    'allowPointSelect': True,
                    'format': '<b>{point.name}</b>: {point.value} ',
                    'dataLabels': {
                        'enabled': True
                    },
                    'showInLegend': True
                }
            }
        }
        chart.set_dict_options(options)
        for item in format_known.elements:
            chart.add_data_set(format_known.elements[item], 'pie')
        chart.buildhtml()
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following graph useful? </input>"
        text_to_return += chart.content
        return text_to_return
