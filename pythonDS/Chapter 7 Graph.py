
'''Graph'''

#implement a Graph with connection tables

class Vertex:
    # store the id and the connecting vertex with a dict
    def __init__(self,key):
        self.id = key
        self.connect={}
    def addNeibor(self,key,weight=0):
        self.connect[key]=weight
    def __str__(self):
        return str(self.id) +'connect to: '+str([x.id for x in self.connect ])
    def getConnections(self):
        return self.connect.keys()
    def getid(self):
        return self.id
    def getweight(self,nbr):
        return self.connect[nbr]


class Graph:
    def __init__(self):
        self.vertlist={}
        self.numvertex=0
    def addvertex(self,key):
        vertex=Vertex(key)
        self.numvertex+=1
        self.vertlist[key]= vertex
        return vertex
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertlist
    def addEdge(self,f,t,cost=0):
        if f not in self.vertlist:
            x=self.addvertex(f)
        if t not in self.vertlist:
            y=self.addvertex(t)
        self.vertlist[f].addNeibor(self.vertlist[y],cost)
    def getVertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())


'''Breadth First Search, BFS'''