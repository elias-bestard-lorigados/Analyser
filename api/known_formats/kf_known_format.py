class KnownF:
    def __init__(self, s_values=[],series_names=[]):
        self.elements = {}
        self.min_value = 9999999999 #minimun bettwen the lows values
        self.max_value = -999999    #maximun bettwen thw highs values
        self.count = len(s_values)

    def extend(self,kf_to_extend):
        for key in kf_to_extend.elements:
            new_key=key+"'_other" if  self.elements.keys().__contains__(key) else key
            self.elements[new_key]=kf_to_extend.elements[key]