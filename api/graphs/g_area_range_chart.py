from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class AreaRangeChart(MyHighchart):
    """ Crear un grafico de area por rango """
    def __init__(self):
        super().__init__()
        self.type="arearange"
        self.kf_permited=[formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]
        self.options['title']= {'text': self.type+' chart'}

    def generate(self, id):
        self.g_id = id
        elements = []
        series_nums = int(random.uniform(1, 4))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp = []
          for item in range(point_nums):
            temp.append([round(random.uniform(0, 7), 2),
                         round(random.uniform(4, 11), 2)])
          elements.append(temp)
        my_format = formats.PairsSeries(elements)
        code = self.graphic(id, my_format)
        return code, my_format
