from .Grammars.Series_List_Gramar import Parse as parse
from .. import An_Format_Known as formats
import re


class Series_List:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    conteniendo varios valores numericos: [value1,value2...] +'\\n'+...
    """
    def parsea(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info=parse(data)
        if info:
            formts=[]
            formts.append(formats.Entire_ListOfList(info))
            return formts
        return None


