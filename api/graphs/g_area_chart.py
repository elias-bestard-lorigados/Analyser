from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

class AreaChart(MyHighchart):
    """ Crear un grafico de areas """
    def __init__(self):
        super().__init__()
        self.type="area"
        self.kf_permited = [formats.NumSeries, formats.PairsSeries,
                            formats.LabeledPairSeries, formats.DictXy]
        self.options['title']= {'text': self.type+' chart'}
