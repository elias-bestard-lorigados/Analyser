import ply.yacc as yacc
import ply.lex as lex
class LexerError(Exception): pass

#List of tokes
tokens = (
    'NUM',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'COMMA',
    'NEWLINE'
)
#regular expression rules for simple tokens
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_COMMA = r'\,'
t_NEWLINE = r'\n+'
def t_NUM(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value)
    return t

t_ignore = ' \t'
#error handling rule

def t_error(t):
    # print("Illegal characters '%s'" % t.value[0])
    raise LexerError("Illegal character '%s'" % t.value)
    t.lexer.skip(1)

def p_start(t):
    ''' start :  expression NEWLINE start 
            | expression'''
            # | NEWLINE start'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]

def p_expression(t):
    '''expression : OPEN_BRACKET numbers CLOSE_BRACKET'''
    t[2].reverse()
    t[0] = t[2]

def p_numbers(t):
    '''numbers  : NUM COMMA numbers
                | NUM  '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]

def p_error(t):
    raise LexerError("Illegal character '%s'" % t.value)
    # print("Syntax error at '%s'" % t.value)


def parse(text:str):
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
# data='''[[label_1, 64.13],[56.36, 97.45],[82.93, 87.65]]
# [[84.54, 69.05],[80.54, 60.72]]
# '''
# print(parse(data))