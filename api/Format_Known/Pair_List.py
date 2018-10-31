class Pair_List:
    """ Almacena una lista de pares (x,y)
    donde x puede tomar como valor un str siendo el label o nombre del punto"""

    def __init__(self, x=[], y=[]):
        ''' y=[valores] x=[labels]
        solo contiene una serie
        la serie correspondiente es la de matcheo de [(x,y),..] donde x puede ser label o numero '''
        self.elements = {0:[]}
        self.values = y
        self.labels = x
        for i in range(0, len(y)):
            self.elements[0].append((x[i], y[i]))
