from api.parsers.grammars.g_labeled_pair_list import parse
from api import an_known_format as formats
import os
from random import uniform
class LabeledPairList:
    """ parsea como las lineas como una serie, de listas de pares x,y 
        donde x es un label
        [[labl_1,valu_1],...,[labl_n,valu_n]]\n... [[labl_1.k,valu_1.k],...,[labl_k,valu_k]]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con gramatica
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = parse(data)
        if info:
            formts=[]
            new_format=formats.LabeledPairSeries()
            new_format.reset_with_series(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
                EJ: 
                [[primero,3.85],[segundo,4.28],[tercero,4],[cuarto,4.57],[quinto,4.25]]
                [[primero,3.85],[segundo,4.28],[tercero,4],[cuarto,4.57],[quinto,4.25]]'''

    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_labeled_pair_list_")]
        file = open(path+"/d_labeled_pair_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                middle_data += "[label"+str(x+item)+","+str(uniform(on_top, below))+"],"
            middle_data = middle_data[:-1]
            data="["+middle_data+"]"
            file.write(data+"\n")
        file.close()
