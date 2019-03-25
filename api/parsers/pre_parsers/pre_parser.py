import sys
from api.utils.config import Config

#importando los parsers dinamicamente
sys.path.append(Config().parsers_path)
__all_parsers = {}
for item in Config().parsers:
    class_name = Config().get_parser_class_name(item)
    # import_module = compile(
    # "from .parsers."+item+" import "+class_name, 'e', mode='exec')
    import_module = compile("import "+item, 'e', mode='exec')
    exec(import_module)
    parser = eval(str(item+"."+class_name+"()"))
    if dir(parser).__contains__("describe"):
        __all_parsers[class_name] = parser
    else:
        print(class_name+"does not has the describe method")
    # __all_parsers[class_name] = eval(str(class_name+"()"))

def procces_text(text):
    text = remove_blank_line(text)
    text_lines=text.split('\n')
    description=[]
    for line in text_lines:
        description.append(procces_line(line))
    return text,description

def procces_line(line):
    if is_comment(line):
        return "COMMENT"
    for parser in __all_parsers:
        description = __all_parsers[parser].describe(line)
        if description:
            return description
    return "UNKNOW"

def is_comment(line):
    return True if line[0] == '#' or(len(line) >= 2 and line[:2] == '//') else False

def remove_blank_line(text:str):
    text=text.split('\n')
    new_text=''
    for line in text:
        if line!="":
            new_text+=line+"\n"
    return new_text[:-1]


def compress_list(info_list: list, kf_list: list):
    poss = 0
    info_result = [info_list[0]]
    kf_result = [kf_list[0]]
    for i in range(1, len(kf_list)):
        if kf_list[i-1] == kf_list[i]:
            info_result[poss] = info_result[poss]+"\n"+info_list[i]
        else:
            poss += 1
            info_result.append(info_list[i])
            kf_result.append(kf_list[i])
    return info_result, kf_result
