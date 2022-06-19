
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

# Word ladder: any words that there exits just one char between them, they can be connected

def buildgraph(wordfile):
    d={}
    g=Graph()
    for line in wordfile:
        word=line
        for i in range(len(word)):
            bucket=word[:i]+'-'+word[i+1:]
            d.get(bucket,[]).append(word)
    for k,v in d.items():
        for word1 in v:
            for word2 in v:
                if word1!= word2:
                    g.addEdge(word1,word2)
    return g


words=['fool','pool','pole','poll','pale','sale','sage']
def bfs(g:Graph,start):
    start.setdistance(0)
    start.setpred(None)
    queue=[]
    while queue:
        current=queue.pop()
        for nbr in current.getConnections():
            if nbr.getcolor() =='white':  #unvisited
                nbr.setcolor('gray')     # first visited
                nbr.setdistance(current.getdistance()+1)
                nbr.setpred(current)
                queue.insert(0,nbr)
        current.setcolor('black') # all the connections has been visited


