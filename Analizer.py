from matplotlib import pyplot
import argparse
import re
import sys
import Identify.An_Identify as identify
import Graphs.An_Graphs as graphs

class Try_to_Parse:
    def __init__(self):
        self.file=None
        if not args.output==sys.stdout:
            self.__ini_HTML(args.output.name)

    def parsea(self,text):
        """ Trata de ir parseando la cadena 'text' por los parsers que ya existen y si matchea con una grafico todos los graficos posibles """

        parser=Parser_Salto_Linea() #tratar de parsearlo con slato de linea
        self.__grafica(parser,text)
        parser = Parser_Salto_Linea_large()  # tratar de parsearlo con slato de linea buscando lista de numeros
        self.__grafica(parser,text)

        # self.__end_HTML()

    def __grafica(self,parser,text):
        """ Dado un formato conocido 'format_' busca que tipos de graficos lo pueden plotear """
        format_ = parser.parsea(text)
        if format_ != None:  # si se pudo parsear
            
            # tratar de graficarlo con PIE
            graph = graphs.Pie_Graph(format_)
            content = graph.graphic(args.output.name)
            if self.file != None:
                self.file.write(content)

            # tratar de graficarlo con Line
            graph = graphs.Line_Graph(format_)
            content = graph.graphic(args.output.name)
            if self.file != None:
                self.file.write(content)
            else:
                print("No pudo con el parser: "+type(parser))

    def __ini_HTML(self,output):
        """ Inicializar el HTML enl a carpeta ./graph/....html """
        self.file = open("../Analizer/output/"+output, "w")
        self.file.write("<head>")
        self.file.write("<script src=\"./highcharts.js\"></script>")
        self.file.write("<script src=\"./jquery.js\"></script>")
        self.file.write("</head>")
        self.file.write("<body>")
    def __end_HTML(self):
        if self.file!=None:
            self.file.write("</body>")
            self.file.close()


class Parser_Salto_Linea:
    """ Parsear un texto en saltos de linea """
    def __init__(self):
        # RE -> (string )* value
        self._re = re.compile(
            '(([A-z]*()*[A-z]*[0-9]*) * [0-9]*()*(\n)*)+|([0-9]*[\n]*)+')
    def parsea(self,text):
        """ Ver si matchea el texto text completo!!! con la expresion regular definida! """
        if self._re.match(text).end() == len(text):
            return identify.Process_By_Line(text)
        return None


class Parser_Salto_Linea_large:
    """ Parsear un texto en saltos de linea esperando que tenga"""

    def __init__(self):
        # RE -> (string )* value
        self._re = re.compile(
            '(([A-z]*()*[A-z]*[0-9]*)* ([0-9]*( )*)*[\s]*)+|(([0-9]*( )*)*[\n]*)+')

    def parsea(self, text):
        """ Ver si matchea el texto text completo!!! con la expresion regular definida! """
        if self._re.match(text).end() == len(text):
            return identify.By_Line_large(text)
        return None



parser = argparse.ArgumentParser(prog="Analizer")
parser.add_argument("-f", "--file",help="The path of the file to analize")
parser.add_argument("-o", "--output", default=sys.stdout,help="Where we puts the results",type=argparse.FileType('w'))
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

var_parse=Try_to_Parse()
var_parse.parsea(data)

