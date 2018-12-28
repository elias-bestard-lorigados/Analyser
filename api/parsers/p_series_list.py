from .grammars.series_list_gramar import parse
from .. import an_known_format as formats
# import grammars
class SeriesList:
    """ parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
        [[labl,valu],vlaue,[value,value],....]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = parse(data)
        if info:
            formts=[]
            # formts.append(info)
            formts.append(formats.NumbersListOfList(info))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
                EJ: 
                [[primero,3.85],[segundo,4.28],[tercero,4],[cuarto,4.57],[quinto,4.25]]
                [2,3,4,5,6,21,12]
                [[1,1],[2,2],[3,3],[4,4]]'''
