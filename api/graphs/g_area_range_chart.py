from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random

from api.utils.rules import check_advance_over_time
from api.utils.rules import check_few_series
from api.utils.rules import check_y_over_x

class AreaRangeChart(MyHighchart):
    """ Crear un grafico de area por rango """
    def __init__(self):
        super().__init__()
        self.message = ['comparison']
        self.type = "arearange"
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

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
            #Verificando que sea una comparacion sobre tiempo, X progrsan
            if type(kf) == formats.LabeledTriosSeries or type(kf) == formats.PairsSeries:
                count += 1
            elif check_advance_over_time(kf):
                count += 1
            #Verificando que contenga pocas series
            if check_few_series(kf,4):
                count += 1
            #verificando que las series tengan valores de Z o Y mayores que Y o X respect
            type_kf = 1 if type(kf) == formats.PairsSeries else 0
            if check_y_over_x(kf, type_kf):
                count += 1
        return count
