import os
from .config import Config
from . import an_known_format as formats
from . import parsers

__all_parsers={}
for item in Config().parsers:
    class_name = Config().get_parser_class_name(item)
    import_module = compile(
                "from .parsers."+item+" import "+class_name, 'e', mode='exec')
    exec(import_module)
    __all_parsers[class_name] = eval(str(class_name+"()"))

def identify(data,parsers:list):
    """ Trata de ir parseando la cadena 'data' por los parsers que pasan como parametro
        y retorna una lista de todos los formatos conocidos posibles"""
    list_formats = []
    for item in parsers:
        format_ = __all_parsers[item].parse(data)
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    for kf,simi in list_formats:
        print(kf.elements)
    return list_formats

