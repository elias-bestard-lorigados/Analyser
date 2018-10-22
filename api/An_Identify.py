import re
from . import An_Format_Known as formats
from .Identify.Salto_Linea import Parser_Salto_Linea as per_line
from .Identify.Salto_Linea_List import Parser_Salto_Linea as per_line_list


all_parsers = {"per_line":per_line(),
                "per_line_list": per_line_list(),
                "all":["per_line","per_line_list"]}

def identify(data,parsers):
    """ Trata de ir parseando la cadena 'data' por los parsers que pasan como parametro
        y retorna una lista de todos los formatos conocidos posibles"""
    if parsers.__contains__("all"):
        parsers=all_parsers["all"]
    list_formats = []
    for item in parsers:
        format_ = all_parsers[item].parsea(data)
        if format_ != None:  # si se pudo parsear
            list_formats.extend(format_)
    return list_formats


# all_parsers = [per_line(), per_line_list()]
# def identify(data):
#     """ Trata de ir parseando la cadena 'data' por los parsers que ya existen 
#         y si matchea con una grafico todos los graficos posibles """
#     list_formats = []
#     for item in all_parsers:
#         format_ = item.parsea(data)
#         if format_ != None:  # si se pudo parsear
#             list_formats.extend(format_)
#     return list_formats
