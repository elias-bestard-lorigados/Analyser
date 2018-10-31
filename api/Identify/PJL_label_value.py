from .. import An_Format_Known as formats
import re

class JL_label_value:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    conteniendo e cada linea un "label"(string) seguido de un solo valor numerico: label + value +'\\n'+...
    Jump_line_label_value """

    def __init__(self):
        ''' RE ->label value 'salto' '''
        self._re = re.compile('([ A-z ]+ [0-9]+[ \n]*)*')

    def parsea(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con un label + num separados por saltos de linea
        label val"salto"... """
        if self._re.match(data).end()==len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera labels+numeros, separados por 'salto de linea'.
        Retorna una lista de FK """
        formatos=[]
        labels = []
        values = [int(item) for item in re.findall("[0-9]+", data)]
        data=data.split("\n")
        for item in data:
            label=''
            for x in re.findall("[A-z]+", item):
                label+=x+' '
            labels.append(label)
        formatos.append(formats.Pair_List(labels, values))
        elements = [[labels[i], values[i]] for i in range(len(values))]
        elements1 = [[[labels[i], values[i]]] for i in range(len(values))]
        formatos.append(formats.Entire_ListOfList(elements))
        formatos.append(formats.Entire_ListOfList(elements1))
        return formatos
