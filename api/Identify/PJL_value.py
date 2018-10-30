from .. import An_Format_Known as formats
import re

class JL_value:
    """ Parser que trata de ver si un texto esta separado en saltos de linea
    conteniendo un solo valor numerico: value +'\\n'+...
    Jump_line_value """

    def __init__(self):
        ''' RE -> value '''
        self._re = re.compile('([0-9\n]+)*')

    def parsea(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        if self._re.match(data).end()==len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera numeros separados por 'salto de linea'.
        Retorna una lista con 'An_Format_Known.Pair_Label_EntireP_List' o 'An_Format_Known.Entire_Pos_List' """
        formatos=[]
        data = re.sub("( )*", '', data)
        data = re.sub("[\n]", ' ', data)
        data = [int(item) for item in data.split()]
        formatos.append(formats.Entire_Pos_List(data))
        #annadir la lista de pares si tiene cantidad par los datos
        return formatos


