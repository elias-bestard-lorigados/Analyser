class Entire_ListOfList:
    """ Almacena una lista de listas de Enteros """

    def __init__(self,elements=[]):
        ''' elements [[],[],[],...]
        espera que elements sea una lista de listas de valores numericos
        self.elements= {"":[]} con cada lista de los obtenidos son las series para plotear '''
        self.elements = {}
        for i in range(len(elements)):
            self.elements[i]=elements[i]
