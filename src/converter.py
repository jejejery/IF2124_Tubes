# File : converter.py
# Berisi coverter CFG ke CNF

# Aturan isi CFG (Untuk memudahkan convert):
# 1. Tidak ada produksi epsilon
# 2. Seluruhnya huruf besar

import os

# File locator
dir_path = os.path.dirname(os.path.realpath(__file__))

def isTerminal(str):
    # Mengembalikan True jika str adalah terminal
    return str in [
        'FUNCTION_NAME',
        'VARIABLE',
        'X'
    ]

def isVariable(str):
    return not isTerminal(str)

def CFG_TO_CNF(File_Path):
    File_Path = os.path.join(dir_path, File_Path)
    file = open(File_Path, 'r')
    fileLines = file.read().split('\n')
    CFG = {}
    for x in fileLines:
        a, b = x.split(' -> ')
        if a not in CFG.keys():
            CFG[a] = []
        CFG[a] += [b.split(' ')]
    
    # Menghilangkan unit production
    for lhs, rhs in CFG.items():
        for prod in rhs:
            if len(prod) > 1 or isTerminal(prod[0]):
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
                for member in prod:
                    if isTerminal(member):
                        newVar = 'V' + str(nomorVar)
                        nomorVar += 1
                        member = newVar
                        CNF[newVar] = [member]
            CNF[lhs] += prod    

    file.close()
    return CNF


def printCFG(CFG):
    for lhs, rhs in CFG.items():
        print(lhs, '->', rhs) 

def Parsing_CYK(word,CNF):
    word = word.split(" ")
    n = len(word)
    T = [[set([]) for j in range(n)] for i in range(n)]

    for j in range(n):
        for head, body in CNF.items():
            for rule in body:
                if len(rule) == 1 and rule[0] == word[j]:
                    T[j][j].add(head)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in T[i][k] and rule[1] in T[k + 1][j]:
                            T[i][j].add(head)

    print(T)
    return len(T[0][n - 1]) != 0
# Driver Code

# Given string
w = "X"

# Function Call
if(Parsing_CYK(w, CFG_TO_CNF("../grammar/testcase.in"))):
    print("yes!")

        
if __name__ == "__main__":
    CFG_TO_CNF("../grammar/Grammar.in")
    printCFG(CFG_TO_CNF("../grammar/testcase.in"))
    print(Parsing_CYK(w, CFG_TO_CNF("../grammar/testcase.in")))
