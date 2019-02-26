from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

class BubbleChart(MyHighchart):
    """ Crear un grafico de burbuja """
    def __init__(self):
        super().__init__()
        self.type="bubble"
        self.kf_permited=[formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]
        self.options['title']= {'text': self.type+' chart'}

