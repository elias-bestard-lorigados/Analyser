from api import an_known_format as formats
from api.utils.generate_js_highcharts_code import add_js_code
import random
class BulletChart:
    """ Crear un grafo"""
    def __init__(self):
        self.type="bullet"
        self.kf_permited=[formats.LabeledTriosSeries,formats.TriosSeries,formats.PairsSeries]

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        name=self.type+" chart"
        js_code= add_js_code(format_known.elements,name,self.type,self.g_id)
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += js_code
        return text_to_return
    
    def generate(self,id):
        elements=[]
        series_nums=int(random.uniform(2,7))
        point_nums = int(random.uniform(7, 15))
        for i in range(series_nums):
          temp=[]
          for item in range(point_nums):
            temp.append([item, round(random.uniform(0, 15), 2),
                         round(random.uniform(0, 15), 2)])
          elements.append(temp)
        my_format=formats.TriosSeries(elements)
        code=self.graphic(id,my_format)
        return code,my_format