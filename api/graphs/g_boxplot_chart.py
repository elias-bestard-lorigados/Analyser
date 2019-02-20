from highcharts import Highchart
from api import an_known_format as formats

class BoxplotChart:
    """ Make a boxplot chart """
    def __init__(self):
        self.type="boxplot"
        self.kf_permited=[formats.BoxplotSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Generate the JS code of the chart and return it '''
        chart = Highchart(renderTo="chart_container_" +
                          str(self.g_id))
        chart.set_options('chart', {'zoomType': 'xy'})
        options = {
            'title': {
                'text': self.type+' chart'
            },
            'tooltip': {
                'pointFormat': '''{series.name}: 
                <b>
                    X: {point.x}, Y: {point.y}, Low: {point.low}, Q1: {point.q1}, Median: {point.median},
                    Q3: {point.q3}, High: {point.high} 
                </b>'''
            },
            'plotOptions': {
                'column': {
                    'allowPointSelect': True,
                    'dataLabels': {
                        'enabled': True
                    }}
            }}
        chart.set_dict_options(options)
        for item in format_known.elements:
            chart.add_data_set(
                format_known.elements[item],series_type=self.type, name=item)
        chart.buildhtml()
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += chart.content
        return text_to_return
