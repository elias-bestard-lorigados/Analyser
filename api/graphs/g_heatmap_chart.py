from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class HeatmapChart(MyHighchart):
    """ Crear un Heat map """
    def __init__(self):
        super().__init__()
        self.message = []
        self.type = "heatmap"
        self.kf_permited=[formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]
        self.options['colorAxis']={'min': 0,'minColor': '#FFFFFF'}
        self.options['title']= {'text': self.type+' chart'}

    def generate(self, id):
        self.g_id = id
        elements = []
        series_nums = int(random.uniform(2, 7))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp = []
          for item in range(point_nums):
            temp.append([item, round(random.uniform(0, 15), 2),
                         round(random.uniform(0, 15), 2)])
          elements.append(temp)
        my_format = formats.TriosSeries(elements)
        code = self.graphic(id, my_format)
        return code, my_format

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count
