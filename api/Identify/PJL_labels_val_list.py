from .. import An_Format_Known as formats
import re


class JL_labels_val_list:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    conteniendo un label y varios valores numericos:label+ value1 value2... +'\\n'+...
    Jump_line_lebels_values_list """

    def __init__(self):
        ''' RE -> value1 value2... '''
        self._re = re.compile('([ A-z ]+[ 0-9]+[\n]*)*')

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
        labels = []
        values = []
        data = data.split("\n")
        for item in data:
            values.append([int(y) for y in re.findall("[0-9]+", item)])
            label = ""
            for x in re.findall("[A-z]+", item):
                label += x+" "
            labels.append(label)
        formatos.append(formats.List_Tuple(values, labels, series=True))
        #annadir la lista de pares si tiene cantidad par los datos
        return formatos


