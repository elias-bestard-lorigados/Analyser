from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class PackedbubbleChart(MyHighchart):
    """ Crear un grafo"""
    def __init__(self):
        super().__init__()
        self.message = ['comparison']
        self.type = "packedbubble"
        self.kf_permited=[formats.LabeledPairSeries,formats.NumSeries,formats.PairsSeries]
        self.options["plotOptions"]["packedbubble"] = {
            'dataLabels': {
                'enabled': 'true',
                'format': '{point.name}',
                'style': {
                    'color': 'black',
                    'textOutline': 'none',
                    'fontWeight': 'normal'}},
            'minPointSize': 5
        }

    def generate(self, id):
        self.g_id = id
        elements = []
        series_nums = int(random.uniform(3, 10))
        point_nums = int(random.uniform(7, 20))
        for i in range(series_nums):
          temp = []
          for item in range(point_nums):
            temp.append(['label_'+str(item), round(random.uniform(1, 50), 2)])
          elements.append(temp)
        my_format = formats.LabeledPairSeries(elements)
        code = self.graphic(id, my_format)
        return code, my_format

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count
