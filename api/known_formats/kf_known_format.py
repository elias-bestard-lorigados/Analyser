class KnownF:
    def __init__(self, s_values=[],series_names=[]):
        self.elements = {}  #almacena las series, las llaves son los nombres de estas
        self.min_value = 9999999999 #valor mínimo
        self.max_value = -999999999    #valor máximo
        self.count = len(s_values)  #cantidad de series
        self.categories = []    #nombre de las categorías
        self.keys = []
    def extend(self,kf_to_extend):
        ''' Extiende el KF self, con el KF kf_to_extend
        agregando a los elements los de kf_to_extend
        si alguna serie tiene el mimso nombre se le cambia el nombre a esta para no sobreescribir
        actualiza el minimo, maximo, cantidad de series '''
        num=len(kf_to_extend.elements)+len(self.elements)
        for key in kf_to_extend.elements:
            new_key=key+"_"+str(num) if  self.elements.keys().__contains__(key) else key
            self.elements[new_key]=kf_to_extend.elements[key]
            num+=1
        self.count=len(self.elements)
        self.min_value=min(self.min_value,kf_to_extend.min_value)
        self.max_value = max(self.max_value, kf_to_extend.max_value)
