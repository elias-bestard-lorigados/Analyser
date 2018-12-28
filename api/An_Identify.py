import os
from . import an_known_format as formats
from . import parsers

__all_parsers={"all":[]}
for item in os.listdir("./api/parsers"):
    p = "./api/parsers/"+item
    if not os.path.isdir(p):
        a = [x.capitalize() for x in item[:-3].split("_")]
        name = ""
        for item2 in a[1:]:
            name += item2
        import_module = compile(
                    "from .parsers."+item[:-3]+" import "+name, 'e', mode='exec')
        exec(import_module)
        __all_parsers[name] = eval(str(name+"()"))
        __all_parsers['all'].append(name)

def identify(data,parsers):
    """ Trata de ir parseando la cadena 'data' por los parsers que pasan como parametro
        y retorna una lista de todos los formatos conocidos posibles"""
    if parsers.__contains__("all"):
        parsers=__all_parsers["all"]
    list_formats = []
    for item in parsers:
        format_ = __all_parsers[item].parse(data)
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    for item in list_formats:
        print(item.elements)
    return list_formats


