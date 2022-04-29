#-------------------------------------------
#  CSC 211 Prim's Algorithm Implementation
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

def prim(g, i):
    '''
    Prim's Algorithm
    returns the minimal spanning tree (mst)
    for graph g, starting with vertex i
    '''

    # initialize values
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the MST adjacent to i 
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)

    # create MST and add vertex i into it 
    D[i]=0  
    mst = LinkedDirectedGraph()
    mst.addVertex(i) ; ''' ~i~ is the starting point '''
    g.getVertex(i).setMark()

    # recently added vertex
    minIndex=i

    # add vertices until the mst has as many vertices as g
    while mst.sizeVertices()<n:

        # update D and V based on minIndex 
        for w in g.neighboringVertices(minIndex):
            ''' greedy algorithm '''
            if not w.isMarked():
                k=w.getLabel() ;'''current neighbor'''
                edgeVal = g.getEdge(minIndex,k).getWeight()
                if D[k]>edgeVal:
                    ''' 
                        k is the label of the vertex which is it's index in D
                        Now it compares its existing value to the edge value of k
                        Below the values of the arrrays are updated
                    '''
                    D[k]=edgeVal
                    V[k]=minIndex
      
        # find the first unvisited vertex
        k=-1
        j=0
        while k<0 and j<n:
            if not g.getVertex(j).isMarked():
                k=j
            j+=1

        # find minimum cost unvisited vertex
        minIndex=k
        for j in range(0,n):    
            if not g.getVertex(j).isMarked():
                if D[j]<D[minIndex]:
                    minIndex=j

        # add new vertex to the MST and mark it in g
        edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        mst.addVertex(minIndex)
        ''' 2-way edge '''
        mst.addEdge(minIndex,V[minIndex],edgeVal) 
        mst.addEdge(V[minIndex],minIndex,edgeVal)

        g.getVertex(minIndex).setMark()

    # print("D= ", D) #debugging; values of D and V arrays
    # print("V= ", V)

    return mst

#-----------------------------------
# Test out the method below

# g = LinkedDirectedGraph()

# # add vertices
# for i in range(0,6):
#     g.addVertex(i)

# # add edges
# g.addEdge(0,1,24)
# g.addEdge(1,0,24)
# g.addEdge(0,3,15)
# g.addEdge(3,0,15)
# g.addEdge(0,5,22)
# g.addEdge(5,0,22)
# g.addEdge(1,2,18)
# g.addEdge(2,1,18)
# g.addEdge(1,3,13)
# g.addEdge(3,1,13)
# g.addEdge(1,5,10)
# g.addEdge(5,1,10)
# g.addEdge(2,4,17)
# g.addEdge(4,2,17)
# g.addEdge(3,4,11)
# g.addEdge(4,3,11)

# # Try out some methods

# print("\n print graph info : g ")
# print(g)

# m=prim(g,0)

# print("\n print graph info : mst ")
# print(m)




