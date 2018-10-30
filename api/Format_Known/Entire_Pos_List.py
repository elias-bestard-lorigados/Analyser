class Entire_Pos_List:
    """ Almacena una lista de Enteros Positivos, [valores] """

    def __init__(self, elements=[], series=False):
        self.elements = elements
        self.values=elements
        self.labels=[]
        self.series = series
