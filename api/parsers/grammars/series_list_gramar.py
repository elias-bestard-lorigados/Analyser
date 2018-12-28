import ply.yacc as yacc
import ply.lex as lex


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
    r'[a-zA-Z_][a-zA-Z0-9_]*'
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
    print("Illegal characters '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
lexer = lex.lex()


def p_start(t):
    ''' start :  expression NEWLINE start 
    | expression'''
    '        | empty'
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]
        t[0].reverse()


def p_expression(t):
    '''expression : OPEN_BRACKET generator CLOSE_BRACKET'''
    t[2].reverse()
    t[0] = t[2]


def p_generator(t):
    ''' generator : pairs
                  | numbers'''
    '        | empty'
    t[0] = t[1]


def p_numbers(t):
    '''numbers  : NUM COMMA generator
                | NUM  '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[3].append(t[1])
        t[0] = t[3]


def p_pairs(t):
    ''' pairs : OPEN_BRACKET NUM COMMA NUM CLOSE_BRACKET COMMA generator 
              | OPEN_BRACKET NUM COMMA NUM CLOSE_BRACKET
              | OPEN_BRACKET LABEL COMMA NUM CLOSE_BRACKET COMMA generator
              | OPEN_BRACKET LABEL COMMA NUM CLOSE_BRACKET '''
    if len(t) == 6:
        t[0] = [[t[2], t[4]]]
    else:
        t[7].append([t[2], t[4]])
        t[0] = t[7]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

def parse(text):
    result=parser.parse(text)
    return result
