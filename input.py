import argparse
import sys
parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file",help="The path of the file to analize")
parser.add_argument("-o", "--output", default=sys.stdout,help="Where we puts the results",type=argparse.FileType('w'))
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
