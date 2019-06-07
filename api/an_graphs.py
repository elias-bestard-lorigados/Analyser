import sys
import logging
from api.utils.config import Config
from api.utils.manage_db import add_data_base,find_count_kf_graphic,find_count_message_graphic
from api.utils.rules import message_comparison,message_distribution,message_relation,message_composition
from api.utils.manage_html import generate_tab, generate_div_html

sys.path.append(Config().graphs_path)
__all_graphs={}

for item in Config().graphs:
    class_name = Config().get_parser_class_name(item)
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    __all_graphs[class_name] = eval(str(item+"."+class_name+"()"))

def to_graphic(kf_list):
    ''' generar codigo html para graficar los formatos "KF" de la entrada
    return LIST[STRING] (codigo js de los graficos)
    retorna el codigo generado y la lista de tabs en los que se van a mostrar en el html'''
    results_tabcontent_charts = ""
    results_tabs = []
    #form ->KF ,sim->similarity
    logging.info("---- KF --> GRAPHICS ----")
    logging.info("-"*30)

    for kf, sim in kf_list:  # recorro todos los formatos para graficar de cada formto todos los graficos posibles
        if kf == ['UNKNOW']:
            continue
        logging.info("KF: "+str(type(kf).__name__)+" --> : ")
        code = find_charts_for_kf(kf)
        for text, chart_id in code:
            results_tabcontent_charts += text
            results_tabs.append(generate_tab(chart_id))
        logging.info("-"*30)
    return results_tabcontent_charts,results_tabs

def find_charts_for_kf(kf):
    """ buscar la lista de graficos a graficar y tratar de generar su codigo si acepta el kf"""
    graphics_list = evaluate_rules(kf) if Config().graphics_selection==1 else Config().available_graphs
    return try_plot(kf, graphics_list)

def try_plot(known_format,graphics_list: list):
    """ Dado un KF busca que tipos de graficos lo pueden plotear de los graficos dados
    graphs: graphics_list <- lista de graficos a graficar
    Retorna el codigo de los graficos con sus ids"""
    id = Config().db_count_id
    result_code=[]
    for chart in graphics_list:
        if Config().message != '' and not __all_graphs[chart].message.__contains__(Config().message):
            continue
        content = __all_graphs[chart].graphic(id,known_format)
        if content!=None:
            logging.info(chart)
            chart_id = __all_graphs[chart].type+"_"+str(id)
            content = generate_div_html(chart_id,content)
            result_code.append((content,chart_id))
            add_data_base(__all_graphs[chart], known_format)
            id+=1
    Config().db_count_id = id
    return result_code

def evaluate_rules(kf,count_to_show=3):
    ''' Recorre los graficos habilitados y evalua las reglas del RBS para ver cuales 
    son los mejores graficos segun el KF
    retorna una lista con los cahrts mejores '''
    dict_result={}
    if  Config().message=='':
        message=check_message(kf)
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
    result=[x for x,j in result]
    return result

def check_message(kf):
    ''' Chequea que mensaje es el que se quiere mostrar a corde a las reglas'''
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
    return result[0][0]

def graphic_generate(graphics_list: list):
    ''' Metodo para generar los graficos con datos aleatorios '''
    result_code = []
    id = Config().db_count_id
    print("-"*30)
    for chart in graphics_list:
        if Config().message != '' and not __all_graphs[chart].message.__contains__(Config().message):
            continue
        content, my_format = __all_graphs[chart].generate(id)
        if content != None:
            chart_id = __all_graphs[chart].type+"_"+str(id)
            print(chart)
            logging.info(chart)
            content = "<div id =\""+chart_id + \
                "\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
            result_code.append((content, chart_id))
            add_data_base(__all_graphs[chart], my_format)
            print("-"*30)
            id += 1
    Config().db_count_id = id
    return result_code
