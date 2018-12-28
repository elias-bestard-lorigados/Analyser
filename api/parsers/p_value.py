from .. import an_known_format as formats
import re

class Value:
    """Intenta parsear una cadena en saltos de linea  donde
        cada linea= value '\\n'+...
        """

    def __init__(self):
        ''' RE -> value '''
        self._re = re.compile('([0-9\n]+)*')

    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la expresion regular definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        if self._re.match(data).end()==len(data):
            return self.process(data)
        return None

    def process(self, data):
        """ Procesa el string 'data'.
        Espera numeros separados por 'salto de linea'.
        Retorna una lista con 'An_Format_Known.Pair_Label_EntireP_List' o 'An_Format_Known.NumbersList' """
        formats_list=[]
        data = re.sub("( )*", '', data)
        data = re.sub("[\n]", ' ', data)
        data = [int(item) for item in data.split()]
        formats_list.append(formats.NumbersList(data))
        if len(data)%2==0:
            pairs=[(data[x],data[x+1]) for x in range(0,len(data),2)]
            pairs_list=[[(data[x],data[x+1])] for x in range(0,len(data),2)]
            labels = [data[x] for x in range(0, len(data), 2)]
            values = [data[x+1] for x in range(0, len(data), 2)]
            formats_list.append(formats.PairsList(labels, values))
            formats_list.append(formats.NumbersListOfList(pairs))
            formats_list.append(formats.NumbersListOfList(pairs_list))
        return formats_list

    def help(self):
        return ''' parsea una cadena con cada linea= value '\\n'+...
                EJ: 
                34
                32
                23 '''

