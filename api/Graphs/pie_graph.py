from matplotlib import pyplot
from highcharts import Highchart
import random

def IsListOfTuple_StrInt(list):
    """ Chequea que 'list' sea una lista de tuplas[(str,int)].
    Retorna dos listas, ([str],[int]) """
    labels = []
    values = []
    for item in list:
        if type(item) == tuple:
            labels.append(item[0])
            values.append(item[1])
        else:
            labels.append("")
            values.append(item)
    return labels, values

class Pie_Graph:
    """ Crear un grafico de Pie """

    def graphic(self, output, format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        # self.__elements = format_known.elements
        if output == "stdout":
            return self.__make_graph(format_known)
        return self.__make_JS_code(format_known)

    def __make_graph(self, format_known):
        ''' hace el grafico en pyplot '''
        labels, values = IsListOfTuple_StrInt(format_known.elements)
        pyplot.pie(values, autopct='%1.1f%%', labels=labels)
        pyplot.show()

    def __make_JS_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="pie_container_" +
                          str(random.uniform(0, 999999)))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Pie Chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            'plotOptions': {
                'pie': {
                    'allowPointSelect': True,
                    'format': '<b>{point.name}</b>: {point.value} ',
                }
            }
        }
        chart.set_dict_options(options)
        chart.add_data_set(format_known.elements, 'pie')
        chart.buildhtml()
        return chart.content
