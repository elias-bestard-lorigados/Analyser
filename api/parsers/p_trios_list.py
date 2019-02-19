from api.parsers.grammars.g_trios_numbers_list import g_trios_numbers_list
from api import an_known_format as formats
import os
from random import uniform

class TriosList:
    """ parsea como las lineas como una serie, de listas de trios [x,y,z] 
        [[value1,value2],....,[valuen,valuem]]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la gramatica definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = g_trios_numbers_list.parse(data)
        if info:
            formts=[]
            new_format=formats.TriosSeries(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de trios x,y,z donde cada uno
        es un numero
                EJ: 
                [[1.1,5,1.2],[2,1,2.2]]
                [[3,1,2],[4,1,23]]
                [[5.1,5.2,7],[6.1,6.2,3]]
                [[7.1,7.2,7],[8.1,8.2,3]]'''


    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_trios_list_")]
        file = open(path+"/d_trios_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                middle_data +=str([round(uniform(on_top, below),2)for x in range(0, 3)])+","
            middle_data = middle_data[:-1]
            data+="["+middle_data+"]"
            file.write(data+"\n")
        file.close()
