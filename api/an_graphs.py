import os
import sys
from api.utils.config import Config
import json

sys.path.append(Config().graphs_path)
__all_graphs={}

for item in Config().graphs:
    class_name = Config().get_parser_class_name(item)
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    __all_graphs[class_name] = eval(str(item+"."+class_name+"()"))

def graph(known_format,id):
    """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graficos que se quieren utilizar"""
    result_code=[]
    for chart in Config().available_graphs:
        content = __all_graphs[chart].graphic(id,known_format)
        if content!=None:
            result_code.append(content)
            add_data_base(__all_graphs[chart], known_format,id)
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

