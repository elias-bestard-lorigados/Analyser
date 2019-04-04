from api.known_formats.kf_known_format import KnownF
class TriosSeries(KnownF):
    """ Stores a list of series with pairs of numbers [(X_1,Y_1,z1),(X_2,Y_2,Z_2),...,(X_n,Y_n,Z_n)]
        Where the X_j, Y_j, Z_j are numbers"""


    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where wich element is a serie
        and series_name where wich elements is a serie_name'''
        self.elements = {}
        self.min_value = [9999999999, 9999999999,99999999]
        self.max_value = [-9999999999, -9999999999,-999999]
        self.count = len(s_values)
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.min_value=min(s_values[i]) if min(s_values[i])<self.min_value else self.min_value
            self.max_value=max(s_values[i]) if max(s_values[i])>self.max_value else self.max_value
            self.elements[series_names[i]]=s_values[i]