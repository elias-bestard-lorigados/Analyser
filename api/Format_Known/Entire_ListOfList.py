class Entire_ListOfList:
    """ Almacena una lista de listas de Enteros """

    def __init__(self,elements=[],series=False):
        self.elements = elements
        self.values = elements
        self.labels = [str(item) for item in range(len(elements))]
        self.series = series
