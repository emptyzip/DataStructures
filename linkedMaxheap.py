#1번 최종
import math
import copy
import sys
sys.setrecursionlimit(10000)

#값을 힙에 하나씩 모두 추가한 뒤 최대값을 하나씩 삭제하기
class Node:
  def __init__(self, item):
    self.llink = None
    self.data = item
    self.parent = None
    self.rlink = None

class HeapSort:
  def __init__(self):
    self.num = []
    self.result = []
    self.head = Node(0)

  def __str__(self):
    for i in range(self.count):
      print("%2d " % self.num[i])

  def create(self, node):
    if self.find(node) is not None : return 

    if self.head.data == 0: #노드가 빈 상태라면 첫 노드를 헤드 노드 연결
      n = Node(node)
      self.head.llink = n
      self.head.rlink = n #헤드 노드의 rlink에 마지막 노드
      self.head.data += 1 #헤드노드 데이터에 총 노드 수
    else:
      n = Node(node)
      last = self.head.rlink #마지막 노드 가져와서
      last.rlink = n
      n.llink = last
      self.head.rlink = n

      self.head.data += 1 #헤드노드 데이터에 총 노드 수
      parent = math.ceil(self.head.data//2) #부모 값 찾기

      temp = self.head.llink
      for i in range(1, parent+1):
        if i==parent:
          #print(i, parent, temp.data, parent+1)
          n.parent = temp.data
          break
        temp = temp.rlink
    #self.view()

  def setParent(self): #정렬 후 parent값 변경해주기
    temp = self.head.llink
    for i in range(1, self.head.data+1):
        n = self.findIdx(i)
        if i==1:
            n.parent = None
            continue
        else:            
            parent = math.ceil(i//2)
            parentNode = self.findIdx(parent)
            n.parent = parentNode.data

  def view(self, t):
    temp = self.head.llink
    print("[", end=' ')
    while temp:
      if t == 's':
        print(temp.data,"(",temp.parent,") ", end=' ')
      else:
        print(temp.data, end=' ')
      temp = temp.rlink
    print("]", end =' ')
    print()

  def postorder(self, node):
    if node:
      self.postorder(node.llink)
      self.postorder(node.rlink)
      #self.result.append(node.data)
      print(node.data, end=' ')

  def find(self, item): #데이터 값이 같은것
    temp = self.head.llink
    for i in range(self.head.data):
    #while temp != self.head.rlink:
      if temp.data == item: return temp
      temp = temp.rlink
    return None

  def findIdx(self, item):
    temp = self.head.llink
    for i in range(0, self.head.data):
    #while temp != self.head.rlink:
      if i == item-1: return temp
      temp = temp.rlink
    return None

  def findIdxNew(self, item):
    temp = self.head.llink
    for i in range(self.head.data):
      if i == item: return temp
      temp = temp.rlink
    return None

  def makeHeap(self, root, n): #루트가 가장 큰지 검사
    #print(root, n)
    #temp = self.findIdx(root) #현재 루트를 temp에 저장해놓고
    temp = copy.deepcopy(self.findIdxNew(root-1))
    tempVal = temp.data
    child = 2 * root # 자식이 후보가 됨
    #print("c", child)    
    while child <= n: #유효한 자식인지 먼저 검사
      childNode = self.findIdx(child)

      #print("t", temp.data)
      if child < n and childNode.data < childNode.rlink.data:
        child += 1
        childNode = self.findIdx(child)
      if temp.data > childNode.data: break
      else:
        acNode = self.findIdx(child//2)
        acNode.data = childNode.data
        #print("t", tempVal, "c", childNode.data, "a", acNode.data)
        child *= 2
        
    acNode = self.findIdx(child//2)
    #print("t", temp.data)
    acNode.data = temp.data


  def swap(self, a, b):
    aNode = self.findIdxNew(a)
    bNode = self.findIdxNew(b)

    temp = aNode.data
    #print("t", temp, "a", a.data, "b", b.data)
    aNode.data = bNode.data
    bNode.data = temp
    
  def sort(self):
    n = self.head.data
    for i in range(n//2, 0, -1):
      self.makeHeap(i, n)
      self.setParent()
    
    self.view('s')

  def delete(self):
    #print(self.head.data)
    n = self.head.data

    for i in range(n-1, 0, -1):
      self.swap(0, i)
      self.makeHeap(1, i)
      self.view('d')

s = HeapSort()

while True:
  print("input", end=' ')
  num = int(input())
  if num == 999:
    print("del root")
    print("-----------")
    s.view('d')
    s.delete()
    break
  else:
    s.create(num)
    s.sort()

