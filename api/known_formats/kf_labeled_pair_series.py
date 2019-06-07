from api.known_formats.kf_known_format import KnownF
class LabeledPairSeries(KnownF):
    """ Stores a list of series with pairs of (label,numbers) [(X_1,Y_1),(X_2,Y_2),...,(X_n,Y_n)]
        Where the X_j list is a label list and Y_j are a numbers list"""

    def __init__(self, series=[],series_names=[]):
        '''Recive two lists: series where wich element is a serie
        and series_name where wich elements is a serie_name.'''
        super().__init__(series, series_names)
        mins=[]
        maxs=[]
        self.proms=[]
        if len(series)!=0:
            maxs=series[0].copy()
            mins=series[0].copy()
            self.proms=[(item,1) for item in series[0]]
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(series))]
        for i in range(len(series)):
            self.elements[series_names[i]]=series[i]
            y=[item[1] for item in series[i]]
            self.min_value=min(y) if min(y)<self.min_value else self.min_value
            self.max_value=max(y) if max(y)>self.max_value else self.max_value
            for j in range(len(series[i])):
                if j>= len(mins):
                    mins.append(series[i][j])
                    maxs.append(series[i][j])
                    self.proms.append((series[i][j],1))
                else:
                    mins[j]= series[i][j] if series[i][j][1]<mins[j][1] else mins[j]
                    maxs[j]= series[i][j] if series[i][j][1]>maxs[j][1] else maxs[j]
                    new_proms_x=series[i][j][0]
                    new_proms_y=self.proms[j][0][1]+series[i][j][1]
                    self.proms[j]=([new_proms_x,new_proms_y],1+self.proms[j][1])
        self.count=len(self.elements)
        self.elements["Maxs_Series"]=maxs
        self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[[i[0],i[1]/j] for i,j in self.proms]
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
                mins[i]=kf_mins[i] if kf_mins[i][1]<mins[i][1] else mins[i]
                maxs[i]=kf_maxs[i] if kf_maxs[i][1]>maxs[i][1] else maxs[i]
                new_proms_x="med_"+str(i)
                new_proms_y=proms[i][0][1]+kf_proms[i][0][1]
                proms[i]=([new_proms_x,new_proms_y],proms[i][1]+kf_proms[i][1])
        # self.elements["Maxs_Series"]=maxs
        # self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[[i[0],i[1]/j] for i,j in proms]