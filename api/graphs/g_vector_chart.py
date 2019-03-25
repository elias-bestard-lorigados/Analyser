from api import an_known_format as formats
from api.utils.generate_js_highcharts_code import add_js_code
import random
class VectorChart:
    """ Crear un diagrama de vectores"""
    def __init__(self):
        self.type="vector"
        self.kf_permited=[formats.TriosSeries,formats.FourTupleSeries,formats.LabeledFourTupleSeries]

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
        elements = []
        numbs_series = int(random.uniform(1,6))
        count = int(random.uniform(20, 50))
        for i in range(numbs_series):
            temp=[]
            for item in range(count):
                y = int(random.uniform(1, 15))
                len_ = random.uniform(1, 3)
                direct = random.uniform(0, 360)
                temp.append([y, len_, direct])
            elements.append(temp)
        my_format=formats.TriosSeries(elements)
        code=self.graphic(id,my_format)
        return code,my_format
