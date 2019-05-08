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
        data = StringIO(data)
        csvreader = csv.reader(data)
        rows = []
        csvreader = list(csvreader)

        for i in range(0, len(csvreader)):
            for j in range(len(csvreader[i])):
                if csvreader[i][j] == '':
                    csvreader[i][j] = '0'
                if self.__is_num(csvreader[i][j]):
                    csvreader[i][j] = float(csvreader[i][j])
                elif i!=0 and j!=0:
                    csvreader[i][j] = 0
            rows.append(csvreader[i])

        series_name = [] if self.__has_series_name == 0 else rows[0]
        series = self.__invert_matrix(
            rows) if self.__has_series_name == 0 else self.__invert_matrix(rows[1:])
        if len(series)!=0:
            categories = [] if not self.__check_series_name_line(
                series[0]) else series[0]
        else: categories=[]
        series = series if categories == [] else series[1:]

        formats_list=[]
        kf=formats.NumSeries(series,series_name)
        kf.categories=categories
        if len(kf.elements) != 0:
            formats_list.append((kf, 1))
        chart_boxplot = formats.BoxplotSeries()
        chart_boxplot.categories=categories
        chart_boxplot.calculate_boxplot_from_list(series,series_name)
        if len(chart_boxplot.elements) != 0:
            formats_list.append((chart_boxplot, 1))
        return formats_list

    def check_csv(self, text: str, separator=','):
        ''' Chequea que text sean labels separados por comas y numeros separados por coma
        Formato CSV donde todas las filas tienen la misma longitud'''
        series = '([ A-Za-z0-9_ ]*'+separator+'*([0-9]+(.[0-9]+)*)+[ \n]*)*'
        regex = re.compile(series)
        text = text.split("\n")
        if len(text) == 0:
            return False
        begin = 1 if self.__check_series_name_line(
            text[0].split(separator)) else 0
        self.__has_series_name = begin
        long = len(text[0].split(separator))
        for i in range(begin, len(text)):
            if regex.match(text[i]).end() != len(text[i]):
                return False
            if len(text[i].split(separator)) != long:
                return False
        return True

    def __check_series_name_line(self, line: list, separator=','):
        ''' Chequea que la linea sean lbl'''
        for item in line:
            if not self.__is_num(item):
                return True
        return False

    def __is_num(self, cadena: str):
        ''' Chequea si la cadena es un numero 
        considero que sea lbl si no es un numero'''
        num = '[0-9]+(.[0-9]+)*'
        regex = re.compile(num)
        match = regex.match(str(cadena))
        if match == None or match.end() != len(str(cadena)):
            return False
        return True

    def help(self):
        return ''' parsea una cadena con formato CSV
                por default espera los valores separados por ','
                EJ: 
                nombres/series,serie1,serie2,serie3
                Madrid,34,38,12
                Barcelona,32,41,12
                Atletico,23,32,24
                Paris,31,12,31'''

    def data_generator(self, path, amount=50, on_top=50, below=100, separator=','):
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

    def __invert_matrix(self, matrix):
        ''' Invertir matriz '''
        if len(matrix)==0:
            return []
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
