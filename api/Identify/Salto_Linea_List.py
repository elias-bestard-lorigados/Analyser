from .. import An_Format_Known as formats
import re


class Parser_Salto_Linea:
    """ Parsear un texto en saltos de linea esperando que tenga varios valores separados por espacio
    """

    def __init__(self):
        # RE -> (string )* value
        self._re = re.compile(
            '(([A-z]*()*[A-z]*[0-9]*)* ([0-9]*( )*)*[\s]*)+|(([0-9]*( )*)*[\n]*)+')

    def parsea(self, text):
        """ Ver si matchea el texto text completo!!! con la expresion regular definida! """
        if self._re.match(text).end() == len(text):
            return self.by_line(text)
        return None

    def by_line(self, data):
        """ Procesa el string 'data'.
        Espera los elementos separados por 'salto de linea' y pueden tener un Label antes del valor,
        contienene varios valores separadospor espacios
        Retorna un 'An_Format_Known.Entire_ListOfList'"""
        alph = re.compile(
            '([A-z]*( )*)*')

        data = data.split("\n")
        names, values, tuplas = [], [], []
        for item in data:
            temp = item.split()
            name=""
            value=[]
            for i in temp:
                if alph.match(i).end()!=0:
                    name+=i+" "
                else:
                    value.append(int(i)) 
            names.append(name)
            values.append(value)
            tuplas.append((name, value))
        formatos=[]
        formatos.append(formats.List_Tuple(tuplas))
        formatos.append(formats.Entire_ListOfList(values))
        return formatos
