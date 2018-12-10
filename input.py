import argparse
parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file", help="The path of the file to analize")
parser.add_argument("-o", "--output", default= "stdout",
                    help="Where we puts the results")
parser.add_argument("-g", "--graph", default="all",
                    help="which one of the graphs do you want graphic the data, ex: 'pie, line, column'",type=str
                    )
parser.add_argument("-p", "--parser", default="all",
                    help="which one of the parsers do you want parse the data, ex: 'value_end, label_value_end, labels_values, values_list, series_list' ", type=str
                    )
def parse():
    args = parser.parse_args()
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
    return data,args
