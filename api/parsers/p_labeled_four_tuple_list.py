from api.parsers.grammars.g_labeled_four_tupple_list import g_labeled_four_tuple_list
from api import an_known_format as formats
import os
from random import uniform

class LabeledFourTupleList:
    """ parsea como las lineas como una serie, de listas de 4-tuplas [(x,y,length,direction)] 
    donde x es un label siendo el nombre del punto"""
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la gramatica definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = g_labeled_four_tuple_list.parse(data)
        if info:
            formts=[]
            new_format=formats.LabeledFourTupleSeries(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de 4-tuplas x,y,length,direction 
        donde y,length,direction son valores numericos y x un label que seria el nombre del punto
                EJ: 
                [[label_0,5,1.2,180],[label_1,1,2.2,90]]
                [[label_2,1,2,45]]
                [[label_3,5.2,7,90],[label_4,6.2,3,10]]
                [[label_5,7.2,7,90],[label_6,8.2,3,10]]'''

    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_labeled_four_tuple_list_")]
        file = open(path+"/d_labeled_four_tuple_list_" +
                    str(len(data_files)+1)+".txt", "w")
        labl_number=0
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                elem_1=str(round(uniform(on_top, below),2))
                elem_2=str(round(uniform(on_top, below),2))
                elem_3=str(round(uniform(on_top, below),2))
                middle_data +="[label_"+str(labl_number)+","+elem_1+","+elem_2+","+elem_3+"],"
                labl_number+=1
            middle_data = middle_data[:-1]
            data+="["+middle_data+"]"
            file.write(data+"\n")
        file.close()

    def describe(self, line):
        """ Ver si matchea el texto "line" con la gramaitca definida
        retorna una None o una descripcioon del la line "LabeledFourTupleList" """
        info = g_labeled_four_tuple_list.parse(line)
        if info:
            return "LabeledFourTupleList"
        return None
