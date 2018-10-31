import re
from . import An_Format_Known as formats
from .Identify.PJL_value import JL_value as value_end
from .Identify.PJL_label_value import JL_label_value as label_value_end
from .Identify.PJL_values_list import JL_values_list as values_list
from .Identify.PJL_labels_val_list import JL_labels_val_list as labels_values


all_parsers = {"value_end": value_end(),
                "label_value_end": label_value_end(),
                "values_list": values_list(),
                "labels_values":labels_values(),
                "all": ["value_end", "label_value_end", "labels_values", "values_list"]}

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
    for item in list_formats:
        print(item.elements)
    return list_formats
