# File : converter.py
# Berisi coverter CFG ke CNF

# Aturan isi CFG (Untuk memudahkan convert):
# 1. Tidak ada produksi epsilon
# 2. Seluruhnya huruf besar

import os
import time
import json

# File locator
dir_path = os.path.dirname(os.path.realpath(__file__))

def isTerminal(str):
    # Mengembalikan True jika str adalah terminal
    return str in [
        'NUMBER',
        'VARIABLE',
        'STRING',
        'FUNCTION',    
        'VARIABLE',
        'OPEN_PARENTHESES',
        'CLOSE_PARENTHESES',
        'OPEN_BRACKET',
        'CLOSE_BRACKET',
        'OPEN_CURLY',
        'CLOSE_CURLY',
        'COMMA',
        'VAR',
        'CONST',
        'LET',
        'EQ',
        'SUBAS',
        'MULAS',
        'SUMAS',
        'DIVAS',
        'MODAS',
        'POWAS',
        'ANDAS',
        'ORAS',
        'IF',
        'ELIF',
        'ELSE',
        'DO',
        'FOR',
        'WHILE',
        'BREAK',
        'CONTINUE',
        'SIGN',
        'OTHER_ARIT_OPERATOR',
        'FALSE',
        'TRUE',
        'LOGI_OPERATOR ',
        'AND',
        'OR',
        'NOT',
        'COLON',
        'SEMICOLON',          
        'ARRAY_DECL',  
        'NEW',
        'NULL',
        'SWITCH',
        'CASE',
        'CATCH',
        'DEFAULT',
        'DELETE',
        'FINALLY',
        'TRY',
        'RETURN',
        'THROW',
        'INCREMENT',
        'DECREMENT',
        



    ]

def isVariable(str):
    return not isTerminal(str)

def CFG_TO_CNF(File_Path):
    File_Path = os.path.join(dir_path, File_Path)
    file = open(File_Path, 'r')
    fileLines = file.read().split('\n')
    CFG = {}
    for x in fileLines:
        if len(x) == 0:
            continue
        a, b = x.split(' -> ')
        if a not in CFG.keys():
            CFG[a] = []
        add = b.split(' ')
        if len(add[-1]) == 0:
            add = add[:-1]
        CFG[a] += [add]
    

    # Menghilangkan unit production
    for lhs, rhs in CFG.items():
        for prod in rhs:
            if len(prod) > 1 or isTerminal(prod[0]):
                continue
            if not prod[0] in CFG:
                print(f'Warning: Variable {prod[0]} cannot reach terminal')
                continue
            for sub in CFG[prod[0]]:
                CFG[lhs] += [sub]
        
        i = 0
        while True:
            if i == len(rhs):
                break
            prod = rhs[i]
            if len(prod) == 1 and isVariable(prod[0]):
                rhs.remove(prod)
                i -= 1
            i += 1


    # Mengubah Produksi dengan > 2 variabel
    # Variabel tambahan = VX , X = angka mulai dari 1
    nomorVar = 1
    CNF = {}
    for lhs, rhs in CFG.items():
        CNF[lhs] = []
        for prod in rhs:
            while len(prod) > 2:
                # Ubah produksi di belakang
                first = prod[:2]
                tail = prod[2:]
                varExist = False
                for key, val in CNF.items():
                    if val == [first]:
                        prod = [key] + tail
                        varExist = True
                        break
                if not varExist:
                    newVar = 'V' + str(nomorVar)
                    CNF[newVar] = [first]
                    prod = [newVar] + tail
                    nomorVar += 1
            CNF[lhs] += [prod]

    # Mengubah Produksi dengan > 1 terminal
    # Atau Campuran variabel dengan terminal
    CFG = CNF
    CNF = {}
    for lhs, rhs in CFG.items():
        CNF[lhs] = []
        for prod in rhs:
            if len(prod) > 1:
                # Tidak boleh ada terminal
                for i in range(len(prod)):
                    if isTerminal(prod[i]):
                        varExist = False
                        for key, val in CNF.items():
                            if(val == [[prod[i]]]):
                                prod[i] = key
                                varExist = True
                                break
                        if not varExist:
                            newVar = 'V' + str(nomorVar)
                            nomorVar += 1
                            CNF[newVar] = [[prod[i]]]
                            prod[i] = newVar
            CNF[lhs] += [prod]    

    file.close()
    return CNF


