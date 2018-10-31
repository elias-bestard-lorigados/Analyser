from .. import An_Format_Known as formats
import re


class JL_values_list:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    conteniendo varios valores numericos: value1 value2... +'\\n'+...
    Jump_line_values_list """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ 0-9]+[ \n]*)*')

    def parsea(self, data):
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
        formatos = []
        data=data.split('\n')
        elements=[]
        for item in data:
            elements.append([int(x) for x in re.findall("[0-9]+", item)])
        formatos.append(formats.Entire_ListOfList(elements))
        #annadir la lista de pares si tiene cantidad par los datos
        return formatos
