import fire
import sys

class CLI:
    def __init__(self,file="",output=sys.stdout):
        '''...
        file:"" representa el path donde buscara el file a analizar
            si file="" buscara por la entrada estandar
        output:stdout representa donde se mostraran los resultados al final
            por default es la salida estandar
          '''
        self.__file = file
        self.__output = output
    
    def Analyze(self):
        ''' Analizara el [FILE] mostrando los resultados por [OUTPUT] '''
        data=""
        if self.__file!="":
            data=open(self.__file,"r").read()
        else:     # Si recibo los datos por la consola hasta que no escriba una linea en blanco
            print("Escribe los datos y para finalizar una linea en blan")
            temp = input()
            while not temp == "":
                data += temp
                temp = input()
                data += "\n" if not temp == "" else ""
        print(data)
        return data,self.__output

def ini():
    fire.Fire(CLI)
