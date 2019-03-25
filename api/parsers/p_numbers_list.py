from api.parsers.grammars.g_numbers_list import g_numbers_list
from api import an_known_format as formats
import os
from random import uniform
# import grammars
class NumbersList:
    """ parsea como las lineas como una serie, de listas de pares x,y donde x puede
        es una lista de numeros
        [value_1,...,value_n]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = g_numbers_list.parse(data)
        if info:
            formts=[]
            formts.append((formats.NumSeries(info),1))
            chart_boxplot=formats.BoxplotSeries()
            chart_boxplot.calculate_boxplot_from_list(info)
            if len(chart_boxplot.elements)!=0:
                formts.append((chart_boxplot,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de numeros
        EJ: 
        [64.15, 52.4, 76.39]
        [51.04, 76.8, 52.14, 81.78, 77.95, 51.14, 94.35]
        [91.7, 83.9, 97.57, 56.65, 77.73, 63.27]
        [94.54, 86.2, 52.69, 96.05, 61.44, 84.79, 63.77, 52.62]'''


    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_numbers_list_")]
        file = open(path+"/d_numbers_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            data += str([round(uniform(on_top, below),2)
                         for x in range(0, num_of_elements)])
            file.write(data+"\n")
        file.close()

    def describe(self, line):
        """ Ver si matchea el texto "line" con la gramaitca definida
        retorna una None o una descripcioon del la line "NumbersList" """
        info = g_numbers_list.parse(line)
        if info:
            return "NumbersList"
        return None
