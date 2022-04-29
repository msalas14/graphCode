#-------------------------------------------
#  structuredGraphs.py
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
import dijkstra

g = LinkedDirectedGraph()

def G(g,N):
    ''' G(N) for any N>= 1'''
    if(N>=1):
        for i in range(N*N): #ADD VERTICES TO GRAPH
            g.addVertex(i)
        for i in range(N*N): #ADD ALL EDGES TO GRAPH
            if(N<=i):   # has up?
                g.addEdge(i,i-N,1)
            if( i%N != 0): #has left?
                g.addEdge(i,i-1,1)
            if((i+1)%N!=0): #has right?
                g.addEdge(i, i+1,1)
            if(i<(N*(N-1))): #has down?
                g.addEdge(i,i+N,1)
        
    else:
        print("invalid G(N)")

def bfsa(g, v):
    """ breadth-first search """
    bfsarray = []
    q=LinkedQueue()
    v.setMark()
    q.add(v)
    while len(q)>0:
        x=q.pop()
        bfsarray.append(x.getLabel())
        for w in g.neighboringVertices(x.getLabel()):
            if not w.isMarked():
                w.setMark()
                q.add(w)
    return bfsarray
    
def dfsa(g, v, array):
    """ recursive depth-first search """
    v.setMark()
    #print(v.getLabel())
    array.append(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfsa(g, w, array)

''' Example of G(N) and representation of the created graph'''
G(g,7)
print(g)

''' DFS and BFS of G(N) '''
dfsarray = []
print("\n depth-first search: ")
g.clearVertexMarks()
dfsa(g,g.getVertex(0), dfsarray)
print(dfsarray)

print("\n breadth-first search: ")
g.clearVertexMarks()
print(bfsa(g,g.getVertex(0)))

print("\n dijkstra algorithm: ")
dijkstra.dijkstraPuzzle(g,0)