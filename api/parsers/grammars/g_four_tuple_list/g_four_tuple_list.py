import ply.yacc as yacc
import ply.lex as lex

class LexerError(Exception): pass
#List of tokes
tokens = (
    'NUM',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'COMMA',
    'NEWLINE',
    'LABEL'
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
    # t.lexer.skip(1)
    raise LexerError("Illegal character '%s'" % t.value)

def p_start(t):
    ''' start :  expression NEWLINE start 
            | expression'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]

def p_expression(t):
    '''expression : OPEN_BRACKET fourtuple CLOSE_BRACKET'''
    t[2].reverse()
    t[0] = t[2]

def p_fourtuple(t):
    ''' fourtuple : OPEN_BRACKET NUM COMMA NUM COMMA NUM COMMA NUM CLOSE_BRACKET COMMA fourtuple 
              | OPEN_BRACKET NUM COMMA NUM COMMA NUM COMMA NUM CLOSE_BRACKET'''
    if len(t) == 10:
        t[0] = [[t[2], t[4],t[6],t[8]]]
    else:
        t[11].append([t[2], t[4],t[6],t[8]])
        t[0] = t[11]

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
    result.reverse() if result else result
    return result

# data='''[[juan,2,3,12]]'''
# print(parse(data))