from matplotlib import pyplot
from highcharts import Highchart
import random
import sys


class Pie_Graph:
    """ Crear un grafico de Pie """

    def __init__(self, format_known):
        self.__My_Formats=[]
        self.__elements = format_known.elements

        print(self.__elements)

    def graphic(self, output):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if output == sys.stdout:
            return self.__make_graph()
        return self.__make_JS_code()


#ver bien esta talla!!!!!!!!!!!!!!!!!!!!!!!!!
    def __make_graph(self):
        ''' hace el grafico en pyplot '''
        labels, values = IsListOfTuple_StrInt(self.__elements)
        pyplot.pie(values, autopct='%1.1f%%', labels=labels)
        pyplot.show()

    def __make_JS_code(self):
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
        chart.add_data_set(self.__elements, 'pie')
        chart.buildhtml()
        return chart.content



file = open("./probando.html", "w")
file.write("<head>")
file.write("<script src=\"./highcharts.js\"></script>")
file.write("<script src=\"./jquery.js\"></script>")
file.write("</head>")
file.write("<body>")

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
chart.add_data_set([(" elias", 16), (" lisandra", 112)], 'pie')
chart.buildhtml()
file.write(chart.content)


file.write("</body>")
file.close()


