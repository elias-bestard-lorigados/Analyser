from api.utils.config import Config
import string

def analyse_line_by_line(text,all_parsers):
    ''' Analiza un texto linea por linea
    Procesa cada linea independientemente con los parsers definidos creando listas de KF por cada linea que parsee
    luego junta los KF similares que estan adyacentes '''
    text_lines=text.split('\n')
    list_kf=[]
    for line in text_lines:
        line_processed = process_text(line, all_parsers)
        if line_processed != [(["UNKNOW"], 0)]:
            list_kf.append(line_processed)
    tm=compress_list(list_kf)
    print("~~~~ FORMATOS EXRAIDOS~~~~~~~")
    print(tm)
    return tm


def analyse_text(text: str, all_parsers:dict):
    ''' Analiza un texto completo
    recorre los parsers definidos tratando de parsear el texto completo
    '''
    return process_text(text,all_parsers)


def process_text(text: str, all_parsers:dict):
    """ Verifica si 'text' se puede parsear con algun parser y
    retorna una lista de todos los KF que se puedan crear a partir de 'text'
    En caso que no parsee con ninguno retorna UNKNOWN """
    list_kf=[]
    for parser in Config().available_parsers:
        temp = all_parsers[parser].parse(text)
        if temp:
            list_kf.extend(temp)
    return [(["UNKNOW"],0)] if list_kf==[] else list_kf

def is_comment(line):
    ''' considerando que una linea es un comentrio si comienza con # o // 
    Retorna True si la linea es un comentario False si no lo es '''
    return True if line[0] == '#' or(len(line) >= 2 and line[:2] == '//') else False

def clean_text(text: str):
    ''' remover lineas en blanco de un str y los comentarios'''
    text=text.split('\n')
    a, b = 'áéíóúüñ/;()!@#$%^&*?><~`','aeiouun                 '
    new_text=''
    for line in text:
        if line!='' and not is_comment(line):
            # line=line.translate(str.maketrans("", "",string.punctuation))
            line=line.translate(str.maketrans(a, b))
            new_text+=line+"\n"
    return new_text[:-1]

def compress_list(info_list: list):
    ''' info_list<- list de List de KF
    revisa si en lineas adyacentes hay dos Kf iguales para unirlos
     '''
    if info_list==[]:
        return []
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
