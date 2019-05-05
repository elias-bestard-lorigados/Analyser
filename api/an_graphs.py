import sys
from api.utils.config import Config
from api.utils.manage_db import add_data_base

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
            chart_id = __all_graphs[chart].type+"_"+str(id)
            content = "<div id =\""+chart_id+"\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
            result_code.append((content,chart_id))
            add_data_base(__all_graphs[chart], known_format)
        id+=1
    return result_code

def graphic_generate(graphics_list:list):
    result_code=[]
    id=Config().db_count_id
    print("="*20)
    for chart in graphics_list:
        content,my_format = __all_graphs[chart].generate(id)
        if content!=None:
            chart_id = __all_graphs[chart].type+"_"+str(id)
            print(chart)
            content = "<div id =\""+chart_id+"\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
            result_code.append((content, chart_id))
            add_data_base(__all_graphs[chart], my_format)
            print("="*20)
        id+=1
    Config().db_count_id=id
    return result_code
