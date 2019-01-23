import os

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
        #Url where the out file will be put
        self.output_url = "./out/"
        #Name of the resulting file
        self.output_name = "out_file_"

        #URl where the parsers are located
        self.parsers_url = "./api/parsers"
        #List of all implemented parsers
        self.parsers = "all"
        self.__set_parsers()
        #List of all availables parsers url
        self.available_parsers = self.parsers
        #List of all parsers will show help
        self.prarsers_help=[]

        #URl where the graphs are located
        self.graphs_url = "./api/graphs"
        #List of all implemented graphs
        self.graphs = "all"
        self.__set_graphs()
        #List of all availables graphs url
        self.available_graphs = self.graphs

        #URl where the graphs are located
        self.data_generated_url = "./data"
        #List of Parsers wich will be use to generate datasets
        self.data_generated = []

    def __set_parsers(self):
        ''' Update self.parsers to a list with all parsers who are implemented '''
        self.parsers=[]
        for item in os.listdir(self.parsers_url):
            p = self.parsers_url+"/"+item
            if (not os.path.isdir(p)):
                self.parsers.append(item[:-3])

    def __set_graphs(self):
        ''' Update self.graphs to a list with all graphs who are implemented '''
        self.graphs = []
        for item in os.listdir(self.graphs_url):
            p = self.graphs_url+"/"+item
            if (not os.path.isdir(p)):
                self.graphs.append(item[:-3])

    def set_available_parsers_graphs(self,in_parsers,in_graphs):
        """ Update self.available_graphs and self.available_parsers to a list of 
        graphs and parsers who are going to be plot in depends of the arguments of the input"""
        available_parsers = in_parsers.split(',')
        available_graphs = in_graphs.split(',')
        self.available_parsers = []
        self.available_graphs = []

        if in_parsers != "all":
            for parser in available_parsers:
                if self.parsers.__contains__(parser):
                    self.available_parsers.append(
                        self.get_parser_class_name(parser))
                else:
                    print("WARNING-- THE PARSER "+parser +" IS NOT DEFIND")
        else:
            self.available_parsers = [self.get_parser_class_name(parser) for parser in self.parsers]

        if in_graphs != "all":
            for graph in available_graphs:
                if self.graphs.__contains__(graph):
                    self.available_graphs.append(graph)
                else:
                    print("WARNING-- THE GRAPH "+graph + " IS NOT DEFIND")
        else:
            self.available_graphs = self.graphs
    
    def set_parsers_help(self,in_parsers_help):
        """ Update self.prarsers_help to a list of parsers who's help are going to be show"""
        if in_parsers_help != None and in_parsers_help != "all":
             for parser in in_parsers_help.split(","):
                if self.parsers.__contains__(parser):
                    self.prarsers_help.append(parser)
                else:
                    print("WARNING-- THE PARSER "+parser + " IS NOT DEFIND")
        else:
            self.prarsers_help = self.parsers

    def set_output_file(self, output_name):
        """ update self.output_name to the params from the input  """
        self.output_name = output_name if output_name != None else "out_file_"+str(len(os.listdir(self.output_url)))+".html"

    def set_data_generated_list(self,in_dg):
        """ update the self.data_generated to a list of all parser who will be use to generate datasets """
        if in_dg != None and in_dg!="all":
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

