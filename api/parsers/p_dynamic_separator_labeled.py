from api import an_known_format as formats
import re
import os
from random import uniform

class DynamicSeparatorLabeled:
    """Intenta parsear una cadena en saltos de linea  donde
        separator es el separador que espera entre numeros, default ','
        cada linea= linea= label + value1 value2 value3... val_i
        """

    def parse(self, data,separator=','):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... 
        separator es el separador que espera entre numeros, default ',' """
        if self.is_this_format(data,separator):
            return self.process(data,separator)
        return None

    def process(self, data,separator=','):
        """ Procesa el string 'data'.
        Espera varios numeros separados por 'salto de linea'.
        Retorna una lista con FK"""
        formats_list = []
        labels = []#stores the names of each series
        values = []#store all the series (list of lists of numbers)
        pairs_values=[]
        for line in data.split('\n'):
            if  line=='':
                continue
            line=line.split(separator)
            labels.append(line[0])
            temp_value=[float(line[i]) for i in range(1,len(line)) ]
            values.append(temp_value)
            #Si tiene cantidad par de numeros los agrupo en pares y agrego una nueva serie!!!!
            if len(temp_value) % 2 == 0:
                pairs_values.append([[temp_value[i],temp_value[i+1]] for i in range(0,len(temp_value),2)])
        formats_list.append((formats.NumSeries(values, labels),1))
        if not len(pairs_values)==0:# si se annadieron pares de elementos
            formats_list.append((formats.PairsSeries(pairs_values, labels),1))
        chart_boxplot=formats.BoxplotSeries()
        chart_boxplot.calculate_boxplot_from_list(values,labels)
        if len(chart_boxplot.elements)!=0:
            formats_list.append((chart_boxplot,1))
        return formats_list

    def help(self):
        return ''' parsea una cadena donde cada linea= label + value1 value2 value3... val_i +'\\n'+...
                por default espera los valores separados por ','
                EJ: 
                Madrid,34,38,12,3,1
                Barcelona,32,41,12,2
                Atletico,23,32
                Paris,31'''

    def data_generator(self,path, amount=50, on_top=50, below=100,separator=','):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_dynamic_separator_labeled_")]
        file = open(path+"/d_dynamic_separator_labeled_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            data += "lbl_"+str(item)+separator
            for x in range(0, int(uniform(1, amount))):
                data += str(int(uniform(on_top, below)))+separator
            file.write(data[:-1]+"\n")
        file.close()

    def is_this_format(self, data,separator=","):
        regex= re.compile('\d+(\.\d+)?')
        data=data.split('\n')
        lines=[item.split(separator) for item in data]
        for i in range(0,len(lines)):
            for j in range(0,len(lines[i])):
                match=regex.match(lines[i][j])
                if match and j==0:
                    if match.end()==len(lines[i][j]):
                        return False
                elif (not match) or (not match.end()==len(lines[i][j])):
                    return False
        return True
