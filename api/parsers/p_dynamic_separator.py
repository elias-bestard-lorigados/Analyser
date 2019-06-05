from api import an_known_format as formats
import re
import os
from random import uniform

class DynamicSeparator:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= linea= label + value1 value2 value3... val_i
        """
    def parse(self, data,separator=','):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por 'separator'
        val"salto"... """
        self._re = re.compile("(\d+(\.\d+)?("+separator+"\d+(\.\d+)?)*[\n]*)*")
        if self._re.match(data).end() == len(data):
            return self.process(data,separator)
        return None

    def process(self, data,separator=','):
        """ Procesa el string 'data'.
        Espera listas de numerosen cada linea, separados por 'separator'
        Retorna una lista con FK"""
        formats_list = []
        elements = []   #los elemetos tal como estan
        #for pairs
        pairs_values = [] #elementos en pairs si son cantidad de numeros pairs
        data=data.split('\n')
        for line in data:
            if  line=='':
                continue
            values = [float(x) for x in line.split(separator)]
            elements.append(values)
            if len(values) % 2 == 0: #si la cantidad de elementos es par hago una lista con los pares consecutivos
                pairs_values.append([[values[i],values[i+1]] for i in range(0,len(values),2)])
        if elements!=[]:
            formats_list.append((formats.NumSeries(elements),1))
            chart_boxplot=formats.BoxplotSeries()
            chart_boxplot.calculate_boxplot_from_list(elements)
            if len(chart_boxplot.elements)!=0:
                formats_list.append((chart_boxplot,1))
        if pairs_values!=[]:
            formats_list.append((formats.PairsSeries(pairs_values),1))
        return formats_list

    def help(self):
        return ''' parsea una cadena donde cada linea= label + value1 value2 value3... val_i +'\\n'+...
                EJ: 
                34 38 12 3 1
                32 41 12 2 
                23 32'''

    def data_generator(self,path, amount=50, on_top=50, below=100,separator=','):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_dynamic_separator_")]
        file = open(path+"/d_dynamic_separator_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            for x in range(0, int(uniform(1, amount))):
                data += str(int(uniform(on_top, below)))+separator
            file.write(data[:-1]+"\n")
        file.close()

