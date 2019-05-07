
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
    series_values=list(kf.elements.values())
    for series in series_values:
        actual=-9999
        for point in series:
            #si los vallres de las series no son pares o trios o 4tetos de numeros
            if len(point)>4:
                return False
            if type(point[0]) == str:
                continue
            if point[0]<actual:
                return False
            actual = point[0]
    return True

#REVISAR
def check_continuous_numbres(kf):
    ''' Chequea que las series tengan numeros continuos '''
    for key in kf.elements:
        for point in kf.elements[key]:
            if type(point[0]) != str and type(point[0])==float:
                return True
    return False

def check_same_x_intervals(kf):
    ''' Chequea que las series tengan los mismos intervalos de avance   
    Para toda serie sean los mismos valores de Xs
    asumiendo que las series tengan pares de numeros o trios'''
    list_of_x=[]
    series_values=list(kf.elements.values())
    for point in series_values[0]:
        if len(point)>4:
            return False
        list_of_x.append(point[0])

    for serie in series_values:
        #si los vallres de las series no son pares o trios o 4tetos de numeros
        if len(serie) != len(list_of_x):
            return False
        for index_p in range(0,len(serie)):
            if len(serie[index_p]) > 4:
                return False
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

def check_similar_part_of_hole(kf,boundary=5):
    ''' Chequea si una serie tiene sus valores muy similares
    considerando similares si estos pican casi en partes iguales a total
     '''
    return False

def check_y_over_x(kf,type=1):
    ''' Chequea que los valores de las Y sean mayores que los de X
    type 1 es si recive lista de pares
    type 0 es si recive lista de trios X Y Z
    o que los de Z sean mayores que los de Y
     '''
    return False

def check_part_of_hole(kf, type=1):
    ''' Chequea que los valores sean parte de un todo'''
    return False

def message_comparison(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de comparacion '''
    result=0
    if check_same_size_btwn_series(kf):
        result+=1
    if check_same_x_intervals(kf):
        result+=1
    return result


def message_distribution(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de distribution '''
    result = 0
    if not check_continuous_numbres(kf):
        result += 1
    if not check_many_points_per_serie(kf, 15):
        result += 1
    if not check_few_series(kf,3):
        result += 1
    if not check_same_size_btwn_series(kf):
        result += 1
    if not check_same_x_intervals(kf):
        result += 1
    return result

def message_relation(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de relation '''
    result = 0
    # if not check_continuous_numbres(kf):
    #     result += 1
    # if not check_many_points_per_serie(kf, 15):
    #     result += 1
    # if not check_few_series(kf, 3):
    #     result += 1
    # if not check_same_size_btwn_series(kf):
    #     result += 1
    # if not check_same_x_intervals(kf):
    #     result += 1
    return result

def message_composition(kf):
    ''' Chequear y calcular cuan se parece el kf a un mensaje de composition '''
    result = 0
    if not check_part_of_hole(kf):
        result += 1
    if not check_few_categories(kf, 7):
        result += 1
    # if not check_few_series(kf, 3):
    #     result += 1
    # if not check_same_size_btwn_series(kf):
    #     result += 1
    # if not check_same_x_intervals(kf):
    #     result += 1
    return result


# class a:
#     def __init__(self):
#         self.elements={
#     'a': [[76.14, 95.68], [52.57, 81.28], [58.79, 89.13]],
#     'b': [[83.69, 68.17], [90.39, 66.33], [78.3, 74.8], [88.94, 53.24]],
#     'c': [[58.46, 91.18], [61.51, 82.19], [52.09, 82.24], [76.0, 84.23], [59.26, 69.81]],
#     'd': [[80.57, 61.78], [56.27, 95.62], [88.73, 79.72]]
# }
# s=a()
# print(check_few_categories(s))
# print(check_few_series(s))
# print(check_advance_over_time(s))
# print(check_continuous_numbres(s))
# print(check_same_x_intervals(s))
# print(check_many_points_per_serie(s))
# print(check_same_size_btwn_series(s))
