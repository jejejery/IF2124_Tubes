import GraphFA
import converter

import sys
import time

if __name__ == "__main__":
    START_TIME = time.time()
    args_num = len(sys.argv)

    CNF = converter.loadCNF()
    if args_num == 2:
        tokens = GraphFA.lexer("../js/" + sys.argv[1])
    else:
        tokens = GraphFA.lexer("../js/test.js")
    converter.printCFG(CNF)
    print(tokens)
    print(converter.CYK_Parsing(CNF, tokens))
    END_TIME = time.time()
    print('Execution time : ', round(END_TIME-START_TIME, 2))
    print('Variable + terminal count :', len(CNF))
