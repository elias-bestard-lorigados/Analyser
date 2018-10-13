from . import An_Format_Known as formats
from .Graphs.line_graph import Line_Graph as line
from .Graphs.pie_graph import Pie_Graph as pie
from matplotlib import pyplot
from highcharts import Highchart
import random

#diccionario donde mantiene cada de cada grafico el formato que entiende
graphs={formats.Pair_List:[pie,line],
        formats.Entire_Pos_List: [pie, line],
        formats.List_Tuple: [line],
        formats.Entire_ListOfList: [line]}
def graph(format_known, output):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear """
    result_code=[]
    for item in graphs[type(format_known)]:
        item=item(format_known)
        content = item.graphic(output)
        if content!=None:
            result_code.append(content)
    return result_code



