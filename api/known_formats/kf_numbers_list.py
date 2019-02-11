class NumbersList:
    """ Almacena una lista de Numeros [valores] """

    def __init__(self, elements=[]):
        self.elements = {0:elements}
        self.min_value = min(elements)
        self.max_value = max(elements)
        self.count = len(elements)