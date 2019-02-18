from api import an_known_format as formats
import re
import os
from random import uniform

class LabelValuesList:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= linea= label + value1 value2 value3... val_i
        """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('(([ A-Za-z ]+(_[0-9]+)*)+ [ 0-9]+[\n]*)*')
        # self._re = re.compile('([ A-z ]+[ 0-9]+[\n]*)*')

    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        if self._re.match(data).end() == len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera varios numeros separados por 'salto de linea'.
        Retorna una lista con FK"""
        formats_list = []
        labels = []
        values = []
        x_values=[]
        y_values=[]
        labels_pairs=[]
        for line in data.split('\n'):
            if  line=='':
                continue
            label = ''
            value = ''
            for item in line.split():
                if(not item.isnumeric()):
                    label +=item+" "
                else:
                    value += item+" "
            labels.append(label)
            value = [int(x) for x in value.split()]
            values.append(value)
            #Si tiene cantidad par de numeros los agrupo en pares y agrego una nueva serie!!!!
            if len(value) % 2 == 0:
                x_values.append([value[i] for i in range(0,len(value),2)])
                y_values.append([value[i] for i in range(1,len(value),2)])
        # formats_list.append((formats.NumSeries(values, labels),1))
        if not len(y_values)==0:# si se annadieron pares de elementos
            formats_list.append((formats.LabeledPairSeries(x_values,y_values, labels_pairs),1))
        return formats_list

    def help(self):
        return ''' parsea una cadena donde cada linea= label + value1 value2 value3... val_i +'\\n'+...
                EJ: 
                Madrid 34 38 12 3 1
                Barcelona 32 41 12 2 
                Atletico 23 32'''

    def data_generator(self,path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_label_values_list_")]
        file = open(path+"/d_label_values_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            data += "lbl_"+str(item)+" "
            for x in range(0, int(uniform(1, amount))):
                data += str(int(uniform(on_top, below)))+" "
            file.write(data+"\n")
        file.close()

