from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class SplineInvertedChart(MyHighchart):
    """ Crear un spline """
    def __init__(self):
        super().__init__()
        self.type="spline"
        self.kf_permited = [formats.NumSeries, formats.PairsSeries,
                            formats.LabeledPairSeries, formats.DictXy]
        self.options['title']= {'text': self.type+' chart'}
        self.options['chart']={'inverted': True}
    def generate(self,id):
        elements=[]
        series_nums=int(random.uniform(1,5))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp=[]
          for item in range(point_nums):
            temp.append([item,round(random.uniform(0,15),2)])
          elements.append(temp)
        my_format=formats.PairsSeries(elements)
        code=self.graphic(id,my_format)
        return code,my_format
