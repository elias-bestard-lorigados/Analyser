from matplotlib import pyplot
import argparse
from api.an_identify import identify
from api.an_graphs import graph
import input
class Analyser:
    def __init__(self,data,output):
        ''' Inicializar las propiedades de la clase
        __output: por donde se retornran los resultados del analisis de los datos
        __data: string que contiene los datos a analizar
         '''
        self.__data=data
        self.__output=output
        self.file=None  # aca se guardara el file donde se escribira el resultado si la salida no es por la consola

    def analyse(self, parsers=['all'], graphs_list=['all']):
        ''' Trata de analizar self.__data con todos los parsers para generar todos los graficos posibles por defecto
        parsers: los parsers que quiere utilizar solamente
        graphs: los graficos que quiere ver solamente  '''
        formats = self.to_identify(parsers)
        results=""
        for item in formats:    #recorro todos los formatos para graficar de cada formto todos los graficos posibles
            code = self.to_graphic(item, graphs_list)
            for text in code:
                results += text
        if self.__output != "stdout": #si los resultados no se esperan por la salida estandar
            self.__ini_HTML()   #creo el archivo html
            self.file.write(results)  # escribo el resultado en el
            self.__end_HTML()   #concluo el html y cierro el archivo

    def to_identify(self,parsers=['all']):
        ''' Identificar todos los posibles tipos de Format_Known se extraen de "self.__data"
        parsers: los parsers que quiere utilizar solamente parsers="" 
        return LIST[FORMAT_KNOWN]  '''
        formats_knowns = identify(self.__data,parsers)
        return formats_knowns

    def to_graphic(self,format_known,graphs_list=['all']):
        ''' graficar los formatos "format_known" de la entrada
        graphs_list: con qu egraficos quiere que grafique 
        return LIST[STRING] (codigo js de los graficos)'''
        graphs = graph(format_known, self.__output, graphs_list)
        return graphs

    def __ini_HTML(self):
        """ Inicializar un HTML enl a carpeta ./output/....html donde se escribira el resultado de analizar los datos """
        self.file = open("./output/"+self.__output, "w")
        self.file.write("<head>")
        self.file.write("<script src=\"./highcharts.js\"></script>")
        self.file.write("<script src=\"./jquery.js\"></script>")
        self.file.write("</head>")
        self.file.write("<body>")

    def __end_HTML(self):
        ''' Cerrara el "body" del HTML final '''
        self.file.write("</body>")
        self.file.close()

data,args=input.parse()
if not data=='':
    # an = Analyser(data, args.output)
    an = Analyser(data, "output.html")
    an.analyse(args.parser.split(','),args.graph.split(','))
