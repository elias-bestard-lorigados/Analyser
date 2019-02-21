import ply.yacc as yacc
import ply.lex as lex

class LexerError(Exception): pass
#List of tokes
tokens = (
    'NUM',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'COMMA',
    'LABEL',
    'NEWLINE'
)
#regular expression rules for simple tokens
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_COMMA = r'\,'

def t_LABEL(t):
    r'([ A-Za-z ]+(_[0-9]+)*)'
    # r'[ a-zA-Z_][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t

def t_NUM(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.value = str(t.value)
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'
#error handling rule
def t_error(t):
    # print("Illegal characters '%s'" % t.value[0])
    raise LexerError("Illegal character '%s'" % t.value)
    # t.lexer.skip(1)

def p_start(t):
    ''' start :  expression NEWLINE start 
            | expression'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]

def p_expression(t):
    '''expression : OPEN_BRACKET seriedata CLOSE_BRACKET'''
    t[2].reverse()
    t[0] = t[2]

def p_seriedata(t):
    ''' seriedata : OPEN_BRACKET LABEL COMMA LABEL COMMA NUM CLOSE_BRACKET COMMA seriedata 
              | OPEN_BRACKET LABEL COMMA LABEL COMMA NUM CLOSE_BRACKET'''
    if len(t) == 8:
        t[0] = [[t[2], t[4], t[6]]]
    else:
        t[9].append([t[2], t[4], t[6]])
        t[0] = t[9]

def p_error(t):
    raise LexerError("Illegal character '%s'" % t.value)
    # print("Syntax error at '%s'" % t.value)

def parse(text):
    #Build the lexer
    lexer = lex.lex()
    parser = yacc.yacc()
    if text[-1]=='\n':
        text=text[:-1]
    result=None
    try:
        result = parser.parse(text)
    except:
        pass
    if result:
        result.reverse()
    return result

# data=''' [[elias,juan,100],[juan,jose ,200],[jose,comio,200]]
# [[pepe,pedro,100],[pedro,jose ,200],[jose,comio,200]] '''
# print(parse(data))