from api import an_known_format as formats
from charts_hierarchy.my_chart import MyChart
import random


class VectorChart(MyChart):
    """ Crear un diagrama de vectores"""
    def __init__(self):
        super().__init__()
        self.message = []
        self.type = "vector"
        self.kf_permited=[formats.TriosSeries,formats.FourTupleSeries,formats.LabeledFourTupleSeries]

    def generate(self,id):
        self.g_id = id
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

    def evaluate_rules(self, kf):
        ''' Evalua las reglas que puntua al grafico y retorna el monto de puntos obtenido '''
        count = 0
        if self.kf_permited.__contains__(type(kf)):
            count += 2
        return count
