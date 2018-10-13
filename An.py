from matplotlib import pyplot
import argparse
from api.An_Identify import identify
from api.An_Graphs import graph
# from CLI import ini
# import CLI
import input
class Analyzer:
    def __init__(self,data,output):
        ''' Inicializar las propiedades de la clase
        __output: por donde se retornran los resultados del analisis de los datos
        __data: string que contiene los datos a analizar
         '''
        self.__data=data
        self.__output=output
        self.file=None  # aca se guardara el file donde se escribira el resultado si la salida no es por la consola
    def analyze(self):
        ''' Trata de analizar self.__data con todos los parsers para generar todos los graficos posibles '''
        formats= self.to_identify()
        results=""
        for item in formats:    #recorro todos los formatos para graficar de cada formto todos los graficos posibles
            code = self.to_graphic(item)
            for text in code:
                results += text
        if self.__output != "<stdout>": #si los resultados no se esperan por la salida estandar
            self.__ini_HTML()   #creo el archivo html
            self.file.write(results)  # escribo el resultado en el
            self.__end_HTML()   #concluo el html y cierro el archivo

    def to_identify(self):
        ''' Identificar todos los posibles tipos de Format_Known se extraen de "self.__data"
        return LIST[FORMAT_KNOWN]  '''
        formats_knowns = identify(self.__data)
        return formats_knowns

    def to_graphic(self,format_known):
        ''' graficar los formatos "format_known" de la entrada 
        return LIST[STRING] (codigo js de los graficos)'''
        graphs=graph(format_known,self.__output)
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
an = Analyzer(data, args.output.name)
an.analyze()

# CLI.ini()
#llamada al cli!!!!
# data,output=CLI.ini()
# data,output='''12
# 13
# 1
# 14''',"stdout"
# # an = Analyzer(data, "stdout")
# an = Analyzer(data, "output.html")
# an.analyze()
