class DictXy:
    """ Stores a list of series with dictionaries 
    [{'x':VALUE,'y':VALUE,'name':VALUE,'color':value}...]"""

    def __init__(self, s_values=[], series_names=[]):
        ''' Recive two lists, s_values where wich element is a serie
        and series_name where wich elements is a serie_name'''
        self.elements = {}
        self.min_value = 9999999999
        self.max_value = -9999999999
        self.count = len(s_values)
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(s_values))]
        for i in range(len(s_values)):
            for item in s_values[i]:
                current_value = item['y']
                self.min_value = current_value if current_value < self.min_value else self.min_value
                self.max_value = current_value if current_value > self.max_value else self.max_value
            self.elements[series_names[i]] = s_values[i]