from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart
import random

class BoxplotChart(MyHighchart):
    """ Make a boxplot chart """
    def __init__(self):
        super().__init__()
        self.message = ['comparison']
        self.type = "boxplot"
        self.kf_permited=[formats.BoxplotSeries]
        self.options['title']= {'text': self.type+' chart'}
        self.options['tooltip']= {
                    'pointFormat': '''{series.name}: 
                    <b>
                        Low: {point.low}, Q1: {point.q1}, Median: {point.median},
                        Q3: {point.q3}, High: {point.high} 
                    </b>'''}

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count

    def generate(self, id):
        '''Genera un gráfico con valores aleatorios '''
        self.g_id = id
        elements = []
        series_nums = int(random.uniform(2, 7))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp = [round(random.uniform(0, 15), 2) for item in range(point_nums)]
          elements.append(temp)
        my_format = formats.BoxplotSeries()
        my_format.calculate_boxplot_from_list(elements)
        code = self.graphic(id, my_format)
        return code, my_format
