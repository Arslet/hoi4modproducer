from lark import Lark
from lark.visitors import Interpreter
import logging
logging.basicConfig(level=logging.DEBUG)

with open('localization.lark', 'r') as file:
    parser = Lark(file, debug=True, propagate_positions=True)

if (False):
    with open('input.yml', 'r', encoding='utf-8-sig') as file:
        childrengeorgia = parsedgeorgia.children
        parsedgeorgia = parser.parse(file.read())
    #print(parser.parse(file.read()).pretty())
tempinput = """
#bick dicc
l_english: # agfagagag
#afdsafs
#slong
GEO_vanguardist_party:0 \"RKP(nc)\" # dick
#cock
"""

tempchildren = parser.parse(tempinput).children

for i in tempchildren:
    for x in i.children:
        print(i, x.type)

