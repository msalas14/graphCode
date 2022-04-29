import dijkstra
from graph import LinkedDirectedGraph 
#-----------------------------------
# Test out the method below

g = LinkedDirectedGraph()

# add vertices
for i in range(0,9):
    g.addVertex(i)

# add edges
g.addEdge(0,1,3.8)
g.addEdge(1,0,3.8)
g.addEdge(1,2,1.3)
g.addEdge(2,1,1.3)
g.addEdge(3,4,1.6)
g.addEdge(4,3,1.6)
g.addEdge(4,5,3.1)
g.addEdge(5,4,3.1)
g.addEdge(6,7,4.3)
g.addEdge(7,7,4.3)
g.addEdge(7,8,1.1)
g.addEdge(8,7,1.1)
g.addEdge(0,3,0.6)
g.addEdge(3,0,0.6)
g.addEdge(1,4,1.2)
g.addEdge(4,1,1.2)
g.addEdge(2,5,0.7)
g.addEdge(5,2,0.7)
g.addEdge(3,6,2.2)
g.addEdge(6,3,2.2)
g.addEdge(4,7,3.4)
g.addEdge(7,4,3.4)
g.addEdge(5,8,1.2)
g.addEdge(8,5,1.2)


print(g)

# try it out
dijkstra.dijkstra(g,0)