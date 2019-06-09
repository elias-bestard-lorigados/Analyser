from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

from api.utils.rules import check_long_categories_name
from api.utils.rules import check_advance_over_time
from api.utils.rules import check_few_categories
from api.utils.rules import check_many_series
from api.utils.rules import check_same_size_btwn_series
from api.utils.rules import check_same_x_intervals


class BarChart(MyHighchart):
    """ Crear un grafico de barras """

    def __init__(self):
        super().__init__()
        self.message = ['comparison', 'distribution']
        self.type = "bar"
        self.kf_permited = [formats.NumSeries, formats.PairsSeries,
                            formats.LabeledPairSeries, formats.DictXy]
        self.options['title'] = {'text': self.type+' chart'}
        self.options['plotOptions']["bar"] = {
            "allowPointSelect": 'true', "dataLabels": {"enabled": 'true'}}

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 1
            #Verificando que  tenga categorias
            if len(kf.categories)!=0:
                count+=1
            #Verificando pocas categorias
            if check_few_categories(kf, 7):
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

            if check_long_categories_name(kf):
                count += 1
        return count
