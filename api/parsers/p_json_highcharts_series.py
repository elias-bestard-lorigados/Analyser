from api.parsers.grammars.g_numbers_list import g_numbers_list
from api import an_known_format as formats
import os
from random import uniform
import json

class JsonHighchartsSeries:
    """ espera un diccionario con llaves series_name y valor dict con las categorias y lso valores:
        [{'name':'serie_name1','data':[#,#,#,...,#]}...]
    """

    def parse(self, data):
        """ Verificar que data tenga la estructura esperada"""
        try:
            info=self.procces(data)
            return info
        except:
            return None

    def procces(self,data):
        series=[]
        series_name=[]
        categories=[]
        deserialization = json.loads(data)
        if len(deserialization)==0:
            return None
        base=[item for item in deserialization[0]]
        #recorro todos los elementos de la lista de series
        for serie in deserialization:
            #seccionrar que contiene un dict con las cateorias y los valores
            if not type(serie)==dict:
                return None
            #recorro el contenido del dictio
            for categorie in serie:
                # Si tiene categoria distinta a las definidas FIN
                if not base.__contains__(categorie):
                    return None
                #verificar si son los valores de la serie
                if type(serie[categorie])==list and g_numbers_list.parse(str(serie[categorie])):
                    series.append(serie[categorie])
                elif categorie=="name":
                    #agrego el nombre de la serie
                    series_name.append(serie[categorie])
                else:
                    categories.append((categorie,serie[categorie]))
        formts=[]
        num_series=formats.NumSeries(series,series_name)
        if len(num_series.elements)!=0:
            formts.append((num_series,1)) 
        chart_boxplot=formats.BoxplotSeries()
        chart_boxplot.calculate_boxplot_from_list(series,series_name)
        if len(chart_boxplot.elements)!=0:
            formts.append((chart_boxplot,1))
        return formts

    def help(self):
        return ''' parsea las lineas como una serie, de listas de diccionarios con keys x,y,name y color
                EJ: 
                [{'name':'serie_name1','data':[#,#,#,...,#]},
                {'name':'serie_name2','data':[#,#,#,...,#]},...]'''

    def data_generator(self, path, amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_json_highcharts_series")]
        file = open(path+"/d_json_highcharts_series_" +
                    str(len(data_files)+1)+".txt", "w")
        labl_count = 0
        len_data=int(uniform(1,amount))
        data = '['
        for item in range(0, amount):
            num_of_elements = int(uniform(1, amount))
            middle_data = '{'
            middle_data += """"name":"Serie_Name_"""+str(item)+"""", """
            middle_data += '''"data":'''+str([round(uniform(on_top,below),2) for i in range(0,len_data)])
            middle_data +="},"
            labl_count += 1
            data += str(middle_data)+"\n"
        file.write(data[:-2]+"]")
        file.close()
