from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
from api.utils.distributions import get_list_random
import random
class Networkgraph(MyHighchart):
    """ Crear un grafo"""
    def __init__(self):
        super().__init__()
        self.type="networkgraph"
        self.message = []
        self.kf_permited = [formats.StrPairSeries]

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

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count
