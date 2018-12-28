import argparse
import os

parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file", help="The path of the file to analize")
parser.add_argument("-o", "--out", default= "stdout",
                    help="Where we puts the results")
parser.add_argument("-g", "--graph", default="all",
                    help="which one of the graphs do you want graphic the data, ex: 'pie, line, column'",
                    type=str)
parser.add_argument("-p", "--parser", default="all",
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
    if args.parsers_help:
        if args.parsers_help=='':
            parsers_help()
        else:
            parsers_help(args.parsers_help.split(','))
        return "",None
    elif args.parsers_list:
        parsers_or_graphs_list("parsers")
        return '',None
    elif args.graphs_list:
        parsers_or_graphs_list("graphs")
    elif args.data_generator:
        data_generator(args.data_generator)
        return "",None
    
    #adquiriendo los valores a procesar en data=STRING
    data=""
    # args.file = "text.txt"
    if args.file:   #Si recibo los datos de un FILE
        data = open(args.file, "r").read()
    else:   #Si recibo los datos por la consola hasta que no escriba una linea en blanco
        print("write the data. To finish it write a blank line")
        temp = input()
        while not temp=="":
            data+=temp
            temp=input()
            data+="\n" if not temp=="" else ""
    #ya con data lleno
    print(data)
    return data, args
    # return '', None

def parsers_or_graphs_list(_type):
    ''' Lista los nombres de los parsers definidos '''
    for item in os.listdir("./api/"+_type):
        p = "./api/"+_type+"/"+item
        if (not os.path.isdir(p)):
            print(item[:-3])

def parsers_help(parsers_list='all'):
    ''' Lista todos los parsers definidos y un ejemplo de los mismos '''
    dirs = os.listdir("./api/parsers")
    print("="*20)
    for item in dirs:
        p = "./api/parsers/"+item
        a = [x.capitalize() for x in item[:-3].split("_")]
        name = ""
        for item2 in a[1:]:
            name += item2
        if (not os.path.isdir(p)) and (parsers_list.__contains__('all') or parsers_list.__contains__(item[:-3])):
            print(item[:-3])
            import_module = compile(
                "from api.parsers."+item[:-3]+" import "+name, 'e', mode='exec')
            exec(import_module)
            print(eval(str(name+"().help()")))
            print("="*20)


def data_generator(parsers_list='all', amount=5, on_top=50, below=100):
    ''' Lista todos los parsers definidos y un ejemplo de los mismos '''
    dirs = os.listdir("./api/parsers")
    print("="*20)
    for item in dirs:
        p = "./api/parsers/"+item
        a = [x.capitalize() for x in item[:-3].split("_")]
        name = ""
        for item2 in a[1:]:
            name += item2
        if (not os.path.isdir(p)) and (parsers_list.__contains__('all') or parsers_list.__contains__(item[:-3])):
            print(item[:-3])
            import_module = compile(
                "from api.parsers."+item[:-3]+" import "+name, 'e', mode='exec')
            exec(import_module)
            eval(str(name+"().data_generator(amount, on_top,below)"))
            print("="*20)
