import re
from . import An_Format_Known as formats
from .Identify.Salto_Linea import Parser_Salto_Linea as per_line

def is_empty(lista):
    for item in lista:
        item2=item.replace(" ","")
        if item2 != "" :
            return False
    return True
def sub_str(text,inicio,fin):
    result=""
    for item in range(inicio,fin):
        result+=text[item]
    return result

class Parser_Salto_Linea_large:
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
            name = sub_str(item, alph.match(item).start(),
                           alph.match(item).end())
            temp = sub_str(item, alph.match(item).end(), len(item)).split(" ")
            value = [int(item) for item in temp if item != ""]
            names.append(name)
            values.append(value)
            tuplas.append((name, value))
        if not is_empty(names):
            return formats.Entire_ListOfListPair(tuplas)
        return formats.Entire_ListOfList(values)


parsers = [per_line()]
# parsers = [per_line(), Parser_Salto_Linea_large()]
# parsers = [ Parser_Salto_Linea_large()]


def identify(data):
    """ Trata de ir parseando la cadena 'data' por los parsers que ya existen 
        y si matchea con una grafico todos los graficos posibles """
    list_formats = []
    for item in parsers:
        format_ = item.parsea(data)
        if format_ != None:  # si se pudo parsear
            # list_formats.append(format_)
            list_formats.extend(format_)
    return list_formats
