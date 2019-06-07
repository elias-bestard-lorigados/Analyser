from api.known_formats.kf_known_format import KnownF

class DictXy(KnownF):
    """ Stores a list of series with dictionaries 
    [{'x':VALUE,'y':VALUE,'name':VALUE,'color':value}...]"""

    def __init__(self, series=[], series_names=[]):
        ''' Recive two lists, series where wich element is a serie
        and series_name where wich elements is a serie_name'''
        super().__init__(series, series_names)
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(series))]
        mins=[]
        maxs=[]
        self.proms=[]
        if len(series)!=0:
            maxs=[item['y'] for item in series[0]]
            mins=[item['y'] for item in series[0]]
            self.proms=[(item['y'],1) for item in series[0]]

        for i in range(len(series)):
            for j in range(len(series[i])):
                current_value = series[i][j]['y']
                self.min_value = current_value if current_value < self.min_value else self.min_value
                self.max_value = current_value if current_value > self.max_value else self.max_value
                if j>=len(mins):
                    mins.append(series[i][j]['y'])
                    maxs.append(series[i][j]['y'])
                    mins.append((series[i][j]['y'],1))
                else:
                    mins[j]= series[i][j]['y'] if series[i][j]['y']<mins[j] else mins[j]
                    maxs[j]= series[i][j]['y'] if series[i][j]['y']>maxs[j] else maxs[j]
                    new_prom=(self.proms[j][0]+series[i][j]['y'],1+self.proms[j][1])
                    self.proms[j]=new_prom
            self.elements[series_names[i]] = series[i]
        self.count=len(self.elements)
        self.elements["Maxs_Series"]=maxs
        self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[i/j for i,j in self.proms]
    
    def update_min_max_meddian(self,kf_mins,kf_maxs,kf_proms):
        maxs=self.elements["Maxs_Series"]
        mins=self.elements["Mins_Series"]
        proms=self.proms
        for i in range(len(kf_mins)):
            if i>=len(mins):
                mins.append(kf_mins[i])
                maxs.append(kf_maxs[i])
                proms.append(kf_proms[i])
            else:
                mins[i]=kf_mins[i] if kf_mins[i]<mins[i] else mins[i]
                maxs[i]=kf_maxs[i] if kf_maxs[i]>maxs[i] else maxs[i]
                proms[i]=(proms[i][0]+kf_proms[i][0],proms[i][1]+kf_proms[i][1])

        # self.elements["Maxs_Series"]=maxs
        # self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[i/j for i,j in proms]