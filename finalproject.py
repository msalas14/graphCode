#-------------------------------------------
#  structuredGraphs.py
#-------------------------------------------

from graph import LinkedDirectedGraph
from random import *
from graphics import *
import dijkstra
g = LinkedDirectedGraph()
def G(g,N):
    ''' G(N) for any N>= 1'''
    x = 0; y = 0
    desired = 50 * N
    messages = ["start", "end"]
    currText=0; cellCt = 0
    blocked = []
    centerPts = []
   

    if(N>=1):
        while  y<desired:
            while(x<desired):
                sq = Rectangle(Point(x,y), Point(x+50,y+50))
                centerPts.append(sq.getCenter())
                if (x == (desired-50) and y == (desired-50)) or (x==0 and y==0):
                    '''start and end cells'''
                    sq.setFill("aquamarine3")
                    sq.draw(workArea)
                    message = Text(Point(x+25,y+25),messages[currText])
                    message.draw(workArea)
                    currText+=1
                    
                elif random()<.25: 
                    blocked.append(cellCt)
                    '''create blocked cell'''
                    #blocked cells will not have up/down/left/right
                    sq.setFill("gray26")
                    sq.draw(workArea)
                else: 
                    '''unblocked cells'''
                    sq.draw(workArea)
                    center = Circle(sq.getCenter(),5)
                    center.setFill("blue")
                    center.draw(workArea)
                x+=50
                cellCt+=1
            x=0; y+=50
        for i in range(N*N): #ADD VERTICES TO GRAPH
            g.addVertex(i)
        for i in range(N*N): #ADD ALL EDGES TO GRAPH
            if i not in blocked:
                if(N<=i):   # has up?
                    if(i-N) not in blocked:
                        g.addEdge(i,i-N,1)
                        line = Line(centerPts[i],centerPts[i-N])
                        line.setFill("red")
                        line.draw(workArea)
                    # else:
                    #     g.addEdge(i, i-N, None)
                if( i%N != 0): #has left?
                    if(i-1) not in blocked:
                        g.addEdge(i,i-1,1)
                        line = Line(centerPts[i],centerPts[i-1])
                        line.setFill("red")
                        line.draw(workArea)
                    # else:
                    #     g.addEdge(i, i-1, None)
                if((i+1)%N!=0): #has right?
                    if(i+1) not in blocked:
                        g.addEdge(i, i+1,1)
                        line = Line(centerPts[i],centerPts[i+1])
                        line.setFill("red")
                        line.draw(workArea)
                    # else:
                    #     g.addEdge(i, i+1, None)
                if(i<(N*(N-1))): #has down?
                    if(i+N) not in blocked:
                        g.addEdge(i,i+N,1)
                        line = Line(centerPts[i],centerPts[i+N])
                        line.setFill("red")
                        line.draw(workArea)
                    # else:
                    #     g.addEdge(i, i+N, None)
        
    else:
        print("invalid G(N)")
    return centerPts
    

workArea = GraphWin("Puzzle Graph", 600,600)
n = 7
points = G(g,n)
print(g)

'''input for testing dijkstra and confirming unsolvable graph'''
#val = input("Enter: ")
#print(val)
#if val == "yes":

V=dijkstra.dijkstraPuzzle(g,0)

currIndex = (n*n)-1
nextIndex=0
while(currIndex>0):
    nextIndex = V[currIndex]
    if(currIndex!=None and nextIndex!=None):

        line = Line(points[currIndex],points[nextIndex])
        line.setFill("blue")
        line.setWidth(6)
        line.draw(workArea)
        currIndex = nextIndex
    else:
        text = Text(Point(400,500),"UNSOLVABLE")
        text.setTextColor("Red")
        text.setSize(30)
        text.draw(workArea)
        break
    
#index is the vertex
#value of index is connecting vertex
'''Drawing the solution'''
# i = 0
# while i < len(V):
#     if V[i] != None:
#         line = Line(points[i],points[V[i]])
#         line.setFill("blue")
#         line.setWidth(6)
#         line.draw(workArea)
#         #print(V[i])
#     i+=1
'''steps to get the solution to draw'''
# use the last {index} or N^2 -1 to store point
# store point of the value of the last index (*store the value as the next index*)
# line for those two points
# use prev point
# * store point of the value of this index (*store the value as the next index*)
# until index is 0???



#print(cellCt)
while True:
    try:
        if workArea.getMouse().getX()!=None: #exit window by clicking on window with mouse
            break
    except GraphicsError: #click exit button and exit window without error
        break
workArea.close() #exits the window after any of the aforementioned actions occur