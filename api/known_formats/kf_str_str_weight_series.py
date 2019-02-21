class StrStrWeightSeries:
    """ Stores a list of all the series, serie exp: [[ str, str,weight]...]
        """


    def __init__(self, s_values=[],series_names=[]):
        ''' Recive two lists, s_values where each element is a serie,
        and series_name, where each elements is a serie_name'''
        self.elements = {}
        self.min_value = 9999999999 #minimun bettwen the lows values
        self.max_value = -999999999   #maximun bettwen thw highs values
        self.count = len(s_values)
        self.keys = ['from', 'to', 'weight']
        if series_names==[]:
            series_names=["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            self.elements[series_names[i]]=s_values[i]
            current_max= max([item[-1] for item in s_values[i]])
            current_min= min([item[-1] for item in s_values[i]])
            self.min_value=current_min if current_min<self.min_value else self.min_value
            self.max_value=current_max if current_max>self.max_value else self.max_value
