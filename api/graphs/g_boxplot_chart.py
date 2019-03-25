from highcharts import Highchart
from api import an_known_format as formats
from charts_hierarchy.my_highchart import MyHighchart

class BoxplotChart(MyHighchart):
    """ Make a boxplot chart """
    def __init__(self):
        super().__init__()
        self.type="boxplot"
        self.kf_permited=[formats.BoxplotSeries]
        self.options['title']= {'text': self.type+' chart'}
        self.options['tooltip']= {
                    'pointFormat': '''{series.name}: 
                    <b>
                        X: {point.x}, Y: {point.y}, Low: {point.low}, Q1: {point.q1}, Median: {point.median},
                        Q3: {point.q3}, High: {point.high} 
                    </b>'''}

