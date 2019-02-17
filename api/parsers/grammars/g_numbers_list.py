import ply.yacc as yacc
import ply.lex as lex

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
    print("Illegal characters '%s'" % t.value[0])
    t.lexer.skip(1)

#Build the lexer
lexer = lex.lex()

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
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

def parse(text:str):
    if text[-1]=='\n':
        text=text[:-1]
    result = parser.parse(text)
    if result:
        result.reverse()
    return result

