from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

class ScatterChart(MyHighchart):
    """ Crear un grafico de dispercion """
    def __init__(self):
        super().__init__()
        self.type="scatter"
        self.kf_permited=[formats.NumSeries,formats.PairsSeries,formats.LabeledPairSeries]
        self.options['title']= {'text': self.type+' chart'}
        