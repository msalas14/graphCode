#-----------------------------------------------
#  CSC 211 Dijkstra's Algorithm Implementation
#-----------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

def dijkstra(g, i):
    
    '''
    Dijkstra's Algorithm
    for graph g, starting with vertex i
    '''
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the graph adjacent to i 
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)
    D[i]=0
    g.getVertex(i).setMark()

    # recently added vertex
    minIndex=i
    ct = 1 #count; keeps track of current vertex
    #go through all vertices using counter
    while n>ct:

        # update D and V based on minIndex 
        for w in g.neighboringVertices(minIndex):
            ''' greedy algorithm '''
            if not w.isMarked():
                k=w.getLabel() ;'' 'current neighbor'''
                edgeVal = g.getEdge(minIndex,k).getWeight()+D[minIndex]# add the previous edge value of D to the neighbor edge 
                if D[k]>edgeVal:
                    ''' 
                        k is the label of the vertex which is it's index in D
                        Now it compares its existing value to the edge value of k
                        Below the values of the arrrays are updated
                    '''
                    D[k]=round(edgeVal,3)
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

        # mark vertex in g
        edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        print("that val: ",edgeVal)
        print("edge: ",g.getEdge(V[minIndex],minIndex))
        g.getVertex(minIndex).setMark()
        ct+=1

    print("D= ", D) #values of D and V arrays
    print("V= ", V)


def dijkstraPuzzle(g, i):
    '''
    Dijkstra's Algorithm
    for graph g, starting with vertex i
    '''
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the graph adjacent to i 
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)
    D[i]=0
    g.getVertex(i).setMark()

    # recently added vertex
    minIndex=i
    ct = 1 #count; keeps track of current vertex
    #go through all vertices using counter
    while n>ct:

        # update D and V based on minIndex 
        for w in g.neighboringVertices(minIndex):
            ''' greedy algorithm '''
            
            if not w.isMarked():
                k=w.getLabel() ;'''current neighbor'''
                if(g.getEdge(minIndex,k).getWeight()!=None):
                    edgeVal = g.getEdge(minIndex,k).getWeight()+D[minIndex]# add the previous edge value of D to the neighbor edge 
                    if D[k]>edgeVal:
                        ''' 
                            k is the label of the vertex which is it's index in D
                            Now it compares its existing value to the edge value of k
                            Below the values of the arrrays are updated
                        '''
                        D[k]=round(edgeVal,3)
                        V[k]=minIndex
                else:
                    D[k]=None
                    V[k]=None
      
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
                if D[j]!=None and D[minIndex] != None:
                    if D[j]<D[minIndex]:
                        minIndex=j

        # mark vertex in g
        if V[minIndex]!=None:
            edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        g.getVertex(minIndex).setMark()
        ct+=1

    print("D= ", D) #values of D and V arrays
    print("V= ", V)
    return V

