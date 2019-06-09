from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random

from api.utils.rules import check_part_of_hole
from api.utils.rules import check_few_categories
from api.utils.rules import check_few_series
from api.utils.rules import check_many_categories

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
                    'allowPointSelect': 'true',
                    'format': '<b>{point.name}</b>: {point.value} ',
                    'dataLabels': {
                        'enabled': 'true'
                    },
                    'showInLegend': 'true'
                }
            }
        self.options['tooltip']= {'pointFormat': '{series.name}: <b>{point.y:.1f}</b>'}
        self.options['title']= {'text': self.type+' chart'}

    def graphic(self, g_id, known_format):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(known_format)) or known_format.count > 1:
            return None
        self.g_id = g_id
        meds=known_format.elements.pop('Meds_Series')
        mins=known_format.elements.pop('Mins_Series')
        maxs=known_format.elements.pop('Maxs_Series')
        code= self._make_js_code(known_format)
        known_format.elements['Meds_Series']=meds
        known_format.elements['Mins_Series']=mins
        known_format.elements['Maxs_Series']=maxs
        return code

    def generate(self,id):
        self.g_id = id
        elements=[]
        slices_nums=int(random.uniform(2,9))
        total=100
        while slices_nums!=0:
            temp=round(random.uniform(1,total),2)
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
                count += 2
            if check_part_of_hole(kf):
                count += 1
        return count
