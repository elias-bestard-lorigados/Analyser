from api.known_formats.kf_known_format import KnownF
class FourTupleSeries(KnownF):
    """ Stores a list of series with 4-tuples of numbers [(X,Y,Lenght,Direction),...]"""

    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where wich element is a serie
        and series_name where wich elements is a serie_name'''
        super().__init__(s_values, series_names)
        self.min_value = [9999999999, 9999999999,99999999,99999999]
        self.max_value = [-9999999999, -9999999999,-999999,-9999999]
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.min_value=min(s_values[i]) if min(s_values[i])<self.min_value else self.min_value
            self.max_value=max(s_values[i]) if max(s_values[i])>self.max_value else self.max_value
            self.elements[series_names[i]]=s_values[i]
