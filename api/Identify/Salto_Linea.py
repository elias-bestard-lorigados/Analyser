from .. import An_Format_Known as formats
import re

class Parser_Salto_Linea:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    de la forma: "label" " " "value"
    or: "value" fin "value"
     """

    def __init__(self):
        # RE -> (string )* value
        self._re = re.compile(
            '((([A-z]*()*[A-z]*[0-9]*) * [0-9]*()*(\n)*)+|([0-9]*[\n]*)+)*')

    def parsea(self, text):
        """ Ver si matchea el texto text completo!!! con la expresion regular definida! """
        if self._re.match(text).end() == len(text):
            return self.process(text)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera los elementos separados por 'salto de linea' y pueden tener un Label antes del valor.
        Retorna una lista con 'An_Format_Known.Pair_Label_EntireP_List' o 'An_Format_Known.Entire_Pos_List' """

        data = data.split("\n")
        names, values, tuplas = [], [], []
        for item in data:  # recorrer cada linea
            temp = item.split()
            name = ""
            value = int(temp[-1])
            for rest in temp[:-1]:
                name += rest+" "
            names.append(name)
            values.append(value)
            tuplas.append((name, value))
        formatos=[]
        # formatos.append(formats.Pair_List(tuplas))
        formatos.append(formats.Pair_List(tuplas))
        # formatos.append(formats.Entire_Pos_List(values))
        return formatos

