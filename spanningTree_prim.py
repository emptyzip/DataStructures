#2번 prim
class Node:
  def __init__(self, value):
    self.data = value

class Graph:
  def __init__(self):
    self.graph = {}
    self.v_list = {}
    self.edge = []
    self.total = 0
    self.visited = {}
    self.visited = set()

  def create(self, v, data, weight):
    node = Node(data)
    if v not in self.graph:
      self.graph[v] = []
    self.graph[v].append((node, weight))

  def find(self, v2):
    for v1, lst in self.v_list.items():
      if v2 == v1: return v1
      if v2 in self.v_list[v1]: return v1
    return -1

  def union(self, s1, s2):
    if s1 < s2:
      self.v_list[s1].append(s2)
      self.v_list[s1].extend(self.v_list[s2])
      del self.v_list[s2]
    else:
      self.v_list[s2].append(s1)
      self.v_list[s2].extend(self.v_list[s1])
      del self.v_list[s1]

  def minNode(self, nodes):
    min_cost=0
    min_v1=0
    min_v2=0
    for v1, v2, cost in network:
      if v2 in nodes or v1 in nodes:
        if min_cost == 0: #맨 처음 비교면 해당 노드의 가장 첫번째 노드의 cost를 넣어줌
          min_cost = cost
          min_v1 = v1
          min_v2 = v2
          continue
        if cost < min_cost: # 노드셋에 포함되는 간선 중 cost가 가장 작은 것을 넣음
          min_cost = cost
          min_v1 = v1
          min_v2 = v2

    return min_v1, min_v2, min_cost

  def prim(self):
    #모든 정점 포함시키기
    for v1, v2, cost in network:
      if v1 not in self.v_list:
        self.v_list[v1] = []
      if v2 not in self.v_list:
        self.v_list[v2] = []
    print('set list=', self.v_list)

    nodes = len(self.v_list)

    print('시작 노드 입력: ',end=' ')
    start = int(input())
    self.visited.add(start)

    while True:
      if len(self.edge) == nodes-1:
        break

      v1, v2, cost = self.minNode(self.visited) #입력받은 노드 중에서 최소 간선 찾기

      s1 = self.find(v1)
      s2 = self.find(v2)
        #print('v1 set:', s1, ', v2 set:', s2)
      if s1 == s2:
        print("(",v1,",",v2,") the same set. rejected for cycle")
        network.remove((v1,v2,cost))
        continue
      else:
        self.visited.update([v1, v2])
        network.remove((v1,v2,cost))
        self.union(s1, s2)
        self.edge.append((v1, v2, cost))
        self.total += cost
        print('(', v1,',',v2,')', 'cost = ', cost)


g = Graph()
#network = [(1,5,6), (1,6,8), (2,3,17), (2,6,9), (5,6,7), (3,7,15), (3,4,5), (3,8,3), (4,8,4), (6,7,10)]
#print("[ 그림 9.24 ]")
network = [(1,2,5),(1,4,3),(2,5,10),(4,5,6),(4,6,7),(5,3,8),(5,7,13),(6,7,15),(3,7,11)]
print("[ 238쪽 - 문제 3 ]")
for v, node, weight in network:
  g.create(v, node, weight)

print('network=', network)
g.prim()
print()
print('Spanning tree vertices=', g.v_list)
print('Spanning tree edge=', g.edge)
print('cost total=', g.total)
