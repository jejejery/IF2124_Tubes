import GraphFA
import converter
from pyfiglet import Figlet
import sys
import time
import os

if __name__ == "__main__":
    
   
    args_num = len(sys.argv)

    if(args_num == 2 and os.path.exists("../js/" + sys.argv[1])):
        START_TIME = time.time()
        converter.printtitle()
        
        CNF = converter.loadCNF()
        tokens = GraphFA.lexer("../js/" + sys.argv[1])
        print(f'Result: {converter.CYK_Parsing(CNF, tokens)}')

        END_TIME = time.time()
        print('Execution time : ', round(END_TIME-START_TIME, 2),'s')
        print('Variable + terminal count :', len(CNF))
    else:
        print("Tidak ada nama file yang sesuai! Pastikan nama file yang anda masukkan benar.")
