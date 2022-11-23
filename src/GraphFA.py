class State:
    def __init__(self, next = {}, term = ""):
        self.next = next
        self.term = term
    
    def connect(self, char, dest):
        self.next[char] = dest

def addWord(root, str):
    # Menambah word ke dalam tree
    # Menambah edge ke State khusus untuk variabel
    for char in str:
        if not char in root.next:
            root.next[char] = State(next = {})
        root = root.next[char]
    root.term = str.upper()

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

if __name__ == "__main__":
    root = State()
    varState = State(next = {}, term = "VARIABLE_NAME")
    addWord(root, "break")
    addWord(root, "const")
    addWord(root, "case")
    addWord(root, "catch")
    addWord(root, "continue")
    addWord(root, "default")
    addWord(root, "delete")
    addWord(root, "else")
    addWord(root, "false")
    addWord(root, "finally")
    addWord(root, "for")
    addWord(root, "function")
    addWord(root, "if")
    addWord(root, "let")
    addWord(root, "null")
    addWord(root, "return")
    addWord(root, "switch")
    addWord(root, "throw")
    addWord(root, "try")
    addWord(root, "true")
    addWord(root, "var")
    addWord(root, "while")
    
