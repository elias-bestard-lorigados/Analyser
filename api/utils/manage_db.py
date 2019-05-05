from api.utils.config import Config
import json

def add_data_base(graphic,kf):
    ''' Escribe en la base de datos el grafico que se utiliza y la info necesaria '''
    db_file = open(Config().db_path, 'r')
    info = db_file.read()
    deserialization = json.loads(info)
    myDictObj = {"useful": True, "id": graphic.g_id, "type": graphic.type,
                 "properties": {"min_value": kf.min_value, "max_value": kf.max_value, "count": kf.count}}
    deserialization.append(myDictObj)
    db_file.close()
    db_file = open(Config().db_path, 'w')
    serialized = json.dumps(deserialization, sort_keys=True, indent=3)
    db_file.write(serialized)
    db_file.close()
