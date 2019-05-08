class KnownF:
    def __init__(self, s_values=[],series_names=[]):
        self.elements = {}
        self.min_value = 9999999999 #minimun bettwen the lows values
        self.max_value = -999999    #maximun bettwen thw highs values
        self.count = len(s_values)
        self.categories = []
        self.keys = []
    def extend(self,kf_to_extend):
        num=len(kf_to_extend.elements)+len(self.elements)
        for key in kf_to_extend.elements:
            new_key=key+"_"+str(num) if  self.elements.keys().__contains__(key) else key
            self.elements[new_key]=kf_to_extend.elements[key]
            num+=1
        self.count=len(self.elements)
        self.min_value=min(self.min_value,kf_to_extend.min_value)
        self.max_value = max(self.max_value, kf_to_extend.max_value)
