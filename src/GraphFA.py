import os

class State:
    def __init__(self, next = {}, term = ""):
        self.next = next
        self.term = term
    
    def connect(self, char, dest):
        self.next[char] = dest

def addWord(root, str, terminal):
    # Menambah word ke dalam tree
    # Menambah edge ke State khusus untuk variabel
    for char in str:
        if not char in root.next:
            root.next[char] = State(next = {})
        root = root.next[char]
    root.term = terminal

def searchWord(root, str):
    # Mengembalikan array of token yang sesuai dengan str
    ret = []
    pos = root
    for x in str:
        if x not in pos.next:
            if len(pos.term) == 0:
                return []
            else:
                ret += [pos.term]
                pos = root
        else:
            pos = pos.next[x]
    if pos != root:
        ret += [pos.term]
    return ret

def lexer(filePath):
    # Mengembalikan string token berisi hasil konversi file .js 
    # Menggunakan FA untuk mengenali karakter / string / numeral / keyword

    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filePath)
    ret = ""
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_"
    numbers = "0123456789"
    keyword = {
        "break"     : "BREAK",
        "const"     : "CONST",
        "case"      : "CASE",
        "catch"     : "CATCH",
        "continue"  : "CONTINUE",
        "default"   : "DEFAULT",
        "delete"    : "DELETE",
        "else"      : "ELSE",
        "false"     : "FALSE",
        "finally"   : "FINALLY",
        "for"       : "FOR",
        "function"  : "FUNCTION",
        "if"        : "IF",
        "let"       : "LET",
        "null"      : "NULL",
        "return"    : "RETURN",
        "switch"    : "SWITCH",
        "throw"     : "THROW",
        "try"       : "TRY",
        "true"      : "TRUE",
        "var"       : "VAR",
        "while"     : "WHILE"
    }


    try:
        file = open(filepath, 'r')
        fileStr = file.read()
        itr = 0
        n = len(fileStr)

        
        while itr < n:
            c = fileStr[itr]
            itr += 1
            if c in ' \r\n':
                pass
            
            elif c in '+-':
                ret += "ARIT_OPERATOR "

            elif c in '/':
                peek = itr
                c = fileStr[peek]
                if c in '/':
                    # Comment, no need to add token
                    while itr < n:
                        c = fileStr[itr]
                        itr += 1
                        if c in '\n':
                            break
                else:
                    ret += "ARIT_OPERATOR "

            elif c in '*':
                c = fileStr[itr]
                if c in '*':
                    # Exponent
                    itr += 1
                ret += "ARIT_OPERATOR "

            elif c in letters:
                # Baca sebuah variabel / keyword
                # Tidak boleh diawali atau diakhiri titik
                s = c
                while itr < n:
                    c = fileStr[itr]
                    if c in letters or c in numbers or c in '.':
                        s += c
                        itr += 1
                    else:
                        break
                if s in keyword:
                    ret += keyword[s] + ' '
                elif fileStr[itr-1] == '.':
                    ret += "ERROR "
                else:
                    ret += "VARIABLE "

            elif c in '\'\"':
                # baca string
                # String harus ditutup
                startStr = c
                closeStr = False
                while itr < n:
                    c = fileStr[itr]
                    if c == '\\':
                        # Ignore possible close string
                        # -> \' is still part of string
                        itr += 2
                    elif c == startStr:
                        closeStr = True
                        break
                    else:
                        itr += 1
                itr += 1
                if closeStr:
                    ret += "STRING "
                else:
                    ret += "ERROR "
            
            elif c in numbers or c in '.':
                # baca angka, bisa punya angka di belakang koma
                # Koma(.) boleh terletak di paling akhir
                jumlahKoma = 0
                if c == '.':
                    jumlahKoma += 1
                while itr < n:
                    c = fileStr[itr]
                    if c == '.':
                        jumlahKoma += 1
                    elif c in numbers:
                        pass
                    else:
                        break
                    itr += 1
                if jumlahKoma <= 1:
                    ret += "NUMBER "
                else:
                    ret += "ERROR "
                
            elif c in '{':
                ret += "OPEN_CURLY "
            elif c in '}':
                ret += "CLOSE_CURLY "
            elif c in '(':
                ret += "OPEN_PARANTHESES "
            elif c in ')':
                ret += "CLOSE_PARANTHESES "
            elif c in ';':
                ret += "SEMICOLON "
            elif c in '[':
                ret += "OPEN_BRACKET "
            elif c in ']':
                ret += "CLOSE_BRACKET "
            elif c in '=':
                ret += "EQ "
            elif c in '<':
                ret += "LT "
            elif c in '>':
                ret += "GT "
            elif c in '|':
                ret += "OR "
            elif c in '&':
                ret += "AND "
            
            
                
                

        file.close()
    except Exception as e:
        print(e)

    return ret
    
    

if __name__ == "__main__":
    root = State()
    varState = State(next = {}, term = "VARIABLE_NAME")
    print(lexer("../js/test.js"))
    
