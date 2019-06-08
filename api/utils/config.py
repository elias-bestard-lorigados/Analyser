import logging
import os
import sys
import json

def singleton(cls):
    instance = None
    def getinstance(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance
    return getinstance

@singleton
class Config:
    def __init__(self):
        """ Fija la configuracion de los parametros por default """
        # Path donde se ubica la info a procesar
        self.input_path = os.path.abspath('./data_generator')

        # Path donde se escribiran los archivos de salida
        self.output_path = os.path.abspath("./out/")
        if  not os.path.exists(self.output_path):
            os.mkdir(self.output_path)
        # Nombre base de los archivos de salida
        self.output_name = "out_file"
        # Contador para guiarme de la cantidad de archivos de salida actuales
        self.output_count=0

        # Path donde estan implementados los parsers definidos
        self.parsers_path = os.path.abspath("./api/parsers")
        # Lista de todos los parsers definidos
        self.parsers = "all" # <- []
        self.__set_parsers()
        # Lista de los parsers que el usuario habilita
        self.available_parsers = self.parsers
        # Lista de parsers que seran mostrados en la ayuda
        self.prarsers_help=[]
        # 0 o 1 si sera mostrado o no la lista de parsers
        self.parser_list=0

        # Path donde estan implementados los graficos definidos
        self.graphs_path = os.path.abspath("./api/graphs")
        # Lista de todos los graficos implementados
        self.graphs = "all"
        self.__set_graphs()
        # Lista de los graficos que el usuario habilita
        self.available_graphs = self.graphs
        # 0 o 1 sis era o no mostrada la lista de graficos en la ayuda
        self.graphs_list=0

        # Path donde se generaran los juegos de datos
        self.data_generated_path = "./data_generator"
        # Lista de parsers que generaran juegos de datos
        self.data_generated = []

        # Path donde sera ubicada la DB
        self.db_path = 'api/utils/data_base.json'
        # Para llevar la cuenta del ultimo grafico_id y no repetir
        self.db_count_id=0 #para saber por que id voy generando los graficos

        # Lista de graficos que se generaran aleatoriamente
        self.graphics_g=[]

        # Parametro para saber su utilizar o no la IA de seleccion de graficos 1 si 0 no
        self.graphics_selection = 1

        self.messages = ['comparison', 'composition',
                         'relation', 'distribution']
        #para ver que mensaje quiere mostrarse
        self.message=''

    def set_in_path(self, path):
        ''' Actualiza self.input_path a la nueva direccion si esta existe '''
        if os.path.isdir(os.path.abspath(path)) or os.path.isfile(os.path.abspath(path)):
            self.input_path = os.path.abspath(path)
        else:
            logging.warning("EL PATH "+ path +" NO ES UN PATH VALIDO")
            # print("WARNING-- EL PATH "+ path +" NO ES UN PATH VALIDO")

    def set_out_path(self, path):
        ''' Actualiza self.output_path a la nueva direccion si esta existe '''
        if os.path.isdir(os.path.abspath(path)):
            self.output_path = os.path.abspath(path)
        else:
            logging.warning("EL PATH "+ path +" NO ES UN PATH VALIDO")
            # print("WARNING-- EL PATH " + path + " NO ES UN PATH VALIDO")

    def set_output_name(self, name):
        """ Actualiza self.output_name para el nombre que adquiriran los archivos de salida
        y self.output_count como el numero de file que existen para no repetir"""
        self.output_count=len(os.listdir(self.output_path))
        self.output_name = name

    def set_parsers_path(self,path):
        ''' actualiza self.parsers_path si existe path 
        actualiza self.parsers con los parsers implementados en este path '''
        if os.path.isdir(os.path.abspath(path)):
            self.parsers_path = os.path.abspath(path)
            self.__set_parsers()
        else:
            logging.warning("EL PATH "+ path +" NO ES UN PATH VALIDO")
            # print("WARNING-- EL PATH "+ path +" NO ES UN PATH VALIDO")
    
    def set_graphs_path(self,path):
        ''' actualiza self.graphs_path si existe path 
        actualiza self.graphs con los graficos implementados en este path '''
        if os.path.isdir(os.path.abspath(path)):
            self.graphs_path = os.path.abspath(path)
            self.__set_graphs()
        else:
            logging.warning("EL PATH "+ path +" NO ES UN PATH VALIDO")
            # print("WARNING-- EL PATH " + path + " NO ES UN PATH VALIDO")

    def __set_parsers(self):
        ''' Actualiza self.parsers a una lista con todos los parsers implementados bajo la interfaz definida
        los busca en la direccion self.parsers_path 
        los importa dinamicamente y chequea que complan con la interfaz de parser'''
        self.parsers = []
        sys.path.append(self.parsers_path)
        for item in os.listdir(self.parsers_path):
            p = self.parsers_path+"/"+item
            if (not os.path.isdir(p)):
                class_name = self.get_parser_class_name(item[:-3])
                import_module = compile("import "+item[:-3], 'e', mode='exec')
                exec(import_module)
                try:
                    temp = eval(str(item[:-3]+"."+class_name+"()"))
                    if dir(temp).__contains__("parse") and dir(temp).__contains__("help"):
                        self.parsers.append(item[:-3])
                    else:
                        
                        logging.warning("EL ARCHIVO "+item +
                          " NO IMPLEMENTA LA INTERFACE DE PARSER")
                        # print("WARNING-- EL ARCHIVO "+item +
                        #   " NO IMPLEMENTA LA INTERFACE DE PARSER")
                except:
                    logging.warning("EL ARCHIVO "+item +
                          " NO IMPLEMENTA LA INTERFACE DE PARSER")
                    # print("WARNING-- EL ARCHIVO "+item +
                        #   " NO IMPLEMENTA LA INTERFACE DE PARSER")

    def __set_graphs(self):
        ''' Actualiza self.graphs a una lista con todos los graficos implementados bajo la interfaz definida
        los busca en la direccion self.graphs_path 
        los importa dinamicamente y chequea que complan con la interfaz de grafico'''
        self.graphs = []
        sys.path.append(self.graphs_path)
        for item in os.listdir(self.graphs_path):
            p = self.graphs_path+"/"+item
            if (not os.path.isdir(p)):
                class_name = self.get_parser_class_name(item[:-3])
                import_module = compile("import "+item[:-3], 'e', mode='exec')
                exec(import_module)
                try:
                    temp = eval(str(item[:-3]+"."+class_name+"()"))
                    if dir(temp).__contains__("graphic") and dir(temp).__contains__("type") and dir(temp).__contains__("evaluate_rules"):
                        self.graphs.append(item[:-3])
                    else:
                        logging.warning("EL ARCHIVO "+item +
                          " NO IMPLEMENTA LA INTERFACE DE GRAFICO")
                        # print("WARNING-- EL ARCHIVO "+item +
                            #   " NO IMPLEMENTA LA INTERFACE DE GRAFICO")
                except:
                    logging.warning("EL ARCHIVO "+item +
                          " NO IMPLEMENTA LA INTERFACE DE GRAFICO")
                    # print("WARNING-- EL ARCHIVO "+item +
                        #   " NO IMPLEMENTA LA INTERFACE DE GRAFICO")

    def set_available_parsers(self,in_parsers='all'):
        """ actualiza self.available_parsers a una lista de parsers
        in_parsers es una lista de parsers separados por ','
        se chequea que existan"""
        self.available_parsers = []
        available_parsers = in_parsers.split(',')
        if available_parsers.__contains__(''):
            available_parsers.remove('')
        if in_parsers != "all":
            for parser in available_parsers:
                if self.parsers.__contains__(parser):
                    self.available_parsers.append(self.get_parser_class_name(parser))
                else:
                    logging.warning("EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
                    # print("WARNING-- EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
        else:
            self.available_parsers = [self.get_parser_class_name(
                parser) for parser in self.parsers]

    def set_available_graphs(self,in_graphs='all'):
        """ actualiza self.available_graphs a una lista de GRAFICOS
        in_graphs es una lista de graficos separados por ','
        se chequea que existan"""
        self.available_graphs = []
        available_graphs = in_graphs.split(',')
        if available_graphs.__contains__(''):
            available_graphs.remove('')
        if in_graphs != "all":
            for graph in available_graphs:
                if self.graphs.__contains__(graph):
                    self.available_graphs.append(self.get_parser_class_name(graph))
                else:
                    logging.warning("EL GRAFICO "+graph + " NO ESTA DEFINIDO EN EL PATH")
                    # print("WARNING-- EL GRAFICO "+graph + " NO ESTA DEFINIDO EN EL PATH")
        else:
            self.available_graphs = [self.get_parser_class_name(
                graph) for graph in self.graphs]

    def set_parsers_help(self,in_parsers_help):
        """ Actualiza self.prarsers_help a una lista de los parsers que mostraran su ayuda 
        si los parsers entrados no existen devuelve una lista con valor none ['none']"""
        self.prarsers_help=[]
        if in_parsers_help != "all":
            in_parsers_help = in_parsers_help.split(",")
            if in_parsers_help.__contains__(''):
                in_parsers_help.remove('')
            for parser in in_parsers_help:
                if self.parsers.__contains__(parser):
                    self.prarsers_help.append(parser)
                else:
                    logging.warning("EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
                    # print("WARNING-- EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
        else:
            self.prarsers_help = self.parsers
        if len(in_parsers_help)!=0 and self.prarsers_help==[]:
            self.prarsers_help=['none']

    def set_parsers_list(self,parser_list):
        '''Actualiza self.parser_list a 0 or 1(false o true), 
        self.parser_list nos dice si mostramos los parsers implementados  '''
        if parser_list.isnumeric():
            self.parser_list=int(parser_list)

    def set_graphs_list(self,graphs_list):
        '''Actualiza self.graphs_list a 0 or 1(false o true), 
        self.graphs_list nos dice si mostramos los graficos implementados  '''
        if graphs_list.isnumeric():
            self.graphs_list=int(graphs_list)

    def set_data_g_path(self,path):
        ''' Actualiza self.data_generated_path a la nueva direccion si esta existe '''
        if os.path.isdir(os.path.abspath(path)):
            self.data_generated_path = os.path.abspath(path)
        else:
            logging.warning("EL PATH " + path + " NO ES UN PATH VALIDO")
            # print("WARNING-- EL PATH " + path + " NO ES UN PATH VALIDO")

    def set_data_generated_list(self,in_dg):
        """ Actualiza self.data_generated con los parsers que generaran juegos de datos """
        self.data_generated=[]
        if in_dg!="all":
            in_dg = in_dg.split(",")
            if in_dg.__contains__(''):
                in_dg.remove('')
            for parser in in_dg:
                if self.parsers.__contains__(parser):
                    self.data_generated.append(parser)
                else:
                    logging.warning("EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
                    # print("WARNING-- EL PARSER "+parser + " NO ESTA DEFINIDO EN EL PATH")
        else:
            self.data_generated = self.parsers
        if len(in_dg) != 0 and self.data_generated == []:
            self.data_generated = ['none']

    def get_parser_class_name(self,parser_name):
        """ From a parser name return the class name 
        Ej: p_series_list -> SeriesList"""
        class_name = ""
        temp = [x.capitalize() for x in parser_name.split("_")]
        for item in temp[1:]:
            class_name += item
        return class_name

    def set_graphics_generated_list(self,in_gg):
        """ Actualiza self.graphics_g con los parsers que generaran juegos de datos """
        self.graphics_g=[]
        sys.path.append(self.graphs_path)
        if in_gg=="all":
            in_gg = self.graphs
        else:
            in_gg = in_gg.split(",")
            if in_gg.__contains__(''):
                in_gg.remove('')
        for graphic in in_gg:
            if self.graphs.__contains__(graphic):
                import_module = compile("import "+graphic, 'e', mode='exec')
                exec(import_module)
                class_name=self.get_parser_class_name(graphic)
                temp = eval(str(graphic+'.'+class_name+"()"))
                if dir(temp).__contains__("generate"):
                    self.graphics_g.append(class_name)
                else:
                    logging.warning("EL GRAFICO "+graphic +
                            " NO TIENE IMPLEMENTADO EL METODO 'GENERATE'")
                    # print("WARNING-- EL GRAFICO "+graphic +
                            # " NO TIENE IMPLEMENTADO EL METODO 'GENERATE'")
            else:
                logging.warning("EL GRAFICO "+graphic + " NO ESTA DEFINIDO EN EL PATH")
                # print("WARNING-- EL GRAFICO "+graphic + " NO ESTA DEFINIDO EN EL PATH")
        if len(in_gg) != 0 and self.graphics_g == []:
            self.graphics_g = ['none']
    def set_db_path(self, path):
        ''' Actualiza self.db_path
        Si el archivo path existe actualizamos self.db_count
        Si no existe el archivo sera creado'''
        if not os.path.isfile(path):
            file = open(path, "w")
            file.write("[]")
            file.close()
            self.db_count_id = 0
        else:
            db_file = open(path, 'r')
            info = db_file.read()
            deserialization = json.loads(info)
            self.db_count_id = 0
            for item in deserialization:
                if item['id'] > self.db_count_id:
                    self.db_count_id = item['id']
            self.db_count_id += 1
        self.db_path = path

    def set_graphics_selection(self, graphics_selection):
        '''Actualiza self.graphics_selection a 0 or 1(false o true), 
        self.graphics_selection nos dice si utilizamos o no la seleccion de graficos basados en reglas  '''
        if graphics_selection.isnumeric():
            self.graphics_selection = int(graphics_selection)

    def set_message(self, message):
        '''Actualiza self.messaga al mensaje que se quiera mostar
        de los siguientes ['comparison','composition','relation','distribution']'''
        if self.messages.__contains__(message):
            self.message=message

