class List_Tuple:
    """ Almacena una lista de (String,[Enteros]) """

    def __init__(self, values=[], labels=[] ,series=False):
        self.elements = []
        self.values = values
        self.labels = labels
        self.series=series
        for i in range(0,len(values)):
            self.elements.append((labels[i], values[i]))
