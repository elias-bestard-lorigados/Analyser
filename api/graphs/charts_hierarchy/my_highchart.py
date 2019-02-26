from highcharts import Highchart
from api import an_known_format as formats

class MyHighchart:
    """ Crear un grafico """
    def __init__(self):
        self.type="line"
        self.kf_permited=[]
        self.options= {
            'title': {
                'text': self.type+' chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.y} </b>',
                'shared': True,
                'crosshairs': True,
            },
            'plotOptions': {
                'scatter': {
                      'marker': {
                        'radius': 7,
                        'states': {
                          'hover': {
                            'enabled': True,
                            'lineColor': 'rgb(100,100,100)'
                          }
                        }
                      },
                      'states': {
                        'hover': {
                          'marker': {
                            'enabled': False
                          }
                        }
                      },
                      'tooltip': {
                        'headerFormat': '<b>{series.name}</b><br>',
                        'pointFormat': '{point.x}, {point.y}'
                      }
                    },
                'column': {
                    'allowPointSelect': True,
                    'dataLabels': {
                        'enabled': True
                    }}
            }
        }
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
        chart.set_dict_options(self.options)
        for item in format_known.elements:
            chart.add_data_set(
                format_known.elements[item],series_type=self.type, name=item)
        chart.buildhtml()
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += chart.content
        return text_to_return
