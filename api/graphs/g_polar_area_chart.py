from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random

from api.utils.rules import check_many_categories
from api.utils.rules import check_advance_over_time
from api.utils.rules import check_few_series
from api.utils.rules import check_same_size_btwn_series
from api.utils.rules import check_same_x_intervals

class PolarAreaChart(MyHighchart):
    """ Crear un grafico polar """
    def __init__(self):
        super().__init__()
        self.message = ['comparison', 'distribution']
        self.type = "area"
        self.kf_permited=[formats.NumSeries,formats.PairsSeries,formats.LabeledPairSeries]
        self.options['chart']={'polar': 'true','type': 'area'}
        self.options['title']= {'text': self.type+' chart'}
        self.options['xAxis']= {'tickmarkPlacement': 'on','lineWidth': 0}
        self.options['yAxis']= {
                    'gridLineInterpolation': 'polygon',
                    'lineWidth': 0,
                    'min': 0
                }
    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)) or format_known.count < 3:
            return None
        self.g_id = g_id
        return self._make_js_code(format_known)
    def generate(self,id):
        self.g_id = id
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

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
            #Verificando que sea una comparacion sobre tiempo, X progrsan
            if type(kf) == formats.LabeledPairSeries or type(kf) == formats.NumSeries:
                count += 2  # check_advance_over_time y check_same_x_intervals
            elif check_advance_over_time(kf):
                count += 1
            #Verificando que las series tienen la misma longitud
            if not check_same_size_btwn_series(kf):
                count += 1
            #Verificando que las series tengan los mismos intervalos en las categorias
            if type(kf) != formats.LabeledPairSeries or type(kf) != formats.NumSeries and not check_same_x_intervals(kf):
                count += 1
            #Verificando tener mas de 3 categorias
            if not check_many_categories(kf, 3):
                count += 1
            #Verificando que contenga menos de 10 series
            if not check_few_series(kf,10):
                count += 1
        return count
