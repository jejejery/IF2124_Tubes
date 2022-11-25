import time

def CYK_Parsing(CNF, string_input):
    print()
    W = string_input.split(" ")
    W = W[:len(W)-1]
    N = len(W)
    table = [[set([]) for j in range(N)] for i in range(N)]
    toc = time.time()
    
    for j in range(N):
        if(time.time() - toc > 0.5):
            print(f"Progress: {round(j*j*j*100/(N*N*N),2)}%")
            toc = time.time()
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

    
    return 'S' in table[0][N - 1]
