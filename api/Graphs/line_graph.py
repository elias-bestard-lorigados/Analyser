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

    def graphic(self, output,format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        # self.__elements = format_known.elements
        # self.__labels, self.__values = IsListOfTuple_StrInt(self.__elements)
        # print(self.__elements)
        if output == "stdout":
            return self.__make_graph(format_known)
        return self.__make_JS_code(format_known)

    def __make_graph(self, format_known):
        ''' hace el grafico en pyplot '''
        try:
            if not format_known.labels:
                pyplot.plot(format_known.elements)
                pyplot.show()
            else:
                pyplot.plot(format_known.values)
        except:
            return

    def __make_JS_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="line_container_" +
                          str(random.uniform(0, 999999)))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Line Chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>point.y</b>'
            },
            'plotOptions': {
                'line': {
                    'allowPointSelect': True,
                    'dataLabels': {
                        'enabled': True
                    }}
        }}
        chart.set_dict_options(options)
        for item in format_known.elements:
            if isinstance(item, int):
                chart.add_data_set(
                    format_known.elements[item], series_type="line")
            else:
                chart.add_data_set(
                    format_known.elements[item], series_type="line", name=item)
        chart.buildhtml()
        return chart.content
