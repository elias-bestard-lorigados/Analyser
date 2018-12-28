class NumbersListOfList:
    """ Almacena una lista de listas de Enteros """

    def __init__(self,elements=[]):
        ''' elements [[],[],[],...]
        espera que elements sea una lista de listas de valores numericos
        self.elements= {"":[]} cada una de las listas son las series para plotear sin name'''
        self.elements = {}
        for i in range(len(elements)):
            self.elements[i]=elements[i]
