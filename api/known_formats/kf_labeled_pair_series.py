class LabeledPairSeries:
    """ Stores a list of series with pairs of (label,numbers) [(X_1,Y_1),(X_2,Y_2),...,(X_n,Y_n)]
        Where the X_j list is a label list and Y_j are a numbers list"""

    def __init__(self, x=[], y=[],series_names=[]):
        ''' Recive two lists, X-list and Y-list, Y-list is a list of series numbers, and X-list labels
        and store a list of series matching x_i with Y_i
        X and Y are list of list '''
        self.elements = {}
        self.min_value = 99999999
        self.max_value = -9999999
        self.count = len(y)
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(y))]
        for i in range(len(y)):
            current_serie= list(zip(x[i],y[i]))
            self.min_value=min(y[i]) if min(y[i])<self.min_value else self.min_value
            self.max_value=max(y[i]) if max(y[i])>self.max_value else self.max_value
            self.elements[series_names[i]]=current_serie
    
    def reset_with_series(self,series,series_names=[]):
        ''' Recive two lists, s_values where wich element is a serie
        and series_name where wich elements is a serie_name'''
        self.elements = {}
        self.min_value = 99999999
        self.max_value = -9999999
        self.count = len(series)
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(series))]
        for i in range(len(series)):
            self.elements[series_names[i]]=series[i]
            y=[item[1] for item in series[i]]
            self.min_value=min(y) if min(y)<self.min_value else self.min_value
            self.max_value=max(y) if max(y)>self.max_value else self.max_value