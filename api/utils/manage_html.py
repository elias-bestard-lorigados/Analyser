# import logging
from api.utils.config import Config

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

def generate_div_html(div_id, content ):
    ''' genera una etiqueta div en HTML '''
    content = "<div id =\""+div_id+"\" class = \"tabcontent\" >\n"+content+"\n</div>\n"
    return content