def printCFG(CFG):
    print("Ini Mulai")
    for lhs, rhs in CFG.items():
        print(lhs, '->', rhs) 

def printToFile(CFG):
    with open('../grammar/Grammar.out', 'w') as f:
        for lhs, rhs in CFG.items():
            f.write(json.dumps(lhs) + ' -> ' + json.dumps(rhs) + '\n') 

def CYK_Parsing(CNF, string_input):
    W = string_input.split(" ")
    W = W[:len(W)-1]
    N = len(W)
    table = [[set([]) for j in range(N)] for i in range(N)]

    for j in range(N):
        table[j][j].add(W[j])
        for lhs, rhs in CNF.items():
            for rule in rhs:
                if len(rule) == 1 and rule[0] == W[j]:
                    table[j][j].add(lhs)
            
            
        for i in range(j, -1, -1):
            for k in range(i, j):
                for lhs, rhs in CNF.items():
                    for rule in rhs:
                        if len(rule) == 2 and rule[0] in table[i][k] and rule[1] in table[k + 1][j]:
                            table[i][j].add(lhs)
            # print(i, j, table[i][j])

    #Bonus?
    # last_s = 0
    # for i in range(N):
    #     if 'S' in table[0][i]: 
    #         last_s = i
    
    # error_line = 1
    # for i in range(last_s + 1):
    #     if '\n' in raw_tokenized[i]:
    #         error_line += 1
    return 'S' in table[0][N - 1]


def cyk_parse(tokenized, grammar):
    tokenized = tokenized.split(" ")
    tokenized.pop(len(tokenized)-1)
    print(tokenized)
    str_length = len(tokenized)
    table = [[[] for i in range(str_length)] for j in range(str_length)]

    for i in range(str_length):
        for left_side in grammar.keys():
            if tokenized[i] in grammar[left_side]:
                table[i][i].append(left_side)

    time_last = time.time()
    for length in range(2, str_length + 1):
        progress = int((length/str_length)*100)
        delta = time.time() - time_last
        print(f"Progress: {progress}%   -   Time Elapsed: {round(delta, 2)} s", end='\r')

        for start in range(0, str_length - length + 1):
            stop = start + length - 1
            for i in range(start, stop):
                for left_side in grammar.keys():
                    if isinstance(grammar[left_side], list):
                        for right_terms in grammar[left_side]:
                            if right_terms[0] in table[start][i] and right_terms[1] in table[i+1][stop]:
                                if left_side not in table[start][stop]:
                                    table[start][stop].append(left_side)
    print()
    
    last_s = 0
    for i in range(str_length):
        if 'S' in table[0][i]: 
            last_s = i

    # i = 0
    # for row in table:
    #     for elmt in row:
    #         print(i, elmt)
    #     i += 1
        
    return 'S' in table[0][str_length - 1], 
# Driver Code

# Given string
w = "DO "




def loadCNF():
    return CFG_TO_CNF("../grammar/Grammar2.in")

if __name__ == "__main__":
    printToFile(CFG_TO_CNF("../grammar/Grammar.in"))
    # CFG_TO_CNF("../grammar/Grammar.in")
    # CFG_TO_CNF("../grammar/testcase.in")
    # printCFG(CFG_TO_CNF("../grammar/testcase.in"))
    # print(CYK_Parsing(CFG_TO_CNF("../grammar/testcase.in"),w))
