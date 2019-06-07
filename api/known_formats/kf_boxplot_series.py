import statistics
from statistics import median
from api.known_formats.kf_known_format import KnownF
class BoxplotSeries(KnownF):
    """ Stores a list of all the series, serie exp: [[ low, q1, median, q3 , high]...]
        """
    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where each element is a serie
        and series_name where each elements is a serie_name
        ASUMING ALL THE VALUES  (low, q1, median, q3 and high) ARE CALCULATED'''
        super().__init__(s_values, series_names)
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.elements[series_names[i]]=s_values[i]
            current_max= max([item[-1] for item in s_values[i]])
            current_min= min([item[0] if len(item)==5 else item[1] for item in s_values[i]])
            self.min_value=current_min if current_min<self.min_value else self.min_value
            self.max_value=current_max if current_max>self.max_value else self.max_value

    def calculate_boxplot_from_list(self,series_list=[], series_names=[]):
        ''' Recive two lists, s_values where each element is a serie
        and series_name where each elements is a serie_name
        ASUMING ALL THE VALUES  (low, q1, median, q3 and high) ARE NOT CALCULATED'''
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(series_list))]
        for i in range(len(series_list)):
            if len(series_list[i])==1:
                continue
            curren_serie=[]
            temp_list=list(series_list[i])
            temp_list.sort()
            middle=int(len(temp_list)/2)
            current_median=statistics.median(temp_list)
            current_min=min(temp_list)
            self.min_value=current_min if current_min<self.min_value else self.min_value
            current_max=max(temp_list)
            self.max_value=current_max if current_max>self.max_value else self.max_value
            current_q1=median(temp_list[:middle])
            current_q3=median(temp_list[middle:])
            curren_serie.append([current_min,current_q1,current_median,current_q3,current_max])
            self.elements[series_names[i]]=curren_serie
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