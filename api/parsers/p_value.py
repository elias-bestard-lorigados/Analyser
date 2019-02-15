from api import an_known_format as formats
import re
import os
from random import uniform
class Value:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= value '\\n'+...
        """

    def __init__(self):
        ''' RE -> value '''
        self._re = re.compile('([0-9]+[\n]*)*')

    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        if self._re.match(data).end()==len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera numeros separados por 'salto de linea'.
        Retorna una lista con 'An_Format_Known.Pair_Label_EntireP_List' o 'An_Format_Known.NumbersList' """
        formats_list=[]
        data = re.sub("[\n]", ' ', data)
        data = [int(item) for item in data.split()]
        data2 = [[item] for item in data]
        formats_list.append((formats.NumSeries([data]),1))#add the serie "data"
        formats_list.append((formats.NumSeries(data2),1))#add  a serie for each number in data
        if len(data)%2==0:
            formats_list.append((formats.PairsSeries([[data[x] for x in range(0, len(data), 2)]],
                                [[data[x] for x in range(1, len(data), 2)]]),1))
            formats_list.append((formats.NumSeries([(data[x],data[x+1]) for x in range(0,len(data),2)]),1))
            formats_list.append((formats.PairsSeries([[data[x]] for x in range(0,len(data),2)],
                                [[data[x]] for x in range(1,len(data),2)]),1))
        return formats_list

    def help(self):
        return ''' parsea una cadena con cada linea= value '\\n'+...
                EJ: 
                34
                32
                23 '''

    def data_generator(self,path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_value_")]
        file = open(path+"/d_value_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = str(int(uniform(on_top, below)))
            file.write(data+"\n")
        file.close()
