class PairsSeries:
    """ Stores a list of series with pairs of numbers [(X_1,Y_1),(X_2,Y_2),...,(X_n,Y_n)]
        Where the X_j and Y_j are numbers"""


    def __init__(self, x=[], y=[],series_names=[]):
        ''' Recive two lists, X-list and Y-list, both list of series numbers,
        and store a list of series matching x_i with Y_i
        X and Y are list of list '''
        self.elements = {}
        self.min_value = (9999999999, 9999999999)
        self.max_value = (-9999999999, -9999999999)
        self.count = len(y)
        if series_names==[]:
            series_names=[i for i in range(len(y))]
        for i in range(len(y)):
            current_serie= list(zip(x[i],y[i]))
            self.min_value=min(current_serie) if min(current_serie)<self.min_value else self.min_value
            self.max_value=max(current_serie) if max(current_serie)>self.max_value else self.max_value
            self.elements[series_names[i]]=current_serie
