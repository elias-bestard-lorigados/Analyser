from api.utils.config import Config
import json

def add_data_base(graphic,kf):
    ''' Escribe en la base de datos el grafico que se utiliza y la info necesaria '''
    db_file = open(Config().db_path, 'r')
    info = db_file.read()
    deserialization = json.loads(info)
    myDictObj = {"useful": False, "id": graphic.g_id, "type": graphic.type,"kf":type(kf).__name__,"message":graphic.message,
                 "properties": {"min_value": kf.min_value, "max_value": kf.max_value, "count": kf.count}}
    deserialization.append(myDictObj)
    db_file.close()
    db_file = open(Config().db_path, 'w')
    serialized = json.dumps(deserialization, sort_keys=True, indent=3)
    db_file.write(serialized)
    db_file.close()


def find_count_kf_graphic(graphic, kf):
    ''' busca en la base de datos todos los graficos del mismo tipo que graphics
    que fueron generados con el KF kf
    retorna la proporcion de los utiles con los que no lo fueron '''
    db_file = open(Config().db_path, 'r')
    info = db_file.read()
    deserialization = json.loads(info)
    db_file.close()
    uselful=0
    total=0
    for item in deserialization:
        if item['type']==graphic.type and item['kf']==type(kf).__name__:
            total+=1
            if item['useful']:
                uselful+=1
    return uselful/total if total!=0 else 0


def find_count_message_graphic(message, kf):
    ''' busca en la base de datos todos los graficos del mismo tipo que graphics
    que fueron generados con el KF kf
    retorna la proporcion de los utiles con los que no lo fueron '''
    db_file = open(Config().db_path, 'r')
    info = db_file.read()
    deserialization = json.loads(info)
    db_file.close()
    uselful = 0
    total = 0
    for item in deserialization:
        if item['message'].__contains__(message) and item['kf'] == type(kf).__name__:
            total += 1
            if item['useful']:
                uselful += 1
    return uselful/total if total != 0 else 0
