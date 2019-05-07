#! /home/elias/anaconda3/bin/python
from api.utils.config import Config
from api.an_identify import identify
from api.an_graphs import graph
import input_parser
class Analyser:
    def __init__(self,data):
        ''' Inicializar las propiedades de la clase
        __output: por donde se retornran los resultados del analisis de los datos
        __data: string que contiene los datos a analizar
         '''
        self.__data=data
        self.file=None  # aca se guardara el file donde se escribira el resultado si la salida no es por la consola

    def analyse(self):
        ''' Trata de analizar self.__data con todos los parsers para generar todos los graficos posibles por defecto'''
        #list of tuple [(KF,#)] # represent how similar is it to a KF
        formats = self.to_identify()
        results_tabcontent_charts = ""
        results_tabs = []
        #form ->KF ,sim->similarity
        for form,sim in formats:    #recorro todos los formatos para graficar de cada formto todos los graficos posibles
            code = self.to_graphic(form)
            for text,chart_id in code:
                results_tabcontent_charts += text
                results_tabs.append(self.__generate_tab(chart_id))
        if results_tabcontent_charts=='':
            results_tabcontent_charts=''' <h1>Sorry, no Chart could be generated</h1> '''
        self.__ini_HTML()   #creo el archivo html
        self.file.write("<div class = \"tab\" >\n")
        for tabs in results_tabs:
            self.file.write(tabs)
        self.file.write("</div>\n")
        self.file.write(results_tabcontent_charts)  # escribo el resultado en el
        self.__end_HTML()   #concluo el html y cierro el archivo

    def to_identify(self):
        ''' Identificar todos los posibles tipos de Format_Known se extraen de "self.__data"
        parsers: los parsers que quiere utilizar solamente parsers="" 
        return LIST[FORMAT_KNOWN]  '''
        formats_knowns = identify(self.__data)
        return formats_knowns

    def to_graphic(self,format_known):
        ''' graficar los formatos "format_known" de la entrada
        return LIST[STRING] (codigo js de los graficos)'''
        graphs = graph(format_known)
        return graphs

    def __ini_HTML(self):
        """ Inicializar un HTML enl a carpeta ./out/....html donde se escribira el resultado de analizar los datos """
        self.file = open(Config().output_path+"/"+Config().output_name+"_"+str(Config().output_count)+".html"
        , "w")
        self.file.write("<head>")
        self.file.write("<script src=\"./js_libraries/jquery.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/highcharts.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/highcharts-more.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/sankey.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/vector.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/heatmap.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/networkgraph.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/bullet.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/tilemap.js\"></script>\n")
        self.file.write("<script src=\"./js_libraries/vertical_tabs.js\"></script>\n")
        self.file.write("<link rel = \"stylesheet\" href = \"./js_libraries/style.css\">\n")
        self.file.write("</head>\n")
        self.file.write("<body>\n")

    def __end_HTML(self):
        ''' Cerrara el "body" del HTML final '''
        self.file.write("</body>")
        self.file.close()

    def __generate_tab(self,chart_id):
        chart = chart_id[:chart_id.index("_")]
        return "<button class = \"tablinks\" onclick = \"openCity(event,'"+chart_id+"')\" >"+chart+" </button >\n"


data = input_parser.parse()
print("="*20)
for info in data:
    an = Analyser(info)
    print(info)
    an.analyse()
    Config().output_count+=1
    print("="*20)
