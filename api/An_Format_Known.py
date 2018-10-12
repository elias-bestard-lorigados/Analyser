
class Entire_Pos_List:
    """ Almacena una lista de Enteros Positivos """
    def __init__(self,elements):
        self.elements=elements

class Pair_List:
    """ Almacena una lista de pares (Label,Enteros Positivos)"""

    def __init__(self, elements):
        self.elements = elements

class Entire_ListOfList:
    """ Almacena una lista de lista de Enteros """
    def __init__(self, elements):
        self.elements = None
        if not isinstance(elements,list):
            raise Exception("Los elementos deben ser una lisat de listas")
        for item in elements:
            if not isListOfEntire(item):
                raise Exception("Los elementos deben ser una lisat de listas")
        self.elements = elements


class Entire_ListOfListPair:
    """ Almacena una lista de lista de (String,Enteros) """

    def __init__(self, elements):
        self.elements = None
        if not isinstance(elements, list):
            raise Exception("Los elementos deben ser una lisat de listas")
        for item in elements:
            if not isinstance(item, tuple) and not isListOfEntire(item[1]):
                raise Exception("Los elementos deben ser una lisat de listas")
        self.elements = elements

def isListOfEntirePos(lista):
    for item in lista:
           if type(item) != int or item < 0:
               return False
    return True
def isListOfEntire(lista):
    for item in lista:
           if type(item) != int :
               return False
    return True
