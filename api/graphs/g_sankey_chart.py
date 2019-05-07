from api import an_known_format as formats
from api.utils.generate_js_highcharts_code import add_js_code 
from api.utils import distributions 
import random

class SankeyChart:
    """ Crear un diagrama de sankey"""
    def __init__(self):
        self.type="sankey"
        self.kf_permited=[formats.StrStrWeightSeries]
        self.message = []

    def graphic(self, g_id, format_known):
        """ Graficar los elementos """
        if not self.kf_permited.__contains__(type(format_known)):
            return None
        self.g_id = g_id
        return self.__make_js_code(format_known)

    def __make_js_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        name=self.type+" chart"
        js_code= add_js_code(format_known.elements,name,self.type,self.g_id,format_known.keys)
        text_to_return = "<input type='checkbox' id=" + \
            str(self.g_id)+"> Is the following chart useful? </input>"
        text_to_return += js_code
        return text_to_return

    def generate(self,id):
        self.g_id = id
        elements=[]
        current=0
        layers=[]
        for layer in range(int(random.uniform(3,7))):
            temp=[]
            for lbl in range(int(random.uniform(2,5))):
                current+=1
                temp.append('label_'+str(current))
            layers.append(temp)
        for i in range(len(layers)-1):
            for lbl1 in layers[i]:
                for lbl2 in layers[i+1]:
                    elements.append([lbl1,lbl2,int(random.uniform(1,5))])
        my_format=formats.StrStrWeightSeries([elements],['Test_'])
        code=self.graphic(id,my_format)
        return code,my_format

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count
