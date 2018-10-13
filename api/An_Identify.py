import re
from . import An_Format_Known as formats
from .Identify.Salto_Linea import Parser_Salto_Linea as per_line
from .Identify.Salto_Linea_List import Parser_Salto_Linea as per_line_list


# parsers = [per_line()]
# parsers = [ per_line_list()]
parsers = [per_line(), per_line_list()]


def identify(data):
    """ Trata de ir parseando la cadena 'data' por los parsers que ya existen 
        y si matchea con una grafico todos los graficos posibles """
    list_formats = []
    for item in parsers:
        format_ = item.parsea(data)
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    return list_formats
