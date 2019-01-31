from matplotlib import pyplot as plt
from highcharts import Highchart

# def IsListOfTuple_StrInt(list):
#     """ Chequea que 'list' sea una lista de tuplas[(str,int)].
#     Retorna dos listas, ([str],[int]) """
#     labels = []
#     values = []
#     for item in list:
#         if type(item) == tuple:
#             labels.append(item[0])
#             values.append(item[1])
#         else:
#             labels.append("")
#             values.append(item)
#     return labels, values


class LineGraph:
    """ Crear un grafico de linea """

    def graphic(self, g_id, format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        self.g_id = g_id
        # if output == "stdout":
        #     return self.__make_graph(format_known)
        return self.__make_js_code(format_known)

    def __make_graph(self, format_known):
        ''' hace el grafico en pyplot '''
        for item in format_known.elements:
            # labels, values = IsListOfTuple_StrInt(format_known.elements[item])
            # plt.plot(values)
            pass
        # plt.show()

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="line_container_" +
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
        return chart.content
