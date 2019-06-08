from api import an_known_format as formats
import os
from random import uniform
import json
import re

class JsonCategories:
    """ espera un diccionario con llaves series_name 
    y valor dict con las categorias y lso valores numericos:
    {'serie_name1':{'label_1':#,'label_2':#,'label_3':#},
    'serie_name2':{'label_1':#,'label_2':#,'label_3':#},...}
    """

    def parse(self, data):
        """ Verificar que data tenga la estructura esperada"""
        try:
            info=self.procces(data)
            return info
        except:
            return None

    def procces(self,data):
        regex= re.compile('\d+(\.\d+)?')
        series=[]
        series_name=[]
        deserialization = json.loads(data)
        if len(deserialization)==0:
            return None
        categories=[item for item in deserialization[list(deserialization.keys())[0]]]
        #recorro todos los elementos del dictionario de series
        for serie in deserialization:
            #agrego el nombre de la serie
            series_name.append(serie)
            #seccionrar que contiene un dict con las cateorias y los valores
            if not type(deserialization[serie])==dict:
                return None
            temp=[]
            #recorro categorias
            for categorie in deserialization[serie]:
                # Si tiene categoria distinta a las definidas FIN
                if not categories.__contains__(categorie):
                    return None
                #verificar si son los valores de la serie
                match= regex.match(str(deserialization[serie][categorie]))
                if  match and match.end()==len(str(deserialization[serie][categorie])):
                    temp.append(deserialization[serie][categorie])
                else:
                    return None
            series.append(temp)
        formts=[]
        num_series=formats.NumSeries(series,series_name)
        num_series.categories=categories
        if num_series.count!=0:
            formts.append((num_series,1)) 
        chart_boxplot=formats.BoxplotSeries()
        chart_boxplot.calculate_boxplot_from_list(series,series_name)
        if len(chart_boxplot.elements)!=0:
            formts.append((chart_boxplot,1))
        return formts

    def help(self):
        return ''' parsea las lineas como una serie, de listas de diccionarios con categorias y su valor numerico
                EJ: 
                {'serie_name1':{'label_1':#,'label_2':#,'label_3':#},
                'serie_name2':{'label_1':#,'label_2':#,'label_3':#},...}'''

    def data_generator(self, path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_json_categories_")]
        file = open(path+"/d_json_categories_" +
                    str(len(data_files)+1)+".txt", "w")
        labl_count = int(uniform(1,amount))
        data = '{'
        for item in range(0, amount):
            middle_data = """"Serie_Name_"""+str(item)+"""" """
            middle_data += ':{'
            for label in range(labl_count):
                middle_data += '''"lbl_'''+str(label)+'''":'''+str(round(uniform(on_top,below),2))+''','''
            middle_data =middle_data[:-1]+"},"
            data += str(middle_data)+"\n"
        file.write(data[:-2]+"}")
        file.close()

