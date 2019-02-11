from . import an_known_format as formats
from .graphs.g_line_graph import LineGraph as line
from .graphs.g_pie_graph import PieGraph as pie
from .graphs.g_column_graph import ColumnGraph as column
from api.utils.config import Config
import json
#diccionario donde mantiene cada de cada grafico el formato que entiende
graphs_per_formats = {formats.PairsList: ["g_pie_graph", "g_line_graph", "g_column_graph"],
                    formats.NumbersList: ["g_pie_graph", "g_line_graph", "g_column_graph"],
                    formats.ListOfSeriesnameAndValues: ["g_line_graph", "g_column_graph"],
                    formats.NumbersListOfList: ["g_line_graph", "g_column_graph"]}

graphs={"g_pie_graph":pie(),
        "g_line_graph":line(),
        "g_column_graph":column()
        }
def graph(known_format,graphs_list,id):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graficos que se quieren utilizar"""
    result_code=[]
    for item in graphs_per_formats[type(known_format)]:
        if graphs_list.__contains__(item) or graphs_list.__contains__("all"):
            content = graphs[item].graphic(id,known_format)
            if content!=None:
                result_code.append(content)
                add_data_base(graphs[item], known_format,id)
        id+=1
    return result_code
def add_data_base(graphic,kf,id):
        ''' Escribe en la base de datos el grafico que se utiliza y la info necesaria '''
        db_file = open(Config().db_path, 'r')
        info = db_file.read()
        deserialization = json.loads(info)
        myDictObj = {"useful":True , "id": id, "type": graphic.type,
                     "properties": {"min_value": kf.min_value, "max_value": kf.max_value, "count": kf.count}}
        deserialization.append(myDictObj)
        db_file.close()
        db_file = open(Config().db_path, 'w')
        serialized = json.dumps(deserialization, sort_keys=True, indent=3)
        db_file.write(serialized)
        db_file.close()

