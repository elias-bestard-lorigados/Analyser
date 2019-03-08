class PairsSeries:
    """ Stores a list of series with pairs of numbers [(X_1,Y_1),(X_2,Y_2),...,(X_n,Y_n)]
        Where the X_j and Y_j are numbers"""

    def __init__(self,series,series_names=[]):
        ''' Recive two lists, series and series_names'''
        self.elements = {}
        self.min_value = [9999999999, 9999999999]
        self.max_value = [-9999999999, -9999999999]
        self.count = len(series)
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(series))]
        for i in range(len(series)):
            self.min_value=min(series[i]) if min(series[i])<self.min_value else self.min_value
            self.max_value=max(series[i]) if max(series[i])>self.max_value else self.max_value
            self.elements[series_names[i]]=series[i]