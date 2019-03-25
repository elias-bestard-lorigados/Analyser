from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class PolarAreaChart(MyHighchart):
    """ Crear un grafico polar """
    def __init__(self):
        super().__init__()
        self.type="area"
        self.kf_permited=[formats.NumSeries,formats.PairsSeries,formats.LabeledPairSeries]
        self.options['chart']={'polar': True,'type': 'area'}
        self.options['title']= {'text': self.type+' chart'}
        self.options['xAxis']= {'tickmarkPlacement': 'on','lineWidth': 0}
        self.options['yAxis']= {
                    'gridLineInterpolation': 'polygon',
                    'lineWidth': 0,
                    'min': 0
                }

    def generate(self,id):
        elements=[]
        len_comp=int(random.uniform(3,9))
        categories=['label_'+str(item) for item in range(len_comp)]
        self.options['xAxis']= {'categories':categories,'tickmarkPlacement': 'on','lineWidth': 0}
        for serie in range(int(random.uniform(1,5))):
            temp=[]
            for lbl in range(len_comp):
                temp.append(int(random.uniform(1,15)))
            elements.append(temp)
        my_format=formats.NumSeries(elements)
        code=self.graphic(id,my_format)
        return code,my_format