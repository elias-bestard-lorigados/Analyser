from .. import an_known_format as formats
import re


class ValuesList:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= value1 value2...value_i '\\n'+...
        """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ 0-9]+[ \n]*)*')

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
        data=data.split('\n')
        elements = []   #los elemetos tal como estan
        elements_pairs = [] #elementos en pairs si son cantidad de numeros pairs
        for item in data:
            items = [int(x) for x in re.findall("[0-9]+", item)]
            elements.append(items)
            if len(items) % 2 == 1: #si la cantidad de elementos no es par le agrego el ultimo elemento denuevo para poder tener los puntos en pairs
                items.append(items[-1])
            temp=[] #para ir almacenando las diferentes series de puntos si son numeros pairs
            for i in range(0,len(items),2):
                temp.append([items[i], items[i+1]])
            elements_pairs.append(temp)
        formats_list.append(formats.NumbersListOfList(elements))
        formats_list.append(formats.NumbersListOfList(elements_pairs))
        return formats_list


    def help(self):
        return ''' parsea una cadena con cada linea= value '\\n'+...
                EJ: 
                34 12 123 32
                32 13 45 
                23  12'''
