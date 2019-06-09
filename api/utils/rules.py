from api import an_known_format as formats

def check_few_categories(kf, boundary=5):
    ''' Chequea si el KF tiene pocas categorias por serie
    Fijando que pocas categorias sean menor boundary=5 por defecto
    Categorias son las secciones en las que se divide una serie
    len(serie) contidad de categorias de la serie '''
    for series_name in kf.elements:
        if len(kf.elements[series_name])>boundary:
            return False
    return True

def check_many_categories(kf, boundary=5):
    ''' Chequea si el KF tiene muchas categorias por serie '''
    return not(check_few_categories(kf,boundary))

def check_few_series(kf, boundary=5):
    ''' Chequea que KF tenga pocas series 
    teniendo como limite boundary=5 '''
    return  len(kf.elements)>boundary 

def check_many_series(kf, boundary=5):
    ''' Chequea que KF tenga muchas series 
    teniendo como limite boundary=5 '''
    return len(kf.elements) < boundary

def check_advance_over_time(kf):
    ''' Chequea que las series tengan un progreso sobre el tiempo   
    Definimos avance sobre el timepo si las Xs avanzan
    [[X1,Y1].....[Xn,Yn]] donde X1<X2<X3...<Xn para todas las series 
    asumiendo que las series tengan pares de numeros o trios'''
    #las siguientes series se asume que el valor de las x progresa en tiempo
    if (type(kf)== formats.NumSeries or type(kf)== formats.LabeledFourTupleSeries or
        type(kf)== formats.LabeledPairSeries or type(kf)== formats.LabeledTriosSeries or
        type(kf)== formats.DictXy):
        return True
    if type(kf)== formats.StrPairSeries or type(kf)== formats.StrStrWeightSeries:
        return False
    for series in kf.elements:
        actual=-9999
        for point in kf.elements[series]:
            #si los vallres de las series no son pares o trios o 4tetos de numeros
            # if len(point)>4:
            #     return False
            if point[0]<actual:
                return False
            actual = point[0]
    return True

def check_continuous_numbres(kf):
    ''' Chequea que las series tengan numeros continuos '''
    for key in kf.elements:
        for point in kf.elements[key]:
            if type(point)==list:
                if type(point[0]) != str and (type(point[0])==float or type(point[1])==float):
                    return True
            elif type(point)==dict and type(point['y'])==float:
                return True
    return False

def check_same_x_intervals(kf):
    ''' Chequea que las series tengan los mismos intervalos de avance   
    Para toda serie sean los mismos valores de Xs
    asumiendo que las series tengan pares de numeros o trios'''
    if (type(kf)== formats.NumSeries or type(kf)== formats.LabeledFourTupleSeries or
        type(kf)== formats.LabeledPairSeries or type(kf)== formats.LabeledTriosSeries or
        type(kf)== formats.DictXy):
        return True
    if (type(kf)== formats.StrPairSeries or type(kf)== formats.StrStrWeightSeries):
        return False
    list_of_x=[]
    series_values=list(kf.elements.values())
    for point in series_values[0]:
        # if len(point) > 4:
        #     return False
        list_of_x.append(point[0])

    for serie in series_values:
        #si los vallres de las series no son pares o trios o 4tetos de numeros
        if len(serie) != len(list_of_x):
            return False
        for index_p in range(0,len(serie)):
            # if len(serie[index_p]) > 4:
            #     return False
            if serie[index_p][0] !=list_of_x[index_p]:
                return False
    return True

def check_many_points_per_serie(kf, boundary=15):
    ''' Chequea que las series tengan minimo boundry puntos'''
    for key in kf.elements:
        if len(kf.elements[key])<15:
            return False
    return True

def check_same_size_btwn_series(kf):
    ''' Chequea que las series tengan el mismo tamano '''
    series = list(kf.elements.values())
    size=len(series[0])
    for item in series:
        if len(item)!=size:
            return False
    return True

