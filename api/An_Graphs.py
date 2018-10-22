from . import An_Format_Known as formats
from .Graphs.line_graph import Line_Graph as line
from .Graphs.pie_graph import Pie_Graph as pie
from matplotlib import pyplot
from highcharts import Highchart
import random

#diccionario donde mantiene cada de cada grafico el formato que entiende
graphs_per_formats={formats.Pair_List:["pie","line"],
        formats.Entire_Pos_List: ["pie", "line"],
        formats.List_Tuple: ["line"],
        formats.Entire_ListOfList: ["line"]}
graphs={"pie":pie,
        "line":line}
def graph(format_known, output,graphs_list):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graficos que se quieren utilizar"""
    result_code=[]
    for item in graphs_per_formats[type(format_known)]:
        if graphs_list.__contains__(item) or graphs_list.__contains__("all"):
            graph=graphs[item](format_known)
            content = graph.graphic(output)
            if content!=None:
                result_code.append(content)
    return result_code



