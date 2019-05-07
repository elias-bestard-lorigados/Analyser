from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random

from api.utils.rules import check_few_categories
from api.utils.rules import check_few_series
from api.utils.rules import check_many_categories
from api.utils.rules import check_similar_part_of_hole

class PieGraph(MyHighchart):
    """ Crear un grafico de Pie """
    def __init__(self):
        super().__init__()
        self.type = "pie"
        self.message = ['distribution']

        self.kf_permited=[formats.NumSeries,
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


    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
            #Verificando pocas categorias
            if check_few_categories(kf, 7) and check_many_categories(kf, 2):
                count += 1
            #Verificando que contenga solo 1 serie
            if check_few_series(kf, 2):
                count += 1
            #Verificando si contiene partes del total similares
            if not check_similar_part_of_hole(kf):
                count += 1
        return count
