import sys
# from api.utils.config import Config
from api.parsers.pre_parsers.pre_parser import analyse_line_by_line
from api.parsers.pre_parsers.pre_parser import analyse_text
from api.parsers.pre_parsers.pre_parser import clean_text

#importando los parsers dinamicamente
# sys.path.append(Config().parsers_path)
# __all_parsers={}
# for item in Config().parsers:
#     class_name = Config().get_parser_class_name(item)
#     import_module = compile("import "+item, 'e', mode='exec')
#     exec(import_module)
#     __all_parsers[class_name] = eval(str(item+"."+class_name+"()"))

parsers_phases = [analyse_line_by_line]
def identify(data):
    """ recorre las fases de parseo y se queda con los formatos conocidos que se extrajeron del texto
        las fases de parseo reciben la cadena a procesar y devuelven una lista de KF
        retorna una lista de todos los formatos conocidos posibles"""
    data = clean_text(data)
    list_kf = analyse_text(data)
    if list_kf != [] and list_kf != [(['UNKNOW'], 0)]:
        return list_kf
    for phase in parsers_phases:
        temp_list=phase(data)
        if temp_list!=[]:
            list_kf.extend(temp_list)
    return list_kf
