from api.parsers.grammars.g_numbers_list import parse
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
        info = parse(data)
        if info:
            formts=[]
            formts.append((formats.NumSeries(info),1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
                EJ: 
                [[primero,3.85],[segundo,4.28],[tercero,4],[cuarto,4.57],[quinto,4.25]]
                [2,3,4,5,6,21,12]
                [[1,1],[2,2],[3,3],[4,4]]'''


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
            data += str([uniform(on_top, below)
                         for x in range(0, num_of_elements)])
            file.write(data+"\n")
        file.close()
