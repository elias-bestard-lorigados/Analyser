import sys
from api.utils.config import Config
from api.parsers.pre_parsers.pre_parser import procces_text
from api.parsers.pre_parsers.pre_parser import compress_list

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
    data,description=procces_text(data)
    data, description = compress_list(data.split('\n'),description)
    list_formats = []
    for i in range(len(data)):
        format_ = create_kf(data[i],description[i])
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    for kf,simi in list_formats:
        print(kf.elements)
    return list_formats

def create_kf(data,kf):
    if kf == "UKNOWN" or kf == "COMMENT":
        return None
    format_ = __all_parsers[kf].parse(data)
    return format_

