import os

def lexer(filePath):
    # Mengembalikan string token berisi hasil konversi file .js 
    # Menggunakan FA untuk mengenali karakter / string / numeral / keyword
    # FA yang digunakan sebagian besar berupa conditional,
    # Hanya beberapa yang menggunakan variable state

    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filePath)
    ret = ""
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_$"
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
        "typeof"    : "TYPEOF",
        "true"      : "TRUE",
        "var"       : "VAR",
        "while"     : "WHILE",
        "new"       : "NEW",
        "do"        : "DO"
    }


    try:
        file = open(filepath, 'r')
        fileStr = file.read()
        itr = 0
        n = len(fileStr)
        state = 0
        # State description :
        # 1 : Program sedang dalam multi-line comment (sudah membaca /*)
        # 2 : Program dalam multi-line comment, karakter yang terakhir dibaca adalah *
        # 0 : Seluruh kondisi selain yang tertulis di atas.

        
        while itr < n:
            c = fileStr[itr]
            itr += 1

            if state == 0:
                if c in ' \r\n':
                    pass
                
                elif c in '+':
                    c = fileStr[itr]
                    if c in '+':
                        itr += 1
                        ret += "INCREMENT "
                    elif c in '=':
                        itr += 1
                        ret += "SUMAS "
                    else:
                        ret += "SIGN "

                elif c in '-':
                    c = fileStr[itr]
                    if c in '-':
                        itr += 1
                        ret += "INCREMENT "
                    elif c in '=':
                        itr += 1
                        ret += "SUBAS "
                    else:
                        ret += "SIGN "

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
                    elif c in '*':
                        # Multi-line comment, change state
                        itr += 1
                        state = 1
                    elif c in '=':
                        itr += 1
                        ret += "DIVAS "
                    else:
                        ret += "OTHER_ARIT_OPERATOR "
                
                elif c in '%':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "MODAS "
                    else:
                        ret += "OTHER_ARIT_OPERATOR "

                elif c in '*':
                    c = fileStr[itr]
                    if c in '*':
                        # Exponent
                        itr += 1
                        c = fileStr[itr]
                        if c in '=':
                            itr += 1
                            ret += "POWAS "
                        else:
                            ret += "OTHER_ARIT_OPERATOR "
                    elif c in '=':
                        itr += 1
                        ret += "MULAS "
                    else:
                        ret += "OTHER_ARIT_OPERATOR "

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
                elif c in ',':
                    ret += "COMMA "
                elif c in ':':
                    ret += "COLON "
                elif c in '[':
                    ret += "OPEN_BRACKET "
                elif c in ']':
                    ret += "CLOSE_BRACKET "
                elif c in '=':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        c = fileStr[itr]
                        if c in '=':
                            itr += 1
                        ret += "LOGI_OPERATOR "
                    else:
                        ret += "EQ "

                elif c in '>':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "LOGI_OPERATOR "
                    elif c in '>':
                        itr += 1
                        c = fileStr[itr]
                        if c in '>':
                            itr += 1
                            c = fileStr[itr]
                            if c in '=':
                                itr += 1
                                ret += "SHRAS "
                            else:
                                ret += "OTHER_ARIT_OPERATOR "
                        elif c in '=':
                            itr += 1
                            ret += "SARAS "
                        else:
                            ret += "OTHER_ARIT_OPERATOR "
                    else:
                        ret += "LOGI_OPERATOR "

                elif c in '<':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "LOGI_OPERATOR "
                    elif c in '<':
                        itr += 1
                        c = fileStr[itr]
                        if c in '=':
                            itr += 1
                            ret += "SHLAS "
                        else:
                            ret += "OTHER_ARIT_OPERATOR "
                    else:
                        ret += "LOGI_OPERATOR "
                elif c in '?':
                    ret += "TERNARY "
                elif c in '&':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "ANDAS "
                    else:
                        if c in '&':
                            itr += 1
                        ret += "OTHER_ARIT_OPERATOR "
                elif c in '|':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "ORAS "
                    else:
                        if c in '|':
                            itr += 1
                        ret += "OTHER_ARIT_OPERATOR "
                elif c in '^':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "XORAS "
                    else:
                        ret += "OTHER_ARIT_OPERATOR "
                elif c in '~':
                    ret += "NOT "
                elif c in '!':
                    c = fileStr[itr]
                    if c in '=':
                        itr += 1
                        ret += "LOGI_OPERATOR "
                    else: 
                        ret += "NOT "


            elif state == 1:
                if c in '*':
                    state = 2
            

            elif state == 2:
                if c in '*':
                    pass
                elif c in '/':
                    state = 0
                else:
                    state = 1

        file.close()
    except Exception as e:
        print(e)

    return ret
    
