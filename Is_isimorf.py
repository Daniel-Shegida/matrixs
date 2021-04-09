# TODO 2 матрицы, если изморфны bool

class Node:
  def __init__(self, no):
    self.no = no
    self.color = None
    self.edges = []

  def connections(self):
    d = {}
    for e in self.edges:
      if e.color in d:
        d[e.color] += 1
      else:
        d[e.color] = 1
    dlist = d.items()
    dlist.sort()
    return (self.color, tuple(dlist))

class Graph:
  def __init__(self, nodeCount):
    self.nodeCount = nodeCount
    self.nodes = [Node(ix) for ix in range(nodeCount)]
    self.edgeCount = 0

  def addEdge(self, a, b):
    self.nodes[a].edges.append(self.nodes[b])
    self.nodes[b].edges.append(self.nodes[a])
    self.edgeCount += 1

  def addEdges(self, edgeList):
    for a, b in edgeList:
      self.addEdge(a, b)

  def _createHistogram(self):
    d = {}
    for n in self.nodes:
      k = n.connections()
      if k in d:
        d[k].append(n)
      else:
        d[k] = [n]
    return d

  def _wipe(self, color):
    for n in self.nodes:
      n.color = color

  def quickCheck(self, other):
    if self.nodeCount != other.nodeCount:
      return False
    if self.edgeCount != other.edgeCount:
      return False
    if self.nodeCount  <= 1:
      return True

    colors = 0
    colorCounters = {0: self.nodeCount}
    self._wipe(colors); other._wipe(colors)
    painted = True
    while painted:
      painted = False
      sHistogram = self._createHistogram(); oHistogram = other._createHistogram()
      for k in sHistogram:
        sNodes = sHistogram[k]; oNodes = oHistogram[k]
        if len(sNodes) != len(oNodes):
          return False
        if len(sNodes) != colorCounters[k[0]]:
          colors += 1
          colorCounters[colors] = len(sNodes)
          colorCounters[k[0]] -= len(sNodes)
          for n in sNodes:
            n.color = colors
          for n in oNodes:
            n.color = colors
          painted = True
    return True


if __name__ == "__main__":
  g1 = Graph(7)
  g1.addEdges([(0,1), (1,2), (2,3), (3,4), (4,5), (5,0), (5,1), (3,6)])

  g2 = Graph(7)
  g2.addEdges([(0,1), (1,2), (2,3), (3,4), (4,5), (5,0), (5,1), (4,6)])

  print "expected False:", g1.quickCheck(g2)
  print "expected True:", g1.quickCheck(g1)

  https: // dxdy.ru / topic1502.html