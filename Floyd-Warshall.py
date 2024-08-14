#3번 플로이드
import sys
INF = float(1e9)

class Node:
  def __init__(self, node, weight):
    self.data = node
    self.weight = weight

class ShortestPath:

  def __init__(self):
    self.graph ={}
    self.visit =[]
    self.dist = {}
    self.prev=[[]]
    self.matrix = [[]]
    INF = '-'

  def create(self, v, dest, weight):
    node = Node(dest, weight)
    if v not in self.graph:
      self.graph[v] = []
    if dest not in self.graph:
      self.graph[dest] = []
      self.graph[dest].append(node)
    self.graph[v].append(node)
  
  def showMatrix(self, n):
    print("dist: A", n)
    print("-----------")
    k = 0
    for i in self.matrix:
      print( k ,":", end=' ')
      for j in i:
        if j >= INF:
          print('inf', end=' ')
          continue
        print(j, end=' ')
      k += 1
      print()

  def floydWarshall(self):

    #정점 수의 2차원 배열
    n = len(self.graph)
    
    self.matrix = [ [INF] * n for _ in range(n) ]
    self.prev = [[0 for j in range(n)] for i in range(n)]
    #print(self.prev)
    
    #초기화
    for no, nodes in self.graph.items():
      for node in nodes:
        vertex = node.data
        cost = node.weight
        self.matrix[no][vertex] = cost
        self.matrix[no][no] = 0
    
    self.showMatrix(-1)
    print()

    for i in range(n):
        for j in range(n):
            if i != j and self.matrix[i][j] != INF:
                self.prev[i][j] = j
            else:
                self.prev[i][j] = -1

    for k in range(n) :  
      for i in range(n) :
        for j in range(n) :
          if self.matrix[i][j] > self.matrix[i][k]+self.matrix[k][j]:
            self.matrix[i][j] = self.matrix[i][k]+self.matrix[k][j]
            self.prev[i][j] = self.prev[i][k] #경로 행렬에 추가
      
      self.showMatrix(k) #행렬 출력
      print()

    #경로 출력
    for s in range(n):
      for d in range(n):
        if s != d:
          path = self.getPath(s, d)
          if len(path) == 0:
            self.matrix[s][d]=0 #경로가 없는 경우 0
          print("s~d:", s, d,", path ",path," len = ", self.matrix[s][d])
  
  def getPath(self, s, d):
    if self.prev[s][d] == -1:
      return []
    path = [s] 
    while s != d:
      s = self.prev[s][d]
      path.append(s) #path에 경로 추가
    return path


g = ShortestPath()
#print("그림 10.2")
#network= [(0,1,8),(0,3,1),(3,1,2),(3,2,9),(1,2,1),(2,0,4)]
print("연습문제 10.3")
network= [(0,1,8),(0,2,3),(0,3,6),(1,2,4),(1,3,1),(3,0,7),(3,2,2)]
#print("연습문제 10.2")
#network= [(0,1,11),(0,2,5),(1,0,2),(1,2,8),(2,1,3)]
for start, dest, weight in network:
  g.create(start, dest, weight)
#g.show()
g.floydWarshall()
