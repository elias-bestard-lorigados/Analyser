from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

from api.utils.rules import check_advance_over_time
from api.utils.rules import check_many_categories
from api.utils.rules import check_many_series
from api.utils.rules import check_continuous_numbres
from api.utils.rules import check_same_size_btwn_series
from api.utils.rules import check_same_x_intervals

class LineGraph(MyHighchart):
    """ Crear un grafico de linea """
    def __init__(self):
        super().__init__()
        self.message = ['comparison', 'distribution']
        self.type = "line"
        self.kf_permited=[formats.NumSeries,formats.PairsSeries,formats.LabeledPairSeries,formats.DictXy]
        self.options['title']= {'text': self.type+' chart'}
    
    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count=0
        if self.kf_permited.__contains__(type(kf)):
            count+=1
            #Verificando que sea una comparacion sobre tiempo, X progrsan
            if type(kf) == formats.LabeledPairSeries or type(kf)==formats.NumSeries:
                count += 2  # check_same_x_intervals y check_advance_over_time
            elif check_advance_over_time(kf):
                count += 1
            #Verificando Muchas categorias
            if check_many_categories(kf,3):
                count+=1
            #Verificando que tenga numeros continuos
            if check_continuous_numbres(kf):
                count += 1
            #Verificando que contenga varias series
            if check_many_series(kf):
                count += 1
            #verificando que las series tengan misma diferencia de intervalos
            if check_same_x_intervals(kf):
                    count += 1
            #Verificando que las series tengan igual tamanno
            if check_same_size_btwn_series(kf):
                count += 1
        return count
