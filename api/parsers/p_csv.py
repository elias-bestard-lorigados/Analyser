from api import an_known_format as formats
from io import StringIO
from random import uniform
import re
import os
import csv

class Csv:
    """Chequea si la cadena son listas separadas por comas
    si lo es asume que es un CSV file y la procesa"""
    
    def __init__(self):
        self.__has_series_name = 0
        self.__has_categories_name = 0

    def parse(self, data, separator=','):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... 
        separator es el separador que espera entre numeros, default ',' """
        if self.check_csv(data, separator):
            return self.process(data, separator)
        return None

    def process(self, data, separator=','):
        """ Procesa el string 'data'.
        Espera csv format for data"""
        formats_list = []
        data = StringIO(data)
        csvreader = csv.reader(data)
        values = []
        csvreader = list(csvreader)
        self.__has_categories_name=1 if self.__check_lbls_line([item[0] for item in csvreader],separator) else 0

        for i in range(self.__has_series_name, len(csvreader)):
            values_temp=[]
            for j in range(self.__has_categories_name,len(csvreader[i])):
                if csvreader[i][j] == '' or self.__is_num(csvreader[i][j])==False:
                    csvreader[i][j] = 0
                values_temp.append(float(csvreader[i][j]))
            values.append(values_temp)
        #si la primera fila tiene lbl la considero series names
        series_name=[str(item) for item in csvreader[0][self.__has_categories_name:]] if self.__has_series_name == 1 else []
        #si la primera columna tiene strings es categorias/series_name
        categories = [str(item[0]) for item in csvreader[self.__has_series_name:]] if self.__has_categories_name == 1 else []
        series=[]
        categories = self.rename(categories)
        series_name = self.rename(series_name)
        #creo los KF
        kf = formats.NumSeries(values,series_name)
        kf.categories = categories
        if len(kf.elements) != 0:
            formats_list.append((kf, 1))
        chart_boxplot = formats.BoxplotSeries()
        chart_boxplot.calculate_boxplot_from_list(series, series_name)
        # chart_boxplot.categories = categories
        if len(chart_boxplot.elements) != 0:
            formats_list.append((chart_boxplot, 1))
        #invierto la matriz de valores
        series = self.__invert_matrix(values)
        #creo los KF
        kf=formats.NumSeries(series,categories)
        kf.categories=series_name
        if len(kf.elements) != 0:
            formats_list.append((kf, 1))
        chart_boxplot = formats.BoxplotSeries()
        chart_boxplot.calculate_boxplot_from_list(series,categories)
        #chart_boxplot.categories=series_names
        if len(chart_boxplot.elements) != 0:
            formats_list.append((chart_boxplot, 1))
        return formats_list

    def check_csv(self, text: str, separator=','):
        ''' Chequea que text sean labels y numeros separados por comas
        Formato CSV donde todas las filas tienen la misma longitud'''
        text = text.split("\n")
        if len(text) == 0:
            return False
        lines=[item.split(separator) for item in text]
        # self.__has_series_name dice si la primera fila del archivo contiene algun lbl
        self.__has_series_name = 1 if self.__check_lbls_line(lines[0]) else 0
        # long para asegurarme que todas las filas tienen la misma longitud
        long = len(lines[0])
        for i in range(self.__has_series_name, len(lines)):
            if len(lines[i]) != long:
                return False
        return True
    
    def __check_lbls_line(self, line: list, separator=','):
        ''' Chequea que la linea contenga almenos un lbl'''
        for item in line:
            if not self.__is_num(item):
                return True
        return False
    
    def __is_num(self, cadena: str):
        ''' Chequea si la cadena es un numero 
        considero que sea lbl si no es un numero'''
        num = "\d+(\.\d+)?"
        regex = re.compile(num)
        match = regex.match(str(cadena))
        if match == None or match.end() != len(str(cadena)):
            return False
        return True
    
    def __invert_matrix(self, matrix):
        ''' Invertir matriz '''
        if len(matrix)==0:
            return []
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    def rename( self,lista: list):
        new_list=[]
        for i in range(0, len(lista)):
            temp = lista[i]
            lista.remove(lista[i])
            if new_list.__contains__(temp):
                temp = temp+'~_~'+str(i)
            lista.insert(i,temp)
            new_list.append(temp)
        return new_list

    def help(self):
        return ''' parsea una cadena con formato CSV
                por default espera los valores separados por ','
                EJ: 
                nombres/series,serie1,serie2,serie3
                Madrid,34,38,12
                Barcelona,32,41,12
                Atletico,23,32,24
                Paris,31,12,31'''

    def data_generator(self, path, amount=20, on_top=50, below=100, separator=','):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_csv_")]
        file = open(path+"/d_csv_" +
                    str(len(data_files)+1)+".txt", "w")
        series_len = int(uniform(1, amount))
        for item in range(0, amount):
            data = ''
            data += "lbl_"+str(item)+separator
            for x in range(0, series_len):
                data += str(int(uniform(on_top, below)))+separator
            file.write(data[:-1]+"\n")
        file.close()
