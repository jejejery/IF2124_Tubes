def startNum(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 2
  else:
    return 0

def state2Num(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 2
  elif ord(char) == 46: # ord('.') = 46
    return 3
  else:
    return 0

def state3Num(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 3
  else:
    return 0

# Memeriksa apakah string merupakan angka yang valid
def isNumber(string):
  state = 1
  for i in range(len(string)):
    if state == 1:
      state = startNum(string[i])
    elif state == 2:
      state = state2Num(string[i])
    elif state == 3:
      state = state3Num(string[i])
    elif state == 0:
      return False
  return True

def startVar(char):
  if ord(char) >= 65 and ord(char) <= 90:
    return 2
  elif ord(char) >= 97 and ord(char) <= 122:
    return 2
  elif ord(char) == 95:
    return 2
  else:
    return 0

def state2Var(char):
  if ord(char) >= 65 and ord(char) <= 90:
    return 2
  elif ord(char) >= 97 and ord(char) <= 122:
    return 2
  elif ord(char) >= 48 and ord(char) <= 57:
    return 2
  else:
    return 0

# Memeriksa apakah string merupakan variabel yang valid
def isVariable(string):
  state = 1
  for i in range(len(string)):
    if state == 1:
      state = startVar(string[i])
    elif state == 2:
      state = state2Var(string[i])
    elif state == 0:
      return False
  return True

def isOps(char):
  if char == '+' or char == '-' or char == '*' or char == '/' or char == '^' or char == '%' or char == '&' or char == '|' or char == '^' or char == '<<' or char == '>>':
    return True
  else:
    return False

def startExp(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 2
  elif ord(char) >= 65 and ord(char) <= 90:
    return 4
  elif ord(char) >= 97 and ord(char) <= 122:
    return 4
  else:
    return 0

def state2Exp(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 2
  elif ord(char) == 46:
    return 4
  elif isOps(char):
    return 1
  else:
    return 0

def state3Exp(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 3
  elif isOps(char):
    return 1
  else:
    return 0

def state4Exp(char):
  if ord(char) >= 48 and ord(char) <= 57:
    return 4
  elif ord(char) >= 65 and ord(char) <= 90:
    return 4
  elif ord(char) >= 97 and ord(char) <= 122:
    return 4
  if isOps(char):
    return 1

# Memeriksa apakah string merupakan ekspresi operasi yang valid
def isExp(string):
  state = 1
  for i in range(len(string)):
    if state == 1:
      state = startExp(string[i])
    elif state == 2:
      state = state2Exp(string[i])
    elif state == 3 :
      state = state3Exp(string[i])
    elif state == 4:
      state = state4Exp(string[i])
    elif state == 0:
      return False
  return True

# print(isVariable('_123asf'))
print(isVariable('_asem'))
# print(isNumber("43.23"))
# print(isExp("a+b-23.41"))
      