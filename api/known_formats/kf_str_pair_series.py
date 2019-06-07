from api.known_formats.kf_known_format import KnownF
class StrPairSeries(KnownF):
    """ Stores a list of all the series, serie exp: [[ str, str]...]
        """


    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where each element is a serie,
        and series_name, where each elements is a serie_name'''
        super().__init__(s_values, series_names)
        self.min_value = "Unknown" #minimun bettwen the lows values
        self.max_value = "Unknown"   #maximun bettwen thw highs values
        self.keys = ['from', 'to']
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.elements[series_names[i]]=s_values[i]
            current_max= max([item[-1] for item in s_values[i]])
            current_min= min([item[-1] for item in s_values[i]])
            self.min_value=current_min if current_min<self.min_value else self.min_value
            self.max_value=current_max if current_max>self.max_value else self.max_value
    def extend(self,kf_to_extend):
        ''' Extiende el KF self, con el KF kf_to_extend
        agregando a los elements los de kf_to_extend
        si alguna serie tiene el mimso nombre se le cambia el nombre a esta para no sobreescribir
        actualiza el minimo, maximo, cantidad de series '''
        num=len(kf_to_extend.elements)+len(self.elements)
        proms=kf_to_extend.proms
        for key in kf_to_extend.elements:
            new_key=key+"_"+str(num) if  self.elements.keys().__contains__(key) else key
            self.elements[new_key]=kf_to_extend.elements[key]
            num+=1
        self.count=len(self.elements)
        self.min_value=min(self.min_value,kf_to_extend.min_value)
        self.max_value = max(self.max_value, kf_to_extend.max_value)