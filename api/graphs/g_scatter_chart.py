from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

from api.utils.rules import check_many_points_per_serie
from api.utils.rules import check_same_size_btwn_series
from api.utils.rules import check_same_x_intervals
from api.utils.rules import check_continuous_numbres
from api.utils.rules import check_few_series

class ScatterChart(MyHighchart):
    """ Crear un grafico de dispercion """
    def __init__(self):
        super().__init__()
        self.type="scatter"
        self.message = ['comparison', 'distribution','relation']
        self.kf_permited = [formats.NumSeries, formats.PairsSeries,
                            formats.LabeledPairSeries, formats.DictXy]
        self.options['title'] = {'text': self.type+' chart'}
        self.options['plotOptions']['scatter'] = {
            "marker": {"radius": 7, "states": {"hover": {"enabled": 'true', "lineColor": "rgb(100,100,100)"}}},
            "states": {"hover": {"marker": {"enabled": 'false'}}},
            "tooltip": {"headerFormat": "<b>{series.name}</b><br>", "pointFormat": "{point.x}, {point.y}"}
        }
    
    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
            #Verificando tener muchos puntos por serie
            if check_many_points_per_serie(kf,15):
                count += 1
            #Verificando que contenga solo 1 0 2 series
            if check_few_series(kf, 3):
                count += 1
            #Verificando que contenga diferentes puntos las series
            if not check_same_size_btwn_series(kf):
                count += 1
            #Verificando que contenga puntos dispersos sin orden
            if type(kf) == formats.LabeledPairSeries or type(kf) == formats.NumSeries or check_same_x_intervals(kf):
                    count += 1
            #Verificando que contenga puntos continuos
            if not check_continuous_numbres(kf):
                count += 1
        return count
