import GraphFA
import converter

import sys

if __name__ == "__main__":
    args_num = len(sys.argv)

    CNF = converter.loadCNF()
    if args_num == 2:
        tokens = GraphFA.lexer("../js/" + sys.argv[1])
    else:
        tokens = GraphFA.lexer("../js/test.js")
    converter.printCFG(CNF)
    print(tokens)
    #\print(converter.CYK_Parsing(CNF, tokens))
