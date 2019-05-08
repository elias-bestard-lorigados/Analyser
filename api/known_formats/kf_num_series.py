from api.known_formats.kf_known_format import KnownF
class NumSeries(KnownF):
    """ Stores a list of series of numbers [X_1,X_2,...,X_n]"""

    def __init__(self, series=[],series_names=[]):
        ''' Recive a list of list with all the series to store  '''
        super().__init__(series, series_names)
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(series))]
        for i in range(len(series)):
            self.elements[series_names[i]]=series[i]
            self.min_value=min(series[i]) if min(series[i])<self.min_value else self.min_value
            self.max_value=max(series[i]) if max(series[i])>self.max_value else self.max_value
                
