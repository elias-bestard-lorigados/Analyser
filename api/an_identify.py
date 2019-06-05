import sys
from api.utils.config import Config
from api.utils.pre_parser import analyse_line_by_line, analyse_text, clean_text

# importando los parsers dinamicamente
sys.path.append(Config().parsers_path)
__all_parsers={}
for item in Config().parsers:
    class_name = Config().get_parser_class_name(item)
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    __all_parsers[class_name] = eval(str(item+"."+class_name+"()"))

parsers_phases = [analyse_line_by_line]

def identify(data):
    """ recorre las fases de parseo y se queda con los formatos conocidos que se extrajeron del texto
        las fases de parseo reciben la cadena a procesar y devuelven una lista de KF
        retorna una lista de todos los formatos conocidos posibles"""
    data = clean_text(data)
    list_kf = analyse_text(data,__all_parsers)
    if list_kf != [] and list_kf != [(['UNKNOW'], 0)]:
        return list_kf
    for phase in parsers_phases:
        temp_list=phase(data,__all_parsers)
        if temp_list!=[]:
            list_kf.extend(temp_list)
    return list_kf


def parsers_help():
    '''Lista todos los parsers definidos con su ayuda '''
    print("="*20)
    for item in Config().prarsers_help:
        print(item)
        p_help = __all_parsers[Config().get_parser_class_name(item)].help()
        print(p_help)
        print("="*20)

def data_generator(amount=10, on_top=50, below=100):
    ''' Generar varios archivos con juegos de datos para poder parsearlos '''
    path = Config().data_generated_path
    print("="*20)
    #Recorrer todos los parsers que quiere ser procesados
    for item in Config().data_generated:
        #Adquirir el nombre de la clase dentro del file item
        class_name = Config().get_parser_class_name(item)
        if dir(__all_parsers[class_name]).__contains__("data_generator"):
            print(item)
            __all_parsers[class_name].data_generator(path,amount,on_top,below)
        else:
            print("WARNING-- THE PARSER "+item +
                  " DOES NOT HAVE THE METHOD data_generator")
        print("="*20)
