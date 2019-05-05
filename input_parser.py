from api.utils.config import Config
from api.an_graphs import graphic_generate
import configparser
import argparse
import os
import sys
parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file", help="The path of the file to analize")
parser.add_argument("-o", "--out", help="Name of the result of the procces")
parser.add_argument("-g", "--graph",
                    help="which one of the graphs do you want graphic the data, ex: 'pie, line, column'",
                    type=str)
parser.add_argument("-p", "--parser",
                    help="To select which one of the parsers do you want parse the info, ex: 'p_label_value, p_series_list' ",
                    type=str)
parser.add_argument("-ph", "--parsers_help",
                    help='''List the help for the parsers that you want separated by ',' , ex: 'p_label_value,p_series_list' ''',
                    type=str)
parser.add_argument("-pl", "--parsers_list",help='''List all the parsers definded ''',
                    action='store_true')
parser.add_argument("-gl", "--graphs_list", help='''List all the graphs definded ''',
                    action='store_true')
parser.add_argument("-dg", "--data_generator", help='''To Generate many files of data to analize, depends of the parse of your choice ex:'p_label_value,p_series_list' ''',
                    type=str)
parser.add_argument("-gg", "--graphics_generator", help='''To Generate many out files with the graphs selected Ex:'g_line_graph.g_pie_graph' ''',
                    type=str)
parser.add_argument("-gc", "--generate_config", help='''Generate config.ini ''',
                    action='store_true')
def parse():
    args = parser.parse_args()
    if(args.generate_config):
        __generate_config()
        return []
    config = Config()
    if os.path.exists('./config.ini'):
        __read_conf()
    __set_config_by_args(args)
    if config.parser_list == 1 or config.prarsers_help != [] or config.data_generated!=[] or config.graphs_list==1 or config.graphics_g!=[]:
        # if args.parsers_help or args.parsers_list or args.graphs_list or args.data_generator or args.graphics_generator:
        if config.prarsers_help != []:
        # if args.parsers_help:
            print("PARSERS HELP")
            parsers_help()
        if config.parser_list == 1:
        # if args.parsers_help:
            print("PARSERS")
            print("="*20)
            [print(item) for item in config.parsers]
            print("="*20)
        if config.graphs_list == 1:
        # if args.graphs_list:
            print("GRAPHS")
            print("="*20)
            [print(item) for item in config.graphs]
            print("="*20)
        if config.data_generated != []:
        # if args.data_generator:
            print("GENERATING DATA")
            data_generator()
        if config.graphics_g != []:
            # if args.graphics_generator:
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
    ''' List all the parsers defined with an example '''
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
    ''' Generate a mount of files with examples of info who can be parse by the parsers definded '''
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
    ''' Read 'config.ini' and set his atributes to the Config() class '''
    config = configparser.ConfigParser()
    config.read('config.ini')
    # file = open('config.ini',"w")
    # config.set('Def', 'GRAPHICS', 'calor')
    # config.write(file)

    input_path = config['INPUT']['path']
    output_path = config['OUTPUT']['path']
    output_name = config['OUTPUT']['name']
    parsers_path = config['PARSERS']['path']
    parsers_availables = config['PARSERS']['available']
    parser_help = config['PARSERS']['help'] if not config['PARSERS']['help']=="" else None
    parser_list = config['PARSERS']['list']
    graphs_path = config['GRAPHS']['path']
    graphs_availables = config['GRAPHS']['available']
    graphs_list = config['GRAPHS']['list']
    datag_path = config['DATA_G']['path']
    datag_parsers = config['DATA_G']['parsers'] if not config['DATA_G']['parsers'] == "" else None
    db_path=config['DB']['path']
    graphics_to_generate=config['GRAPHICS_G']['graphichs']
    # Config().db_path=db_path
    Config().set_db_path(db_path)
    Config().set_in_path(input_path)
    Config().set_out_path(output_path)
    Config().set_output_name(output_name)
    Config().set_parsers_path(parsers_path)
    Config().set_graphs_path(graphs_path)
    Config().set_available_parsers(parsers_availables)
    Config().set_available_graphs( graphs_availables)
    Config().set_parsers_help(parser_help)
    Config().set_graphs_list(graphs_list)
    Config().set_parsers_list(parser_list)
    Config().set_data_g_path(datag_path)
    Config().set_data_generated_list(datag_parsers)
    Config().set_graphics_generated_list(graphics_to_generate)

def __set_config_by_args(args):
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

def __graphics_generator():
    ''' Generate a mount of files with examples of info who can be parse by the parsers definded '''
    path = Config().output_path
    data_files = [item
                for item in os.listdir(path) if item.__contains__("output_generated_")]
    file = open(path+"/output_generated_" +
                str(len(data_files)+1)+".html", "w")
    file.write('''<head>
        <script src=\"./js_libraries/jquery.js\"></script>
        <script src=\"./js_libraries/highcharts.js\"></script>
        <script src=\"./js_libraries/highcharts-more.js\"></script>
        <script src=\"./js_libraries/sankey.js\"></script>
        <script src=\"./js_libraries/vector.js\"></script>
        <script src=\"./js_libraries/heatmap.js\"></script>
        <script src=\"./js_libraries/networkgraph.js\"></script>
        <script src=\"./js_libraries/bullet.js\"></script>
        <script src=\"./js_libraries/tilemap.js\"></script>
        <script src=\"./js_libraries/vertical_tabs.js\"></script>\n
        <link rel = \"stylesheet\" href = \"./js_libraries/style.css\">\n
        </head>
        <body>''')
    graphics_code= graphic_generate(Config().graphics_g)
    code_result=""
    tabs_result=[]
    for code,chart_id in graphics_code:
        code_result+=code
        chart = chart_id[:chart_id.index("_")]
        tabs_result.append(
            "<button class = \"tablinks\" onclick = \"openCity(event,'" +chart_id+"')\" >"+chart+" </button >\n")
    
    file.write("<div class = \"tab\" >\n")
    for tabs in tabs_result:
        file.write(tabs)
    file.write("</div>\n")
    file.write(code_result)
    file.write("</body>")
    file.close()

def __generate_config():
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
