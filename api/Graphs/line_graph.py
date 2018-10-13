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
            # labels.append("")
            values.append(item)
    return labels, values


class Line_Graph:
    """ Crear un grafico de linea """

    def __init__(self, format_known):
        self.__My_Formats = []
        self.__elements = format_known.elements
        self.__labels, self.__values = IsListOfTuple_StrInt(self.__elements)
        print(self.__elements)

    def graphic(self, output):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if output == "<stdout>":
            return self.__make_graph()
        return self.__make_JS_code()

    def __make_graph(self):
        ''' hace el grafico en pyplot '''
        pyplot.plot(self.__values)
        pyplot.show()

    def __make_JS_code(self):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="line_container_" +
                          str(random.uniform(0, 999999)))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Line Chart'
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
        if len(self.__labels) == 0:
            chart.add_data_set(self.__elements, "line")
        else:
            for item in range(len(self.__labels)):
                data = self.__values[item]
                label = self.__labels[item]
                chart.add_data_set(data=[data],name=label, series_type="line")

        chart.buildhtml()
        return chart.content
