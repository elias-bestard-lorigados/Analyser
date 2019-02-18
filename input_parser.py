from api.utils.config import Config
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

def parse():
    args = parser.parse_args()
    config = Config()
    if os.path.exists('./config.ini'):
        __read_conf()
    __set_config_by_args(args)
    if config.parser_list == 1 or config.prarsers_help != [] or config.data_generated!=[] or config.graphs_list==1:
        # if args.parsers_help or args.parsers_list or args.graphs_list or args.data_generator:
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

