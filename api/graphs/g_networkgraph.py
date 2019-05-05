from api import an_known_format as formats
from api.utils.generate_js_highcharts_code import add_js_code
from api.utils.distributions import get_list_random
import random
class Networkgraph:
    """ Crear un grafo"""
    def __init__(self):
        self.type="networkgraph"
        self.kf_permited=[formats.StrPairSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        name=self.type+" chart"
        js_code= add_js_code(format_known.elements,name,self.type,self.g_id,format_known.keys)
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += js_code
        return text_to_return

    def generate(self,id):
        self.g_id = id
        elements = []
        numbs_vert = int(random.uniform(15, 50))
        labels = ['label_'+str(i+1) for i in range(numbs_vert)]
        for lbl in labels:
            count_neigh = int(random.uniform(0, numbs_vert))
            neightboors = get_list_random(labels, count_neigh)
            for item in neightboors:
                if item != lbl:
                    elements.append([lbl,item ])
        my_format= formats.StrPairSeries([elements])
        code=self.graphic(id,my_format)
        return code,my_format
