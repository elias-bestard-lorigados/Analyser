from .. import an_known_format as formats
import re
from random import uniform
import os

class LabelValue:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= label + value +'\\n'+...
        """

    def __init__(self):
        ''' RE ->label value 'salto' '''
        self._re = re.compile('([ A-z ]+ [0-9]+[ \n]*)*')
        # self._re = re.compile('([ A-z ]+ [0-9]+(\.[0-9]+)?[ \n]*)*')

    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con un label + num separados por saltos de linea
        label val"salto"... """
        if self._re.match(data).end()==len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera labels+numeros, separados por 'salto de linea'.
        Retorna una lista de FK """
        formats_list=[]
        labels = []
        values = [int(item) for item in re.findall("[0-9]+", data)]
        data=data.split("\n")
        for item in data:
            label=''
            for x in re.findall("[A-z]+", item):
                label+=x+' '
            labels.append(label)
        formats_list.append(formats.PairsList(labels, values))
        elements = [[labels[i], values[i]] for i in range(len(values))]
        elements_pairs = [[[labels[i], values[i]]] for i in range(len(values))]
        formats_list.append(formats.NumbersListOfList(elements))
        formats_list.append(formats.NumbersListOfList(elements_pairs))
        return formats_list
    def help(self):
        return ''' parsea una cadena con cada linea= label + value +'\\n'+...
                EJ: 
                Madrid 34
                Barcelona 32
                Atletico 23 '''

    def data_generator(self,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir("./data") if item.__contains__("d_label_valule_")]
        file = open("./data/d_label_value_"+str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            data += "l"*item+" "
            data += str(int(uniform(on_top, below)))
            file.write(data+"\n")
        file.close()
