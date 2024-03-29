from api.parsers.grammars.g_str_tuple import g_str_tuple
from api import an_known_format as formats
import os
from random import uniform

class StrTupleList:
    """ parsea como las lineas como una serie, de listas de pairs [x,y] 
    donde x y son labels
        [[label1,label2],....,[labeln,labelm]]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la gramatica definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = g_str_tuple.parse(data)
        if info:
            formts=[]
            new_format=formats.StrPairSeries(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de pairs [x,y]
        donde 'x,y' son labels
                EJ: 
                [[label_0,label_10],[label_1,label_12]]
                [[label_2,label_21]]
                [[label_3,label_34],[label_4,label_61]]
                [[label_5,label_56],[label_6,label_81]]'''

    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_str_tuple_list_")]
        file = open(path+"/d_str_tuple_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                elem_1=str(int(uniform(on_top, below)))
                elem_2=str(int(uniform(on_top, below)))
                middle_data +="[label_"+str(elem_1)+",label_"+str(elem_2)+"],"
            middle_data = middle_data[:-1]
            data+="["+middle_data+"]"
            file.write(data+"\n")
        file.close()

    def describe(self, line):
        """ Ver si matchea el texto "line" con la gramaitca definida
        retorna una None o una descripcioon del la line "StrTupleList" """
        info = g_str_tuple.parse(line)
        if info:
            return "StrTupleList"
        return None