def check_y_over_x(kf):
    ''' Chequea que los valores de las Y sean mayores que los de X
    o que los de Z sean mayores que los de Y'''
    if (type(kf)== formats.NumSeries or type(kf)== formats.LabeledFourTupleSeries or
        type(kf)== formats.LabeledPairSeries or type(kf)== formats.StrPairSeries or
        type(kf)== formats.StrStrWeightSeries or type(kf)==formats.DictXy):
        return True
    type_kf=0
    if (type(kf)==formats.LabeledFourTupleSeries or type(kf)==formats.FourTupleSeries or
        type(kf)==formats.LabeledTriosSeries or type(kf)==formats.TriosSeries):
        type_kf=1
    for serie in kf.elements:
        for item in kf.elements[serie]:
            if item[type_kf]> item[type_kf+1]:
                return False
    return True

def check_part_of_hole(kf):
    ''' Chequea que los valores sean parte de un todo
    partiendo que las series tiene el mismo tamanno
    que todas las categorias tengan el mismo tamanno
    que la suma de la primera columna de lo mismo que las demas'''
    if not check_same_size_btwn_series(kf):
        return False
    if (type(kf)== formats.LabeledFourTupleSeries or type(kf)== formats.LabeledTriosSeries or
        type(kf)== formats.StrPairSeries or type(kf)== formats.StrStrWeightSeries or 
        type(kf)== formats.TriosSeries or type(kf)== formats.FourTupleSeries):
        return False
    sums=[0 for item in kf.elements[list(kf.elements.keys())[0]]]
    for serie in kf.elements:
        for i in range(len(kf.elements[serie])):
            if type(kf)== formats.DictXy:
                sums[i]+=kf.elements[serie]['y']
            elif type(kf)== formats.NumSeries:
                sums[i]+=kf.elements[serie][i]
            else: sums[i]+=kf.elements[serie][i][1]
    for i in range(1,len(sums)):
        if  sums[i-1]!=sums[i]:
            return False
    return True

def check_long_categories_name(kf,boundary=7):
    ''' Chequear si tiene los nombres de las categorias largos,
    mas largos que boundary '''
    for categorie in kf.categories:
        if len(str(categorie))> boundary:
            return True
    return False

def message_comparison(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de comparacion '''
    result=0
    if check_same_size_btwn_series(kf):
        result+=1
    # if check_same_x_intervals(kf):
    #     result+=1
    if check_advance_over_time(kf):
        result+=1
    return result

def message_distribution(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de distribution '''
    result = 0
    if check_continuous_numbres(kf):
        result += 1
    if check_many_points_per_serie(kf, 15):
        result += 1
    if check_few_series(kf,3):
        result += 1
    if not check_same_size_btwn_series(kf):
        result += 1
    # if not check_same_x_intervals(kf):
    #     result += 1
    return result

def message_relation(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de relation '''
    result = 0
    if check_continuous_numbres(kf):
        result += 1
    # if not check_same_x_intervals(kf):
    #     result += 1
    if check_many_points_per_serie(kf, 15):
        result += 1
    if check_few_categories(kf,3):
        result += 1
    if not check_same_size_btwn_series(kf):
        result += 1
    return result

def message_composition(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de composition '''
    result = 0
    if check_part_of_hole(kf):
        result += 1
    if check_few_categories(kf, 7):
        result += 1
    if check_same_size_btwn_series(kf):
        result += 1
    # if check_same_x_intervals(kf):
    #     result += 1
    return result


# class a:
#     def __init__(self):
#         self.elements={
#     'a': [[1,2],[3,4]],
#     'b': [[3,4],[1,2]]}
# s=a()
# print(check_part_of_hole(s,1))
# print(check_few_series(s))
# print(check_advance_over_time(s))
# print(check_continuous_numbres(s))
# print(check_same_x_intervals(s))
# print(check_many_points_per_serie(s))
# print(check_same_size_btwn_series(s))
