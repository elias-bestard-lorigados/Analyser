from api.parsers.grammars.g_str_str_weight_list import g_str_str_weight_list
from api import an_known_format as formats
import os
from random import uniform

class StrStrNumList:
    """ parsea como las lineas como una serie, de listas de trios [x,y,z] 
    donde x y son labels
        [[label1,label2,value],....,[labeln,labelm,value]]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la gramatica definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = g_str_str_weight_list.parse(data)
        if info:
            formts=[]
            new_format=formats.StrStrWeightSeries(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de trios x,y,z 
        donde z es un valor numerico y 'x,y' son labels
                EJ: 
                [[label_0,label_10,1.2],[label_1,label_12,2.2]]
                [[label_2,label_21,2]]
                [[label_3,label_34,7],[label_4,label_61,3]]
                [[label_5,label_56,7],[label_6,label_81,3]]'''

    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_str_str_num_list_")]
        file = open(path+"/d_str_str_num_list_" +
                    str(len(data_files)+1)+".txt", "w")
        labl_number=0
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                elem_2=str(round(uniform(on_top, below),2))
                middle_data +="[label_"+str(labl_number)+",label_"+str(labl_number+1)+","+elem_2+"],"
                labl_number+=2
            middle_data = middle_data[:-1]
            data+="["+middle_data+"]"
            file.write(data+"\n")
        file.close()
