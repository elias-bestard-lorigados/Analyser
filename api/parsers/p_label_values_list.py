from .. import an_known_format as formats
import re


class LabelValuesList:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= linea= label + value1 value2 value3... val_i
        """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ A-z ]+[ 0-9]+[\n]*)*')

    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        if self._re.match(data).end() == len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera varios numeros separados por 'salto de linea'.
        Retorna una lista con FK"""
        formats_list = []
        labels = []
        values = []
        values_pairs=[]
        data = data.split("\n")
        for item in data:
            items = [int(y) for y in re.findall("[0-9]+", item)]
            values.append(items)
            if len(items)%2==1:
                items.append(items[-1])
            temp=[]
            for i in range(0,len(items),2):
                temp.append([items[i], items[i+1]])
            values_pairs.append(temp)
            label = ""
            for x in re.findall("[A-z]+", item):
                label += x+" "
            labels.append(label)
        formats_list.append(formats.ListOfSeriesnameAndValues(values, labels))
        formats_list.append(formats.ListOfSeriesnameAndValues(values_pairs, labels))
        return formats_list

    def help(self):
        return ''' parsea una cadena donde cada linea= label + value1 value2 value3... val_i +'\\n'+...
                EJ: 
                Madrid 34 38 12 3 1
                Barcelona 32 41 12 2 
                Atletico 23 32'''
