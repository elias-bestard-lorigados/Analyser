from .. import an_known_format as formats
import re
import os
from random import uniform

class LabelValuesList:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= linea= label + value1 value2 value3... val_i
        """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ A-z ]+[ 0-9]+[\n]*)*')

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
        values_pairs=[]
        data = data.split("\n")
        for item in data:
            items = [int(y) for y in re.findall("[0-9]+", item)]
            values.append(items)
            if len(items)%2==1:
                items.append(items[-1])
            temp=[]
            for i in range(0,len(items),2):
                temp.append([items[i], items[i+1]])
            values_pairs.append(temp)
            label = ""
            for x in re.findall("[A-z]+", item):
                label += x+" "
            labels.append(label)
        formats_list.append((formats.ListOfSeriesnameAndValues(values, labels),1))
        formats_list.append((formats.ListOfSeriesnameAndValues(values_pairs, labels),1))
        return formats_list

    def help(self):
        return ''' parsea una cadena donde cada linea= label + value1 value2 value3... val_i +'\\n'+...
                EJ: 
                Madrid 34 38 12 3 1
                Barcelona 32 41 12 2 
                Atletico 23 32'''

    def data_generator(self, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir("./data") if item.__contains__("d_label_values_list_")]
        file = open("./data/d_label_values_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            data += "lbl"*item+" "
            for x in range(0, int(uniform(1, amount))):
                data += str(int(uniform(on_top, below)))+" "
            file.write(data+"\n")
        file.close()
