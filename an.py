#! /home/elias/anaconda3/bin/python
from api.utils.analyse import analyse_data
from api.utils.config import Config
import input_parser

data = input_parser.parse()
print("="*20)
for info in data:
    print(info)
    analyse_data(info)
    print("========== EL PROCESO DEL ARCHIVO CONCLUYO ==========")
    Config().output_count+=1
    print("="*20)
