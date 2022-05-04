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
        '''Graphics set up and blocked cells chosen (using index)'''
        while  y<desired: # make "columns"
            while(x<desired): # make "rows"
                sq = Rectangle(Point(x,y), Point(x+50,y+50))
                centerPts.append(sq.getCenter()) #add Point object of coordinates of current cell's center
                if (x == (desired-50) and y == (desired-50)) or (x==0 and y==0):
                    '''if start and end cells'''
                    sq.setFill("aquamarine3")
                    sq.draw(workArea)
                    message = Text(Point(x+25,y+25),messages[currText])
                    message.draw(workArea)
                    currText+=1
                    
                elif random()<.25: 
                    '''create blocked cell'''
                    blocked.append(cellCt) #add index of cell to the bloacked array
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
            if i not in blocked: #only add edges for cells that are not blocked
                if(N<=i):   # has up?
                    if(i-N) not in blocked: #only add edges for vertices that have an up vertex that isn't blocked
                        g.addEdge(i,i-N,1)
                        line = Line(centerPts[i],centerPts[i-N])
                        line.setFill("red")
                        line.draw(workArea)
                if( i%N != 0): #has left?
                    if(i-1) not in blocked: #only add edges for vertices that have a left vertex that isn't blocked
                        g.addEdge(i,i-1,1)
                        line = Line(centerPts[i],centerPts[i-1])
                        line.setFill("red")
                        line.draw(workArea)
                if((i+1)%N!=0): #has right?
                    if(i+1) not in blocked: #only add edges for vertices that have a right vertex that isn't blocked
                        g.addEdge(i, i+1,1)
                        line = Line(centerPts[i],centerPts[i+1])
                        line.setFill("red")
                        line.draw(workArea)
                if(i<(N*(N-1))): #has down?
                    if(i+N) not in blocked: #only add edges for vertices that have a down vertex that isn't blocked
                        g.addEdge(i,i+N,1)
                        line = Line(centerPts[i],centerPts[i+N])
                        line.setFill("red")
                        line.draw(workArea)
        
    else:
        print("invalid G(N)")
    return centerPts #return array of Point objects for each cell's center point
    
def puzzleGraph(workArea, N):
    points = G(g,N); ''' make structured graph for g Graph and store the center points array from the graphics grid '''
    #graph 
    print(g) #print graph representation

    V=dijkstra.dijkstraPuzzle(g,0)  #store dijkstra algorithm V array
    #shortest path solved

    currIndex = (N*N)-1 #start at last index
    nextIndex=0 #init variable
    pathStr = "->" + str(currIndex)


    ''' Representation for the shortest path '''
    while(currIndex>0): #while the path being created hasn't reached the beginning vertex/cell
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
            pathStr = "unsolvable "
            break
        if(currIndex!= 0):
            pathStr = "->" + str(currIndex) + pathStr
        else:
            pathStr = "0" + pathStr
    print("Path: " , pathStr)

    ''' Graphics Window Exit Code'''
    while True:
        try:
            if workArea.getMouse().getX()!=None: #exit window by clicking on window with mouse
                break
        except GraphicsError: #click exit button and exit window without error
            break
    workArea.close() #exits the window after any of the aforementioned actions occur


workArea = GraphWin("Puzzle Graph", 600,600) #Make graphics window
puzzleGraph(workArea,9) #construct puzzle graph on the graphics window for a 9x9 grid