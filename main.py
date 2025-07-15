import sys
import os
from lark import Lark
from ast_builder import ASTBuilder
from interpreter import Interpreter

# Garante que grammar.lark seja encontrado mesmo em executável
if getattr(sys, 'frozen', False):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

grammar_path = os.path.join(base_path, "grammar.lark")
with open(grammar_path) as f:
    grammar = f.read()

parser = Lark(grammar, parser='lalr', transformer=ASTBuilder())
interpreter = Interpreter()

if len(sys.argv) < 2:
    print("Uso: python main.py <arquivo_fonte>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    codigo = f.read()

tree = parser.parse(codigo)
for stmt in tree.children:
    interpreter.exec(stmt)
