from api.known_formats.kf_known_format import KnownF
class PairsSeries(KnownF):
    """ Stores a list of series with pairs of numbers [(X_1,Y_1),(X_2,Y_2),...,(X_n,Y_n)]
        Where the X_j and Y_j are numbers"""

    def __init__(self,series,series_names=[]):
        ''' Recive two lists, series and series_names'''
        super().__init__(series, series_names)
        mins=[]
        maxs=[]
        self.proms=[]
        if len(series)!=0:
            maxs=series[0].copy()
            mins=series[0].copy()
            self.proms=[(item,1) for item in series[0]]
        self.min_value = [9999999999, 9999999999]
        self.max_value = [-9999999999, -9999999999]
        if series_names == []:
            series_names = ["serie_"+str(i) for i in range(len(series))]
        for i in range(len(series)):
            self.min_value=min(series[i]) if min(series[i])<self.min_value else self.min_value
            self.max_value=max(series[i]) if max(series[i])>self.max_value else self.max_value
            self.elements[series_names[i]]=series[i]
            for j in range(len(series[i])):
                if j>= len(mins):
                    mins.append(series[i][j])
                    maxs.append(series[i][j])
                    self.proms.append((series[i][j],1))
                else:
                    mins[j]= series[i][j] if series[i][j]<mins[j] else mins[j]
                    maxs[j]= series[i][j] if series[i][j]>maxs[j] else maxs[j]
                    new_proms_x=self.proms[j][0][0]+series[i][j][0]
                    new_proms_y=self.proms[j][0][1]+series[i][j][1]
                    self.proms[j]=([new_proms_x,new_proms_y],1+self.proms[j][1])
        self.count=len(self.elements)
        self.elements["Maxs_Series"]=maxs
        self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[[i[0]/j,i[1]/j] for i,j in self.proms]

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
                new_proms_x=proms[i][0][0]+kf_proms[i][0][0]
                new_proms_y=proms[i][0][1]+kf_proms[i][0][1]
                proms[i]=([new_proms_x,new_proms_y],proms[i][1]+kf_proms[i][1])
        # self.elements["Maxs_Series"]=maxs
        # self.elements["Mins_Series"]=mins
        self.elements["Meds_Series"]=[[i[0]/j,i[1]/j] for i,j in proms]