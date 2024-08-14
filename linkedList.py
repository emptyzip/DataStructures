class Node:
    def __init__(self, item):
        self.data = item
        self.rlink = None
        self.llink = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return not self.head
    
    def find(self, item):
        temp = self.head
        while temp:
            if temp.data == item: return temp
            temp = temp.rlink
            if temp == self.tail: break
        return None

    def findLoc(self, item):
      temp = self.head
      i=0
      while temp:
          if temp.data == item.data: return i
          temp = temp.rlink
          i += 1
          if temp == self.tail: break
      return 0

    def view(self):
        temp = self.head
        print("[", end=' ')
        while True:
            print(temp.data, end=' ')
            temp = temp.rlink
            if temp == self.tail: break
        print("]")

    def add(self, item):
        node = Node(item)
        if self.isEmpty():
          self.head = node
          self.tail = node
          node.llink = self.tail
          node.rlink = self.head
        else:
          temp = self.tail # 마지막 값
          self.tail.rlink = node
          node.llink = temp # 노드의 llink에 마지막 값을 넣어줌
          node.rlink = self.head
          self.head.llink = node
          self.tail = node
          
    def move(self, item, player):
      if self.isEmpty():
            print("List Empty")
            return
      node = self.find(player) # 넘어온 플레이어의 값을 찾음
      if not node:
        print("Not found")
        return
      
      ###노드의 원래 위치의 prev, next
      prev = node.llink
      next = node.rlink

      loc = self.findLoc(node) #노드 위치 찾기
      if loc == 0: #플레이어가 0번째 위치에 있다면 헤드노드를 변경해줌 
        self.head = next #head 변경
        next.llink = self.tail
        self.tail.rlink = next
      if self.tail == node: #tail 변경
        self.tail = prev
        prev.rlink = self.head
        self.head.llink = prev
      
      #노드가 빠진 자리 이어주기 
      prev.rlink = next
      next.llink = prev

      #이동할 자리에 노드 위치시키기
      prev = self.head
      temp = 0
      for i in range((item+loc)-1):
        #print(i)
        prev = prev.rlink #최종 목적지의 prev값을 가져옴
        temp = i+1
      next = prev.rlink

      if prev.data > 0: 
        print(player," player won!")
        return 0
      
      #기존 노드 위치에서
      #prev와 next 사이에 node를 이어주기
      prev.rlink = node
      node.llink = prev
      next.llink = node
      node.rlink = next

    def back(self, player):
       return
    
    def switching(self):
       return
    
board = Linkedlist()

while True:
  print("노드 수 입력:", end=' ')
  n = int(input())
  if n < 8 or n > 32:
    print("노드 값은 8~32 사이의 값을 입력하세요.", end=' ')
  else:
    break

print()
print("Game Start!")
print("플레이어 초기 위치")
#플레이어의 값
p1 = 1
p2 = 2

#플레이어 위치 값
p1_loc = 0
p2_loc = (n//2)
if(n%2 == 1): p2_loc -= 1 #홀수면 -1
p2_loc -= 1

#보드판 초기화 #보드에 플레이어 위치 지정
for i in range(n):
    if i==p1_loc:
      board.add(p1)
    if i==(p2_loc):
      board.add(p2)
    else:
      board.add(0)

board.view()
print()

i = p1
while i > 0: # 잡히면 잡은 플레이어의 값으로 업데이트, 각각 잡히지 않았을 때 반복
  #현재 위치
  
  print(i,"(", end=' ')
  x, y = map(int, input().split())

  if x==6 and y==6:
    print(") 이동방향 전환", end=' ')
    board.switching()
  elif x==5 and y==5:
    print(") 말의 위치 교환", end=' ')
  elif x==1 and y==1:
    print(") 뒤로 1칸 이동", end=' ')
    board.back(i)
  else:
    print(")", x+y,"칸 전진")
    result = board.move(x+y, i) #현재위치, 전진할칸, 플레이어
    if result == 0: break
    board.view()

  if i== p1: 
    i=p2
  else: 
    i=p1
