from api.an_graphs import graphic_generate
from api.utils.config import Config
from api.utils.analyse import ini_html, end_html, generate_tab
import configparser
import argparse
import os
import sys

parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file", help="Path donde se ubica la info a procesar")
parser.add_argument("-o", "--out", help="Nombre base de los archivos de salida")
parser.add_argument("-g", "--graph",
                    help="Lista de los graficos que se quieren utilizar, ex: 'g_pie_graph,g_line_graph,g_column_graph'",
                    type=str)
parser.add_argument("-p", "--parser",
                    help="Lista de los parsers que se quieren utilizar, ex: 'p_label_value, p_series_list' ",
                    type=str)
parser.add_argument("-ph", "--parsers_help",
                    help='''Lista la ayuda de los parsers de la lista separada por ',' , ex: 'p_label_value,p_series_list' ''',
                    type=str)
parser.add_argument("-pl", "--parsers_list",help='''Lista todos los parsers definidos ''',
                    action='store_true')
parser.add_argument("-gl", "--graphs_list", help='''List todos los graficos definidos''',
                    action='store_true')
parser.add_argument("-dg", "--data_generator", help='''Generar juegos de datos, genera juegos de datos de los parsers que desee ex:'p_label_value,p_series_list' ''',
                    type=str)
parser.add_argument("-gg", "--graphics_generator", help='''Genera archivos de salida con los graficos a su eleccion Ex:'g_line_graph.g_pie_graph' ''',
                    type=str)
parser.add_argument("-gc", "--generate_config", help='''Genera config.ini ''',action='store_true')
parser.add_argument("-gs", "--graphics_selection", help='''Para activar el Sistema en Base Reglas para determinar mejores graficos 0 desactiva 1 activa, por default es 1''',
                    type=str, choices=['0', '1'], default='1')
parser.add_argument("-m", "--message", help='''Para definir que mensaje quiere mostrar con los graficos, uno de los siguienes : comparison,composition,relation,distribution''',
                    type=str, choices=['comparison','composition','relation','distribution'])

def parse():
    ''' Parsear la entrada por default y luego ajustar los archivos de configuracion de acuerdo a los parametros
    1ro lee archivo CONFIG.INI si existe y se ajusta la config acorde a este
    2do se leen los parametros del CLI y se ajusta CONFIG a estos
    luego lee el archivo a analizar y comienza el flujo del programa '''
    args = parser.parse_args()
    # Ver si el usuario quiere generar el archivo config.ini
    if(args.generate_config):
        __generate_config()
        return []
    config = Config()
    if os.path.exists('./config.ini'):
        try:
            __read_conf()
        except :
            print("WARNING--- HAY ALGO MAL CON EL ARCHIVO CONFIG.INI")
        __read_conf()
    __set_config_by_args(args)

    if config.prarsers_help != [] or config.parser_list != 0 or config.graphs_list != 0:
        if config.prarsers_help != []:
            print("PARSERS HELP")
            parsers_help()
        if config.parser_list == 1:
            print("PARSERS")
            print("="*20)
            [print(item) for item in config.parsers]
            print("="*20)
        if config.graphs_list == 1:
            print("GRAPHS")
            print("="*20)
            [print(item) for item in config.graphs]
            print("="*20)
        return []
    if config.data_generated!=[] or config.graphics_g!=[]:
        if config.data_generated != []:
            print("GENERATING DATA")
            data_generator()
        if config.graphics_g != []:
            print("GENERATING GRAPHICS")
            __graphics_generator()
        return []
    # data=STRING a procesar
    data = ""
    path_to_proccess=config.input_path
    data=[]
    if os.path.isdir(path_to_proccess):# si e sun directorio
        for item in os.listdir(path_to_proccess):
            temp = open(path_to_proccess+'/'+item, "r")
            data.append(temp.read())
            temp.close()
    else: #si es un file
        data = [open(path_to_proccess, "r").read()]
    return data

def parsers_help():
    '''Lista todos los parsers definidos con su ayuda '''
    print("="*20)
    for item in Config().prarsers_help:
        class_name = Config().get_parser_class_name(item)
        print(item)
        import_module = compile(
            "from api.parsers."+item+" import "+class_name, 'e', mode='exec')
        exec(import_module)
        print(eval(str(class_name+"().help()")))
        print("="*20)

def data_generator(amount=10, on_top=50, below=100):
    ''' Generar varios archivos con juegos de datos para poder parsearlos '''
    path = Config().data_generated_path
    sys.path.append(Config().parsers_path)
    print("="*20)
    #Recorrer todos los parsers que quiere ser procesados
    for item in Config().data_generated:
        #Adquirir el nombre de la clase dentro del file item
        print(item)
        class_name = Config().get_parser_class_name(item)
        import_module = compile("import "+item, 'e', mode='exec')
        exec(import_module)
        try:
            eval(item+"."+class_name + "().data_generator('{0}',{1},{2},{3})".format(path,amount,on_top,below))
        except:
            print("WARNING-- THE PARSER "+item+" DOES NOT HAVE THE METHOD data_generator")
        print("="*20)

