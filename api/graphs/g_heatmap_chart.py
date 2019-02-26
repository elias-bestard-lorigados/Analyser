from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

class HeatmapChart(MyHighchart):
    """ Crear un Heat map """
    def __init__(self):
        super().__init__()
        self.type="heatmap"
        self.kf_permited=[formats.PairsSeries,
                        formats.TriosSeries,formats.LabeledTriosSeries]
        self.options['colorAxis']={'min': 0,'minColor': '#FFFFFF'}
        self.options['title']= {'text': self.type+' chart'}

