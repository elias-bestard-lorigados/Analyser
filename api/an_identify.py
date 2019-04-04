import sys
# from api.utils.config import Config
from api.parsers.pre_parsers.pre_parser import procces_text
from api.parsers.pre_parsers.pre_parser import compress_list

#importando los parsers dinamicamente
# sys.path.append(Config().parsers_path)
# __all_parsers={}
# for item in Config().parsers:
#     class_name = Config().get_parser_class_name(item)
#     import_module = compile("import "+item, 'e', mode='exec')
#     exec(import_module)
#     __all_parsers[class_name] = eval(str(item+"."+class_name+"()"))

def identify(data):
    """ Trata de ir parseando la cadena 'data' por los parsers que pasan como parametro
        y retorna una lista de todos los formatos conocidos posibles"""
    list_kf=procces_text(data)
    # data, description = compress_list(data.split('\n'),description)
    return list_kf
