from api.utils.config import Config
import configparser
import argparse
import os
import sys
parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file", help="The path of the file to analize")
parser.add_argument("-o", "--out", help="Name of the result of the procces")
parser.add_argument("-g", "--graph", default = 'all',
                    help="which one of the graphs do you want graphic the data, ex: 'pie, line, column'",
                    type=str)
parser.add_argument("-p", "--parser", default = 'all',
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
    # if os.path.exists('config.ini'):
    #     __read_conf()
    config.set_available_parsers_graphs(args.parser,args.graph)
    config.set_data_generated_list(args.data_generator)
    config.set_output_file(args.out)
    config.set_parsers_help(args.parsers_help)
    
    
    if args.parsers_help or args.parsers_list or args.graphs_list or args.data_generator:
        if args.parsers_help:
            print("PARSERS HELP")
            parsers_help()
        if args.parsers_list:
            print("PARSERS")
            print("="*20)
            [print(item) for item in config.parsers]
            print("="*20)
        if args.graphs_list:
            print("GRAPHS")
            print("="*20)
            [print(item) for item in config.graphs]
            print("="*20)
        if args.data_generator:
            print("GENERATING DATA")
            data_generator()
        return []
    
    # data=STRING a procesar
    data = ""
    if args.file:   #Si recibo los datos de un FILE
        data=[]
        if os.path.isdir(args.file):
            for item in os.listdir(args.file):
                temp = open(args.file+item, "r")
                data.append(temp.read())
                temp.close()
        else:
            data = [open(args.file, "r").read()]
    else:   #Si recibo los datos por la consola hasta que no escriba una linea en blanco
        print("write the data. To finish it write a blank line")
        temp = input()
        while not temp=="":
            data+=temp
            temp=input()
            data+="\n" if not temp=="" else ""
            data=[data]
    #ya con data lleno
    
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

def data_generator(amount=5, on_top=50, below=100):
    ''' Generate a mount of files with examples of info who can be parse by the parsers definded '''
    path = Config().data_generated_url
    sys.path.append(Config().parsers_url)

    print("="*20)
    #Recorrer todos los parsers que quiere ser procesados
    for item in Config().data_generated:
        #Adquirir el nombre de la clase dentro del file item
        print(item)
        class_name = Config().get_parser_class_name(item)
        import_module = compile("import "+item, 'e', mode='exec')
        exec(import_module)
        # try:
        eval(item+"."+class_name + "().data_generator('{0}',{1},{2},{3})".format(path,amount,on_top,below))
        # except:
            # print("WARNING-- THE PARSER "+item+" DOES NOT HAVE THE METHOD data_generator")
        print("="*20)

def __read_conf():
    pass

# config = configparser.ConfigParser()
# config.read('config.ini')
# # file = open('config.ini',"w")

# name = config['Def']['OUT']  # 'secret-key-of-myapp'

# config.set('Def', 'GRAPHICS', 'calor')
# # config.write(file)

# tiempo = config['Def']['GRAPHICS']  # 'web-hooking-url-from-ci-service'


# print((name))
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# print(tiempo)
