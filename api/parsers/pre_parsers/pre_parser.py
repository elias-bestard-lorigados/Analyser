import sys
from api.utils.config import Config

#importando los parsers dinamicamente
sys.path.append(Config().parsers_path)
__all_parsers = {}
for item in Config().parsers:
    class_name = Config().get_parser_class_name(item)
    # import_module = compile(
    # "from .parsers."+item+" import "+class_name, 'e', mode='exec')
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    parser = eval(str(item+"."+class_name+"()"))
    if dir(parser).__contains__("describe"):
        __all_parsers[class_name] = parser
    else:
        print(class_name+"does not has the describe method")
    # __all_parsers[class_name] = eval(str(class_name+"()"))

def procces_text(text):
    ''' Procesa un texto linea por linea
    Remueve lineas en blanco
    Procesa cada linea independientemente con los parsers definidos creando KF por cada linea que parsee
    luego junta los KF similares adyacentes '''
    text = remove_blank_line(text)
    text_lines=text.split('\n')
    list_kf=[]
    for line in text_lines:
        list_kf.append(procces_line(line))
    for item in list_kf:
        print(item)
    tm=compress_list(list_kf)
    return tm

def procces_line(line):
    """ Verifica si 'line' se puede parsear con algun parser y
    retorna una lista de todos los KF que se puedan crear a partir de 'line'
    Verifica igual si es un comentario y en caso que no parsee con ninguno retorna UNKNOWN """
    if is_comment(line):
        return ["COMMENT"]
    list_kf=[]
    for parser in __all_parsers:
        temp = __all_parsers[parser].parse(line)
        if temp:
            list_kf.extend(temp)
    return ["UNKNOW"] if list_kf==[] else list_kf

def is_comment(line):
    ''' considerando que una linea es un comentrio si comienza con # o // 
    Retorna True si la linea es un comentario False si no lo es '''
    return True if line[0] == '#' or(len(line) >= 2 and line[:2] == '//') else False

def remove_blank_line(text:str):
    ''' remover lineas en blanco de un str '''
    text=text.split('\n')
    new_text=''
    for line in text:
        if line!="":
            new_text+=line+"\n"
    return new_text[:-1]

def compress_list(info_list: list):
    ''' info_list<- list de List de KF
    revisa si en lineas adyacentes hay dos Kf iguales para unirlos
     '''
    kf_temp = info_list[0]
    kf_result=[]
    for i in range(1,len(info_list)):
        poss_to_delete=[]
        if (info_list[i] == ["COMMENT"] or info_list[i] == ["UNKNOW"]):
            continue
        for j in range(0,len(kf_temp)):
            poss=my_contain_by_type(kf_temp[j],info_list[i])#vir si hay mas de un tipo en la proxima linea
            if  poss==-1:
                kf_result.append(kf_temp[j])
                poss_to_delete.append(kf_temp[j])
            else:
                kf_temp[j][0].extend(info_list[i][poss][0])
        for item in poss_to_delete:
            kf_temp.remove(item)
    kf_result.extend(kf_temp)
    return kf_result

def my_contain_by_type(a,b):
    ''' retorna poss(X) si b<- list de KF contiene a un X con type(X)==type(a)
    else return -1 '''
    for i in range(0,len(b)):
        if type(b[i][0])==type(a[0]):
            return i
    return -1
