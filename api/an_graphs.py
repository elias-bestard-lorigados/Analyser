import sys
from api.utils.config import Config
from api.utils.manage_db import add_data_base
from api.utils.manage_db import find_count_kf_graphic
from api.utils.manage_db import find_count_message_graphic
from api.utils.rules import message_comparison
from api.utils.rules import message_distribution
from api.utils.rules import message_relation
from api.utils.rules import message_composition
sys.path.append(Config().graphs_path)
__all_graphs={}

for item in Config().graphs:
    class_name = Config().get_parser_class_name(item)
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    __all_graphs[class_name] = eval(str(item+"."+class_name+"()"))

def graph(kf):
    """ decide si ver cuales son los mejores graficos a mostrar
    o si los muestra sin importancia"""
    graphics_list = evaluate_rules(kf) if Config().graphics_selection==1 else Config().available_graphs
    return select_graph_to_do(kf, graphics_list, Config().graphics_selection)

def evaluate_rules(kf,count_to_show=20):
    ''' Recorre los graficos habilitados y evalua las reglas del RBS para ver cuales 
    son los mejores graficos segun el KF
    return un diccionario con el chart y los puntos que adquirieron '''
    dict_result={}
    if  Config().message=='':
        message,p=check_message(kf)
    else:
        message = Config().message
    for chart in Config().available_graphs:
        if Config().message != '' and not __all_graphs[chart].message.__contains__(Config().message):
            continue
        points = __all_graphs[chart].evaluate_rules(kf)
        feedback=find_count_kf_graphic(__all_graphs[chart],kf)
        points+=feedback
        if __all_graphs[chart].message.__contains__(message):
            points += 1
            # points += p
        if  points>0:
            dict_result[chart]=points
    result=list(dict_result.items())
    result.sort(key=(lambda x:x[1]),reverse=True)
    if len(result)>count_to_show:
        result=result[:count_to_show]
    return result

def select_graph_to_do(known_format,graphics_list: list,call_type=1):
    """ Dado un formato conocido 'known_format' busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graphics_list <- lista de graficos a graficar
    call_type==0 se trabaja con los graficos habilitados,
    call_type==1 se trabaja con los graficos que se asumen mas importantes"""
    id = Config().db_count_id
    to_graphic = [items for items, value in graphics_list] if call_type == 1 else graphics_list
    result_code=[]
    for chart in to_graphic:
        if Config().message != '' and not __all_graphs[chart].message.__contains__(Config().message):
            continue
        content = __all_graphs[chart].graphic(id,known_format)
        if content!=None:
            chart_id = __all_graphs[chart].type+"_"+str(id)
            content = "<div id =\""+chart_id+"\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
            result_code.append((content,chart_id))
            add_data_base(__all_graphs[chart], known_format)
            id+=1
    Config().db_count_id = id
    return result_code

def check_message(kf):
    ''' Chequea que mensaje es el que se quiere mostrar '''
    result=[]
    result.append(('comparison',
                  find_count_message_graphic('comparison', kf) + message_comparison(kf)))
    result.append(('composition',
                  find_count_message_graphic('composition', kf) + message_composition(kf)))
    result.append(('relation',
                  find_count_message_graphic('relation', kf) + message_relation(kf)))
    result.append(('distribution',
                  find_count_message_graphic('distribution', kf) + message_distribution(kf)))
    result.sort(key=(lambda x: x[1]), reverse=True)
    return result[0]

def graphic_generate(graphics_list: list):
    ''' Metodo para generar los graficos con datos aleatorios '''
    result_code = []
    id = Config().db_count_id
    print("="*20)
    for chart in graphics_list:
        if Config().message != '' and not __all_graphs[chart].message.__contains__(Config().message):
            continue
        content, my_format = __all_graphs[chart].generate(id)
        if content != None:
            chart_id = __all_graphs[chart].type+"_"+str(id)
            print(chart)
            content = "<div id =\""+chart_id + \
                "\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
            result_code.append((content, chart_id))
            add_data_base(__all_graphs[chart], my_format)
            print("="*20)
            id += 1
    Config().db_count_id = id
    return result_code
