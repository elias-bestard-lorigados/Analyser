class Pair_List:
    """ Almacena una lista de pares (x,y)
    donde x puede tomar como valor un str siendo el label o nombre del punto"""

    def __init__(self, labels=[], values=[], series=False):
        self.elements = []
        self.values = values
        self.labels = labels
        self.series=series
        for i in range(0,len(values)):
            self.elements.append((labels[i], values[i]))
