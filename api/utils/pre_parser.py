from api.utils.config import Config
import string
import logging

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
    tm = compress_list1(list_kf)
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
    logging.info("---- PARSERS --> KF ----")
    logging.info("-"*30)
    for parser in Config().available_parsers:
        temp = all_parsers[parser].parse(text)
        if temp:
            logging.info("PARSER: "+parser+" --> : ")
            [logging.info(str(type(kf_g).__name__)) for kf_g,j in temp]
            list_kf.extend(temp)
            logging.info("-"*30)
    return [(["UNKNOW"],0)] if list_kf==[] else list_kf

def is_comment(line):
    ''' considerando que una linea es un comentrio si comienza con # o // 
    Retorna True si la linea es un comentario False si no lo es '''
    return True if line[0] == '#' or(len(line) >= 2 and line[:2] == '//') else False

def clean_text(text: str):
    ''' remover lineas en blanco de un str y los comentarios'''
    text=text.split('\n')
    a, b = 'áéíóúüñ/;()!@#$%^&*?><~ `','aeiouun                  '
    new_text=''
    for line in text:
        if line!='' and not is_comment(line):
            # line=line.translate(str.maketrans("", "",string.punctuation))
            line=line.translate(str.maketrans(a, b))
            new_text+=line+"\n"
    return new_text[:-1]

def my_contain_by_type1(type_to_compare, elements):
    ''' retorna lista de elementos de igual tipo que type_to_compare
    de los elementos de elements'''
    result=[]
    for item in elements:
        if type_to_compare == type(item[0]):
            result.append(item)
    return result

def compress_list1(info_list: list):
    ''' info_list<- list de List de KF
    revisa si en lineas adyacentes hay dos Kf iguales para unirlos
     '''
    result=[]
    while len(info_list)!=0:
        my_elements=info_list[0]
        for item in my_elements:
            for i in range(1,len(info_list)):
                elements_to_compress = my_contain_by_type1(type(item[0]), info_list[i])
                if elements_to_compress!=[]:
                    for x in elements_to_compress:
                        item[0].extend(x[0])
                        info_list[i].remove(x)
                else:
                    break
        result.extend(my_elements)
        info_list.remove(info_list[0])
    return result
