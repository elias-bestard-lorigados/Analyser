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
        # path where is located the info to procces
        self.input_path = os.path.abspath('./data_generator')

        #path where the out file will be put
        self.output_path = os.path.abspath("./out/")
        #Name of the resulting file
        self.output_name = "out_file"
        self.output_count=0
        #path where the parsers are located
        self.parsers_path = os.path.abspath("./api/parsers")
        #List of all implemented parsers
        self.parsers = "all"
        self.__set_parsers()
        #List of all availables parsers path
        self.available_parsers = self.parsers
        #List of all parsers will show help
        self.prarsers_help=[]
        self.parser_list=0
        #path where the graphs are located
        self.graphs_path = os.path.abspath("./api/graphs")
        #List of all implemented graphs
        self.graphs = "all"
        self.__set_graphs()
        #List of all availables graphs path
        self.available_graphs = self.graphs
        self.graphs_list=0

        #path where the data_generated is located
        self.data_generated_path = "./data_generator"
        #List of Parsers777 wich will be use to generate datasets
        self.data_generated = []

        self.db_path = 'api/utils/data_base.json'
        self.db_count_id=0 #para saber por que id voy generando los graficos

    def set_db_path(self,path):
        ''' Set 'path' as the data base path, a file where we puts the necesary info for our system
        if the file exist then update the 'db_count_id'
        if not then it will be create '''
        if not os.path.isfile(path):
            file = open(path, "w")
            file.write("[]")
            file.close()
            self.db_count_id=0
        else:
            db_file = open(path, 'r')
            info = db_file.read()
            deserialization = json.loads(info)
            self.db_count_id=0
            for item in deserialization:
                if item['id']>self.db_count_id:
                    self.db_count_id=item['id']
            self.db_count_id+=1
        self.db_path = path

    def set_in_path(self, in_path):
        ''' Set 'in_path' as the path where the program would be looking the input files '''
        self.input_path = os.path.abspath(in_path)

    def set_out_path(self, out_path):
        ''' Set 'out_path' as the path where the program would put the output files '''
        self.output_path = os.path.abspath(out_path)

    def set_output_name(self, output_name):
        """ set output_name as the default name for the outputs files
        and output count as the number of the file that we have for not repetitions"""
        self.output_name = output_name if output_name != None else "out_file"
        self.output_count=len(os.listdir(Config().output_path))

    def set_parsers_path(self,p_path):
        ''' Set 'p_path' as the path where the program would be looking the parsers '''
        self.parsers_path = os.path.abspath(p_path)
        self.__set_parsers()

    def set_graphs_path(self,g_path):
        ''' Set 'g_path' as the path where the program would be looking the graphs '''
        self.graphs_path=os.path.abspath(g_path)
        self.__set_graphs()

    def __set_parsers(self):
        ''' Update self.parsers to a list with all parsers who are implemented and implement the interface of parsers
        will print a warning if not '''
        sys.path.append(self.parsers_path)
        self.parsers = []
        for item in os.listdir(self.parsers_path):
            p = self.parsers_path+"/"+item
            if (not os.path.isdir(p)):
                class_name = self.get_parser_class_name(item[:-3])
                # import_module = compile("from ..parsers."+item[:-3] +
                                        # " import "+class_name, 'e', mode='exec')
                import_module = compile("import "+item[:-3], 'e', mode='exec')
                exec(import_module)
                # temp = eval(str(class_name+"()"))
                try:
                    temp = eval(str(item[:-3]+"."+class_name+"()"))
                    if dir(temp).__contains__("parse") and dir(temp).__contains__("help"):
                        self.parsers.append(item[:-3])
                    else:
                        print("WARNING-- THE FILE "+item +
                          " DOES NOT IMPLEMENT THE INTERFACE")
                except:
                    print("WARNING-- THE FILE "+item +
                          " DOES NOT IMPLEMENT THE INTERFACE")

    def __set_graphs(self):
        ''' Update self.graphs to a list with all graphs who are implemented '''
        sys.path.append(self.graphs_path)
        self.graphs = []
        for item in os.listdir(self.graphs_path):
            p = self.graphs_path+"/"+item
            if (not os.path.isdir(p)):
                class_name = self.get_parser_class_name(item[:-3])
                import_module = compile("import "+item[:-3], 'e', mode='exec')
                exec(import_module)
                try:
                    temp = eval(str(item[:-3]+"."+class_name+"()"))
                    if dir(temp).__contains__("graphic") and dir(temp).__contains__("type"):
                        self.graphs.append(item[:-3])
                    else:
                        print("WARNING-- THE FILE "+item +
                          " DOES NOT IMPLEMENT THE INTERFACE")
                except:
                    print("WARNING-- THE FILE "+item +
                          " DOES NOT IMPLEMENT THE INTERFACE")


    def set_available_parsers(self,in_parsers='all'):
        """ Update self.available_parsers to a list of parsers
            who are going to be plot in depends of the arguments of the input"""
        available_parsers = in_parsers.split(',')
        self.available_parsers = []
        if in_parsers != "all":
            for parser in available_parsers:
                if self.parsers.__contains__(parser):
                    self.available_parsers.append(self.get_parser_class_name(parser))
                else:
                    print("WARNING-- THE PARSER "+parser + " IS NOT DEFIND")
        else:
            self.available_parsers = [self.get_parser_class_name(
                parser) for parser in self.parsers]

    def set_available_graphs(self,in_graphs='all'):
        """ Update self.available_graphs to a list of
        graphs  who are going to be plot in depends of the arguments of the input"""
        available_graphs = in_graphs.split(',')
        self.available_graphs = []
        if in_graphs != "all":
            for graph in available_graphs:
                if self.graphs.__contains__(graph):
                    self.available_graphs.append(self.get_parser_class_name(graph))
                else:
                    print("WARNING-- THE GRAPH "+graph + " IS NOT DEFIND")
        else:
            self.available_graphs = [self.get_parser_class_name(
                graph) for graph in self.graphs]

    def set_parsers_help(self,in_parsers_help):
        """ Update self.prarsers_help to a list of parsers who's help are going to be show"""
        if in_parsers_help == None:
            return
        if in_parsers_help != "all":
             for parser in in_parsers_help.split(","):
                if self.parsers.__contains__(parser):
                    self.prarsers_help.append(parser)
                else:
                    print("WARNING-- THE PARSER "+parser + " IS NOT DEFIND")
        else:
            self.prarsers_help = self.parsers

    def set_parsers_list(self,parser_list):
        self.parser_list=int(parser_list)
    def set_graphs_list(self,graphs_list):
        self.graphs_list=int(graphs_list)

    def set_data_g_path(self,dg_path):
        self.data_generated_path =dg_path

    def set_data_generated_list(self,in_dg):
        """ update the self.data_generated to a list of all parser who will be use to generate datasets """
        if in_dg == None:
            return
        if in_dg!="all":
            for parser in in_dg.split(","):
                if self.parsers.__contains__(parser):
                    self.data_generated.append(parser)
                else:
                    print("WARNING-- THE PARSER "+parser + " IS NOT DEFIND")
        else:
            self.data_generated = self.parsers

    def get_parser_class_name(self,parser_name):
        """ From a parser name return the class name 
        Ej: p_series_list -> SeriesList"""
        class_name = ""
        temp = [x.capitalize() for x in parser_name.split("_")]
        for item in temp[1:]:
            class_name += item
        return class_name