def __read_conf():
    ''' Lee el archivo config.ini y actualiza la instancia de Config() 
    Mirando si existen las secciones y las opciones buscadas y modificandolas en Config()'''
    config = configparser.ConfigParser()
    config.read('config.ini')
    # file = open('config.ini',"w")
    # config.set('Def', 'GRAPHICS', 'calor')
    # config.write(file)

    if config.has_option('INPUT','path'):
        Config().set_in_path(config['INPUT']['path'])

    if config.has_option('OUTPUT', 'path'):
        Config().set_out_path(config['OUTPUT']['path'])
    if config.has_option('OUTPUT', 'name'):
        Config().set_output_name(config['OUTPUT']['name'])

    if config.has_option('PARSERS', 'path'):
        Config().set_parsers_path(config['PARSERS']['path'])
    if config.has_option('PARSERS', 'available'):
        Config().set_available_parsers(config['PARSERS']['available'])
    if config.has_option('PARSERS', 'help'):
        Config().set_parsers_help(config['PARSERS']['help'])
    if config.has_option('PARSERS', 'list'):
        Config().set_parsers_list(config['PARSERS']['list'])

    if config.has_option('GRAPHS', 'path'):
        Config().set_graphs_path(config['GRAPHS']['path'])
    if config.has_option('GRAPHS', 'available'):
        Config().set_available_graphs(config['GRAPHS']['available'])
    if config.has_option('GRAPHS', 'list'):
        Config().set_graphs_list(config['GRAPHS']['list'])
    if config.has_option('GRAPHS', 'selection'):
        Config().set_graphics_selection(config['GRAPHS']['selection'])
    if config.has_option('GRAPHS', 'message'):
        Config().set_message(config['GRAPHS']['message'])

    if config.has_option('DATA_G', 'path'):
        Config().set_data_g_path(config['DATA_G']['path'])
    if config.has_option('DATA_G', 'parsers'):
        Config().set_data_generated_list(config['DATA_G']['parsers'])

    if config.has_option('DB', 'path'):
        Config().set_db_path(config['DB']['path'])

    if config.has_option('GRAPHICS_G', 'graphichs'):
        Config().set_graphics_generated_list(config['GRAPHICS_G']['graphichs'])

def __set_config_by_args(args):
    ''' Actualiza la instancia de la clase Config() segun los argumentos recibidos por el CLI '''
    if args.file:
        Config().set_in_path(args.file)
    if args.out:
        Config().set_output_name(args.out)
    if args.parser:
        Config().set_available_parsers(args.parser)
    if args.graph:
        Config().set_available_graphs(args.graph)
    if args.parsers_help:
        Config().set_parsers_help(args.parsers_help)
    if args.parsers_list:
        Config().set_parsers_list(1)
    if args.graphs_list:
        Config().set_graphs_list(1)
    if args.data_generator:
        Config().set_data_generated_list(args.data_generator)
    if args.graphics_generator:
        Config().set_graphics_generated_list(args.graphics_generator)
    if args.graphics_selection:
        Config().set_graphics_selection(args.graphics_selection)
    if args.message:
        Config().set_message(args.message)

def __graphics_generator():
    ''' Genera ejemplos con valores aleatorios de los graficos elejidos  '''
    path = Config().output_path
    data_files = [item
                for item in os.listdir(path) if item.__contains__("output_generated_")]
    file_name = "output_generated_" +str(len(data_files)+1)
    graphics_code= graphic_generate(Config().graphics_g)
    code_result=""
    tabs_result=[]
    for code,chart_id in graphics_code:
        code_result+=code
        tabs_result.append(generate_tab(chart_id))
    if code_result == '':
        print("Lo sentimos no se pudo generar ningun grafico")
        return
    file = ini_html(file_name)
    end_html(file,code_result,tabs_result)

def __generate_config():
    ''' Genera el archivo config.ini con los valores por default '''
    file=open('config.ini','w')
    file.write('''[INPUT]
                ;;  path where is located the info to procces
                path = ./data_generator/

                [OUTPUT]
                ;; path where the parsers are located
                path = ./out/
                ; name of the resulting file
                name = out_file

                [PARSERS]
                ; path where the parsers are located
                path = ./api/parsers

                ; List of all parsers that you wnat be availables
                ; available = p_labeled_pair_list,p_nums_pair_list,p_numbers_list
                available = all

                ; List of all parsers will show help
                help =
                ; help = p_values_list,p_series_list
                ; help = all

                ;1 if you want see a list with all parsers 0 if not
                list= 0
                ; list = 1

                [GRAPHS]
                ; path where the charts are located
                path = ./api/graphs
                ; List of all graphs that you want be availables
                ; available = 
                ;available = g_pie_graph,g_line_graph,g_column_graph
                available = all
                ; available = g_pie_graph

                ;1 if you want see a list with all graphs 0 if not
                list= 0
                ; list= 1
                selection=1
                message=

                [DATA_G]
                ; path where the data_generated is located
                path = ./data_generator
                ; List of Parsers wich will be use to generate datasets
                parsers =
                ; parsers = p_values_list
                ; parsers = all

                [DB]
                path=api/utils/data_base.json 
                [GRAPHICS_G]
                graphichs=''')
