#-------------------------------------------
#  CSC 211 Examples with Graphs
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()

# add vertices
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")

# add edges
g.addEdge("A", "B", 1)
g.addEdge("B", "A", 1)
g.addEdge("A", "C", 1)
g.addEdge("C", "A", 1)
g.addEdge("B", "D", 1)
g.addEdge("D", "B", 1)

# Try out some methods

print("\n print graph info: ")
print(g)


print("\n neighboring vertices of A:")
for vertex in g.neighboringVertices("A"):
    print(vertex)


print("\n incident edges of A:")
for edge in g.incidentEdges("A"):
    print(edge)

# ---- Test the DFS traversal ----

def dfs(g, v):
    """ recursive depth-first search """
    v.setMark()
    print(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w)

def dfsa(g, v, array):
    """ recursive depth-first search """
    v.setMark()
    #print(v.getLabel())
    array.append(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfsa(g, w, array)

print("\n depth-first search: ")
g.clearVertexMarks()
dfs(g,g.getVertex("A"))

# ---- Test the BFS traversal ----

def bfs(g, v):
    """ breadth-first search """
    q=LinkedQueue()
    v.setMark()
    q.add(v)
    while len(q)>0:
        x=q.pop()
        print(x.getLabel())
        for w in g.neighboringVertices(x.getLabel()):
            if not w.isMarked():
                w.setMark()
                q.add(w)
        
def bfsa(g, v):
    """ breadth-first search """
    bfsarray = []
    q=LinkedQueue()
    v.setMark()
    q.add(v)
    while len(q)>0:
        x=q.pop()
        bfsarray.append(x.getLabel())
        #print(x.getLabel())
        for w in g.neighboringVertices(x.getLabel()):
            if not w.isMarked():
                w.setMark()
                q.add(w)
    return bfsarray

print("\n breadth-first search: ")
g.clearVertexMarks()
bfs(g,g.getVertex("A"))



        
    
