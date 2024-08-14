class Sym:
  OPEN_B = 1
  CLOSE_B = 2
  PLUS = 3
  MINUS = 4
  TIMES =5
  DIVIDE = 6
  MOD = 7
  OPERAND = 8

class Expression:
  def __init__(self, expr):
    self.stack = []
    self.size =100
    self.expr = expr
    self.top = -1
    self.output = ""
    self.tokens = [] # expr 공백 제거 후 피연산자와 연산자로 구분하는 stack
    self.postfix = [] # infix -> postfix 변환 결과 스택

  def push(self, item):
    if not self.isFull():
      self.top += 1
      self.stack.append(item)
      print("스택:", self.stack)
    else:
      print("Stack full")

  def pop(self):
    if not self.isEmpty():
      self.top -= 1
      return self.stack.pop()
    else:
      print("stack empty")

  def eval_postfix(self):
    print("expr to evaluate:",self.postfix)
    for sym in self.postfix:
      sym_type = self.getSymtype(sym)
      if sym_type == Sym.OPERAND:
        self.push(int(sym))
      else:
        op2 = self.pop()
        op1 = self.pop()
        print("연산:", op1, op2, sym)
        print()
        if sym_type == Sym.PLUS:
          self.push(op1 + op2)
        elif sym_type == Sym.MINUS:
          self.push(op1 - op2)
        elif sym_type == Sym.TIMES:
          self.push(op1 * op2)
        elif sym_type == Sym.DIVIDE:
          self.push(op1 / op2)
        elif sym_type == Sym.MOD:
          self.push(op1 % op2)
    return self.pop()

  def splitTokens(self): # 공백 제거 및 피연산자와 연산자로 구분하는 함수
    self.tokens=[]
    tmp=""
    i=0
    for token in self.expr:
      i+=1
      if token.isdigit(): #숫자면
        tmp += token #tmp에 저장
        if i==len(self.expr): #마지막 값이라면 현재까지의 tmp값을 스택에 저장
          self.tokens.append(int(tmp))
      else:
        if token != ' ': #공백이 아니고
          if tmp != '': #tmp값이 있다면
            self.tokens.append(int(tmp)) #tmp에 저장된 숫자 stack에 추가
            tmp="" #추가 후 tmp 초기화
          self.tokens.append(token) #연산자 추가
    print("splitTokens: ",self.tokens)

  def infix_postfix(self):
    for token in self.tokens:
      #print(token, type(token), end=' ')
      if type(token) == int : #숫자면
        self.postfix.append(token) #스택에 추가
        print("postfix:", self.postfix)
      elif token == '(':
        self.push(token)
      elif token == ')':
        sym=self.pop()
        while sym != '(':
          self.postfix.append(sym)
          sym = self.pop()
      else: #연산자인 경우 
        while not self.isEmpty() and self.precedence(self.stack[-1]) >= self.precedence(token):
          sym = self.pop()
          self.postfix.append(sym)
        self.push(token)
      

    while not self.isEmpty():
      self.postfix.append(self.pop())
    
  def isEmpty(self): return len(self.stack)==0

  def isFull(self): return len(self.stack)==self.size

  def show_stack(self): print(self.stack)

  def precedence(self, op):
    if op == '(': return 0
    elif op in ['+', '-']: return 1
    elif op in ['*', '/', '%']: return 2

  def getSymtype(self, sym):
    if sym == '(': sym_type = Sym.OPEN_B
    elif sym == ')': sym_type = Sym.CLOSE_B
    elif sym == '+': sym_type = Sym.PLUS
    elif sym == '-': sym_type = Sym.MINUS
    elif sym == '*': sym_type = Sym.TIMES
    elif sym == '/': sym_type = Sym.DIVIDE
    elif sym == '%': sym_type = Sym.MOD
    else: sym_type = Sym.OPERAND
    return sym_type

#expr = "12 * ( 25 - 15 ) + ( 13 + 4 * 2 ) / 2"
print("input an infix :", end=' ')
expr = input()
e = Expression(expr)
e.splitTokens()
e.infix_postfix()
print("-------")
print("infix to postfix:", e.postfix)
print("-------")
e.stack =[]
print("evaluation = ", e.eval_postfix())