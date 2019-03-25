from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class BubbleChart(MyHighchart):
    """ Crear un grafico de burbuja """
    def __init__(self):
        super().__init__()
        self.type="bubble"
        self.kf_permited=[formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]
        self.options['title']= {'text': self.type+' chart'}

    def generate(self,id):
        elements=[]
        series_nums=int(random.uniform(2,7))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp=[]
          for item in range(point_nums):
            temp.append([item, round(random.uniform(0, 15), 2),
                         round(random.uniform(0, 15), 2)])
          elements.append(temp)
        my_format=formats.TriosSeries(elements)
        code=self.graphic(id,my_format)
        return code,my_format
