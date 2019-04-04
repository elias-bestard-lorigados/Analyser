from api import an_known_format as formats
import os
from random import uniform
import json

class DictXy:
    """ espera una lista de diccionarios con llaves x y name color:
        [{'x':VALUE,'y':VALUE,'name':VALUE,'color':value}...]
    """

    def parse(self, data):
        """ VErificar que data tenga la estructura esperada"""
        try:
            info=self.procces(data)
            return info
        except:
            return None

    def procces(self,data):
        data=data.split('\n')
        elements=[]
        for item in data:
            deserialization = json.loads(item)
            for x in deserialization:
                if not x.keys().__contains__('y') or (type(x['y']) != float and type(x['y']) != int):
                    return None
            elements.append(deserialization)
        return [(formats.DictXy(elements),1)]

    def help(self):
        return ''' parsea las lineas como una serie, de listas de diccionarios con keys x,y,name y color
                EJ: 
                [{'x':VALUE,'y':VALUE,'name':VALUE,'color':value}...]
                [{'x':VALUE,'y':VALUE,'name':VALUE,'color':value}...]'''

    def data_generator(self, path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_dict_xy_")]
        file = open(path+"/d_dict_xy_" +
                    str(len(data_files)+1)+".txt", "w")
        labl_count = 0
        data = ''
        for item in range(0, amount):
            num_of_elements = int(uniform(1, amount))
            temp = '['
            for x in range(0, num_of_elements):
                middle_data = '{'
                middle_data += '''"x":'''+str(x)
                middle_data += ''', "y":'''+str(round(uniform(on_top, below), 2))
                middle_data += ''', "name":"label_''' + str(labl_count)+'''"'''
                middle_data +="},"
                labl_count += 1
                temp+=middle_data
            data += str(temp[:-1]+"]")+"\n"
        file.write(data[:-1])
        file.close()

    def describe(self, line):
        """ Ver si matchea el texto "line" con la gramaitca definida
        retorna una None o una descripcioon del la line "DictXy" """
        try:
            info = self.procces(data)
            return "DictXy"
        except:
            return None
        return None
