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
        elements = []   #los elemetos tal como estan
        elements_pares = [] #elementos en pares si son cantidad de numeros pares
        for item in data:
            items = [int(x) for x in re.findall("[0-9]+", item)]
            elements.append(items)
            if len(items) % 2 == 1: #si la cantidad de elementos no es par le agrego el ultimo elemento denuevo para poder tener los puntos en pares
                items.append(items[-1])
            temp=[] #para ir almacenando las diferentes series de puntos si son numeros pares
            for i in range(0,len(items),2):
                temp.append([items[i], items[i+1]])
            elements_pares.append(temp)
        formatos.append(formats.Entire_ListOfList(elements))
        formatos.append(formats.Entire_ListOfList(elements_pares))
        return formatos
