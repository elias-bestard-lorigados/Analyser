from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

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
