from api import an_known_format as formats
import re
import os
from random import uniform


class ValuesList:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= value1 value2...value_i '\\n'+...
        """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ 0-9]+[ \n]*)*')

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
        elements = []   #los elemetos tal como estan
        elements_pairs = [] #elementos en pairs si son cantidad de numeros pairs
        data=data.split('\n')
        for item in data:
            if  item=='':
                continue
            items = [int(x) for x in re.findall("[0-9]+", item)]
            elements.append(items)
            if len(items) % 2 == 0: #si la cantidad de elementos es par hago una lista con los pares consecutivos
                temp=[]
                for i in range(0,len(items),2):
                    temp.append([items[i], items[i+1]])
                elements_pairs.append(temp)
        if elements!=[]:
            formats_list.append((formats.NumbersListOfList(elements),1))
        if elements_pairs!=[]:
            formats_list.append((formats.NumbersListOfList(elements_pairs),1))
        return formats_list

    def help(self):
        return ''' parsea una cadena con cada linea= value '\\n'+...
                EJ: 
                34 12 123 32
                32 13 45 
                23  12'''

    def data_generator(self,path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_values_list_")]
        file = open(path+"/d_values_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            for x in range(0, int(uniform(1, amount))):
                data += str(int(uniform(on_top, below)))+" "
            file.write(data+"\n")
        file.close()
