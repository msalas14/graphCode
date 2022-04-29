"""
File: graph.py
"""

from abstractcollection import AbstractCollection

class LinkedEdge(object):

    # An edge has a source vertex, a destination vertex,
    # a weight, and a mark attribute.
    
    def __init__(self, fromVertex, toVertex, weight = None):         
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight 
        self.mark = False
    
    def clearMark(self):
        """Clears the mark on the edge."""
        self.mark = False
    
    def __eq__(self, other):
        """Two edges are equal if they connect
        the same vertices."""
        if self is other: return True
        if type(self) != type(other):
            return False
        return self.vertex1 == other.vertex1 and \
               self.vertex2 == other.vertex2
    
    def getOtherVertex(self, thisVertex):
        """Returns the vertex opposite thisVertex."""
        if thisVertex == None or thisVertex == self.vertex2:
            return self.vertex1
        else:
            return self.vertex2

    def getToVertex(self):
        """Returns the edge's destination vertex."""
        return self.vertex2
    
    def getWeight(self):
        """Returns the edge's weight."""
        return self.weight
    
    def isMarked(self):
        """Returns True if the edge is marked
        or False otherwise."""
        return self.mark
    
    def setMark(self):
        """Sets the mark on the edge."""
        self.mark = True
    
    def setWeight(self, weight):
        """Sets the weight on the edge to weight."""
        self.weight = weight     
          
    def __str__(self):
        """Returns the string representation of the edge."""
        return str(self.vertex1) + ">" + \
               str(self.vertex2)   + ":" + \
               str(self.weight)

class LinkedVertex(object):

    # A vertex has a label, a list of incident edges,
    # and a mark attribute.

    def __init__(self, label):
        self.label = label
        self.edgeList = list()
        self.mark = False

    def clearMark(self):
        """Clears the mark on the vertex."""
        self.mark = False
    
    def getLabel(self):
        """Returns the label of the vertex."""
        return self.label
    
    def isMarked(self):
        """Returns True if the vertex is marked
        or False otherwise."""
        return self.mark
    
    def setLabel(self, label, g):
        """Sets the vertex's label to label."""
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label          

    def setMark(self):
        """Sets the mark on the vertex."""
        self.mark = True
    
    def __str__(self):
        """Returns the string representation of the vertex."""
        return str(self.label)

    def __eq__(self, other):
        """Two vertices are equal if they have
        the same labels."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.getLabel() == other.getLabel()

    def __hash__(self):
        """Supports hashing on a vertex."""
        return hash(self.label)

    # Methods used by LinkedGraph
    
    def addEdgeTo(self, toVertex, weight):
        """Connects the vertices with an edge."""
        edge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(edge)
    
    def getEdgeTo(self, toVertex):
        """Returns the connecting edge if it exists, or
        None otherwise."""
        edge = LinkedEdge(self, toVertex)
        try:
            return self.edgeList[self.edgeList.index(edge)]
        except:
            return None

    def incidentEdges(self):
        """Returns the incident edges of this vertex."""
        return iter(self.edgeList)
        
    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self.edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
            
    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False


class LinkedDirectedGraph(AbstractCollection):

    # A graph has a count of vertices, a count of edges,
    # and a dictionary of label/vertex pairs.

    def __init__(self, sourceCollection = None):
        self.edgeCount = 0
        self.vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        
    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        """Clears the graph."""
        self.size = 0
        self.edgeCount = 0
        self.vertices = {}        

    def clearEdgeMarks(self):
        """Clears all the edge marks."""
        for edge in self.edges():
            edge.clearMark()
    
    def clearVertexMarks(self):
        """Clears all the vertex marks."""
        for vertex in self.getVertices():
            vertex.clearMark()
    
    def sizeEdges(self):
        """Returns the number of edges."""
        return self.edgeCount
    
    def sizeVertices(self):
        """Returns the number of vertices."""
        return len(self)
    
    def __str__(self):
        """Returns the string representation of the graph."""
        result = str(self.sizeVertices()) + " Vertices: "
        for vertex in self.vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)

    # Vertex related methods
    
    def addVertex(self, label):
        """Adds a vertex with the given label to the graph."""
        self.vertices[label] = LinkedVertex(label)
        self.size += 1
        
    def containsVertex (self, label):
        return label in self.vertices
    
    def getVertex(self, label):
        return self.vertices[label]
    
    def removeVertex(self,  label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self.vertices.pop(label, None)
        if removedVertex is None: 
            return False
        
        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.getVertices():
            if vertex.removeEdgeTo(removedVertex): 
                self.edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self.edgeCount -= 1           
        self.size -= 1
        return True
    
    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight."""
        fromVertex = self.getVertex(fromLabel)
        toVertex   = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self.edgeCount += 1
    
    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return self.getEdge(fromLabel, toLabel) != None
    
    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists."""
        fromVertex = self.getVertex(fromLabel)
        toVertex   = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)
    
    def removeEdge(self, fromLabel, toLabel): 
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg: 
            self.edgeCount -= 1
        return edgeRemovedFlg

    # Iterators
    
    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.vertices()

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.getVertices():
            result += list(vertex.incidentEdges())
        return iter(result)
    
    def getVertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self.vertices.values())

    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex."""
        return self.getVertex(label).incidentEdges()
    
    def neighboringVertices(self, label):
        """Supports iteration over the neighboring vertices of the
        given verrtex."""
        return self.getVertex(label).neighboringVertices()
    
