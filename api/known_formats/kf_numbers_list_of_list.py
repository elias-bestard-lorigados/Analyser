class NumbersListOfList:
    """ Almacena una lista de listas de Enteros """

    def __init__(self,elements=[]):
        ''' elements [[(,)],[],[],...]
        espera que elements sea una lista de listas de valores numericos
        self.elements= {"":[]} cada una de las listas son las series para plotear sin name'''
        self.elements = {}
        self.min_value=99999999999999999999
        self.max_value=-99999999999999999999
        if elements.__contains__([]):
            elements.remove([]) 
        for i in range(len(elements)):
            # if self.max_value<max(elements[i]):
            #     self.max_value = max(elements[i])
            # if self.min_value>min(elements[i]):
            #     self.min_value = min(elements[i])
            self.elements[i]=elements[i]
        self.count = len(elements)
