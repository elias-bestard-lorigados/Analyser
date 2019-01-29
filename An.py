from api.utils.config import Config
from api.an_identify import identify
from api.an_graphs import graph
import input
import os
class Analyser:
    def __init__(self,data):
        ''' Inicializar las propiedades de la clase
        __output: por donde se retornran los resultados del analisis de los datos
        __data: string que contiene los datos a analizar
         '''
        self.__data=data
        self.__output=Config().output_name
        self.file=None  # aca se guardara el file donde se escribira el resultado si la salida no es por la consola

    def analyse(self):
        ''' Trata de analizar self.__data con todos los parsers para generar todos los graficos posibles por defecto'''
        #list of tuple [(KF,#)] # represent how similar is it to a KF
        formats = self.to_identify()
        results=""
        #form ->KF ,sim->similarity
        for form,sim in formats:    #recorro todos los formatos para graficar de cada formto todos los graficos posibles
            code = self.to_graphic(form)
            for text in code:
                results += text
        if self.__output != "stdout": #si los resultados no se esperan por la salida estandar
            self.__ini_HTML()   #creo el archivo html
            self.file.write(results)  # escribo el resultado en el
            self.__end_HTML()   #concluo el html y cierro el archivo

    def to_identify(self):
        ''' Identificar todos los posibles tipos de Format_Known se extraen de "self.__data"
        parsers: los parsers que quiere utilizar solamente parsers="" 
        return LIST[FORMAT_KNOWN]  '''
        formats_knowns = identify(self.__data,Config().available_parsers)
        return formats_knowns

    def to_graphic(self,format_known):
        ''' graficar los formatos "format_known" de la entrada
        return LIST[STRING] (codigo js de los graficos)'''
        graphs = graph(format_known, self.__output, Config().graphs)
        return graphs

    def __ini_HTML(self):
        """ Inicializar un HTML enl a carpeta ./out/....html donde se escribira el resultado de analizar los datos """
        self.file = open(Config().output_url+"/"+self.__output, "w")
        self.file.write("<head>")
        self.file.write("<script src=\"./highcharts.js\"></script>")
        self.file.write("<script src=\"./jquery.js\"></script>")
        self.file.write("</head>")
        self.file.write("<body>")

    def __end_HTML(self):
        ''' Cerrara el "body" del HTML final '''
        self.file.write("</body>")
        self.file.close()

data=input.parse()
for info in data:
    print("="*20)
    print(info)
    an = Analyser(info)
    an.analyse()
    Config().output_name = "out_file_"+str(len(os.listdir(Config().output_url)))+".html"
