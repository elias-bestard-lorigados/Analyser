from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random
class PieGraph(MyHighchart):
    """ Crear un grafico de Pie """
    def __init__(self):
        super().__init__()
        self.type = "pie"
        self.kf_permited=[formats.NumSeries,
                        formats.PairsSeries,
                          formats.LabeledPairSeries, formats.DictXy]
        self.options['plotOptions']= {
                'pie': {
                    'allowPointSelect': True,
                    'format': '<b>{point.name}</b>: {point.value} ',
                    'dataLabels': {
                        'enabled': True
                    },
                    'showInLegend': True
                }
            }
        self.options['tooltip']= {'pointFormat': '{series.name}: <b>{point.y:.1f}</b>'}
        self.options['title']= {'text': self.type+' chart'}

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)) or format_known.count > 1:
            return None
        self.g_id = g_id
        return self._make_js_code(format_known)
    def generate(self,id):
        self.g_id = id
        elements=[]
        slices_nums=int(random.uniform(2,9))
        total=100
        while slices_nums!=0:
            temp=random.uniform(1,total)
            elements.append(['label_'+str(slices_nums),temp])
            total-=temp
            slices_nums-=1
        my_format=formats.LabeledPairSeries([elements])
        code=self.graphic(id,my_format)
        return code,my_format
