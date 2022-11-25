import GraphFA
import converter
import parser

import sys
import time
import os

def printtitle():
    print("""
    ____  __  ____  _____  ____  ____ _   ____  ____ ______________  _____
   / __ \/ / / / / / / _ \/ __ \/ __ `/  / __ \/ __ `/ ___/ ___/ _ \/ ___/
  / /_/ / /_/ / /_/ /  __/ / / / /_/ /  / /_/ / /_/ / /  (__  )  __/ /
 / .___/\__,_/\__, /\___/_/ /_/\__, /  / .___/\__,_/_/  /____/\___/_/
/_/          /____/           /____/  /_/
    """)


if __name__ == "__main__":
    
   
    args_num = len(sys.argv)

    if(args_num == 2 and os.path.exists("../js/" + sys.argv[1])):
        START_TIME = time.time()
        printtitle()
        
        CNF = converter.loadCNF()
        tokens = GraphFA.lexer("../js/" + sys.argv[1])
        if parser.CYK_Parsing(CNF, tokens):
            print("\nResult : Accepted")
        else:
            print("\nResult : Syntax Error")

        END_TIME = time.time()
        print('Execution time : ', round(END_TIME-START_TIME, 2),'s')
        print('Variable + terminal count :', len(CNF))
    else:
        print("Tidak ada nama file yang sesuai! Pastikan nama file yang anda masukkan benar.")

