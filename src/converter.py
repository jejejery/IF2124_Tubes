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
        'XORAS',
        'SHLAS',
        'SARAS',
        'SHRAS',
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
        'TYPEOF',
        'RETURN',
        'THROW',
        'INCREMENT',
        'TERNARY'
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


def loadCNF():
    return CFG_TO_CNF("../grammar/Grammar.in")
