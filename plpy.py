import lexer
import parser


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class BinOp(Node):
    def __init__(self, op, left, right):
        super().__init__(op)
        self.children = [left, right]


class Number(Node):
    def __init__(self, value):
        super().__init__(value)


# convert the AST to Python code
def to_python(node):
    if isinstance(node, BinOp):
        left = to_python(node.children[0])
        right = to_python(node.children[1])
        return f"({left} {node.value} {right})"
    elif isinstance(node, Number):
        return str(node.value)


# example usage
# ast = BinOp("+", Number(1), Number(2))
# print(to_python(ast))  # prints "(1 + 2)"

perl_code = "1+2"
ast = parser.parser.parse(perl_code,lexer=lexer.lexer)
print(to_python(ast))





































































# import sys
# from lib2to3.main import main
#
# def convert_perl_to_python(perl_code:str)->str:
#     # Saving the Perl code to a file
#     with open("perl_code.pl", "w") as file:
#         file.write(perl_code)
#
#     # Using 2to3 to convert the Perl code to Python code
#     sys.argv = ["2to3", "-n", "-w", "perl_code.pl"]
#     main()
#
#     # Reading the converted Python code
#     with open("perl_code.pl", "r") as file:
#         python_code = file.read()
#     return python_code
#
# perl_code = '''#!/usr/bin/perl
# print "Hello, World!\n";'''
#
# python_code = convert_perl_to_python(perl_code)
# print(python_code)
#
#
#
# import ply.lex as lex
# import ply.yacc as yacc
#
# # Token definitions for the lexer
# tokens = (
#     'VAR',
#     'ASSIGN',
#     'PLUS',
#     'MINUS',
#     'TIMES',
#     'DIVIDE',
#     'LPAREN',
#     'RPAREN',
#     'NUMBER',
# )
#
# # Regular expressions for the lexer
# t_VAR = r'\$[a-zA-Z_][a-zA-Z0-9_]*'
# t_ASSIGN = r'='
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_NUMBER = r'\d+'
#
# # Ignored characters
# t_ignore = " \t"
#
#
# # Error handling for the lexer
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)
#
#
# # Build the lexer
# lexer = lex.lex()
#
#
# # Grammar rules and actions for the parser
# def p_statement_assign(p):
#     'statement : VAR ASSIGN expression'
#     p[0] = ('assign', p[1], p[3])
#
#
# def p_expression_binop(p):
#     '''expression : expression PLUS expression
#                   | expression MINUS expression
#                   | expression TIMES expression
#                   | expression DIVIDE expression'''
#     p[0] = (p[2], p[1], p[3])
#
#
# def p_expression_group(p):
#     'expression : LPAREN expression RPAREN'
#     p[0] = ('group', p[2])
#
#
# def p_expression_number(p):
#     'expression : NUMBER'
#     p[0] = ('number', p[1])
#
#
# def p_expression_var(p):
#     'expression : VAR'
#     p[0] = ('var', p[1])
#
#
# def p_error(p):
#     print("Syntax error at '%s'" % p.value)
#
#
# # Build the parser
# parser = yacc.yacc()
#
# # Test the parser
# data = "$x = (2 + 3) * 4"
# parser.parse(data)
