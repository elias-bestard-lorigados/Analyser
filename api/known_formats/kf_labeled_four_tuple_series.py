from api.known_formats.kf_known_format import KnownF
class LabeledFourTupleSeries(KnownF):
    """ Stores a list of series with 4-tuples of numbers [(X,Y,Lenght,Direction),...]
        where X is the name of the vector"""

    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where wich element is a serie
            and series_name where wich elements is a serie_name'''
        self.elements = {}
        self.min_value = [9999999999,999999,9999999]
        self.max_value = [-9999999999,-999999,-9999999]
        self.count = len(s_values)
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.elements[series_names[i]]=s_values[i]
            y=[[item[1],item[2],item[3]] for item in s_values[i]]
            self.min_value=min(y) if min(y)<self.min_value else self.min_value
            self.max_value=max(y) if max(y)>self.max_value else self.max_value