from highcharts import Highchart
from api import an_known_format as formats

class LineGraph:
    """ Crear un grafico de linea """
    def __init__(self):
        self.type="line"
        self.kf_permited=[formats.PairsList,formats.NumbersList,
                formats.ListOfSeriesnameAndValues,formats.NumbersListOfList]
    
    def graphic(self, g_id, format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="chart_container_" +
                          str(self.g_id))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Line Chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.y}</b>'
            },
            'plotOptions': {
                'line': {
                    'allowPointSelect': True,
                    'dataLabels': {
                        'enabled': True
                    }}
        }}
        chart.set_dict_options(options)
        for item in format_known.elements:
            if isinstance(item, int):
                chart.add_data_set(
                    format_known.elements[item], series_type="line")
            else:
                chart.add_data_set(
                    format_known.elements[item], series_type="line", name=item)
        chart.buildhtml()
        text_to_return = "<input type='checkbox' id="+str(self.g_id)+"> Is the following graph useful? </input>"
        text_to_return +=chart.content
        return text_to_return
