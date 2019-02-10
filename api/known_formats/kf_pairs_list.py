class PairsList:
    """ Almacena una lista de pares (x,y)
    donde x puede tomar como valor un str siendo el label o nombre del punto"""

    def __init__(self, x=[], y=[]):
        ''' y=[valores] x=[labels]
        solo contiene una serie
        la serie correspondiente es la de matcheo de [(x_i,y_i),..] donde x puede ser label o numero '''
        self.elements = {0:[]}
        self.values = y
        self.labels = x
        self.min_value = (9999999999, 9999999999)
        self.max_value = (-9999999999, -9999999999)
        self.count = len(y)
        for i in range(0, len(y)):
            pair = (x[i], y[i])
            if type(x[i])!=str:
                if self.min_value>pair:
                    self.min_value=pair
                if self.max_value < pair:
                    self.max_value = pair
            self.elements[0].append(pair)
