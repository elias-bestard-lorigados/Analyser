from api.utils.config import Config
from api.an_identify import identify
from api.an_graphs import graph

def analyse_data(data):
    ''' Identificar todos los posibles tipos de Known_Format que se extraen de "data"
    y generar codigo html para cada grafico que recibe cada tipo de formato
    crea el file.html final  '''
    formats = identify(data)
    charts_code,results_tabs =to_graphic(formats)
    if charts_code == '':
        print("Lo sentimos no se pudo generar ningun grafico")
        return
    file=ini_html()  # creo el archivo html
    end_html(file,charts_code,results_tabs)  # concluo el html y cierro el archivo

def to_graphic(kf):
    ''' generar codigo html para graficar los formatos "KF" de la entrada
    return LIST[STRING] (codigo js de los graficos)
    retorna el codigo generado y la lista de tabs en los que se van a mostrar en el html'''
    results_tabcontent_charts = ""
    results_tabs = []
    #form ->KF ,sim->similarity
    for form, sim in kf:  # recorro todos los formatos para graficar de cada formto todos los graficos posibles
        if form == ['UNKNOW']:
            continue
        code = graph(form)
        for text, chart_id in code:
            results_tabcontent_charts += text
            results_tabs.append(generate_tab(chart_id))
    return results_tabcontent_charts,results_tabs

def ini_html(file_name=None):
    """ Inicializar un HTML enl a carpeta de salida donde se escribira el resultado de analizar los datos """
    name = Config().output_name +"_"+str(Config().output_count)
    file_name=name if file_name==None else file_name
    file = open(Config().output_path+"/"+name+".html", "w")
    file.write("<head>")
    file.write("<script src=\"./js_libraries/jquery.js\"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/highcharts.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/highcharts-more.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/sankey.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/vector.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/heatmap.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/networkgraph.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/bullet.js \"></script>\n")
    file.write("<script src=\"./js_libraries/Highcharts_JS/modules/tilemap.js \"></script>\n")
    # file.write("<script src=\"./js_libraries/highcharts.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/highcharts-more.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/sankey.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/vector.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/heatmap.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/networkgraph.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/bullet.js\"></script>\n")
    # file.write("<script src=\"./js_libraries/tilemap.js\"></script>\n")
    file.write("<script src=\"./js_libraries/vertical_tabs.js\"></script>\n")
    file.write("<link rel = \"stylesheet\" href = \"./js_libraries/style.css\">\n")
    file.write("</head>\n")
    file.write("<body>\n")
    return file

def end_html(file, charts_code, tabs_list):
    '''genera y escribe ne el file los tabs y su contenido"graficos"
     Cerrara el "body" del HTML final '''
    file.write("<div class = \"tab\" >\n")
    for tabs in tabs_list:
        file.write(tabs)
    file.write("</div>\n")
    file.write(charts_code)
    file.write("</body>")
    file.close()

def generate_tab(chart_id):
    chart = chart_id[:chart_id.index("_")]
    return "<button class = \"tablinks\" onclick = \"OpenChart(event,'"+chart_id+"')\" >"+chart+" </button >\n"
