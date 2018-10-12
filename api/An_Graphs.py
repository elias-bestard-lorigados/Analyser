from matplotlib import pyplot
from highcharts import Highchart
import random
import sys
class Pie_Graph:
    """ Crear un grafico de Pie """
    def __init__(self,format_known):
        self.__elements, self.__labels = None, None
        self.__elements=format_known.elements
        self.__labels,self.__values=IsListOfTuple_StrInt(self.__elements)
        print(self.__elements)
    def graphic(self,output):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if output == sys.stdout:
            pyplot.pie(self.__values, autopct='%1.1f%%', labels=self.__labels)
            pyplot.show()
        else:
            chart = Highchart(renderTo="pie_container_"+str(random.uniform(0,999999)))
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

class Line_Graph:
    """ Crear un grafico de lineas """

    def __init__(self, format_known):
        self.__elements, self.__labels = None, None
        self.__elements = format_known.elements
        self.__labels, self.__values = IsListOfTuple_StrInt(self.__elements)

    def graphic(self, output):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if output == sys.stdout:
            pyplot.plot(self.__values)
            pyplot.show()
        else:
            chart = Highchart(renderTo="line_container_" +
                              str(random.uniform(0, 99999)))
            chart.set_options('chart', {})
            options = {
                'title': {
                    'text': 'A Line Chart'
                },
                'tooltip': {
                    'pointFormat': '{series.name}'
                }
            }
            chart.set_dict_options(options)
            chart.add_data_set(self.__elements,"line")
            chart.buildhtml()
            return chart.content



def IsListOfTuple_StrInt(list):
    """ Chequea que 'list' sea una lista de tuplas[(str,int)].
    Retorna dos listas, ([str],[int]) """
    labels=[]
    values=[]
    for item in list:
        # if type(item) == tuple and not(type(item[0]) == str and type(item[1]) == int):
        #     raise Exception("The elements of the list must be (str,int)")
        if type(item)==tuple:
            labels.append(item[0])
            values.append(item[1])
        else:
            labels.append("")
            values.append(item)
    return labels,values


def graph(format_known, output):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear """
    graphs = [Pie_Graph(format_known), Line_Graph(format_known)]
    result_code=[]
    for item in graphs:
        content = item.graphic(output)
        if content!=None:
            result_code.append(content)
    return result_code


