class ListOfSeriesnameAndValues:
    """ Almacena una lista de tuplas (String,[Enteros])
    una lista de tuplas Series name , [values]  """

    def __init__(self, values=[], labels=[] ):
        ''' espera una lista de valores y una lista de labels, donde cada labels es el nombre de la serie de su valor correspondiente
        values es una lista de listas de numeros '''
        self.elements = {}
        for i in range(len(values)):
            self.elements[labels[i]] = values[i]
        self.values = values
        self.labels = labels
        self.min_value=min(values)
        self.max_value = max(values)
        self.count = len(values)

print(min([[2,1],[1,2]]))