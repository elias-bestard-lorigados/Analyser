from api import an_known_format as formats
from api.utils.generate_js_highcharts_code import add_js_code
import random

from api.utils.rules import check_advance_over_time
from api.utils.rules import check_few_categories
from api.utils.rules import check_few_series
from api.utils.rules import check_same_size_btwn_series
from api.utils.rules import check_same_x_intervals

class BulletChart:
    """ Crear un grafo"""
    def __init__(self):
        self.message = ['comparison','distribution']
        self.type = "bullet"
        self.kf_permited=[formats.LabeledTriosSeries,formats.TriosSeries,formats.PairsSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        name=self.type+" chart"
        js_code= add_js_code(format_known.elements,name,self.type,self.g_id)
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += js_code
        return text_to_return
    
    def generate(self,id):
        self.g_id = id
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
            #Verificando pocas categorias
            if check_few_categories(kf, 7):
                count += 1
            #Verificando que contenga pocas series
            if check_few_series(kf):
                count += 1
            #verificando que las series tengan misma diferencia de intervalos
            if check_same_x_intervals(kf):
                    count += 1
            #Verificando que las series tengan igual tamanno
            if check_same_size_btwn_series(kf):
                count += 1
        return count
