#4 위상정렬
class Node:
  def __init__(self, value):
    self.data = value

class Graph:
  def __init__(self):
    self.graph = {}
    self.visit = []
    self.queue = []
    self.degree = []

  def create(self, v1, v2):
    inNode = Node(v1)
    outNode = Node(v2)
    if v1 not in self.graph:
      self.graph[v1] = []
    if v2 not in self.graph:
      self.graph[v2] = []
    self.graph[v2].append(v1)

  def getDegree(self, n):
    for key in self.graph.keys():
      if key not in self.graph: continue
      if n == len(self.graph[key]):
        if key not in self.degree:
          self.degree.append(key)
    print("queue:", self.degree)
    #self.degree.sort()
    return self.degree

  def topology(self):
    node_length = len(self.graph)

    while True:
      if len(self.graph) == 0:
        if len(self.visit) == node_length: break
        else:
          print("사이클이 발생했습니다.")
          break

      self.getDegree(0) #차수가 0인 노드 degree에 추가
      self.visit.append(self.degree[0]) #graph 가장 앞에 있는 노드를 방문

      #기존 그래프의 진입노드도 삭제
      for no, alist in self.graph.items():
        if self.degree[0] in alist:
          alist.remove(self.degree[0])

      self.graph.pop(self.degree[0])
      self.degree.pop(0) #degree에서는 pop

      self.show()

  def show(self):
    print(self.graph)

g = Graph()
#data = [(0,2),(1,2),(2,4),(3,5),(5,8),(5,4),(4,6),(4,7),(6,9),(7,10)]
#0,2,1,2,2,4,3,5,5,8,5,4,4,6,4,7,6,9,7,10
#print("[ 그림 10.3 ]")
#data = [(1,2),(1,3),(1,4),(2,5),(3,5),(4,6),(5,7),(6,7),(6,8),(7,9),(8,9)]
print("[ 그림 10.4 ]")
#1,2,1,3,1,4,2,5,3,5,4,6,5,7,6,7,6,8,7,9,8,9

ary = []
input_node = input("간선 정보 입력: ")
data = list(map(int, input_node.split(",")))

rows = len(data)//2
cols = 2

for i in range(rows):
    row = data[i*cols:(i+1)*cols]
    ary.append(row)

for v, node in ary:
  g.create(v, node)

g.show()
g.topology()
print("topological sort", g.visit)
