from . import an_known_format as formats
from .graphs.g_line_graph import LineGraph as line
from .graphs.g_pie_graph import PieGraph as pie
from .graphs.g_column_graph import ColumnGraph as column
from matplotlib import pyplot
from highcharts import Highchart
import random

#diccionario donde mantiene cada de cada grafico el formato que entiende
graphs_per_formats = {formats.PairsList: ["g_pie_graph", "g_line_graph", "g_column_graph"],
                    formats.NumbersList: ["g_pie_graph", "g_line_graph", "g_column_graph"],
                    formats.ListOfSeriesnameAndValues: ["g_line_graph", "g_column_graph"],
                    formats.NumbersListOfList: ["g_line_graph", "g_column_graph"]}

graphs={"g_pie_graph":pie(),
        "g_line_graph":line(),
        "g_column_graph":column()
        }
def graph(format_known, output,graphs_list):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graficos que se quieren utilizar"""
    result_code=[]
    for item in graphs_per_formats[type(format_known)]:
        if graphs_list.__contains__(item) or graphs_list.__contains__("all"):
            content = graphs[item].graphic(output,format_known)
            if content!=None:
                result_code.append(content)
    return result_code



