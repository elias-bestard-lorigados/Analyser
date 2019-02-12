import os
import sys
from api.utils.config import Config

#importando los parsers dinamicamente
sys.path.append(Config().parsers_path)
__all_parsers={}
for item in Config().parsers:
    class_name = Config().get_parser_class_name(item)
    # import_module = compile(
                # "from .parsers."+item+" import "+class_name, 'e', mode='exec')
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    __all_parsers[class_name] = eval(str(item+"."+class_name+"()"))
    # __all_parsers[class_name] = eval(str(class_name+"()"))

def identify(data):
    """ Trata de ir parseando la cadena 'data' por los parsers que pasan como parametro
        y retorna una lista de todos los formatos conocidos posibles"""
    list_formats = []
    for item in Config().available_parsers:
        format_ = __all_parsers[item].parse(data)
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    for kf,simi in list_formats:
        print(kf.elements)
    return list_formats

