from graph import LinkedDirectedGraph
import prim

g = LinkedDirectedGraph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,.4)
g.addEdge(1,0,.4)
g.addEdge(0,2,.2)
g.addEdge(2,0,.2)
g.addEdge(0,5,2.2)
g.addEdge(5,0,2.2)

g.addEdge(1,2,.1)
g.addEdge(2,1,.1)
g.addEdge(1,3,.2)
g.addEdge(3,1,.2)

g.addEdge(2,3,.6)
g.addEdge(3,2,.6)
g.addEdge(2,4,.8)
g.addEdge(4,2,.8)

g.addEdge(3,4,.3)
g.addEdge(4,3,.3)
g.addEdge(3,5,.5)
g.addEdge(5,3,.5)

print("Original Graph: ")
print(g, "\n \n MST: ")
mst = prim.prim(g,0)
print(mst)