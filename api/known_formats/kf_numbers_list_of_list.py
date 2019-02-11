class NumbersListOfList:
    """ Almacena una lista de listas de Enteros """

    def __init__(self,elements=[]):
        ''' elements [[(,)],[],[],...]
        espera que elements sea una lista de listas de valores numericos
        self.elements= {"":[]} cada una de las listas son las series para plotear sin name'''
        self.elements = {}
        self.min_value="UKNOW"
        self.max_value="UKNOW"
        if elements.__contains__([]):
            elements.remove([]) 
        for i in range(len(elements)):
            self.elements[i]=elements[i]
        self.count = len(elements)
