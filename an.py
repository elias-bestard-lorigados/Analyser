#! /home/elias/anaconda3/bin/python
# from api.utils.analyse import analyse_data
from api.an_identify import identify
from api.an_graphs import to_graphic
from api.utils.manage_html import ini_html,end_html
from api.utils.config import Config
from api.utils.my_logguer import *
import input_parser

def analyse_data(data):
    ''' Identificar todos los posibles tipos de Known_Format que se extraen de "data"
    y generar codigo html para cada grafico que recibe cada tipo de formato
    crea el file.html final  '''
    formats = identify(data)
    charts_code,results_tabs =to_graphic(formats)
    if charts_code == '':
        print("Lo sentimos no se pudo generar ningun grafico")
        logging.info("Lo sentimos no se pudo generar ningun grafico")
        return
    file=ini_html()  # creo el archivo html
    end_html(file,charts_code,results_tabs)  # concluo el html y cierro el archivo

logging.info('========INICIO=======')
data = input_parser.parse()

print("="*20)
for info in data:
    print(info)
    analyse_data(info)
    logging.info('--- Archivo Finalizado ---')
    Config().output_count+=1
    logging.info("-"*30)

logging.info('======== FIN =======')
logging.info('.'*30)
